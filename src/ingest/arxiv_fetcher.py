"""ArXiv paper fetcher and metadata retriever."""
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Tuple
from src.ingest.pdf_parser import parse_pdf
from src.ingest.manifest import PaperManifest

ARXIV_API_BASE = "http://export.arxiv.org/api/query?id_list="

def extract_arxiv_id(query: str) -> Optional[str]:
    """Extracts arXiv ID from URL or raw ID string."""
    # Matches: 2401.12345, 2401.12345v2, abs/2401.12345, pdf/2401.12345.pdf
    pattern = r"(?:arxiv\.org\/(?:abs|pdf)\/)?([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?)"
    match = re.search(pattern, query.strip())
    if match:
        return match.group(1)
    return None

def fetch_arxiv_metadata(arxiv_id: str) -> Tuple[str, str, list, str]:
    """Retrieves title, abstract, authors, and published date from arXiv API."""
    url = f"{ARXIV_API_BASE}{arxiv_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'PaperReadingPlaybook/1.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entry = root.find('atom:entry', ns)
    if entry is None:
        raise ValueError(f"arXiv ID {arxiv_id} not found.")

    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
    published = entry.find('atom:published', ns).text.strip()[:10]
    authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
    
    return title, summary, authors, published

def fetch_and_parse_arxiv(query: str, download_dir: Path) -> PaperManifest:
    """Downloads PDF from arXiv and constructs a PaperManifest."""
    arxiv_id = extract_arxiv_id(query)
    if not arxiv_id:
        raise ValueError(f"Invalid arXiv query or ID: {query}")

    download_dir.mkdir(parents=True, exist_ok=True)
    pdf_filename = f"arxiv_{arxiv_id.replace('.', '_')}.pdf"
    pdf_path = download_dir / pdf_filename

    # Download PDF if not already present
    if not pdf_path.exists():
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        req = urllib.request.Request(pdf_url, headers={'User-Agent': 'PaperReadingPlaybook/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(pdf_path, 'wb') as out_f:
            out_f.write(resp.read())

    # Get metadata
    try:
        title, abstract, authors, pub_date = fetch_arxiv_metadata(arxiv_id)
    except Exception:
        title, abstract, authors, pub_date = f"arXiv:{arxiv_id}", "", [], "Unknown"

    manifest = parse_pdf(pdf_path, paper_id=f"arxiv-{arxiv_id}")
    if title:
        manifest.title = title
    if abstract:
        manifest.abstract = abstract
    if authors:
        manifest.authors = authors
    manifest.publication_date = pub_date
    manifest.venue_or_status = f"arXiv preprint ({arxiv_id})"
    return manifest

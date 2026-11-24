"""Unified paper ingestion interface."""
from pathlib import Path
from src.ingest.manifest import PaperManifest
from src.ingest.pdf_parser import parse_pdf
from src.ingest.arxiv_fetcher import fetch_and_parse_arxiv, extract_arxiv_id
from src.ingest.text_parser import parse_text_paper

def load_paper(source: str, download_dir: Path = Path("downloads")) -> PaperManifest:
    """Ingests a research paper from a file path, arXiv URL/ID, or plain text."""
    # Check if arXiv source
    if extract_arxiv_id(source) and ("arxiv.org" in source or source.replace(".", "").isdigit()):
        return fetch_and_parse_arxiv(source, download_dir)
    
    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(f"Input paper source not found: {source}")

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return parse_pdf(path)
    elif suffix in [".md", ".txt", ".tex", ".html"]:
        return parse_text_paper(path)
    else:
        # Default attempt text
        return parse_text_paper(path)

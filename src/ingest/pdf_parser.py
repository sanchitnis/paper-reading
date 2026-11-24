"""PDF parser using PyMuPDF (fitz) or PyPDF fallback."""
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from src.ingest.manifest import PaperManifest, Section, Figure, Table

try:
    import pymupdf
    fitz = pymupdf
    HAS_PYMUPDF = True
except ImportError:
    try:
        import fitz
        HAS_PYMUPDF = True
    except ImportError:
        HAS_PYMUPDF = False

def parse_pdf(file_path: Path, paper_id: Optional[str] = None) -> PaperManifest:
    """Extracts structured paper manifest from PDF."""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found at {file_path}")

    slug = paper_id or file_path.stem.lower().replace(" ", "-")
    
    if not HAS_PYMUPDF:
        # Fallback basic parser
        return _fallback_parser(file_path, slug)

    doc = fitz.open(file_path)
    full_text_pages = []
    figures = []
    
    output_asset_dir = file_path.parent / "assets" / slug
    output_asset_dir.mkdir(parents=True, exist_ok=True)

    img_count = 0
    for page_idx, page in enumerate(doc):
        text = page.get_text("text")
        full_text_pages.append(text)
        
        # Extract images if present
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                img_count += 1
                img_name = f"fig_p{page_idx+1}_{img_count}.{image_ext}"
                img_path = output_asset_dir / img_name
                with open(img_path, "wb") as f_img:
                    f_img.write(image_bytes)
                figures.append(Figure(
                    figure_id=f"fig_{img_count}",
                    caption=f"Figure extracted from page {page_idx+1}",
                    image_path=str(img_path),
                    page_number=page_idx + 1
                ))
            except Exception:
                pass

    total_text = "\n".join(full_text_pages)
    title, abstract, sections = _extract_sections(total_text, file_path.stem)
    
    return PaperManifest(
        paper_id=slug,
        title=title,
        abstract=abstract,
        sections=sections,
        figures=figures,
        raw_source_type="pdf",
        file_path=str(file_path)
    )

def _extract_sections(text: str, fallback_title: str):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if not lines:
        return fallback_title, "No abstract found.", []

    title = lines[0] if len(lines[0]) > 5 else fallback_title
    abstract = ""
    sections: List[Section] = []
    current_sec = None
    current_lines = []

    # Regex for section headers like "1. Introduction", "2 Related Work", "III. METHODOLOGY"
    sec_regex = re.compile(r"^(\d+|[I|V|X]+)\.?\s+([A-Z][A-Za-z0-9\s\-_:]{3,60})$")
    
    in_abstract = False
    for line in lines:
        if line.lower().startswith("abstract"):
            in_abstract = True
            abstract = line[8:].strip()
            continue
        
        match = sec_regex.match(line)
        if match:
            in_abstract = False
            if current_sec:
                current_sec.content = "\n".join(current_lines).strip()
                sections.append(current_sec)
                current_lines = []
            heading = line
            current_sec = Section(heading=heading, level=1, content="")
            continue
        
        if in_abstract:
            abstract += " " + line
        elif current_sec:
            current_lines.append(line)

    if current_sec:
        current_sec.content = "\n".join(current_lines).strip()
        sections.append(current_sec)

    if not abstract:
        abstract = lines[1] if len(lines) > 1 else "No abstract identified."
    
    if not sections:
        sections.append(Section(heading="Main Content", level=1, content=text[:10000]))

    return title, abstract.strip(), sections

def _fallback_parser(file_path: Path, slug: str) -> PaperManifest:
    return PaperManifest(
        paper_id=slug,
        title=file_path.stem.replace("-", " ").title(),
        abstract="Extracted via fallback parser.",
        sections=[Section(heading="Full Document", level=1, content="Content parsing available via PyMuPDF.")],
        raw_source_type="pdf",
        file_path=str(file_path)
    )

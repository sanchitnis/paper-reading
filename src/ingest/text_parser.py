"""Parser for text, markdown, and HTML research paper sources."""
from pathlib import Path
from typing import Optional
from src.ingest.manifest import PaperManifest, Section
import re

def parse_text_paper(file_path: Path, paper_id: Optional[str] = None) -> PaperManifest:
    """Parses a Markdown, LaTeX, or plain text paper."""
    file_path = Path(file_path)
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        raw_text = f.read()

    slug = paper_id or file_path.stem.lower().replace(" ", "-")
    lines = raw_text.splitlines()

    # Simple title and section parsing
    title = file_path.stem.replace("-", " ").title()
    abstract = ""
    sections = []
    current_sec = None
    sec_lines = []

    for line in lines:
        if line.startswith("# ") and title == file_path.stem.replace("-", " ").title():
            title = line[2:].strip()
            continue
        if line.lower().startswith("abstract:") or line.lower().startswith("**abstract**"):
            abstract = re.sub(r"^\*\*?abstract\*\*?:?\s*", "", line, flags=re.IGNORECASE).strip()
            continue
        if line.startswith("## "):
            if current_sec:
                current_sec.content = "\n".join(sec_lines).strip()
                sections.append(current_sec)
                sec_lines = []
            current_sec = Section(heading=line[3:].strip(), level=2, content="")
            continue
        if current_sec:
            sec_lines.append(line)
        elif not abstract and len(line) > 60:
            abstract = line.strip()

    if current_sec:
        current_sec.content = "\n".join(sec_lines).strip()
        sections.append(current_sec)

    if not sections:
        sections.append(Section(heading="Full Document", level=1, content=raw_text))

    return PaperManifest(
        paper_id=slug,
        title=title,
        abstract=abstract or "Abstract not explicitly separated.",
        sections=sections,
        raw_source_type="text",
        file_path=str(file_path)
    )

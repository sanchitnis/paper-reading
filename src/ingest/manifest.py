"""Data models for ingested papers, sections, and manifests."""
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class Figure(BaseModel):
    figure_id: str
    caption: str
    image_path: Optional[str] = None
    page_number: Optional[int] = None

class Table(BaseModel):
    table_id: str
    caption: str
    markdown: str
    page_number: Optional[int] = None

class Section(BaseModel):
    heading: str
    level: int = 1
    content: str
    equations: List[str] = Field(default_factory=list)
    subsections: List['Section'] = Field(default_factory=list)

class BibliographyItem(BaseModel):
    key: str
    citation: str
    doi_or_url: Optional[str] = None

class PaperManifest(BaseModel):
    paper_id: str
    title: str
    authors: List[str] = Field(default_factory=list)
    publication_date: Optional[str] = None
    venue_or_status: str = "Preprint / In Review"
    abstract: str
    primary_category: str = "Computer Science"
    tags: List[str] = Field(default_factory=list)
    sections: List[Section] = Field(default_factory=list)
    figures: List[Figure] = Field(default_factory=list)
    tables: List[Table] = Field(default_factory=list)
    bibliography: List[BibliographyItem] = Field(default_factory=list)
    raw_source_type: str = "pdf"
    file_path: Optional[str] = None

    def get_full_text(self) -> str:
        text_parts = [f"# {self.title}\n", f"**Abstract**: {self.abstract}\n"]
        for sec in self.sections:
            text_parts.append(f"\n## {sec.heading}\n{sec.content}")
            for sub in sec.subsections:
                text_parts.append(f"\n### {sub.heading}\n{sub.content}")
        return "\n".join(text_parts)

---
name: paper-ingest
description: Ingests research papers from multiple formats (PDF, arXiv URL/ID, HTML, Markdown, LaTeX) and extracts structured metadata, sections, math, tables, and figures.
---

# Paper Ingest Skill

## Overview
This skill handles multi-format ingestion of academic papers, converting heterogeneous sources into a normalized, structured document representation ready for multi-pass analysis, vault generation, and AI explanation.

## Supported Formats & Sources
- **PDF Files**: Local files (`.pdf`) parsed via `pymupdf` (fitz) or `pdfplumber` with text, layout, bounding boxes, and figure extraction.
- **arXiv URLs & Identifiers**: E.g., `https://arxiv.org/abs/2401.12345`, `2401.12345`, or `arxiv:2401.12345v2`. Downloads PDF and pulls metadata from the arXiv API.
- **HTML & Web Articles**: Papers hosted on OpenReview, Distill, Semantic Scholar, GitHub pages, or Nature/Science journals.
- **Markdown & LaTeX Sources**: Overleaf exports, `.tex` bundles, and `.md` archives.

## Output Schema
The skill produces a normalized JSON document `paper_manifest.json`:
```json
{
  "paper_id": "unique-slug",
  "title": "Title of the Paper",
  "authors": ["Author 1", "Author 2"],
  "publication_date": "YYYY-MM-DD",
  "venue_or_status": "NeurIPS / arXiv preprint / Unverified",
  "abstract": "Full abstract text...",
  "primary_category": "cs.CC / cs.LG / cs.AI",
  "sections": [
    {
      "heading": "1 Introduction",
      "level": 1,
      "content": "Text content...",
      "equations": ["$$E = mc^2$$"],
      "subsections": []
    }
  ],
  "figures": [
    {
      "figure_id": "fig_1",
      "caption": "Caption text...",
      "image_path": "assets/fig_1.png"
    }
  ],
  "tables": [
    {
      "table_id": "table_1",
      "caption": "Caption text...",
      "markdown": "| Col 1 | Col 2 |..."
    }
  ],
  "bibliography": [
    {
      "key": "Valiant79",
      "citation": "L. G. Valiant. Completeness classes in algebra. STOC 1979."
    }
  ]
}
```

## Extraction Rules & Quality Checks
1. **Math Preservation**: Preserve LaTeX expressions inline (`$...$`) and display blocks (`$$...$$`). Clean OCR math artifacts where possible.
2. **Structural Integrity**: Ensure headings hierarchy (`#`, `##`, `###`) matches the paper's logical flow.
3. **Artifact Isolation**: Extract figures and tables into a dedicated `assets/` subfolder with clear cross-references.
4. **Metadata Normalization**: Clean author affiliations, resolve arXiv DOIs, and record the publication/revision timestamp.

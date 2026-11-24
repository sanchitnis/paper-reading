---
name: obsidian-vault-builder
description: Generates a modular, interconnected Obsidian knowledge vault with Map of Content (00 Index), numbered reading path, Wikilinks, Mermaid charts, callouts, and frontmatter.
---

# Obsidian Vault Builder Skill

## Overview
Generates a complete, modular, hyperlinked Obsidian markdown vault for any ingested paper, formatted identically to the gold-standard `vp-vnp-vault` architecture.

## Vault Topology & Standard Structure
Every generated paper vault adheres to this canonical structure:

```
<vault-root>/
├── 00 Index.md                                   # Map of Content (MOC), audience, reading path
├── 01 Big picture.md                             # Mermaid overview diagram, 1-paragraph summary
├── 02 Foundations and context.md                 # Background, prior art, why standard methods hit barriers
├── 03 Core objects and definitions.md            # Formal notation, mathematical objects, spaces
├── 04 What the paper claims.md                   # Precise theorems, claimed bounds, exact statements
├── 05 Proof architecture.md (or System architecture.md) # Top-down map of the main argument/pipeline
├── 06 Deep dive - Case 1.md                      # Detailed technical breakdown of branch 1
├── 07 Deep dive - Case 2.md                      # Detailed technical breakdown of branch 2
├── 08 What the result does not say.md            # Caveats, non-claims, boundaries, open questions
├── 09 Relevance and consequences.md              # Broader implications, applications, theoretical impact
├── 10 Formalization and code verification.md    # Lean/Coq proof checks or executable Python implementation
├── 11 Reception and valid comments.md            # Community reactions, peer reviews, critique, open scrutiny
├── 12 How to evaluate it yourself.md             # Active recall checks, verification steps, homework
├── 13 Glossary.md                                # Alphabetical definitions with cross-linked wikilinks
└── 14 References.md                              # Key citations with context and outbound links
```

## Formatting Guidelines
1. **Frontmatter**: Every file must start with YAML frontmatter:
   ```yaml
   ---
   tags: [tag1, tag2, topic]
   aliases: [Alternate Name, Short Title]
   ---
   ```
2. **Wikilinks**: Use double-bracket links `[[01 Big picture]]` or `[[13 Glossary#Term|Term]]` generously to weave an associative web.
3. **Mermaid Diagrams**: Include valid Mermaid flowcharts (`flowchart TD` / `flowchart LR`) illustrating pipelines, proof branches, or system components.
4. **Distinction Markers**:
   - `*(paper)*`: Statements sourced directly from the paper.
   - `*(analogy)*`: Explanatory simplifications and analogies for the learner.
5. **Callouts**:
   - `> [!NOTE]` for contextual background.
   - `> [!IMPORTANT]` for primary theorem statements.
   - `> [!WARNING]` for common pitfalls or mistaken interpretations.
   - `> [!QUESTION]` for active-reading comprehension checks.

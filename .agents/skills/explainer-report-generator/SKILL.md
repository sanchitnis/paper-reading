---
name: explainer-report-generator
description: Synthesizes a comprehensive, rigorous technical explainer report (Executive Summary, Mathematical Formulations, Architecture, Reproducibility, Critique).
---

# Explainer Report Generator Skill

## Overview
Generates an exhaustive, high-density technical explainer report (`EXPLAINER_REPORT.md` and optional PDF export) designed for technical leaders, researchers, and senior engineers.

## Required Report Architecture
1. **Executive Summary & Metadata**:
   - Title, Authors, Affiliation, Venue/Date, Review Status.
   - Core Breakthrough in 3 Sentences.
   - Bottom-Line Significance for Industry and Academia.
2. **Context & Motivation**:
   - The historical barrier or prior state of the art.
   - Why previous techniques (e.g. natural proofs, relativization, algebrization) failed.
3. **Problem Formulation & Notation**:
   - Explicit definitions of all sets, spaces, algebraic fields, and computational classes.
   - Clear distinction between assumptions and deduced properties.
4. **Methodology & Theoretical Architecture**:
   - Step-by-step deconstruction of the proof or algorithmic pipeline.
   - Architectural flowcharts (Mermaid).
   - Key lemmas and their operational roles.
5. **Detailed Mathematical Derivations**:
   - Unpacking crucial formulas and algebraic reductions.
   - Explaining intermediate steps that typical papers condense.
6. **Empirical Results & Benchmark Validation** (or Formal Verification Details):
   - Experimental setups, datasets, baseline comparisons, compute resources.
   - If formal math: Lean/Coq verification coverage, axiom audit, lines of code.
7. **Critical Evaluation & Failure Modes**:
   - Hidden assumptions and fragility analysis.
   - Non-claims (what the paper deliberately does *not* prove).
   - Potential points of vulnerability or unresolved questions.
8. **Engineering & Implementation Takeaways**:
   - Practical relevance for systems engineers, ML practitioners, or researchers.
   - Actionable takeaways for the specific learner.
9. **Verification & Reproduction Guide**:
   - Step-by-step checklist to independently test or verify the claims.

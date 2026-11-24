---
tags: [14_swin_transformer_iccv2021_best, overview]
aliases: [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows Big Picture]
---
# Big picture

```mermaid
flowchart TD
    A["Swin Transformer: Hierarchical Vision Transformer using Shifted Windows<br/>Core Problem Landscape"] -->|"Identifies barrier in existing art"| B["Key Innovation / Bifurcation"]
    B --> C["Branch A / Case 1:<br/>Structural Analysis"]
    B --> D["Branch B / Case 2:<br/>Asymptotic & Complexity Bounds"]
    C --> E{"Core Resolution / Contradiction"}
    D --> E
    E --> F["Paper's Main Result:<br/>Swin Transformer: Hierarchical Vision Transformer using Shifted Windows"]
    F -.->|"Deliberate Non-Claim"| G["Does NOT solve broader open problems<br/>(See 08 What the result does not say)"]
    F --> H["Verification Status:<br/>Preprint / In Review"]
```

## One-paragraph version
**Title:** Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

*(analogy)* Think of this paper's core contribution as identifying an invariant in the problem space: either the system is constrained by geometric rigidity, or it admits an exponential reduction, leaving no middle ground for polynomial-size shortcuts.

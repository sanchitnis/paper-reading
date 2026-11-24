---
tags: [11_neural_odes_neurips2018_best, overview]
aliases: [Neural Ordinary Differential Equations (Neural ODEs) Big Picture]
---
# Big picture

```mermaid
flowchart TD
    A["Neural Ordinary Differential Equations (Neural ODEs)<br/>Core Problem Landscape"] -->|"Identifies barrier in existing art"| B["Key Innovation / Bifurcation"]
    B --> C["Branch A / Case 1:<br/>Structural Analysis"]
    B --> D["Branch B / Case 2:<br/>Asymptotic & Complexity Bounds"]
    C --> E{"Core Resolution / Contradiction"}
    D --> E
    E --> F["Paper's Main Result:<br/>Neural Ordinary Differential Equations (Neural ODEs)"]
    F -.->|"Deliberate Non-Claim"| G["Does NOT solve broader open problems<br/>(See [[08 What the result does not say]])"]
    F --> H["Verification Status:<br/>Preprint / In Review"]
```

## One-paragraph version
**Authors:** Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud (University of Toronto, Vector Institute)

*(analogy)* Think of this paper's core contribution as identifying an invariant in the problem space: either the system is constrained by geometric rigidity, or it admits an exponential reduction, leaving no middle ground for polynomial-size shortcuts.

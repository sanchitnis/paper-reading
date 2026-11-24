---
tags: [13_densenet_cvpr2017_best, overview]
aliases: [Densely Connected Convolutional Networks (DenseNet) Big Picture]
---
# Big picture

```mermaid
flowchart TD
    A["Densely Connected Convolutional Networks (DenseNet)<br/>Core Problem Landscape"] -->|"Identifies barrier in existing art"| B["Key Innovation / Bifurcation"]
    B --> C["Branch A / Case 1:<br/>Structural Analysis"]
    B --> D["Branch B / Case 2:<br/>Asymptotic & Complexity Bounds"]
    C --> E{"Core Resolution / Contradiction"}
    D --> E
    E --> F["Paper's Main Result:<br/>Densely Connected Convolutional Networks (DenseNet)"]
    F -.->|"Deliberate Non-Claim"| G["Does NOT solve broader open problems<br/>(See [[08 What the result does not say]])"]
    F --> H["Verification Status:<br/>Preprint / In Review"]
```

## One-paragraph version
**Authors:** Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger (Cornell University, Tsinghua University, Facebook AI Research)

*(analogy)* Think of this paper's core contribution as identifying an invariant in the problem space: either the system is constrained by geometric rigidity, or it admits an exponential reduction, leaving no middle ground for polynomial-size shortcuts.

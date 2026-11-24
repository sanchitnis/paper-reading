---
tags: [07_instructgpt_rlhf, proof, architecture]
---
# Proof architecture

```mermaid
flowchart TD
    Hyp["Assume contrary / target condition holds"] --> DichotomyFundamental Dichotomy
    Dichotomy -->|"Case 1"| Flat["06 Primary mechanism - Branch A<br/>Geometric / Tensor rigidity"]
    Dichotomy -->|"Case 2"| Contract["07 Primary mechanism - Branch B<br/>Speed-up & Diagonalization"]
    Flat --> Contradiction1["Contradiction with small circuit assumption"]
    Contract --> Contradiction2["Contradiction via complexity lower bound"]
    Contradiction1 & Contradiction2 --> Conclusion["Conclusion: Main Theorem holds"]
```

## Top-Down Argument
The proof proceeds by dividing the universe of possibilities into two mutually exhaustive branches:
1. **Branch A**: Examined in [06 Primary mechanism - Branch A](06%20Primary%20mechanism%20-%20Branch%20A.md).
2. **Branch B**: Examined in [07 Primary mechanism - Branch B](07%20Primary%20mechanism%20-%20Branch%20B.md).

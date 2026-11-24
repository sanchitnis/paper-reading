---
tags: [vp-vnp, relevance]
---
# Relevance and consequences

*If the claim holds up.* Everything below depends on verification. See [12 How to evaluate it yourself](12%20How%20to%20evaluate%20it%20yourself.md).

## 1. Mathematics and theoretical CS
- **Settles Valiant's 1979 conjecture** over every field. This is the central question of algebraic complexity.
- **First strong general-circuit lower bound.** Moving from about n log d to a quasi-polynomial bound on general circuits would be the largest jump in the area since the 1980s.
- **Geometric Complexity Theory.** Theorem 1.4 implies the permanent is not approximated by poly-size determinants. That is the border-complexity statement Mulmuley and Sohoni targeted, though the paper's proof uses no representation theory. This consequence is the part not yet in Lean.
- **New toolbox.** Strassen's asymptotic spectrum, CAT(0) geometry, and diagonalization over tensor networks. If correct, these become methods other researchers will push, for instance to improve the exponent 1/3.

## 2. Link to P vs NP
- It is a **necessary-type milestone** on one route: VP = VNP would give P/poly = NP/poly, so you cannot get there while VP ≠ VNP is open.
- It is **not** sufficient. Boolean circuits are untouched, and the paper has not analysed relativization or algebrization.

## 3. Derandomization
Lower bounds for the permanent connect to **polynomial identity testing (PIT)** via Kabanets–Impagliazzo (2004). The paper explicitly says it has not worked out what its bound gives there. This is one concrete follow-up to watch.

## 4. AI and mathematics
- Claimed as the first end-to-end AI discovery of a result of this kind, with a machine-checked proof.
- **Trust model is the real story.** Lean certifies "proof matches typed statement". It does *not* certify "typed statement matches the mathematical question". The README admits this gap. See [10 Lean formalization and what it checks](10%20Lean%20formalization%20and%20what%20it%20checks.md).
- A template for how AI-generated mathematics could be audited: small human-readable statement file, large machine-checked proof file, independent checkers.

## 5. What it does *not* touch
Cryptography, practical algorithms, or the Boolean permanent's hardness.

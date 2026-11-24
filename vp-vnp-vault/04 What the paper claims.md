---
tags: [vp-vnp, theorem]
---
# What the paper claims

**Theorem 1.1** *(paper)*. There is an absolute constant c > 0 such that, for every characteristic p (zero or prime), there is an m₀ with this property. Over every field of characteristic p, for every m ≥ m₀, every circuit for **HCₘ**, and every circuit for **PERMₘ** when p ≠ 2, has more than **m^{c·(log₂ m)^{1/3}}** gates.

| Statement | Meaning |
|---|---|
| Thm 1.1 | the quantitative lower bound, in the form 2^{c(log m)^{4/3}} |
| **Cor 1.2** | VP ⊊ VNP over every field |
| **Thm 1.4** | the same bound for *approximating* circuits (border complexity), so VNP ⊄ closure(VP) |
| Consequence (Remark N.6) | the permanent is not approximated by poly-size determinants. This is the Mulmuley–Sohoni GCT conjecture, and it is the **one statement not formalized in Lean** |

## Caveats stated by the paper itself
- m₀ has **no explicit value**, because in the contracting case the constants depend on an integer μ that the proof does not compute.
- The exponent 1/3 is not claimed to be optimal.
- The result "says nothing about whether NP-complete problems have fast algorithms."
- Not known which of the two proof cases actually occurs, even over ℝ.

## How big a jump is this?
Previously, the best lower bound for any explicit polynomial and general circuits was **Ω(n log d)** (Strassen; Baur–Strassen 1983). For the permanent, nothing above about m² log m was known *(paper §1.2)*. The claim goes from near-linear to quasi-polynomial in one step. That is why the claim needs unusually careful checking. See [11 Reception and valid comments](11%20Reception%20and%20valid%20comments.md).

---
tags: [vp-vnp, complexity, moc]
aliases: [VP vs VNP map]
---
# VP ≠ VNP over every field: explainer vault

**Paper:** *VP ≠ VNP over every field*, credited to "Claude (Anthropic)". It was posted 23 Nov 2026 in `anthropics/formal-math/vp-vnp` with a Lean 4 formalization. **Status: unverified by any human mathematician.** The paper and README both say so. See [10 Lean formalization and what it checks](10%20Lean%20formalization%20and%20what%20it%20checks.md).

**Audience:** someone who knows P and NP but nothing more. Read top-down.

## Reading path
1. [01 Big picture](01%20Big%20picture.md): the whole story on one page
2. [02 From P vs NP to VP vs VNP](02%20From%20P%20vs%20NP%20to%20VP%20vs%20VNP.md): what changes when bits become numbers
3. [03 Arithmetic circuits and the permanent](03%20Arithmetic%20circuits%20and%20the%20permanent.md): the objects in the theorem
4. [04 What the paper claims](04%20What%20the%20paper%20claims.md): precise statements
5. [05 Proof architecture](05%20Proof%20architecture.md): the top-down map of the argument
   - [06 Flat case](06%20Flat%20case.md)
   - [07 Contracting case](07%20Contracting%20case.md)
6. [08 What the result does not say](08%20What%20the%20result%20does%20not%20say.md): why not P ≠ NP, and why the determinant escapes
7. [09 Relevance and consequences](09%20Relevance%20and%20consequences.md)
8. [10 Lean formalization and what it checks](10%20Lean%20formalization%20and%20what%20it%20checks.md)
9. [11 Reception and valid comments](11%20Reception%20and%20valid%20comments.md)
10. [12 How to evaluate it yourself](12%20How%20to%20evaluate%20it%20yourself.md)
11. [13 Glossary](13%20Glossary.md) · [14 References](14%20References.md)

> Convention: statements sourced to the paper are marked *(paper)*. Analogies and simplifications are mine and are marked *(analogy)*. Reactions come from secondary web sources and are in [11 Reception and valid comments](11%20Reception%20and%20valid%20comments.md).

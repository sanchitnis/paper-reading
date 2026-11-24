---
tags: [vp-vnp, complexity, moc]
aliases: [VP vs VNP map]
---
# VP ≠ VNP over every field: explainer vault

**Paper:** *VP ≠ VNP over every field*, credited to "Claude (Anthropic)". It was posted 23 Nov 2026 in `anthropics/formal-math/vp-vnp` with a Lean 4 formalization. **Status: unverified by any human mathematician.** The paper and README both say so. See [[10 Lean formalization and what it checks]].

**Audience:** someone who knows P and NP but nothing more. Read top-down.

## Reading path
1. [[01 Big picture]]: the whole story on one page
2. [[02 From P vs NP to VP vs VNP]]: what changes when bits become numbers
3. [[03 Arithmetic circuits and the permanent]]: the objects in the theorem
4. [[04 What the paper claims]]: precise statements
5. [[05 Proof architecture]]: the top-down map of the argument
   - [[06 Flat case]]
   - [[07 Contracting case]]
6. [[08 What the result does not say]]: why not P ≠ NP, and why the determinant escapes
7. [[09 Relevance and consequences]]
8. [[10 Lean formalization and what it checks]]
9. [[11 Reception and valid comments]]
10. [[12 How to evaluate it yourself]]
11. [[13 Glossary]] · [[14 References]]

> Convention: statements sourced to the paper are marked *(paper)*. Analogies and simplifications are mine and are marked *(analogy)*. Reactions come from secondary web sources and are in [[11 Reception and valid comments]].

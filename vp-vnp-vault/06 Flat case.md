---
tags: [vp-vnp, proof]
---
# Flat case: geometry of tensor networks

**When it applies:** every finite set of points in Euclidean space can be realized (approximately) as a "price". Think of a perfectly flat, ordinary geometry being available.

## The target polynomial
f_{k,ℓ} lives on the **complete graph on k nodes**, with an ℓ-bit string on every edge. Each node's variable depends on the strings on its edges. Each edge couples its two endpoints, so the polynomial is a **product of wires** over all edges.

## The intuition *(analogy, mine)*
- A circuit with L gates lets you cut the polynomial at any **balanced** set of nodes into ≤ 2^k pieces, each of rank ≤ L across the cut.
- In a **path** (an iterated matrix product), some balanced cut is crossed by a single wire. That is why such polynomials are easy.
- In the **complete network**, a constant fraction of all wires, at least 2k²/9, cross *every* balanced cut. No cheap hub structure can serve all cuts at once.
- With flat geometry you can place the wire ends in ℝ^k so that every wire has length 1. Any hub for a balanced cut must then sit far from some ends, so shortcuts through hubs cost too much. The only way to pay is a large rank L.

## Numbers
- Result: log L ≥ ℓ·k^{3/2}/16 for ℓ ≥ 100√k.
- Choose k = r², ℓ = 100r. Then log m ≈ r³ and log L ≈ r⁴ = (log m)^{4/3}.
- Hence L ≥ 2^{c(log m)^{4/3}}, which is Theorem 1.1's bound in the flat case.

## Where the permanent is used
Once: a circuit with L′ gates for PERMₘ (with m ≥ 3k³ℓ2^{kℓ}) gives a circuit with L = 5L′ gates for f_{k,ℓ}. This is lem_fkl_perm in the Lean development.

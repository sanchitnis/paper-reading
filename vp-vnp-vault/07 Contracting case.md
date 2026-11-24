---
tags: [vp-vnp, proof]
---
# Contracting case: speed-up plus diagonalization

**When it applies:** for some μ, every price on the 𝜇×𝜇 matrices over 𝔽₂ falls short of a Euclidean rectangle by a fixed factor. Geometry is "bent inward".

The argument is **indirect**. It resembles the diagonal proofs of computability and complexity theory, which is why the paper calls it a diagonalization.

```mermaid
flowchart TD
    S1["Steps 1-3: contraction ⇒ Poincaré inequality ⇒<br/>'rerouting laws' ⇒ every tensor network equals a sum of tree networks"]
    S1 --> S4["Step 4 (Cutting theorem): any computation of a<br/>nondeterministic program with weighted runs can be cut<br/>into short pieces listed by a fast program"]
    S4 --> S5["Step 5: assume PERM has a circuit with v^a gates.<br/>Then there is an accelerator at scale v:<br/>a program that gives the same sums in fewer steps"]
    S5 --> ACC["Accelerators propagate to larger scales v^α<br/>(rounds of cutting + running the accelerator)"]
    ACC --> DIAG["Diagonal program P: guess a bit; either accept with weight 1,<br/>or apply the accelerator to 'P applied to P'"]
    DIAG --> BAD["Then value V = 1 + V,<br/>impossible in a nonzero ring"]
```

## Plain-language reading *(analogy)*
1. Without any circuit at all, the geometry forces a structure theorem: long computations can be chopped into small independent pieces.
2. A small permanent circuit would be a **magic shortcut** that evaluates sums over runs faster than the structure theorem allows.
3. Use the shortcut to build a program that talks about itself: the **V = 1 + V** paradox, like the halting problem. Contradiction.

## Technical flags *(paper)*
- The permanent is used once, via a clause-sum circuit for Φ = Σ_w U_t(w)·y^w. This polynomial encodes runs of a fixed universal automaton.
- The "evaluation lemma" looks inside the circuit at the low-degree part. Correctness of an accelerator is a family of polynomial identities, so it survives reduction to a finite field.
- The bound is limited by the condition (log v)^{O(a)} ≤ v and gives 2^{c(log m)²/log log m}.
- Constants depend on μ, for which the proof gives **no value**. That is why m₀ is not explicit.

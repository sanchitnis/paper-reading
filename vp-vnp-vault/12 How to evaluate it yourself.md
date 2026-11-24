---
tags: [vp-vnp, verification, howto]
---
# How to evaluate it yourself

## Level 1: 30 minutes, no Lean skill required
Read `Statement.lean` (98 lines, printed in paper §3). Check, in order:

1. **`Computes`**: a list of `s` polynomials, each a variable, a constant, or the sum or product of two *earlier* entries; target appears in the list. Does it allow any cheating (e.g. unlimited constants for free)? Constants count as gates here. Standard.
2. **`perm` and `hc`**: sum over permutations of Πᵢ X(σ i, i) (perm) and over *single-cycle* permutations (hc). The index convention is transposed relative to the paper's x_{i,σ(i)}. This only renames variables.
3. **`VP`**: variables, degree and circuit size all ≤ n^a + a. Matches Valiant's definition.
4. **`VNP`**: sum over Boolean vectors e of a VP polynomial g(x,e). Matches.
5. **`Beyond`**: m^{c·(log₂ m)^{1/3}} < s. Check the precedence: `Real.logb 2 m ^ (1/3)` should parse as (log₂ m)^{1/3}. In Lean, function application binds tighter than `^`, so it does.
6. **`MainTheorem`**: ∃ c>0, ∀ characteristic p, ∃ m₀, ∀ fields F of char p, ∀ m ≥ m₀, … Check that no quantifier is vacuous (for instance that the set of fields isn't empty).

*My own pass through these found nothing obviously off, but a read by me is **not** verification. Review by a specialist is.*

## Level 2: a few hours, Lean installed
- Build the repo; run `#print axioms` on the main theorem. Expect only `propext`, `Classical.choice`, `Quot.sound`.
- Run the Comparator on `Challenge.lean` vs `Solution.lean` (Appendix Q.1 says it accepted them and that nanoda re-checked; see also `scripts/PrintAxioms.lean`).
- Grep for `sorry`, `axiom`, `native_decide`, `unsafe`, `implemented_by`.

## Level 3: months, specialist
- Read the proof for the two cases: [[06 Flat case]] and [[07 Contracting case]].
- Test against barriers: relativization, algebrization, algebraic natural proofs ([[05 Proof architecture]]).
- Sanity-check by seeing where the proof **must** break: for the determinant (reduction step P) and for Boolean circuits (inspection steps C). The paper explains both in §2.5 ([[08 What the result does not say]]).
- Check that Remark N.6 follows from Theorem 1.4, since it has no Lean proof.

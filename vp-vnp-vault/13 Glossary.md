---
tags: [vp-vnp, glossary]
---
# Glossary

- **Arithmetic circuit**: DAG of + and × gates over a field; size = number of gates.
- **VP**: polynomial families with polynomial-size circuits (and polynomial degree).
- **VNP**: exponential sums of VP families.
- **Permanent**: Σ_σ Π x_{i,σ(i)}. The determinant without signs. VNP-complete when char ≠ 2.
- **Hamiltonian cycle polynomial (HC)**: sum over single-cycle permutations. VNP-complete in every characteristic.
- **Characteristic**: smallest n with 1+…+1 (n times) = 0 in the field; 0 for ℝ, ℂ.
- **Clause sum**: sum over bit vectors of products of local weights. The kind of polynomial the permanent can simulate.
- **Tensor**: multi-dimensional array of numbers; a multilinear polynomial's coefficients form one.
- **Restriction (of tensors)**: apply linear maps on each index.
- **Rank across a split**: ordinary matrix rank after grouping the indices into two sets.
- **Spectral point (Strassen)**: a multiplicative, sub-additive function on tensors, monotone under restriction. Used here as a "price".
- **Price / metric dφ**: distance between "parties" induced by a spectral point; log φ of a wire = size × distance.
- **CAT(0) / non-positive curvature**: metric-space notion of "no more curved than flat". The Bruhat–Tits inequality is its quadrilateral form.
- **Flat vs contracting hypothesis**: the two cases of the proof ([[06 Flat case]], [[07 Contracting case]]).
- **Border complexity / approximate computation**: computing f as a limit of polynomials computed by small circuits (ε → 0).
- **Determinantal complexity**: smallest d such that f is a projection of the d×d determinant.
- **Geometric Complexity Theory (GCT)**: Mulmuley–Sohoni programme using representation theory and orbit closures.
- **Lean 4 / Mathlib**: proof assistant and its maths library.
- **Comparator / nanoda**: tools for checking a proof against a fixed statement, and an independent proof re-checker.
- **Statement fidelity**: whether the formal theorem says what the informal claim says.

---
tags: [vp-vnp, scope]
---
# What the result does not say

## 1. Not P ≠ NP
*(paper)* The bound is for arithmetic circuits that must compute the polynomial symbolically. A Boolean circuit for HCₘ amounts to an arithmetic circuit over 𝔽₂ that only needs to be right on inputs 0 and 1. It may compute any polynomial g = HCₘ + Σ (xᵢ² − xᵢ)hᵢ, and the theorem says nothing about such g.

The proof breaks at the two steps that look inside the circuit (marked "C" in the paper's Figure 1). The example the paper gives: (x₁₁² − x₁₁)·x₂₁⋯x_k1 vanishes on all 0/1 inputs, but its multilinear part is −x₁₁x₂₁⋯x_k1. The parts that the proof reads off are not the parts of HC.

Direction of known implications: VP = VNP ⇒ (roughly) P/poly = NP/poly. The converse is not known. So a *separation* in the algebraic world gives no direct Boolean separation.

## 2. Why the determinant escapes
The determinant is very similar to the permanent but has polynomial-size circuits, so the proof must fail for it. The paper says it fails at one place only: **the reduction from clause sums to the permanent**. Consequence: the paper's polynomials have no comparable-size reduction to determinants.

## 3. Characteristic 2
Permanent = determinant there, so only HC is covered. HC's reduction needs no division and works in every field.

## 4. Not a tight bound
Quasi-polynomial 2^{(log m)^{4/3}} versus an exponential upper bound 2^{O(m)}. The paper says "plenty of room".

## 5. No practical algorithms change
Evaluating the permanent of a 0/1 matrix is #P-complete, which is a Boolean statement. This paper does not alter what you can compute in practice.

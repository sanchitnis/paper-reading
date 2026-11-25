---
tags: [agrawal-vinay-2008, background, history]
aliases: [Foundations and context]
---
# Foundations and Context

## 1. The P vs NP Quest in the Algebraic Realm

In 1979, Leslie Valiant formulated the algebraic analogue of the $P \text{ vs } NP$ question. While classical computer science operates on bits ($0$ and $1$) using Boolean logic gates ($	ext{AND}, 	ext{OR}, 	ext{NOT}$), algebraic complexity operates over mathematical fields $\mathbb{F}$ (such as $\mathbb{Q}, \mathbb{R}, \mathbb{C}$, or finite fields $\mathbb{F}_p$) using arithmetic operations ($+$ and $\times$).

Valiant identified two benchmark polynomial families defined on an $n \times n$ matrix $X$:
1. **The Determinant**: Computable by small arithmetic circuits (size $O(n^3)$ via Gaussian elimination). It characterizes the class **VP** (Valiant's P).
2. **The Permanent**: Appears structurally identical, but lacks sign cancellations. It is complete for the counting class $\#P$ and Valiant's class **VNP**.

Valiant conjectured that $\mathrm{VP} \neq \mathrm{VNP}$, meaning the Permanent requires superpolynomial-sized arithmetic circuits.

---

## 2. The Quest for Lower Bounds and the "Depth" Obstacle

For decades, proving that an explicit polynomial cannot be computed by a small circuit proved immensely difficult:
- **Depth 2 ($\Sigma\Pi$)**: Every polynomial can be expanded into monomials (sum of products). But the permanent has $n!$ monomials, so any depth-2 circuit has size $\ge n! = 2^{\Omega(n \log n)}$. This was too weak to say anything about deeper, recursive computation.
- **Depth 3 ($\Sigma\Pi\Sigma$)**: In the late 1990s and 2000s, researchers attacked depth-3 circuits:
  - *Shpilka & Wigderson (1999)* proved quadratic lower bounds over $\mathbb{Q}$.
  - *Grigoriev & Razborov (2000)* proved exponential lower bounds over finite fields.
  - *Kayal & Saxena (2007)* developed polynomial identity tests for depth-3 circuits.

### The Stalling Point
Researchers wondered: *Why are all the breakthroughs stuck at depth 3? Why hasn't anyone proved similar bounds for depth 4, 5, or 6?*

The answer was elusive until Agrawal and Vinay realized that depth 3 and depth 4 are fundamentally on opposite sides of a computational precipice:
- The **Determinant** requires *exponential* size on depth-3 circuits over finite fields (Grigoriev & Razborov).
- But the **Determinant** can be computed by a **depth-4 circuit of subexponential size** $n^{O(\sqrt{n})} = 2^{o(n)}$!
- Thus, depth 4 is already powerful enough to efficiently compute VP-complete polynomials!

---

## 3. Polynomial Identity Testing (PIT) & The Kabanets-Impagliazzo Bridge

In 2004, Valentine Kabanets and Russell Impagliazzo discovered a profound duality:
$$\text{Efficient Deterministic PIT} \iff \text{Proving Circuit Lower Bounds}$$
If you can deterministically check whether an arithmetic circuit computes the identically zero polynomial without evaluating it on random inputs, you can prove arithmetic circuit lower bounds (and vice versa).

Agrawal and Vinay aimed to bridge this connection directly to depth-4 circuits: derandomizing depth-4 PIT would yield derandomization of general arithmetic circuits.

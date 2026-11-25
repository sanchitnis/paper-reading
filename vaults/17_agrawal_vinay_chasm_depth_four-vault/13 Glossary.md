---
tags: [agrawal-vinay-2008, glossary, definitions]
aliases: [Glossary]
---
# Glossary: Foundational Terms in Algebraic Complexity

### Arithmetic Circuit
A directed acyclic graph (DAG) where internal nodes are addition ($+$) or multiplication ($\times$) gates, and leaves are variables or constants from a field $\mathbb{F}$.

### Black-Box Algorithm
An algorithm that interacts with an arithmetic circuit solely by querying it on chosen input values and observing the output, without reading its internal wiring.

### Clow (Closed Walk)
A closed walk in a directed graph where the minimum vertex index appears exactly once. Introduced by Mahajan and Vinay (1997) to compute the determinant combinatorially without division.

### Degree (of a Gate / Circuit)
The maximum formal algebraic degree of the polynomial computed at a gate or output.

### Depth (of a Circuit)
The length of the longest directed path from any input variable to the output gate.

### Depth Reduction
A mathematical theorem showing that a circuit of arbitrary depth can be transformed into a shallow circuit of small depth while controlling the increase in size.

### Determinant ($\det$)
The unique alternating multilinear function of an $n \times n$ matrix measuring oriented hypervolume scaling. Computable in $O(n^3)$ operations; belongs to class VP.

### Fan-in
The number of incoming edges feeding into a gate.

### Homogeneous Polynomial / Circuit
A polynomial where every monomial has the exact same total degree. A circuit is homogeneous if every internal gate computes a homogeneous polynomial.

### Permanent ($\operatorname{perm}$)
The matrix function defined identically to the determinant but without permutation signs. Complete for class VNP and $\#P$.

### Polynomial Identity Testing (PIT)
The algorithmic problem of determining whether an arithmetic circuit computes the zero polynomial.

### Proof Tree
A subcircuit obtained by choosing exactly one incoming wire for each addition gate and keeping all wires for multiplication gates. Computes a single monomial.

### Size (of a Circuit)
The total number of gates (or edges) in an arithmetic circuit.

### VP (Valiant's P)
The complexity class of polynomial families of polynomial degree computable by polynomial-sized arithmetic circuits.

### VNP (Valiant's NP)
The complexity class of polynomial families expressible as exponential projection sums of VP polynomials.

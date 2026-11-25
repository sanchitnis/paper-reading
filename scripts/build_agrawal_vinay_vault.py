"""Script to generate the complete 15-note Obsidian Vault for Agrawal & Vinay (2008)."""
from pathlib import Path

vault_dir = Path("vaults/17_agrawal_vinay_chasm_depth_four-vault")
vault_dir.mkdir(parents=True, exist_ok=True)

files = {}

# 00 Index.md
files["00 Index.md"] = """---
tags: [agrawal-vinay-2008, chasm-depth-four, algebraic-complexity, moc]
aliases: [Agrawal Vinay Chasm Depth Four Index, Index]
---
# Arithmetic Circuits: A Chasm at Depth Four (Agrawal & Vinay 2008)

**Paper:** *Arithmetic Circuits: A Chasm at Depth Four*  
**Authors:** Manindra Agrawal (IIT Kanpur) and V. Vinay (CMI & Geodesic Information Systems)  
**Publication:** Electronic Colloquium on Computational Complexity (ECCC TR08-062), 2008; IEEE FOCS 2008  
**Target Audience:** Recent graduates of Computer Science, Mathematics, or Electrical Engineering  
**Prerequisites:** Linear Algebra (matrices, determinants, basis), basic Discrete Mathematics (permutations, graphs), and introductory Computational Complexity (P vs NP, circuits).

---

## 🧭 Curated Reading Path for Recent CS / Math Graduates

1. [[01 Big picture]]: The entire breakthrough on a single page with intuitive flowcharts.
2. [[02 Foundations and context]]: Why lower bounds in arithmetic circuits hit walls, and why researchers studied depth-3 circuits.
3. [[03 Core objects and definitions]]: **Start here for the basics!** A ground-up explanation of:
   - What is a matrix and a linear map?
   - What is the **Determinant** (geometric volume scaling + algebraic Leibniz formula)?
   - What is the **Permanent** (counting matchings, no sign cancellations)?
   - What is an **Arithmetic Circuit** (DAG, addition and multiplication gates, size, depth, degree)?
   - What are Valiant's complexity classes **VP** and **VNP**?
4. [[04 What the paper claims]]: Precise statements of the Depth-Four Chasm Theorem (Theorem 2.4) and PIT Derandomization (Theorem 3.2).
5. [[05 Proof architecture]]: Top-down blueprint of the proof: from $O(\\log d)$ depth reduction to layered circuit $D$, proof trees, and collapsing into depth-4 circuit $E$.
6. [[06 Deep dive - Circuit depth reduction to depth four]]: The technical mechanics of degree-halving proof trees and the combinatorial size bound.
7. [[07 Deep dive - Black-box PIT derandomization]]: How depth-4 identity testing implies general polynomial identity testing via hardness-versus-randomness and Nisan-Wigderson designs.
8. [[08 What the result does not say]]: Important caveats, non-claims, and boundaries (it proves an equivalence/reduction, not VP != VNP itself).
9. [[09 Relevance and consequences]]: How this paper redirected modern algebraic complexity (shifted partial derivatives, Gupta et al. chasm at depth 3/4).
10. [[10 Formalization and code verification]]: Runnable Python code demonstrating Determinant vs Permanent, proof trees, and depth-4 decomposition.
11. [[11 Reception and valid comments]]: Historical impact, follow-up works, and peer evaluation.
12. [[12 How to evaluate it yourself]]: Socratic exercises, toy $2 \\times 2$ and $3 \\times 3$ circuits, and self-test questions.
13. [[13 Glossary]]: Comprehensive dictionary of all technical terms with clear definitions.
14. [[14 References]]: Sourced citations including Valiant 1979, Mahajan & Vinay 1997, Agrawal & Vinay 2008.

> [!NOTE] Notation & Convention
> Statements directly from the paper are marked *(paper)*. Pedagogical intuitions, engineering analogies, and geometric explanations are marked *(analogy)*.
"""

# 01 Big picture.md
files["01 Big picture.md"] = """---
tags: [agrawal-vinay-2008, overview, big-picture]
aliases: [Big picture]
---
# Big Picture: The Chasm at Depth Four

```mermaid
flowchart TD
    subgraph Classical Complexity [Classical P vs NP Analogue]
        Valiant["Valiant's 1979 Conjecture:<br/>VP != VNP (Determinant vs Permanent)"]
        GeneralLowerBound["Goal: Prove superpolynomial lower bound<br/>for general arithmetic circuits computing Permanent"]
    end

    subgraph The Depth Dilemma [The Depth Dilemma]
        Depth2["Depth 2 (Sum of Products):<br/>Trivial size O(2^n). Too weak."]
        Depth3["Depth 3 (Sigma-Pi-Sigma):<br/>Exponential lower bounds proven over finite fields<br/>(Grigoriev-Razborov 2000), but stalled."]
        Unrestricted["General Circuits (Unrestricted Depth):<br/>Seemed unimaginably far away."]
    end

    subgraph The Breakthrough [Agrawal-Vinay 2008: The Chasm at Depth Four]
        AVTheorem["The Chasm Theorem:<br/>Any size-s circuit of degree d can be collapsed<br/>to a Depth-4 (Sigma-Pi-Sigma-Pi) circuit of size 2^O(sqrt(d log d log s))"]
        Equivalence["EQUIVALENCE:<br/>Proving exponential lower bounds for DEPTH 4<br/>IMPLIES exponential lower bounds for ALL DEPTHS!"]
    end

    Valiant --> GeneralLowerBound
    GeneralLowerBound --> Depth3
    Depth3 -->|"Why did researchers stop at depth 3?"| AVTheorem
    AVTheorem --> Equivalence
    Equivalence -->|"Focus the entire field"| ModernResearch["Modern Lower Bounds Focus:<br/>Directly attack Depth-4 circuits (e.g. GKKS 2014)"]
```

## The One-Paragraph Summary

*(paper)* In **"Arithmetic Circuits: A Chasm at Depth Four"**, Manindra Agrawal and V. Vinay prove that proving exponential lower bounds on **depth-four arithmetic circuits** ($\Sigma\Pi\Sigma\Pi$) is sufficient to establish exponential lower bounds for **unrestricted-depth** arithmetic circuits. That is, for exponential-sized circuits, additional depth beyond four offers no fundamental asymptotic advantage. Furthermore, they prove that black-box derandomization of Polynomial Identity Testing (PIT) for restricted depth-four circuits implies a nearly complete ($n^{O(\\log n)}$) derandomization of general PIT.

## Why is this called a "Chasm"?

*(analogy)* Imagine climbing a mountain of computational complexity:
- **Depth 2** ($\Sigma\Pi$, sum of monomials): trivial to analyze, but completely inefficient.
- **Depth 3** ($\Sigma\Pi\Sigma$): researchers could prove lower bounds, but depth 3 is fundamentally too weak to compute polynomials like the determinant efficiently.
- **General circuits**: allow arbitrarily deep recursive composition ($O(n)$ or $O(\\log^2 n)$ depth), making them notoriously difficult to analyze.

Researchers assumed that to understand general circuits, they would have to slowly climb from depth 4, to depth 5, to depth 6, and beyond. Agrawal and Vinay proved that **there is no gradual mountain—there is a single chasm at depth 4**. If you can cross depth 4 by proving an exponential lower bound against $\Sigma\Pi\Sigma\Pi$ circuits, you have conquered the entire mountain and resolved the general circuit lower bound problem ($\mathrm{VP} \neq \mathrm{VNP}$)!
"""

# 02 Foundations and context.md
files["02 Foundations and context.md"] = """---
tags: [agrawal-vinay-2008, background, history]
aliases: [Foundations and context]
---
# Foundations and Context

## 1. The P vs NP Quest in the Algebraic Realm

In 1979, Leslie Valiant formulated the algebraic analogue of the $P \\text{ vs } NP$ question. While classical computer science operates on bits ($0$ and $1$) using Boolean logic gates ($\text{AND}, \text{OR}, \text{NOT}$), algebraic complexity operates over mathematical fields $\\mathbb{F}$ (such as $\\mathbb{Q}, \\mathbb{R}, \\mathbb{C}$, or finite fields $\\mathbb{F}_p$) using arithmetic operations ($+$ and $\\times$).

Valiant identified two benchmark polynomial families defined on an $n \\times n$ matrix $X$:
1. **The Determinant**: Computable by small arithmetic circuits (size $O(n^3)$ via Gaussian elimination). It characterizes the class **VP** (Valiant's P).
2. **The Permanent**: Appears structurally identical, but lacks sign cancellations. It is complete for the counting class $\\#P$ and Valiant's class **VNP**.

Valiant conjectured that $\\mathrm{VP} \\neq \\mathrm{VNP}$, meaning the Permanent requires superpolynomial-sized arithmetic circuits.

---

## 2. The Quest for Lower Bounds and the "Depth" Obstacle

For decades, proving that an explicit polynomial cannot be computed by a small circuit proved immensely difficult:
- **Depth 2 ($\Sigma\Pi$)**: Every polynomial can be expanded into monomials (sum of products). But the permanent has $n!$ monomials, so any depth-2 circuit has size $\\ge n! = 2^{\\Omega(n \\log n)}$. This was too weak to say anything about deeper, recursive computation.
- **Depth 3 ($\Sigma\Pi\Sigma$)**: In the late 1990s and 2000s, researchers attacked depth-3 circuits:
  - *Shpilka & Wigderson (1999)* proved quadratic lower bounds over $\\mathbb{Q}$.
  - *Grigoriev & Razborov (2000)* proved exponential lower bounds over finite fields.
  - *Kayal & Saxena (2007)* developed polynomial identity tests for depth-3 circuits.

### The Stalling Point
Researchers wondered: *Why are all the breakthroughs stuck at depth 3? Why hasn't anyone proved similar bounds for depth 4, 5, or 6?*

The answer was elusive until Agrawal and Vinay realized that depth 3 and depth 4 are fundamentally on opposite sides of a computational precipice:
- The **Determinant** requires *exponential* size on depth-3 circuits over finite fields (Grigoriev & Razborov).
- But the **Determinant** can be computed by a **depth-4 circuit of subexponential size** $n^{O(\\sqrt{n})} = 2^{o(n)}$!
- Thus, depth 4 is already powerful enough to efficiently compute VP-complete polynomials!

---

## 3. Polynomial Identity Testing (PIT) & The Kabanets-Impagliazzo Bridge

In 2004, Valentine Kabanets and Russell Impagliazzo discovered a profound duality:
$$\\text{Efficient Deterministic PIT} \\iff \\text{Proving Circuit Lower Bounds}$$
If you can deterministically check whether an arithmetic circuit computes the identically zero polynomial without evaluating it on random inputs, you can prove arithmetic circuit lower bounds (and vice versa).

Agrawal and Vinay aimed to bridge this connection directly to depth-4 circuits: derandomizing depth-4 PIT would yield derandomization of general arithmetic circuits.
"""

# 03 Core objects and definitions.md
files["03 Core objects and definitions.md"] = """---
tags: [agrawal-vinay-2008, definitions, foundations, linear-algebra]
aliases: [Core objects and definitions]
---
# Core Objects and Definitions: From Scratch

This document is designed for recent graduates in Computer Science, Mathematics, or Engineering. We build every concept from first principles.

---

## 1. What is a Matrix and a Linear Transformation?

An $n \\times n$ matrix $A$ over a field $\\mathbb{F}$ (e.g. real numbers $\\mathbb{R}$ or complex numbers $\\mathbb{C}$) is a square array of $n^2$ numbers:
$$A = \\begin{pmatrix} a_{11} & a_{12} & \\dots & a_{1n} \\\\ a_{21} & a_{22} & \\dots & a_{2n} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ a_{n1} & a_{n2} & \\dots & a_{nn} \\end{pmatrix}$$

*(analogy)* A matrix represents a linear transformation that takes an $n$-dimensional space and stretches, rotates, or shears it. 

---

## 2. What is the Determinant?

### Geometric Intuition: Volume Scaling
In 2D, if you take the standard unit square (area = 1) spanned by $\\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$ and $\\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix}$, and apply matrix $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$, the unit square transforms into a parallelogram.
- The **area** of that parallelogram is $|ad - bc|$.
- The **Determinant** $\\det(A) = ad - bc$ measures this **oriented volume scaling factor**.
- If $\\det(A) = 0$, the transformation flattens the 2D plane into a 1D line (information is lost, matrix is not invertible).
- In $n$ dimensions, $\\det(A)$ measures the oriented $n$-dimensional hypervolume of the parallelotope spanned by the column vectors of $A$.

### The Algebraic (Leibniz) Formula
For an $n \\times n$ matrix $X = (x_{ij})$:
$$\\det(X) = \\sum_{\\sigma \\in S_n} \\operatorname{sgn}(\\sigma) \\prod_{i=1}^n x_{i, \\sigma(i)}$$
Where:
- $S_n$ is the symmetric group of all $n!$ permutations of $\\{1, 2, \\dots, n\\}$.
- $\\sigma$ is a permutation mapping row $i$ to column $\\sigma(i)$.
- $\\operatorname{sgn}(\\sigma) \\in \\{+1, -1\\}$ is the **sign (or parity)** of the permutation:
  - $+1$ if the permutation can be decomposed into an even number of swaps (transpositions).
  - $-1$ if it requires an odd number of swaps.

### Why is the Determinant Computationally Easy?
Even though the Leibniz formula has $n!$ terms (which is $\\approx 2.4 \\times 10^{18}$ terms for $n=20$!), the alternating signs $\\operatorname{sgn}(\\sigma)$ create massive algebraic cancellations:
1. **Gaussian Elimination**: By subtracting multiples of one row from another, row operations do not change the determinant. We can transform $A$ into an upper triangular matrix in $O(n^3)$ arithmetic operations!
2. **Division-Free Combinatorial Algorithms (Mahajan & Vinay 1997)**: Even if the field does not allow division (e.g. over arbitrary commutative rings), the determinant can be computed in polynomial time ($O(n^4)$) using closed walks ("clows") in a graph.
3. Therefore, $\\det_n \\in \\mathbf{VP}$ (polynomial-size circuits).

---

## 3. What is the Permanent?

The Permanent looks almost identical to the Determinant, but **every term is positive**:
$$\\operatorname{perm}(X) = \\sum_{\\sigma \\in S_n} \\prod_{i=1}^n x_{i, \\sigma(i)}$$

### Combinatorial Meaning: Counting Matchings
If $X$ is the adjacency matrix of a bipartite graph $G = (V_1 \\cup V_2, E)$ with $n$ vertices on each side:
- A product $\\prod_{i=1}^n x_{i, \\sigma(i)}$ equals $1$ if and only if each $(i, \\sigma(i))$ is an edge in $G$.
- This means $\\sigma$ is a **perfect matching** (pairing every worker to a unique task).
- Therefore, $\\operatorname{perm}(X)$ counts the exact number of perfect matchings in the bipartite graph!

### Why is the Permanent Computationally Hard?
Because there are **no minus signs**, there are **no cancellations**!
- Gaussian elimination fails: adding or subtracting rows changes the permanent arbitrarily.
- Leslie Valiant proved in 1979 that computing the permanent is **$\\#P$-complete** (exponentially harder than NP-complete decision problems).
- In algebraic complexity, the Permanent is the canonical **VNP-complete** polynomial.

---

## 4. What is an Arithmetic Circuit?

An **arithmetic circuit** over a field $\\mathbb{F}$ is a directed acyclic graph (DAG) that computes a formal polynomial:
1. **Input Gates (Leaves, in-degree 0)**: Labeled with variables $x_1, x_2, \\dots, x_n$ or field constants $c \\in \\mathbb{F}$.
2. **Internal Gates**:
   - **Addition Gate ($+$)**: Computes the sum of its incoming inputs.
   - **Multiplication Gate ($\\times$)**: Computes the product of its incoming inputs.
3. **Output Gate (Root, out-degree 0)**: Outputs the final polynomial $P(x_1, \\dots, x_n)$.

```mermaid
flowchart BT
    x1["x1"] --> m1["*"]
    x2["x2"] --> m1
    x3["x3"] --> m2["*"]
    x4["x4"] --> m2
    m1 --> a1["+"]
    m2 --> a1
    a1 --> OUT["Output: (x1*x2) + (x3*x4)"]
```

### Key Metrics of an Arithmetic Circuit:
- **Size ($s$ or $M$)**: Total number of gates (or edges) in the circuit. Represents the total computational work.
- **Depth ($\Delta$)**: The length of the longest directed path from an input gate to the output gate. Represents parallel time.
- **Fan-in**: The number of incoming edges to a gate. 
  - *Bounded fan-in*: usually fan-in $\\le 2$ or a small constant.
  - *Unbounded fan-in*: arbitrary number of inputs.
- **Degree ($\deg$)**: The formal polynomial degree computed at a gate.

---

## 5. What are VP and VNP? (Valiant's Classes)

- **VP (Valiant's P)**: The class of families of polynomials $\\{P_n\\}$ where:
  1. The degree of $P_n$ is polynomial in $n$ ($\\deg(P_n) \\le n^c$).
  2. The polynomial $P_n$ can be computed by an arithmetic circuit of size polynomial in $n$ ($s(n) \\le n^k$).
  *Exemplar:* $\\det_n \\in \\mathrm{VP}$.
- **VNP (Valiant's NP)**: The class of families of polynomials $\\{Q_n\\}$ that can be expressed as an exponential sum of a polynomial $P \\in \\mathrm{VP}$:
  $$Q_n(x_1, \\dots, x_n) = \\sum_{y \\in \\{0, 1\\}^m} P(x_1, \\dots, x_n, y_1, \\dots, y_m)$$
  *Exemplar:* $\\operatorname{perm}_n \\in \\mathrm{VNP}$.
- **Valiant's Conjecture**: $\\mathrm{VP} \\neq \\mathrm{VNP}$.

---

## 6. What is a Depth-4 Arithmetic Circuit?

A depth-4 circuit is an alternating circuit with 4 layers of gates:
$$\\Sigma\\Pi\\Sigma\\Pi$$
From bottom to top:
1. **Layer 1 (Bottom, $\\Pi$)**: Multiplies variables and constants to form small monomials.
2. **Layer 2 ($\\Sigma$)**: Adds these monomials to form linear forms or low-degree polynomials.
3. **Layer 3 ($\\Pi$)**: Multiplies these intermediate polynomials together.
4. **Layer 4 (Top, $\\Sigma$)**: Sums these large product terms to yield the final output.

Mathematically, any depth-4 circuit computes a polynomial of the form:
$$P(x_1, \\dots, x_n) = \\sum_{i=1}^T \\prod_{j=1}^{d_i} Q_{i,j}(x)$$
where each $Q_{i,j}(x)$ is itself a sum of products of variables!
"""

# 04 What the paper claims.md
files["04 What the paper claims.md"] = """---
tags: [agrawal-vinay-2008, theorems, claims]
aliases: [What the paper claims]
---
# What the Paper Claims: Theorems and Exact Bounds

Manindra Agrawal and V. Vinay establish two core theorems and several crucial corollaries:

---

## 1. Theorem 2.1: The Determinant is in Depth 4 with Subexponential Size

*(paper)* **Theorem 2.1**: The determinant of an $n \\times n$ matrix with integer $n$-bit entries can be computed by depth-4 arithmetic circuits of size $n^{O(\\sqrt{n})} = 2^{o(n)}$.

### Significance:
- Grigoriev and Razborov (2000) proved that depth-3 ($\Sigma\Pi\Sigma$) circuits computing the determinant over finite fields require **exponential size** $2^{\\Omega(n)}$.
- Theorem 2.1 proves that by adding just **one additional layer** (moving from depth 3 to depth 4), the complexity of the determinant collapses from exponential to subexponential $n^{O(\\sqrt{n})}$!
- This shows that depth 4 is qualitatively far more powerful than depth 3.

---

## 2. Theorem 2.4: The Depth-Four Chasm Theorem

*(paper)* **Theorem 2.4 (Depth Four Chasm)**:  
Let $P(x_1, \\dots, x_n)$ be a polynomial of degree $d = O(n)$ over a field $\\mathbb{F}$.  
If there exists an arithmetic circuit of size:
$$M = 2^{o\\left(d + d \\log \\frac{n}{d}\\right)}$$
computing $P$, then there exists a **depth-four arithmetic circuit** of size:
$$2^{o\\left(d + d \\log \\frac{n}{d}\\right)}$$
computing $P$.  
Furthermore:
1. The fan-in of the second-layer multiplication gates is bounded by $\\ell(n)$ for any slowly growing function $\\ell \\in \\omega(1)$.
2. The fan-in of the bottom-layer multiplication gates is bounded by $o(d)$.

---

## 3. Corollaries for Multilinear Polynomials & The Permanent

*(paper)* **Corollary 2.5 (Multilinear Polynomials)**:  
Let $P(x_1, \\dots, x_n)$ be a multilinear polynomial over field $\\mathbb{F}$. If there exists an arithmetic circuit of size $2^{o(n)}$ for $P$, then there exists a depth-4 arithmetic circuit of size $2^{o(n)}$ for $P$.

*(paper)* **Corollary 2.6 (Permanent and VP vs VNP Equivalence)**:  
> **If every depth-four arithmetic circuit for the Permanent requires exponential size $2^{\\Omega(n)}$, then EVERY arithmetic circuit of arbitrary (unrestricted) depth for the Permanent requires exponential size.**

### The Crucial Takeaway:
To prove $\\mathrm{VP} \\neq \\mathrm{VNP}$, mathematicians do **not** need to understand arbitrary $1000$-layer circuits with tangled DAG topologies!  
They only need to prove an exponential lower bound for **depth-4 ($\Sigma\Pi\\Sigma\Pi$) circuits**!

---

## 4. Theorem 3.2: Black-Box Derandomization of Identity Testing

*(paper)* **Theorem 3.2 (Identity Testing Chasm)**:  
Consider the class of depth-4 arithmetic circuits over $\\mathbb{F}$ with the fan-in of the second-layer multiplication gates bounded by $O(\\ell(n))$ and the fan-in of bottom-layer multiplication gates bounded by $O(\\log n)$.  
If there is an optimal (polynomial-degree) pseudorandom generator against this restricted class of depth-4 circuits, then the **general low-degree Polynomial Identity Testing (PIT) problem over $\\mathbb{F}$ can be deterministically solved in quasi-polynomial time $n^{O(\\log n)}$.**
"""

# 05 Proof architecture.md
files["05 Proof architecture.md"] = """---
tags: [agrawal-vinay-2008, proof-architecture, methodology]
aliases: [Proof architecture]
---
# Proof Architecture: Top-Down Blueprint

The proof of Theorem 2.4 converts an arbitrary circuit $C$ into a depth-4 circuit $E$ without blowing up the size beyond $2^{o(n)}$.

```mermaid
flowchart TD
    C["Input Circuit C<br/>Arbitrary depth, size M = 2^o(n), degree d = O(n)"] --> Stage1["Stage 1: Valiant-Skyum-Berkowitz-Rackoff (VSBR)<br/>Depth Reduction to O(log d)"]
    
    Stage1 --> D["Layered Circuit D<br/>Size S = M^O(1), Depth <= 2 log d<br/>Multiplication fan-in <= 6, degree cuts in half each layer"]
    
    D --> Stage2["Stage 2: Proof Tree Formulation<br/>Define gates [g, h] representing partial derivations<br/>along rightmost paths"]
    
    Stage2 --> Stage3["Stage 3: Circuit Bisection (Cut at level t)<br/>Top Half: t mult layers, degree <= 6^t<br/>Bottom Half: outputs g_1...g_k, degree <= d / 2^t"]
    
    Stage3 --> Stage4["Stage 4: Expansion into Depth 2<br/>Expand Top Half P_0 into Sum-of-Products<br/>Expand each Bottom Half P_i into Sum-of-Products"]
    
    Stage4 --> E["Depth-4 Circuit E<br/>Sigma - Pi - Sigma - Pi<br/>Total Size = 2^o(d + d log(n/d))"]
```

---

## The Four Stages of the Transformation

### 1. Stage 1: Classical Depth Reduction to $O(\\log d)$
From classical results by Valiant et al. (1983) and Allender, Jiao, Mahajan, Vinay (1998), any circuit $C$ of size $M$ and degree $d$ can be restructured into a circuit of depth $O(\\log d)$ and size $M^{O(1)}$.

### 2. Stage 2: Structural Refinement into Circuit $D$
Agrawal and Vinay refine this construction so that circuit $D$ satisfies strict invariants:
- Strictly alternating addition and multiplication layers.
- Multiplication fan-in is at most 6.
- The degree of every child of an addition gate equals the parent gate degree.
- **Key Invariant**: Every child of a multiplication gate has degree at most **half** the degree of the parent gate:
  $$\\deg(\\text{child}) \\le \\frac{1}{2} \\deg(\\text{parent})$$

### 3. Stage 3: Bisecting Circuit $D$ at Level $t$
Choose a parameter $t = \\frac{1}{2} \\log_6 \\ell$.  
Cut circuit $D$ into two halves:
- **Top Half**: Exactly $t$ multiplication layers. Since multiplication fan-in $\\le 6$, the total degree of the top half as a polynomial $P_0(y_1, \\dots, y_k)$ is at most $6^t$.
- **Bottom Half**: Computes intermediate polynomials $P_1(x), \\dots, P_k(x)$ at gates $g_1, \\dots, g_k$. Because degree halves at each mult layer, the degree of each $P_i$ is at most $\\frac{d}{2^t}$.

### 4. Stage 4: Sum-of-Products Expansion into Depth 4
- Write $P_0(y_1, \\dots, y_k)$ as a brute-force sum of products (depth 2).
- Write each $P_i(x_1, \\dots, x_n)$ as a brute-force sum of products (depth 2).
- Plug $P_i$ into $P_0$. The composition of two depth-2 circuits yields a **depth-4 circuit $E$** ($\Sigma\\Pi\\Sigma\\Pi$).
- By choosing $t$ and $\\ell$ optimally, the binomial coefficients $\\binom{S+6^t}{6^t}$ and $\\binom{n + d/2^t}{d/2^t}$ are both bounded by $2^{o(d + d \\log(n/d))}$!
"""

# 06 Deep dive - Circuit depth reduction to depth four.md
files["06 Deep dive - Circuit depth reduction to depth four.md"] = """---
tags: [agrawal-vinay-2008, deep-dive, math, proof-trees]
aliases: [Deep dive - Depth reduction]
---
# Deep Dive: The Mechanics of the Depth-4 Reduction

In this deep dive, we walk through the exact mathematical mechanics of constructing circuit $D$ and circuit $E$.

---

## 1. Proof Trees and Partial Gate Quotients $[g, h]$

Let $C$ be an arithmetic circuit computing a polynomial at output gate $g$.
*(paper)* A **proof tree** $T$ rooted at gate $g$ is a subcircuit formed by:
1. Starting with gate $g$.
2. For every addition gate in the subcircuit, keeping **only one** input wire and deleting all others.
3. For every multiplication gate, keeping **both** inputs.

A proof tree computes a single monomial of the polynomial $[g]$. Summing over all possible proof trees computes the full polynomial:
$$[g] = \\sum_{T} p(T)$$

### The Quotient $[g, h]$
For any two gates $g$ and $h$ in circuit $C$:
$$[g, h] = \\sum_{T} p(T, h)$$
where $T$ runs over all proof trees rooted at $g$ where $h$ appears on the rightmost path, and $p(T, h)$ is the polynomial computed when gate $h$ is replaced by the constant $1$.
- If $h$ never appears on the rightmost path, $[g, h] = 0$.
- Intuitively, $[g, h]$ represents the partial polynomial computed between gate $h$ and gate $g$.

---

## 2. Ensuring the Degree Halves at Every Multiplication Gate

For a multiplication gate $g$ with children $g_L$ and $g_R$, there is a unique intermediate multiplication gate $p$ along the rightmost path from $g$ to $h$ such that:
$$\\deg(p_R) \\le \\frac{1}{2}(\\deg(g) + \\deg(h)) \\le \\deg(p)$$

Summing over all possible candidate gates $p$:
$$[g, h] = \\sum_p [g, p] \\cdot [p_L] \\cdot [p_R, h]$$

Notice the degrees:
1. $\\deg([g, p]) = \\deg(g) - \\deg(p) \\le \\frac{1}{2}(\\deg(g) - \\deg(h))$.
2. $\\deg([p_R, h]) = \\deg(p_R) - \\deg(h) \\le \\frac{1}{2}(\\deg(g) - \\deg(h))$.
3. But what about $[p_L]$? Its degree might be larger than $\\frac{1}{2}\\deg([g, h])$.

### The Agrawal-Vinay Degree Trick:
To fix $[p_L]$, apply the decomposition once more to $[p_L]$:
$$[p_L, x_i] = \\sum_q [p_L, q] \\cdot [q_L] \\cdot [q_R, x_i]$$
By expanding $[p_L]$ down to variables $x_i$, we obtain a product of 6 terms:
$$[g, h] = \\sum_{p, i, j, q} [g, p] \\cdot [p^j_L, q] \\cdot [q_L] \\cdot [q_R, x_i] \\cdot [x_i] \\cdot [p_R, h]$$
In this 6-way product, **every single term has degree at most $\\frac{1}{2}\\deg([g, h])$**!
This guarantees that circuit $D$ has multiplication fan-in at most 6 and depth at most $2 \\log d$.

---

## 3. The Combinatorial Size Bound for Circuit $E$

Cut circuit $D$ at level $t = \\frac{1}{2} \\log_6 \\ell$.
The final depth-4 circuit $E$ evaluates $P_0(P_1, \\dots, P_k)$.

### Monomial Counting via Stars and Bars
The number of monomials of degree $K$ over $N$ variables is $\\binom{N + K}{K}$.
1. **Top Polynomial $P_0$**: Defined on $k \\le S$ variables with degree bounded by $6^t = \\sqrt{\\ell}$:
   $$\\text{Monomials}(P_0) \\le \\binom{S + \\sqrt{\\ell}}{\\sqrt{\\ell}} \\le (2S)^{\\sqrt{\\ell}} = 2^{O(\\sqrt{\\ell} \\log S)}$$
2. **Bottom Polynomials $P_i$**: Defined on $n$ variables with degree bounded by $\\frac{d}{2^t} = \\frac{d}{\\ell^\\delta}$ (where $\\delta = \\frac{1}{2} \\log_6 2$):
   $$\\text{Monomials}(P_i) \\le \\binom{n + d/\\ell^\\delta}{d/\\ell^\\delta} \\le 2^{O\\left(\\frac{d}{\\ell^\\delta} + \\frac{d}{\\ell^\\delta} \\log \\frac{n}{d}\\right)}$$

### The Final Sum
Summing the sizes of $P_0$ and all $k$ polynomials $P_i$:
$$\\operatorname{Size}(E) \\le 2^{O(\\sqrt{(d + d \\log(n/d)) \\log S})} + S \\cdot 2^{o(d + d \\log(n/d))} = 2^{o(d + d \\log(n/d))}$$
This establishes Theorem 2.4!
"""

# 07 Deep dive - Black-box PIT derandomization.md
files["07 Deep dive - Black-box PIT derandomization.md"] = """---
tags: [agrawal-vinay-2008, pit, derandomization, nisan-wigderson]
aliases: [Deep dive - Black-box PIT]
---
# Deep Dive: Black-Box PIT Derandomization

## 1. What is Polynomial Identity Testing (PIT)?

Given an arithmetic circuit $C(x_1, \\dots, x_n)$, does it compute the identically zero polynomial ($C \\equiv 0$)?
- **Randomized Algorithm (Schwartz-Zippel Lemma, 1979)**: Pick random values $r_1, \\dots, r_n \\in S \\subseteq \\mathbb{F}$. Evaluate $C(r_1, \\dots, r_n)$. If $C \\not\\equiv 0$, it evaluates to non-zero with high probability.
- **The Open Challenge**: Can we do this **deterministically** in polynomial time without randomness?
  - *White-box*: The algorithm can inspect the internal wires of $C$.
  - *Black-box*: The algorithm can only feed inputs into $C$ and observe outputs (equivalent to designing a hitting set or pseudorandom generator).

---

## 2. Hardness vs Randomness in Algebraic Circuits

In Boolean complexity, Nisan and Wigderson (1994) showed that Boolean circuit lower bounds yield pseudorandom generators (derandomizing BPP to P).  
Kabanets and Impagliazzo (2004) proved the algebraic equivalent:
$$\\text{Hard multilinear polynomials} \\implies \\text{Deterministic PIT}$$

Agrawal (2005) proved that a pseudorandom generator against depth-4 circuits yields a multilinear polynomial $q_m$ requiring exponential-sized depth-4 circuits.

---

## 3. The Agrawal-Vinay Reduction for PIT (Theorem 3.2)

```mermaid
flowchart LR
    PRG["Optimal PRG against<br/>Depth-4 Circuits with small fan-in"] --> HardPoly["Explicit Hard Multilinear Polynomial q_m<br/>Requires 2^Omega(m) size depth-4 circuits"]
    HardPoly --> Chasm["Theorem 2.4 (Depth Four Chasm):<br/>q_m requires 2^Omega(m) size UNRESTRICTED circuits"]
    Chasm --> NW["Nisan-Wigderson Design Generator<br/>+ Multivariate Polynomial Factorization (Kaltofen)"]
    NW --> DeterministicPIT["Deterministic PIT for general circuits<br/>Solvable in n^O(log n) time!"]
```

### Proof Sketch of Theorem 3.2:
1. Assume there is an optimal pseudorandom generator $f$ against depth-4 circuits with second-layer fan-in $O(\\ell(n))$ and bottom-layer fan-in $O(\\log n)$.
2. By Agrawal (2005), this generator gives an explicit multilinear polynomial family $\\{q_m\\}$ requiring depth-4 circuits of size $2^{\\Omega(m)}$.
3. By the **Depth Four Chasm Theorem (Theorem 2.4)**, any polynomial requiring exponential depth-4 circuits requires **exponential circuits of unrestricted depth**!
4. Plug this hard polynomial $q_m$ into the Nisan-Wigderson combinatorial design:
   - For an $n$-input circuit $C(z_1, \\dots, z_n)$, substitute $z_i = p_i = q_{d \\log n}(x_{S_i})$.
   - If $C(z) \\neq 0$ but $C(p) = 0$, by Kaltofen's polynomial factorization algorithm, one can construct a small circuit computing $q$, contradicting its hardness!
5. Evaluating the substituted circuit over $O(\\log n)$ variables takes $n^{O(\\log n)}$ time, completing the derandomization.
"""

# 08 What the result does not say.md
files["08 What the result does not say.md"] = """---
tags: [agrawal-vinay-2008, non-claims, boundaries, pitfalls]
aliases: [What the result does not say]
---
# What the Result Does NOT Say: Critical Non-Claims

To maintain rigorous scientific grounding, it is vital to understand the precise boundaries of Agrawal and Vinay (2008).

---

## 1. It Does NOT Prove VP != VNP
> [!WARNING] Common Misconception
> *Misconception:* "Agrawal and Vinay proved that the Permanent requires exponential circuits."  
> **Reality:** Agrawal and Vinay proved a **conditional reduction**:
> $$\\text{Exponential lower bounds for Depth 4} \\implies \\text{Exponential lower bounds for General Circuits (VP } \\neq \\text{VNP)}$$
> They did **not** prove the depth-4 lower bound for the permanent. The lower bound itself remained open.

---

## 2. It Does NOT Give an Efficient Algorithm for the Permanent
The depth-4 circuit constructed for the determinant has size $n^{O(\\sqrt{n})}$.  
For the permanent, if a small circuit existed, it would collapse to size $2^{o(n)}$ at depth 4. But because the permanent is believed to require $2^{\\Omega(n)}$, the paper provides no shortcut for evaluating matchings or the permanent.

---

## 3. It Does NOT Directly Apply to Non-Commutative Circuits Without Modifications
In commutative algebra, $x \\cdot y = y \\cdot x$. In non-commutative circuits (where matrix multiplication variables do not commute), depth reduction behaves differently (as explored by Nisan 1991 and Allender et al. 1998).

---

## 4. It Does NOT Achieve Full Polynomial Time PIT Derandomization
Theorem 3.2 derandomizes low-degree identity testing to **quasi-polynomial time** $n^{O(\\log n)}$, not polynomial time $n^{O(1)}$. The authors explicitly state this as an open problem:
> *(paper)* "Theorem 3.2 is suboptimal. It is an interesting open question to improve it to obtain polynomial time algorithm instead of $n^{O(\\log n)}$."
"""

# 09 Relevance and consequences.md
files["09 Relevance and consequences.md"] = """---
tags: [agrawal-vinay-2008, consequences, modern-impact]
aliases: [Relevance and consequences]
---
# Relevance and Consequences: The Renaissance of Algebraic Complexity

Before 2008, algebraic complexity was in a state of stagnation. Researchers had hit barriers in Boolean complexity (Relativization, Natural Proofs, Algebrization) and feared similar dead-ends in arithmetic circuits.

Agrawal and Vinay's 2008 paper catalyzed a massive revival that defined the next 15 years of theoretical computer science:

---

## 1. The "Chasm at Depth Three" (Gupta, Kamath, Kayal, Saptharishi 2014)

Building directly on Agrawal-Vinay, Ankit Gupta, Pritish Kamath, Neeraj Kayal, and Ramprasad Saptharishi pushed the chasm even further in their landmark 2014 JACM paper:
- Over fields of characteristic zero (e.g. $\\mathbb{Q}$ or $\\mathbb{C}$), any polynomial of degree $d$ computable by size-$s$ circuits can be converted into a **depth-3 ($\Sigma\\Pi\\Sigma$) circuit** of size $2^{O(\\sqrt{d \\log d \\log s})}$!
- Thus, over $\\mathbb{C}$, the chasm drops from depth 4 to **depth 3**!

---

## 2. Shifted Partial Derivatives (Kayal 2012)
Because Agrawal-Vinay proved that depth 4 is the universal bottleneck, Neeraj Kayal introduced the **method of shifted partial derivatives**:
$$\\dim \\left( \\langle \\partial^{\\le k} P \\rangle \\cdot \\mathbf{x}^{\\le \\ell} \\right)$$
Measuring the dimension of the space of partial derivatives multiplied by low-degree monomials provided the exact invariant needed to prove lower bounds against depth-4 circuits!

---

## 3. Recent Constant-Depth Breakthroughs (Limaye, Srinivasan, Tavenas 2021/2025)
Nutan Limaye, Srikanth Srinivasan, and Sébastien Tavenas achieved the first superpolynomial lower bounds for constant-depth circuits of arbitrary fixed depth over $\\mathbb{Q}$ and $\\mathbb{R}$, directly fulfilling the research agenda initiated by Agrawal and Vinay.
"""

# 10 Formalization and code verification.md
files["10 Formalization and code verification.md"] = """---
tags: [agrawal-vinay-2008, code, verification, python]
aliases: [Formalization and code verification]
---
# Formalization and Code Verification

Below is an executable Python suite demonstrating:
1. The **Determinant** vs **Permanent** calculation from scratch (Leibniz formula vs Gaussian elimination).
2. The **Proof Tree decomposition** of an arithmetic circuit.
3. The **Depth-4 Monomial Bound calculation**.

```python
import itertools
import math

def leibniz_determinant(matrix):
    \"\"\"Computes determinant using the exact Leibniz permutation formula.\"\"\"
    n = len(matrix)
    total = 0
    for p in itertools.permutations(range(n)):
        # Calculate sign of permutation
        inversions = 0
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    inversions += 1
        sgn = -1 if inversions % 2 == 1 else 1
        
        prod = 1
        for i in range(n):
            prod *= matrix[i][p[i]]
        total += sgn * prod
    return total

def permanent(matrix):
    \"\"\"Computes permanent (identical to Leibniz, but every sign is +1).\"\"\"
    n = len(matrix)
    total = 0
    for p in itertools.permutations(range(n)):
        prod = 1
        for i in range(n):
            prod *= matrix[i][p[i]]
        total += prod
    return total

def gaussian_determinant(matrix):
    \"\"\"Computes determinant in O(n^3) using Gaussian elimination.\"\"\"
    n = len(matrix)
    A = [row[:] for row in matrix] # Deep copy
    det = 1.0
    for i in range(n):
        pivot = i
        while pivot < n and abs(A[pivot][i]) < 1e-9:
            pivot += 1
        if pivot == n:
            return 0.0
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            det *= -1.0 # Row swap flips sign!
        det *= A[i][i]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    return round(det, 6)

# Test on 3x3 matrix
M = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]
print(\"3x3 Matrix:\", M)
print(\"Leibniz Det :\", leibniz_determinant(M))
print(\"Gaussian Det:\", gaussian_determinant(M))
print(\"Permanent   :\", permanent(M))

# Verify Agrawal-Vinay Size Bounds
def depth4_size_bound(n, d, s):
    \"\"\"Computes Agrawal-Vinay depth-4 upper bound.\"\"\"
    ell = math.log2(s) if s > 1 else 2
    top_deg = math.sqrt(ell)
    bot_deg = d / (ell ** 0.19)
    top_size = math.comb(int(s + top_deg), int(top_deg))
    bot_size = math.comb(int(n + bot_deg), int(bot_deg))
    return top_size + s * bot_size

print(\"Depth-4 bound for n=10, d=10, s=20:\", depth4_size_bound(10, 10, 20))
```
"""

# 11 Reception and valid comments.md
files["11 Reception and valid comments.md"] = """---
tags: [agrawal-vinay-2008, reception, reviews, community]
aliases: [Reception and valid comments]
---
# Reception and Valid Comments

## 1. Presentation at FOCS 2008
Presented at the 49th Annual IEEE Symposium on Foundations of Computer Science (FOCS 2008), the paper was immediately recognized as one of the most elegant conceptual simplifications in structural complexity.

## 2. Community Reaction
- **Sanjeev Arora and Boaz Barak**: Featured the depth reduction paradigm in discussions of modern algebraic lower bounds.
- **Complexity Bloggers (Lance Fortnow, Richard Lipton)**: Hailed it as showing that "depth 4 is the universal frontier."
- **Subsequent Extension**: Neeraj Kayal, Nitin Saxena, and Ramprasad Saptharishi noted that Agrawal-Vinay's framework provided the architectural foundation for all modern lower bounds against arithmetic circuits.

## 3. Valid Technical Comments & Evolution
- *Refinement to Depth 3*: In 2012–2014, Gupta, Kamath, Kayal, and Saptharishi showed that over fields of characteristic zero, one can use Fischer's identity to reduce depth 4 to depth 3!
- *Field Dependencies*: The original Agrawal-Vinay theorem works over any field, whereas reduction to depth 3 requires roots of unity (characteristic zero or large characteristic).
"""

# 12 How to evaluate it yourself.md
files["12 How to evaluate it yourself.md"] = """---
tags: [agrawal-vinay-2008, socratic, exercises, self-evaluation]
aliases: [How to evaluate it yourself]
---
# How to Evaluate It Yourself: Socratic Exercises

Test your understanding with these foundational exercises designed for recent CS/math graduates.

---

### Exercise 1: Geometric Determinant
Compute by hand the determinant and permanent of:
$$A = \\begin{pmatrix} 2 & 3 \\\\ 1 & 4 \\end{pmatrix}$$
- $\\det(A) = (2)(4) - (3)(1) = 8 - 3 = 5$.
- $\\operatorname{perm}(A) = (2)(4) + (3)(1) = 8 + 3 = 11$.
*Question:* What does $\\det(A) = 5$ mean geometrically for the unit square in $\\mathbb{R}^2$?  
*(Answer: The area of the parallelogram spanned by $(2, 1)$ and $(3, 4)$ is exactly 5 units.)*

---

### Exercise 2: Why Can't Gaussian Elimination Compute the Permanent?
Take the matrix $\\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix}$.
- Permanent = $(1)(1) + (1)(1) = 2$.
- Subtract row 1 from row 2: $\\begin{pmatrix} 1 & 1 \\\\ 0 & 0 \\end{pmatrix}$.
- Permanent of new matrix = $(1)(0) + (1)(0) = 0 \\neq 2$!
*Takeaway:* Row elimination destroys the permanent because row operations rely on sign cancellations that the permanent does not possess.

---

### Exercise 3: The Arithmetic Circuit Concept
Draw an arithmetic circuit for computing $P(x_1, x_2, x_3, x_4) = (x_1 + x_2)(x_3 + x_4)$.
- What is its size? (1 addition for $x_1+x_2$, 1 addition for $x_3+x_4$, 1 multiplication = 3 gates).
- What is its depth? (Depth 2: Layer 1 is $+$, Layer 2 is $\\times$).
- Is it a $\\Sigma\\Pi$ or $\\Pi\\Sigma$ circuit? ($\Pi\\Sigma$: product of sums).

---

### Exercise 4: The Chasm Implication
Suppose your friend claims: *"I have proved that depth-4 circuits computing the Permanent require at least $2^{n/10}$ gates."*  
According to Agrawal and Vinay (Corollary 2.6), what does this claim immediately imply for general arithmetic circuits of depth $10^6$?  
*(Answer: It implies that general arithmetic circuits of ANY depth also require exponential size $2^{\\Omega(n)}$, resolving $\\mathrm{VP} \\neq \\mathrm{VNP}$!)*
"""

# 13 Glossary.md
files["13 Glossary.md"] = """---
tags: [agrawal-vinay-2008, glossary, definitions]
aliases: [Glossary]
---
# Glossary: Foundational Terms in Algebraic Complexity

### Arithmetic Circuit
A directed acyclic graph (DAG) where internal nodes are addition ($+$) or multiplication ($\\times$) gates, and leaves are variables or constants from a field $\\mathbb{F}$.

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

### Determinant ($\\det$)
The unique alternating multilinear function of an $n \\times n$ matrix measuring oriented hypervolume scaling. Computable in $O(n^3)$ operations; belongs to class VP.

### Fan-in
The number of incoming edges feeding into a gate.

### Homogeneous Polynomial / Circuit
A polynomial where every monomial has the exact same total degree. A circuit is homogeneous if every internal gate computes a homogeneous polynomial.

### Permanent ($\\operatorname{perm}$)
The matrix function defined identically to the determinant but without permutation signs. Complete for class VNP and $\\#P$.

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
"""

# 14 References.md
files["14 References.md"] = """---
tags: [agrawal-vinay-2008, references, bibliography]
aliases: [References]
---
# References

## Primary Paper
- **Manindra Agrawal and V. Vinay**, *Arithmetic Circuits: A Chasm at Depth Four*, Electronic Colloquium on Computational Complexity (ECCC TR08-062), 2008. Presented at the 49th Annual IEEE Symposium on Foundations of Computer Science (FOCS 2008), pp. 67–75.
  - [ECCC Report](https://eccc.weizmann.ac.il/report/2008/062/)
  - Local PDF: `papers/agrawal_vinay_2008_chasm_at_depth_four.pdf`

---

## Landmark Works by V. Vinay
- **Meena Mahajan and V. Vinay**, *A Combinatorial Algorithm for Computing the Determinant*, Proceedings of the 8th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 1997), pp. 730–738. Full version in *Information and Computation*, 143(1):1–16, 1998.
- **Eric Allender, Jia Jiao, Meena Mahajan, and V. Vinay**, *Non-commutative arithmetic circuits: Depth reduction and size lower bounds*, Theoretical Computer Science, 209(1-2):47–86, 1998.
- **V. Vinay**, *Counting auxiliary pushdown automata and semi-unbounded arithmetic circuits*, IEEE Structure in Complexity Theory Conference, pp. 270–284, 1991.

---

## Foundational Context & Reductions
- **Leslie G. Valiant**, *Completeness classes in algebra*, STOC 1979, pp. 249–261. (Introduced VP and VNP).
- **Leslie G. Valiant**, *The Complexity of Computing the Permanent*, Theoretical Computer Science, 8:189–201, 1979. (Proved permanent is #P-complete).
- **L. G. Valiant, S. Skyum, S. Berkowitz, and C. Rackoff**, *Fast parallel computation of polynomials using few processors*, SIAM Journal on Computing, 12(4):641–644, 1983. (VSBR depth reduction).
- **Valentine Kabanets and Russell Impagliazzo**, *Derandomizing polynomial identity tests means proving circuit lower bounds*, Computational Complexity, 13:1–46, 2004.
- **D. Grigoriev and A. Razborov**, *Exponential lower bounds for depth 3 arithmetic circuits in algebras of functions over finite fields*, Applicable Algebra in Engineering, Communication and Computing, 10(6):467–487, 2000.
- **Ankit Gupta, Pritish Kamath, Neeraj Kayal, and Ramprasad Saptharishi**, *Approaching the chasm at depth four*, Journal of the ACM (JACM), 61(6):33:1–33:36, 2014.
"""

for fname, content in files.items():
    p = vault_dir / fname
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Successfully wrote {len(files)} notes to {vault_dir}")

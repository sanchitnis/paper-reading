---
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
> $$\text{Exponential lower bounds for Depth 4} \implies \text{Exponential lower bounds for General Circuits (VP } \neq \text{VNP)}$$
> They did **not** prove the depth-4 lower bound for the permanent. The lower bound itself remained open.

---

## 2. It Does NOT Give an Efficient Algorithm for the Permanent
The depth-4 circuit constructed for the determinant has size $n^{O(\sqrt{n})}$.  
For the permanent, if a small circuit existed, it would collapse to size $2^{o(n)}$ at depth 4. But because the permanent is believed to require $2^{\Omega(n)}$, the paper provides no shortcut for evaluating matchings or the permanent.

---

## 3. It Does NOT Directly Apply to Non-Commutative Circuits Without Modifications
In commutative algebra, $x \cdot y = y \cdot x$. In non-commutative circuits (where matrix multiplication variables do not commute), depth reduction behaves differently (as explored by Nisan 1991 and Allender et al. 1998).

---

## 4. It Does NOT Achieve Full Polynomial Time PIT Derandomization
Theorem 3.2 derandomizes low-degree identity testing to **quasi-polynomial time** $n^{O(\log n)}$, not polynomial time $n^{O(1)}$. The authors explicitly state this as an open problem:
> *(paper)* "Theorem 3.2 is suboptimal. It is an interesting open question to improve it to obtain polynomial time algorithm instead of $n^{O(\log n)}$."

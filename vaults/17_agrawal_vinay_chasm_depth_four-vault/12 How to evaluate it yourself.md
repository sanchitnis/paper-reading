---
tags: [agrawal-vinay-2008, socratic, exercises, self-evaluation]
aliases: [How to evaluate it yourself]
---
# How to Evaluate It Yourself: Socratic Exercises

Test your understanding with these foundational exercises designed for recent CS/math graduates.

---

### Exercise 1: Geometric Determinant
Compute by hand the determinant and permanent of:
$$A = \begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}$$
- $\det(A) = (2)(4) - (3)(1) = 8 - 3 = 5$.
- $\operatorname{perm}(A) = (2)(4) + (3)(1) = 8 + 3 = 11$.
*Question:* What does $\det(A) = 5$ mean geometrically for the unit square in $\mathbb{R}^2$?  
*(Answer: The area of the parallelogram spanned by $(2, 1)$ and $(3, 4)$ is exactly 5 units.)*

---

### Exercise 2: Why Can't Gaussian Elimination Compute the Permanent?
Take the matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
- Permanent = $(1)(1) + (1)(1) = 2$.
- Subtract row 1 from row 2: $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$.
- Permanent of new matrix = $(1)(0) + (1)(0) = 0 \neq 2$!
*Takeaway:* Row elimination destroys the permanent because row operations rely on sign cancellations that the permanent does not possess.

---

### Exercise 3: The Arithmetic Circuit Concept
Draw an arithmetic circuit for computing $P(x_1, x_2, x_3, x_4) = (x_1 + x_2)(x_3 + x_4)$.
- What is its size? (1 addition for $x_1+x_2$, 1 addition for $x_3+x_4$, 1 multiplication = 3 gates).
- What is its depth? (Depth 2: Layer 1 is $+$, Layer 2 is $\times$).
- Is it a $\Sigma\Pi$ or $\Pi\Sigma$ circuit? ($\Pi\Sigma$: product of sums).

---

### Exercise 4: The Chasm Implication
Suppose your friend claims: *"I have proved that depth-4 circuits computing the Permanent require at least $2^{n/10}$ gates."*  
According to Agrawal and Vinay (Corollary 2.6), what does this claim immediately imply for general arithmetic circuits of depth $10^6$?  
*(Answer: It implies that general arithmetic circuits of ANY depth also require exponential size $2^{\Omega(n)}$, resolving $\mathrm{VP} \neq \mathrm{VNP}$!)*

---
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
$$[g] = \sum_{T} p(T)$$

### The Quotient $[g, h]$
For any two gates $g$ and $h$ in circuit $C$:
$$[g, h] = \sum_{T} p(T, h)$$
where $T$ runs over all proof trees rooted at $g$ where $h$ appears on the rightmost path, and $p(T, h)$ is the polynomial computed when gate $h$ is replaced by the constant $1$.
- If $h$ never appears on the rightmost path, $[g, h] = 0$.
- Intuitively, $[g, h]$ represents the partial polynomial computed between gate $h$ and gate $g$.

---

## 2. Ensuring the Degree Halves at Every Multiplication Gate

For a multiplication gate $g$ with children $g_L$ and $g_R$, there is a unique intermediate multiplication gate $p$ along the rightmost path from $g$ to $h$ such that:
$$\deg(p_R) \le \frac{1}{2}(\deg(g) + \deg(h)) \le \deg(p)$$

Summing over all possible candidate gates $p$:
$$[g, h] = \sum_p [g, p] \cdot [p_L] \cdot [p_R, h]$$

Notice the degrees:
1. $\deg([g, p]) = \deg(g) - \deg(p) \le \frac{1}{2}(\deg(g) - \deg(h))$.
2. $\deg([p_R, h]) = \deg(p_R) - \deg(h) \le \frac{1}{2}(\deg(g) - \deg(h))$.
3. But what about $[p_L]$? Its degree might be larger than $\frac{1}{2}\deg([g, h])$.

### The Agrawal-Vinay Degree Trick:
To fix $[p_L]$, apply the decomposition once more to $[p_L]$:
$$[p_L, x_i] = \sum_q [p_L, q] \cdot [q_L] \cdot [q_R, x_i]$$
By expanding $[p_L]$ down to variables $x_i$, we obtain a product of 6 terms:
$$[g, h] = \sum_{p, i, j, q} [g, p] \cdot [p^j_L, q] \cdot [q_L] \cdot [q_R, x_i] \cdot [x_i] \cdot [p_R, h]$$
In this 6-way product, **every single term has degree at most $\frac{1}{2}\deg([g, h])$**!
This guarantees that circuit $D$ has multiplication fan-in at most 6 and depth at most $2 \log d$.

---

## 3. The Combinatorial Size Bound for Circuit $E$

Cut circuit $D$ at level $t = \frac{1}{2} \log_6 \ell$.
The final depth-4 circuit $E$ evaluates $P_0(P_1, \dots, P_k)$.

### Monomial Counting via Stars and Bars
The number of monomials of degree $K$ over $N$ variables is $\binom{N + K}{K}$.
1. **Top Polynomial $P_0$**: Defined on $k \le S$ variables with degree bounded by $6^t = \sqrt{\ell}$:
   $$\text{Monomials}(P_0) \le \binom{S + \sqrt{\ell}}{\sqrt{\ell}} \le (2S)^{\sqrt{\ell}} = 2^{O(\sqrt{\ell} \log S)}$$
2. **Bottom Polynomials $P_i$**: Defined on $n$ variables with degree bounded by $\frac{d}{2^t} = \frac{d}{\ell^\delta}$ (where $\delta = \frac{1}{2} \log_6 2$):
   $$\text{Monomials}(P_i) \le \binom{n + d/\ell^\delta}{d/\ell^\delta} \le 2^{O\left(\frac{d}{\ell^\delta} + \frac{d}{\ell^\delta} \log \frac{n}{d}\right)}$$

### The Final Sum
Summing the sizes of $P_0$ and all $k$ polynomials $P_i$:
$$\operatorname{Size}(E) \le 2^{O(\sqrt{(d + d \log(n/d)) \log S})} + S \cdot 2^{o(d + d \log(n/d))} = 2^{o(d + d \log(n/d))}$$
This establishes Theorem 2.4!

---
tags: [vp-vnp, background]
---
# From P vs NP to VP vs VNP

| | Boolean world | Algebraic world |
|---|---|---|
| Objects | yes/no functions on bit strings | polynomials in variables over a field (ℝ, ℂ, 𝔽_p …) |
| Machine | Turing machine / Boolean circuit (AND, OR, NOT) | **arithmetic circuit** (+, × gates) |
| "Easy" class | P | **VP** |
| "Guess-and-check" class | NP: OR over witnesses | **VNP**: *sum* over witnesses |
| Hard-looking complete problem | SAT, Hamiltonian cycle | **permanent**, Hamiltonian cycle *polynomial* |

*(analogy)* NP asks "does any witness work?" and VNP asks "what is the total weight of all witnesses?" The OR of NP becomes a sum.

## Why the algebraic version is a different problem
An arithmetic circuit must compute the polynomial **as a formal expression**. It has to be right for every number in the field and in its extensions, not only for 0 and 1. A Boolean circuit can exploit that inputs are only 0/1, for example x² = x. An arithmetic circuit cannot *(paper, §1)*.

So the algebraic problem is more rigid. That rigidity is why lower bounds are *plausibly* easier to prove there, and why a result there does not transfer to Boolean circuits.

## How they connect
- If **VP = VNP** (under suitable assumptions), then P/poly = NP/poly. This is Bürgisser (2000) *(paper)*. So *proving VP ≠ VNP is a necessary step on one route to P ≠ NP*. In this sense a separation is a warm-up.
- The reverse implication is **not known**. VP ≠ VNP does not imply P ≠ NP. See [08 What the result does not say](08%20What%20the%20result%20does%20not%20say.md).

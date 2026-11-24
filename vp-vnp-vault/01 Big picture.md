---
tags: [vp-vnp, overview]
---
# Big picture

```mermaid
flowchart TD
    A["P vs NP<br/>Boolean world: bits, AND/OR/NOT"] -->|"replace bit operations by + and ×<br/>on numbers"| B["VP vs VNP<br/>algebraic world: polynomials, + and ×"]
    B --> C["VP = polynomials with small circuits<br/>e.g. determinant"]
    B --> D["VNP = exponential sums of VP terms<br/>e.g. permanent, Hamiltonian cycle"]
    C --> E{"Valiant 1979: is VP = VNP?<br/>Open for 47 years"}
    D --> E
    E --> F["Paper's claim: NO, over every field.<br/>Permanent / HC circuits need<br/>more than m^(c·(log m)^(1/3)) gates"]
    F --> G["Superpolynomial but quasi-polynomial.<br/>Best upper bound is exponential.<br/>Previous best lower bound: about n log d"]
    F --> H["Proof: assume a small circuit exists,<br/>then reach a contradiction in one of two cases"]
    H --> I["Flat case:<br/>geometry of tensor networks"]
    H --> J["Contracting case:<br/>speed-up plus diagonalization"]
    F -.->|"does NOT follow"| K["P ≠ NP<br/>still open"]
    F --> L["Lean 4 proof, ~73k lines.<br/>No human has checked it yet"]
```

## One-paragraph version
Computing the **permanent** of an m×m matrix is believed to need exponentially many arithmetic operations if you want a formula that works symbolically, for all numbers rather than just 0/1. Nobody could prove even a *superpolynomial* lower bound for general circuits. The paper claims one: roughly m^{c·(log m)^{1/3}}. It reaches this through a dichotomy about the geometry of certain "price" metrics on tensors. Either the geometry is Euclidean-capable (flat case) or it is strictly contracting (contracting case), and each case yields a contradiction with a small circuit. It does not prove P ≠ NP.

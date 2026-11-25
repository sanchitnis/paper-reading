"""Generate comprehensive NotebookLM and Video Explainer Assets for Agrawal & Vinay (2008)."""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dir = Path("outputs/17_agrawal_vinay_chasm_depth_four")
output_dir.mkdir(parents=True, exist_ok=True)
frames_dir = output_dir / "video_frames"
frames_dir.mkdir(parents=True, exist_ok=True)

# 1. AUDIO_OVERVIEW_SCRIPT.md
audio_script = """# NotebookLM Audio Overview: Arithmetic Circuits — A Chasm at Depth Four
*Hosts: Alex (The Rigorous Complexity Theorist) & Jordan (The Intuitive Conceptual Synthesizer)*  
*Paper: Manindra Agrawal & V. Vinay (FOCS 2008 / ECCC TR08-062)*  
*Target Audience: Recent graduates in Computer Science, Mathematics, or Engineering*  
*Target Runtime: ~12 minutes*

---

**[AUDIO CHIME / THEME MUSIC]**

**Jordan:** "Welcome back to the Deep Dive. Today we are exploring a paper that completely rewired how theoretical computer scientists think about proving lower bounds. It's titled *Arithmetic Circuits: A Chasm at Depth Four*, by Manindra Agrawal and V. Vinay."

**Alex:** "Right. And for any recent graduate in computer science or math, this paper is an absolute masterpiece of conceptual clarity. Because before this paper, people thought proving that arithmetic circuits require exponential size meant climbing an endless, tangled mountain of recursive logic. Agrawal and Vinay showed there isn't an endless mountain—there is a single, dramatic chasm at depth four."

**Jordan:** "A chasm at depth four! But Alex, before we plunge into depth four, let's start where every student of linear algebra starts: the matrix determinant. Why is the determinant such a big deal in computational complexity?"

**Alex:** "Let's ground it. Take an $n \\times n$ matrix $A$. Geometrically, if you think of the rows as vectors in space, the determinant measures the oriented volume of the $n$-dimensional box they span. If the determinant is zero, the space collapses into a flat pancake, and the matrix isn't invertible."

**Jordan:** "And algebraically, if you write down the definition—the Leibniz formula—it's a sum over all $n!$ permutations:
$$\\det(A) = \\sum_{\\sigma \\in S_n} \\operatorname{sgn}(\\sigma) \\prod_{i=1}^n A_{i, \\sigma(i)}$$
For a $20 \\times 20$ matrix, $20!$ is over two quintillion terms! If you tried to calculate that term by term, your computer would run until the heat death of the universe."

**Alex:** "Exactly. But here is the miracle of the determinant: that little term $\\operatorname{sgn}(\\sigma)$ alternates signs—plus one, minus one, plus one, minus one. Because of those alternating signs, if you do basic row operations—Gaussian elimination—everything cancels out cleanly. You can find the determinant in just $O(n^3)$ operations! A tiny fraction of a second. In complexity terms, the determinant belongs to **VP**—polynomial-sized arithmetic circuits."

**Jordan:** "And then enters its evil twin: the **Permanent**."

**Alex:** "The Permanent looks identical, except you remove the $\\operatorname{sgn}(\\sigma)$. Every single term is positive:
$$\\operatorname{perm}(A) = \\sum_{\\sigma \\in S_n} \\prod_{i=1}^n A_{i, \\sigma(i)}$$
Combinatorially, the permanent counts the exact number of perfect matchings in a bipartite graph. But because there are no minus signs, there is zero cancellation. Gaussian elimination completely breaks down. Leslie Valiant proved back in 1979 that computing the permanent is $\\#P$-complete and complete for the algebraic class **VNP**."

**Jordan:** "And Valiant conjectured that $\\mathrm{VP} \\neq \\mathrm{VNP}$. In other words: no polynomial-sized arithmetic circuit can compute the permanent. That's the algebraic analogue of P versus NP!"

**Alex:** "Right. Now, what is an arithmetic circuit? Think of a directed graph where the inputs at the bottom are your variables and constants. As you move up, you have addition gates and multiplication gates. The size is the number of gates, and the depth is the length of the longest path from bottom to top."

**Jordan:** "So depth is like parallel time! Depth 2 is just a sum of products—like writing out all the monomials. Depth 3 is a sum of products of sums. And for years, people were proving lower bounds for depth-3 circuits. But everyone got completely stuck trying to move to depth 4, 5, or 6!"

**Alex:** "And this is where Agrawal and Vinay stepped in and asked: *Why are we stuck at depth 3?* 
And their answer was shocking: Depth 3 is fundamentally weak. Grigoriev and Razborov had already proved that the determinant requires exponential size on depth-3 circuits over finite fields. But Agrawal and Vinay proved that at **depth 4**, the determinant can be computed in subexponential size $n^{O(\\sqrt{n})}$!"

**Jordan:** "Wait—so depth 4 is already powerful enough to compute the determinant?"

**Alex:** "Yes! And not just the determinant. Their grand theorem—The Chasm Theorem—says: take *any* polynomial computed by a circuit of size $s$ and degree $d$. You can collapse that entire arbitrary-depth circuit into a **depth-four circuit** of size $2^{O(\\sqrt{d \\log d \\log s})}$!"

**Jordan:** "Let that sink in! If you have a circuit that is 500 layers deep, you can smash it down into just FOUR alternating layers: Sum-Product-Sum-Product ($\Sigma\\Pi\\Sigma\\Pi$) without paying an exponential price!"

**Alex:** "Which leads to their sensational corollary for the Permanent: If you can prove that depth-four circuits for the Permanent require exponential size, you have automatically proved that circuits of **ANY depth** require exponential size! That settles $\\mathrm{VP} \\neq \\mathrm{VNP}$!"

**Jordan:** "Boom! You don't have to study crazy 10,000-gate graph topologies. All of algebraic complexity boils down to understanding shallow, 4-layer circuits. And they didn't stop there—they connected this to Polynomial Identity Testing, or PIT."

**Alex:** "Right! In PIT, you want to know if an arithmetic circuit simplifies to identically zero. With randomness, you just plug in random numbers—the Schwartz-Zippel lemma tells you that if it's non-zero, it will evaluate to non-zero almost certainly. But can you do it deterministically without randomness? Agrawal and Vinay showed that if you can build a pseudorandom generator for depth-four circuits, you can derandomize general PIT in quasi-polynomial time $n^{O(\\log n)}$!"

**Jordan:** "Using the Nisan-Wigderson design and hardness-versus-randomness! This paper basically handed the theoretical computer science community a roadmap for the next two decades. It led to Gupta, Kamath, Kayal, and Saptharishi's work on depth 3 over characteristic zero, and Kayal's method of shifted partial derivatives."

**Alex:** "If you're a recent graduate, the lesson is clear: computational depth is not a smooth ramp. In algebraic complexity, depth 4 is where the entire hardness of the universe is concentrated. Master depth 4, and you master general circuits."

**Jordan:** "Check out the accompanying Obsidian vault, run the Python code in note 10, and review the slide deck. Until next time, keep exploring the foundations!"

**[OUTRO THEME / FADE OUT]**
"""

with open(output_dir / "AUDIO_OVERVIEW_SCRIPT.md", "w", encoding="utf-8") as f:
    f.write(audio_script.strip() + "\n")

# 2. EXPLAINER_REPORT.md
report = """# Technical Explainer Report: Arithmetic Circuits — A Chasm at Depth Four

| Metadata | Details |
| :--- | :--- |
| **Paper Title** | *Arithmetic Circuits: A Chasm at Depth Four* |
| **Authors** | Manindra Agrawal (IIT Kanpur) & V. Vinay (CMI & Geodesic Information Systems) |
| **Venue / Record** | Electronic Colloquium on Computational Complexity (ECCC TR08-062, 2008); IEEE FOCS 2008 |
| **Target Audience** | Recent Graduates in Computer Science, Mathematics, or Electrical Engineering |
| **Primary Breakthrough** | Establishing that exponential lower bounds for depth-4 arithmetic circuits imply exponential lower bounds for unrestricted-depth circuits, collapsing the $\\mathrm{VP} \\neq \\mathrm{VNP}$ quest to depth 4. |

---

## 1. Executive Summary
In computational complexity theory, determining whether Leslie Valiant's algebraic conjecture $\\mathrm{VP} \\neq \\mathrm{VNP}$ holds has stood open since 1979. This paper proves a structural depth-reduction theorem: any polynomial of degree $d = O(n)$ computable by an arithmetic circuit of size $2^{o(d + d \\log(n/d))}$ can also be computed by a **depth-four ($\Sigma\\Pi\\Sigma\\Pi$) arithmetic circuit** of size $2^{o(d + d \\log(n/d))}$.

### Three Core Takeaways:
1. **The Chasm at Depth Four**: Additional circuit depth beyond 4 does not help for exponential-sized circuits. Proving lower bounds against $\\Sigma\\Pi\\Sigma\\Pi$ circuits is equivalent to proving lower bounds for general circuits.
2. **Determinant Complexity Collapse**: While the determinant requires exponential size at depth 3 over finite fields, it collapses to subexponential size $n^{O(\\sqrt{n})}$ at depth 4.
3. **PIT Derandomization**: Black-box derandomization of Polynomial Identity Testing for restricted depth-4 circuits yields a deterministic quasi-polynomial time ($n^{O(\\log n)}$) algorithm for general low-degree PIT.

---

## 2. Foundational Primer for Recent Graduates

```mermaid
flowchart TD
    subgraph Fundamentals [The Fundamental Algebraic Dilemma]
        Det["Determinant: det(X)<br/>Alternating permutation signs (+/-)<br/>Gaussian elimination O(n^3)<br/>Class VP"]
        Perm["Permanent: perm(X)<br/>All positive permutation signs (+)<br/>Counts perfect matchings in bipartite graphs<br/>Class VNP-Complete (#P-complete)"]
    end

    subgraph The Circuit Model [Arithmetic Circuit DAG]
        Gates["Gates: Addition (+) and Multiplication (*)<br/>Size s: Number of gates<br/>Depth Delta: Longest path from input to root"]
    end

    subgraph The Chasm [Agrawal-Vinay Reduction]
        D4["Depth 4 (Sigma - Pi - Sigma - Pi):<br/>Top Pi fan-in <= o(d)<br/>Bottom Pi fan-in <= o(d)"]
        Theorem["Theorem 2.4:<br/>General Size s Circuit == Depth-4 Size 2^O(sqrt(d log d log s))"]
    end

    Det & Perm --> Gates
    Gates --> D4
    D4 --> Theorem
```

### 2.1 What is the Determinant?
Given an $n \\times n$ matrix $X = (x_{ij})$:
$$\\det(X) = \\sum_{\\sigma \\in S_n} \\operatorname{sgn}(\\sigma) \\prod_{i=1}^n x_{i, \\sigma(i)}$$
- **Geometric Meaning**: Oriented volume scaling factor of the linear transformation.
- **Why it's in VP**: The alternating sign $\\operatorname{sgn}(\\sigma)$ ensures that elementary row operations (adding a multiple of one row to another) preserve the determinant, enabling Gaussian elimination in $O(n^3)$ operations. Mahajan & Vinay (1997) proved it can also be computed division-free in $O(n^4)$ time using clow sequences.

### 2.2 What is the Permanent?
$$\\operatorname{perm}(X) = \\sum_{\\sigma \\in S_n} \\prod_{i=1}^n x_{i, \\sigma(i)}$$
- **Combinatorial Meaning**: Counts perfect matchings in a bipartite graph.
- **Why it's in VNP-complete**: Without sign cancellations, row operations fail. Valiant showed that computing the permanent is $\\#P$-complete.

---

## 3. Mathematical Proof Architecture

The transformation proceeds in four distinct phases:
1. **VSBR Depth Reduction**: The input circuit $C$ of size $M$ and degree $d$ is converted into an $O(\\log d)$-depth circuit with multiplication fan-in 2.
2. **Structural Balancing (Circuit $D$)**: Using partial proof tree derivatives $[g, h]$, the circuit is refactored so that multiplication fan-in is $\\le 6$, and crucially, **every child of a multiplication gate has at most half the degree of the parent gate**:
   $$\\deg(\\text{child}) \\le \\frac{1}{2} \\deg(\\text{parent})$$
3. **Bisecting the Circuit**: Circuit $D$ is split at level $t = \\frac{1}{2} \\log_6 \\ell$:
   - Top component $P_0(y_1, \\dots, y_k)$: has $t$ multiplication layers, degree $\\le 6^t = \\sqrt{\\ell}$.
   - Bottom components $P_1, \\dots, P_k$: degree bounded by $\\frac{d}{2^t} = \\frac{d}{\\ell^\\delta}$.
4. **Sum-of-Products Assembly (Circuit $E$)**: Expanding $P_0$ and each $P_i$ into depth-2 forms yields a 4-layer $\\Sigma\\Pi\\Sigma\\Pi$ circuit of total size:
   $$2^{O(\\sqrt{(d + d \\log(n/d)) \\log S})} + S \\cdot 2^{o(d + d \\log(n/d))} = 2^{o(d + d \\log(n/d))}$$

---

## 4. Black-Box PIT Derandomization

1. An optimal pseudorandom generator against depth-4 circuits produces a hard multilinear polynomial family $\\{q_m\\}$ requiring $2^{\\Omega(m)}$ size depth-4 circuits.
2. By Theorem 2.4, $\\{q_m\\}$ must require exponential size on **unrestricted-depth** circuits.
3. Using the Nisan-Wigderson combinatorial generator combined with Kaltofen's multivariate polynomial factorization, this hardness is converted into a deterministic identity test running in $n^{O(\\log n)}$ time.

---

## 5. Critical Boundaries & Non-Claims
- **Does not prove VP != VNP**: It proves the equivalence between depth-4 lower bounds and general lower bounds.
- **Does not give efficient permanent algorithms**: The permanent is still believed to require exponential size.
- **Quasi-polynomial PIT**: The derandomization achieves $n^{O(\\log n)}$, leaving full polynomial time $n^{O(1)}$ open.

---

## 6. Actionable Takeaways for Researchers
- When proving circuit lower bounds, focus all analytical machinery (such as shifted partial derivatives) directly on depth-4 circuits.
- Explore the companion 15-note Obsidian vault in `vaults/17_agrawal_vinay_chasm_depth_four-vault/` and the interactive Python code.
"""

with open(output_dir / "EXPLAINER_REPORT.md", "w", encoding="utf-8") as f:
    f.write(report.strip() + "\n")

# 3. slides.html
slides_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Arithmetic Circuits: A Chasm at Depth Four (Agrawal & Vinay 2008)</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0b0f19; color: #f1f5f9; margin: 0; padding: 20px; }
  .deck { max-width: 960px; margin: 0 auto; }
  .slide { background: #131d31; border-radius: 12px; padding: 40px; margin-bottom: 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.6); border-left: 6px solid #38bdf8; }
  h1 { color: #38bdf8; font-size: 2.2rem; margin-top: 0; }
  h2 { color: #94a3b8; font-size: 1.3rem; margin-bottom: 20px; }
  p, li { font-size: 1.15rem; line-height: 1.7; color: #cbd5e1; }
  .highlight { color: #fbbf24; font-weight: bold; }
  .box { background: #1e293b; padding: 18px 24px; border-radius: 8px; margin: 20px 0; border: 1px solid #334155; }
  .accent-box { background: #1e1b4b; border-left: 4px solid #818cf8; padding: 18px; border-radius: 8px; margin: 20px 0; }
  .footer { font-size: 0.85rem; color: #64748b; margin-top: 30px; border-top: 1px solid #1e293b; padding-top: 10px; display: flex; justify-content: space-between; }
  code { background: #0f172a; padding: 3px 8px; border-radius: 4px; color: #38bdf8; font-family: monospace; }
</style>
</head>
<body>
<div class="deck">

  <!-- Slide 1 -->
  <div class="slide">
    <h1>Arithmetic Circuits: A Chasm at Depth Four</h1>
    <h2>Manindra Agrawal (IIT Kanpur) & V. Vinay (CMI / Geodesic) &bull; FOCS 2008</h2>
    <div class="accent-box">
      <strong>Core Question:</strong> To prove Valiant's conjecture (VP &ne; VNP), do we need to analyze arbitrarily deep arithmetic circuits, or can we collapse the problem to shallow circuits?
    </div>
    <p><strong>Audience:</strong> Recent graduates in Computer Science, Mathematics, and Engineering.</p>
    <div class="footer"><span>Slide 1 of 6</span><span>Paper Reading Playbook</span></div>
  </div>

  <!-- Slide 2 -->
  <div class="slide">
    <h1>1. Groundwork: Determinant vs Permanent</h1>
    <h2>Volume Scaling (Easy) vs Matchings (Hard)</h2>
    <ul>
      <li><strong>The Determinant (&isin; VP):</strong> <span class="highlight">Alternating signs</span> allow cancellations &rarr; $O(n^3)$ Gaussian elimination &rarr; polynomial-size circuits.</li>
      <li><strong>The Permanent (&isin; VNP-Complete):</strong> <span class="highlight">All positive signs</span> &rarr; counts bipartite perfect matchings &rarr; no cancellations &rarr; believed to require exponential size $2^{\Omega(n)}$.</li>
    </ul>
    <div class="box">
      <strong>Valiant's 1979 Conjecture:</strong> $\text{VP} \neq \text{VNP}$ &mdash; the fundamental algebraic analogue of $P \neq NP$.
    </div>
    <div class="footer"><span>Slide 2 of 6</span><span>Foundations</span></div>
  </div>

  <!-- Slide 3 -->
  <div class="slide">
    <h1>2. The Arithmetic Circuit Model & Depth</h1>
    <h2>Directed Acyclic Graphs of Addition (+) and Multiplication (&times;)</h2>
    <ul>
      <li><strong>Depth 2 (&Sigma;&Pi;):</strong> Sum of monomials. Trivial size $n! = 2^{\Omega(n \log n)}$. Too weak.</li>
      <li><strong>Depth 3 (&Sigma;&Pi;&Sigma;):</strong> Sum of products of sums. Lower bounds proved over finite fields, but stalled.</li>
      <li><strong>The Mystery:</strong> Why did everyone get stuck moving past Depth 3?</li>
    </ul>
    <div class="accent-box">
      <strong>The Key Insight:</strong> The Determinant requires exponential size at Depth 3, but collapses to subexponential size $n^{O(\sqrt{n})}$ at <strong>Depth 4</strong>! Depth 4 is where the real power begins!
    </div>
    <div class="footer"><span>Slide 3 of 6</span><span>The Depth Dilemma</span></div>
  </div>

  <!-- Slide 4 -->
  <div class="slide">
    <h1>3. The Depth Four Chasm Theorem</h1>
    <h2>Theorem 2.4 (Agrawal & Vinay 2008)</h2>
    <div class="box">
      If a polynomial $P(x_1, \dots, x_n)$ of degree $d = O(n)$ has an arithmetic circuit of size $2^{o(d + d \log(n/d))}$, then it can be computed by a <strong>Depth-4 (&Sigma;&Pi;&Sigma;&Pi;) circuit</strong> of size $2^{o(d + d \log(n/d))}$!
    </div>
    <ul>
      <li><strong>For the Permanent:</strong> If the Permanent requires exponential size at Depth 4, it requires exponential size for <em>ALL</em> unrestricted circuits!</li>
      <li><strong>The Chasm:</strong> Crossing Depth 4 is as hard as resolving the entire general circuit lower bound!</li>
    </ul>
    <div class="footer"><span>Slide 4 of 6</span><span>Core Theorem</span></div>
  </div>

  <!-- Slide 5 -->
  <div class="slide">
    <h1>4. Polynomial Identity Testing (PIT) Derandomization</h1>
    <h2>From Depth 4 to General Identity Testing</h2>
    <ul>
      <li><strong>PIT:</strong> Determining whether a circuit $C(x_1, \dots, x_n) \equiv 0$ without using random coin flips.</li>
      <li><strong>Theorem 3.2:</strong> An optimal pseudorandom generator against restricted Depth-4 circuits implies deterministic general PIT in $n^{O(\log n)}$ time!</li>
      <li><strong>Mechanism:</strong> Uses Nisan-Wigderson designs and Kaltofen's multivariate polynomial factorization.</li>
    </ul>
    <div class="footer"><span>Slide 5 of 6</span><span>PIT Derandomization</span></div>
  </div>

  <!-- Slide 6 -->
  <div class="slide">
    <h1>5. Takeaways for Students & Researchers</h1>
    <h2>How this Shaped the Next 15 Years</h2>
    <ul>
      <li><strong>Target Depth 4:</strong> You don't need to analyze arbitrary 10,000-gate graph topologies. Focus on $\Sigma\Pi\Sigma\Pi$ circuits.</li>
      <li><strong>Catalyzed Modern Techniques:</strong> Led to the Chasm at Depth 3 over characteristic zero (Gupta et al. 2014) and Kayal's shifted partial derivatives.</li>
      <li><strong>Interactive Exploration:</strong> Check <code>vaults/17_agrawal_vinay_chasm_depth_four-vault/</code> for the complete 15-note Obsidian wiki!</li>
    </ul>
    <div class="footer"><span>Slide 6 of 6</span><span>Summary & Legacy</span></div>
  </div>

</div>
</body>
</html>
"""

with open(output_dir / "slides.html", "w", encoding="utf-8") as f:
    f.write(slides_html.strip() + "\n")

# 4. Render 6 High-Res Storyboard Video Frames
print("Rendering visual video storyboard frames...")

def create_frame(filename, title, subtitle, bullets, highlight_box=None):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('#0b0f19')
    ax.set_facecolor('#0b0f19')
    ax.axis('off')

    # Header
    ax.text(0.08, 0.88, title, fontsize=24, color='#38bdf8', weight='bold')
    ax.text(0.08, 0.82, subtitle, fontsize=15, color='#94a3b8')
    ax.axhline(y=0.79, xmin=0.08, xmax=0.92, color='#334155', linewidth=1.5)

    # Content
    y_pos = 0.70
    for bullet in bullets:
        ax.text(0.10, y_pos, f"• {bullet}", fontsize=14, color='#e2e8f0', wrap=True)
        y_pos -= 0.10

    if highlight_box:
        rect = patches.FancyBboxPatch((0.08, 0.12), 0.84, 0.18, boxstyle="round,pad=0.03", 
                                       facecolor='#1e1b4b', edgecolor='#818cf8', linewidth=2)
        ax.add_patch(rect)
        ax.text(0.10, 0.23, highlight_box[0], fontsize=13, color='#fbbf24', weight='bold')
        ax.text(0.10, 0.16, highlight_box[1], fontsize=12, color='#cbd5e1')

    plt.tight_layout()
    plt.savefig(frames_dir / filename, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)

create_frame(
    "frame_01_title.png",
    "Arithmetic Circuits: A Chasm at Depth Four",
    "Manindra Agrawal & V. Vinay (FOCS 2008 / ECCC TR08-062)",
    [
        "Foundational Landmark in Algebraic Complexity Theory",
        "Targeting Leslie Valiant's 1979 Conjecture: VP vs VNP",
        "Proves that Depth 4 is as powerful as unrestricted circuit depth for lower bounds"
    ],
    ["Key Question:", "Why did decades of lower bound research stall at Depth 3?"]
)

create_frame(
    "frame_02_det_vs_perm.png",
    "Foundations: Determinant vs Permanent",
    "Volume Scaling (Easy) vs Perfect Matchings (Hard)",
    [
        "Determinant: Alternating signs (+/-) permit Gaussian elimination in O(n^3) [Class VP]",
        "Permanent: Identical formula with all positive signs (+), counts matchings [Class VNP]",
        "Absence of sign cancellations prevents Gaussian elimination and creates hardness",
        "Valiant's 1979 Conjecture: Proving the Permanent requires superpolynomial circuits"
    ],
    ["Core Takeaway:", "Determinant in VP (Easy) <---> Permanent in VNP-Complete (Exponentially Hard)"]
)

create_frame(
    "frame_03_depth_hierarchy.png",
    "The Circuit Model & The Depth Dilemma",
    "From Depth 2 to Unrestricted Deep DAGs",
    [
        "Depth 2 (Sigma-Pi): Trivial monomial expansion, size n! = 2^Omega(n log n)",
        "Depth 3 (Sigma-Pi-Sigma): Exponential lower bounds proven over finite fields",
        "The Stalling Point: Researchers could not prove lower bounds for Depth 4, 5, or 6",
        "Agrawal & Vinay Discovery: Determinant requires exponential size at Depth 3,",
        "but collapses to SUBEXPONENTIAL size n^O(sqrt(n)) at Depth 4!"
    ],
    ["The Power of Depth 4:", "Adding a single fourth layer unlocks the full computational capacity of VP!"]
)

create_frame(
    "frame_04_the_chasm.png",
    "The Depth-Four Chasm Theorem",
    "Theorem 2.4: Collapsing Arbitrary Depth to Depth 4",
    [
        "Any degree-d polynomial computed by a size-s circuit collapses to Depth 4",
        "Depth 4 Circuit Form: Sigma - Pi - Sigma - Pi (Sum-Product-Sum-Product)",
        "Resulting Size: 2^O(sqrt(d log d log s)) -- preserves subexponential size!",
        "Permanent Corollary: Proving 2^Omega(n) lower bound for Depth 4 IMPLIES",
        "an exponential lower bound for ALL unrestricted circuits (VP != VNP)!"
    ],
    ["The Grand Equivalence:", "Exponential Lower Bounds at Depth 4 <===> Exponential Lower Bounds at ALL Depths!"]
)

create_frame(
    "frame_05_pit_bridge.png",
    "Derandomizing Polynomial Identity Testing (PIT)",
    "Hardness vs Randomness via Depth 4",
    [
        "PIT Problem: Does an arithmetic circuit identically equal the zero polynomial?",
        "Randomized solution is easy (Schwartz-Zippel Lemma: evaluate on random field points)",
        "Theorem 3.2: Optimal pseudorandom generator against restricted Depth 4 circuits",
        "yields a deterministic general PIT algorithm running in n^O(log n) time",
        "Combines Nisan-Wigderson designs with Kaltofen's polynomial factorization"
    ],
    ["Algorithmic Duality:", "Circuit Lower Bounds <===> Deterministic Identity Testing"]
)

create_frame(
    "frame_06_takeaways.png",
    "Takeaways for Students & The Modern Legacy",
    "The Foundation for 15+ Years of Breakthroughs",
    [
        "Do not be intimidated by deep circuits: focus analytical tools directly on Depth 4",
        "Led to Gupta, Kamath, Kayal, Saptharishi (2014) Chasm at Depth 3 over Reals/Complex",
        "Inspired Neeraj Kayal's Method of Shifted Partial Derivatives",
        "Explore the 15-note Obsidian Vault in vaults/17_agrawal_vinay_chasm_depth_four-vault/"
    ],
    ["Conclusion:", "Depth 4 is the universal bottleneck of algebraic computation!"]
)

print(f"Generated {len(list(frames_dir.glob('*.png')))} video storyboard frames in {frames_dir}")

# 5. notebooklm_guide.md
guide = """# Google NotebookLM Study Kit: Arithmetic Circuits — A Chasm at Depth Four

Use this guide when importing `papers/agrawal_vinay_2008_chasm_at_depth_four.pdf` into Google NotebookLM.

---

## 📚 Suggested NotebookLM Prompts

1. **Foundations Prompt**:
   > *"Explain the difference between the Determinant and the Permanent to a recent computer science graduate. Why does the determinant have polynomial-size circuits while the permanent is believed to be exponential?"*

2. **The Chasm Theorem Prompt**:
   > *"Explain Agrawal and Vinay's Depth-Four Chasm Theorem in simple terms. How does a circuit of arbitrary depth get converted into a depth-4 circuit without exponential blowup?"*

3. **PIT Prompt**:
   > *"How does black-box identity testing for depth-4 circuits help derandomize general polynomial identity testing? Explain the connection to hardness vs randomness."*

---

## 🧠 Interactive Flashcards

| Front (Question) | Back (Answer) |
| :--- | :--- |
| **What is an arithmetic circuit?** | A directed acyclic graph (DAG) where leaves are variables/constants and internal nodes are addition ($+$) or multiplication ($\\times$) gates over a field $\\mathbb{F}$. |
| **Why is the Determinant in VP?** | Alternating signs in the Leibniz formula allow row operations and Gaussian elimination to compute it in $O(n^3)$ operations. |
| **Why is the Permanent VNP-complete?** | It has no alternating signs; every term is positive. It counts perfect matchings and allows no sign cancellations. |
| **What is the Depth-4 Chasm Theorem?** | Any polynomial of degree $d$ computed by a size-$s$ circuit can be computed by a depth-4 circuit of size $2^{O(\\sqrt{d \\log d \\log s})}$. |
| **What does Corollary 2.6 state for VP vs VNP?** | If every depth-4 circuit for the Permanent requires exponential size, then EVERY circuit of unrestricted depth requires exponential size. |
"""

with open(output_dir / "notebooklm_guide.md", "w", encoding="utf-8") as f:
    f.write(guide.strip() + "\n")

print("All NotebookLM and video assets created successfully!")

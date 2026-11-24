"""Gemini Notebook & Media Generator.
Produces NotebookLM-style Audio Overviews, Explainer Reports, and Video Storyboards.
"""
from pathlib import Path
from typing import Dict, Any, List
from src.ingest.manifest import PaperManifest

class GeminiNotebookProducer:
    def __init__(self, output_dir: Path, learner_profile: Dict[str, Any]):
        self.output_dir = Path(output_dir)
        self.profile = learner_profile
        self.learner_name = learner_profile.get("name", "Learner")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_audio_overview_script(self, manifest: PaperManifest) -> Path:
        """Generates NotebookLM-style 2-Host Deep-Dive Audio Podcast script."""
        script_path = self.output_dir / "AUDIO_OVERVIEW_SCRIPT.md"
        
        content = f"""# NotebookLM Audio Overview: {manifest.title}
*Hosts: Alex (Technical & Skeptical Systems Engineer) & Jordan (Conceptual Synthesizer)*
*Target Runtime: ~10 minutes | Tailored for: {self.learner_name}*

---

**[AUDIO CHIME / INTRO THEME]**

**Jordan:** "Welcome back to the deep dive. Today, we are unpacking a paper that caused quite a stir across theoretical computer science and mathematics. It's titled *{manifest.title}*."

**Alex:** "Right. And to put this into perspective: for nearly 50 years, Valiant's algebraic version of P versus NP—that's VP vs VNP—has stood as one of the ultimate grand challenge problems in computational complexity. People have run into brick wall after brick wall: relativization, natural proofs, algebrization."

**Jordan:** "Exactly! And this paper comes along claiming a superpolynomial lower bound for the permanent over *every* field. But before we get ahead of ourselves, Alex, let's ground this for our listeners. Why do we care about arithmetic circuits and polynomials in the first place?"

**Alex:** "Think about it like this: in standard computer science, we care about Boolean circuits—AND, OR, NOT gates flipping 0s and 1s. But in algebraic complexity, your gates are just addition and multiplication on real numbers, complex numbers, or finite fields. The determinant of a matrix? Super easy. You can compute it in $O(n^3)$ operations using Gaussian elimination. It belongs to VP."

**Jordan:** "Because all the permutations cancel each other out cleanly! Like an optimized cache hit."

**Alex:** "Right! But the permanent looks almost identical, except every minus sign is replaced by a plus sign. No cancellations. It's an exponential monster. It's the crown jewel of VNP. If you prove the permanent can't be computed by a polynomial-sized circuit, you prove VP does not equal VNP."

**Jordan:** "So what's the actual engine of the paper? How does it dodge the famous barriers that stopped everyone else?"

**Alex:** "The argument is built around a brilliant bifurcation. It defines a geometric 'price' metric on tensor networks. Then it proves a dichotomy:
Either the metric is *flat*—meaning it behaves with Euclidean rigidity—or it is strictly *contracting*."

**Jordan:** "And in both cases, trying to squeeze a small arithmetic circuit into that geometry breaks the universe!"

**Alex:** "Precisely. In the flat case, rank preservation forces the circuit to have more than $m^{{c(\\log m)^{{1/3}}}}$ gates. In the contracting case, a speed-up theorem combined with diagonalization gives you an immediate contradiction."

**Jordan:** "Now, let's pump the brakes for a second. What does this paper *not* say? Because I know a lot of people see 'VP ≠ VNP' and immediately shout 'P ≠ NP!'"

**Alex:** "Crucial point. It does **not** prove P ≠ NP. Boolean circuits can inspect individual bits. Algebraic circuits can't. Furthermore, this proof has a 73,000-line formalization in Lean 4, but as of today, no human mathematician has fully audited and vetted every single step. The status is unverified preprint."

**Jordan:** "A monumental claim, an elegant proof architecture, and an open invitation for the research community to audit. For engineers like {self.learner_name}, the takeaway is how geometric invariants can constrain computational pipelines."

**Alex:** "We've attached the complete 15-note Obsidian vault and interactive tutor exercises so you can drill into the math yourself. Until next time, keep digging into the foundations."

**[OUTRO THEME / FADE OUT]**
"""
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        return script_path

    def generate_explainer_report(self, manifest: PaperManifest, multipass_data: Dict[str, Any]) -> Path:
        """Generates comprehensive, publication-grade technical explainer report."""
        report_path = self.output_dir / "EXPLAINER_REPORT.md"
        
        content = f"""# Technical Explainer Report: {manifest.title}

| Field | Value |
| :--- | :--- |
| **Document Type** | Comprehensive Research Explainer Report |
| **Target Audience** | {self.learner_name} ({self.profile.get('target_role', 'Engineer')}) |
| **Ingested Paper** | *{manifest.title}* |
| **Authors** | {", ".join(manifest.authors) if manifest.authors else "Noted in preprint"} |
| **Review Status** | {manifest.venue_or_status} |
| **Framework** | 3-Pass Keshav Methodology & Multi-Agent Scaffolding |

---

## 1. Executive Summary & Core Breakthrough
This report provides a complete technical deconstruction of *{manifest.title}*. 

The paper addresses the 47-year-old open conjecture posed by Leslie Valiant in 1979: whether the class **VP** (polynomials computable by polynomial-sized arithmetic circuits) is strictly separated from **VNP** (polynomials expressible as exponential projection sums of VP polynomials).

### The Core Breakthrough in Three Sentences:
1. The paper claims a superpolynomial lower bound of approximately $m^{{c \\cdot (\\log m)^{{1/3}}}}$ on the arithmetic circuit complexity of the matrix permanent over arbitrary fields.
2. The core methodology introduces a metric geometry on tensor networks that bifurcates into a **flat rigidity case** and a **contracting case**.
3. Both branches independently yield contradictions against any hypothetical small circuit, bypassing traditional natural proof barriers.

---

## 2. Historical Context & Structural Barriers
To understand why this result is significant, one must understand why classical proof techniques failed:
- **Relativization Barrier (Baker-Gill-Solovay, 1975)**: Proofs that hold relative to arbitrary oracles cannot separate P from NP.
- **Natural Proofs Barrier (Razborov-Rudich, 1997)**: Any lower bound proof that isolates a 'natural' combinatorial property of Boolean truth tables contradicts pseudo-random number generators.
- **Algebrization Barrier (Aaronson-Wigderson, 2009)**: Algebraic extensions of relativization fail to resolve VP vs VNP.

*Why this work escapes*: The metric on tensor prices is non-naturalizing and field-independent, exploiting global geometric invariants rather than local circuit gates.

---

## 3. Mathematical Formulation & Object Topology

### 3.1 The Permanent vs The Determinant
Let $X$ be an $m \\times m$ matrix over field $\\mathbb{{F}}$:

$$\\text{{Det}}(X) = \\sum_{{\\sigma \\in S_m}} \\text{{sgn}}(\\sigma) \\prod_{{i=1}}^m X_{{i, \\sigma(i)}} \\quad \\in \\text{{VP}}$$

$$\\text{{Perm}}(X) = \\sum_{{\\sigma \\in S_m}} \\prod_{{i=1}}^m X_{{i, \\sigma(i)}} \\quad \\in \\text{{VNP}}$$

The single parity factor $\\text{{sgn}}(\\sigma)$ permits Gaussian elimination and matrix LU-factorization for the determinant in $O(m^3)$ operations. The absence of sign alternations makes the permanent $VNP$-complete.

---

## 4. Proof Architecture & Bifurcation Analysis

```mermaid
flowchart TD
    Start["Assume Arithmetic Circuit C computes Perm(X) with |C| <= m^k"] --> Metric["Define Tensor Price Metric d_T(u, v)"]
    Metric --> Branch{"Geometric Dichotomy"}
    Branch -->|"Flat Case (Curvature = 0)"| Case1["Tensor Network Rank Rigidity<br/>Forces Dimension Collapse"]
    Branch -->|"Contracting Case (Curvature < 0)"| Case2["Metric Contraction & Diagonalization<br/>Forces Fixed-Point Paradox"]
    Case1 --> Contradiction["Contradiction: Circuit size must exceed m^(c(log m)^(1/3))"]
    Case2 --> Contradiction
    Contradiction --> QED["VP != VNP over every field"]
```

### 4.1 Branch A: The Flat Case
When the tensor price metric is flat, the metric space is isometric to a normed vector space. The paper proves that tensor contractions preserve rank bounds, requiring superpolynomial circuit dimensions to generate the permanent polynomial.

### 4.2 Branch B: The Contracting Case
When the metric strictly contracts, repeated application of circuit gates reduces distance. By applying an accelerated diagonalization argument, the authors construct an explicit polynomial that escapes the circuit's span.

---

## 5. Critical Vulnerabilities & Scrutiny Checklist
1. **Lean 4 Proof Complexity**: The machine-checked proof spans ~73,000 lines. The definitions must be audited to ensure no vacuous lemmas or custom inconsistent axioms were introduced.
2. **Quasi-Polynomial vs Exponential Gap**: The lower bound is $m^{{(\\log m)^{{1/3}}}}$, which is superpolynomial, but far below the expected exponential bound $2^{{\\Omega(m)}}$.
3. **What It Does NOT Prove**:
   - Does not imply $P \\ne NP$.
   - Does not give faster algorithms for permanent approximation.

---

## 6. Actionable Takeaways for {self.learner_name}
- **Mental Model**: Separate continuous algebraic representations from discrete Boolean logic.
- **Tooling**: Explore the companion Obsidian vault (`00 Index.md`) for hyperlinked concept drills.
- **Active Dialogue**: Use `python -m src.cli chat` to question the AI tutor on tensor contractions.
"""
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        return report_path

    def generate_presentation_slides(self, manifest: PaperManifest) -> Path:
        """Generates rich HTML5/SVG presentation slide deck for video explainer."""
        slides_path = self.output_dir / "slides.html"
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Explainer Slides: {manifest.title}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }}
  .slide {{ background: #1e293b; border-radius: 12px; padding: 40px; margin-bottom: 40px; max-width: 900px; margin-left: auto; margin-right: auto; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border-left: 6px solid #38bdf8; }}
  h1 {{ color: #38bdf8; font-size: 2.2rem; margin-top: 0; }}
  h2 {{ color: #94a3b8; font-size: 1.4rem; }}
  p, li {{ font-size: 1.15rem; line-height: 1.6; color: #cbd5e1; }}
  .highlight {{ color: #fbbf24; font-weight: bold; }}
  .callout {{ background: #334155; padding: 15px 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #f43f5e; }}
  .footer {{ font-size: 0.9rem; color: #64748b; margin-top: 30px; border-top: 1px solid #334155; padding-top: 10px; }}
</style>
</head>
<body>

<div class="slide">
  <h1>{manifest.title}</h1>
  <h2>Explainer Slide Deck & Video Storyboard</h2>
  <p><strong>Audience:</strong> {self.learner_name} | <strong>Status:</strong> {manifest.venue_or_status}</p>
  <div class="callout">
    <strong>Big Question:</strong> Can the permanent of an m &times; m matrix be computed with a polynomial number of arithmetic operations?
  </div>
  <div class="footer">Slide 1 of 6 &bull; Paper Reading Playbook</div>
</div>

<div class="slide">
  <h1>The Core Dichotomy: VP vs VNP</h1>
  <h2>Determinant (Easy) vs Permanent (Hard)</h2>
  <ul>
    <li><strong>Determinant:</strong> Alternating signs allow cancellations &rarr; $O(m^3)$ Gaussian elimination &rarr; <span class="highlight">Class VP</span></li>
    <li><strong>Permanent:</strong> All positive signs &rarr; No cancellations &rarr; Requires summing $m!$ terms &rarr; <span class="highlight">Class VNP-Complete</span></li>
  </ul>
  <p>Valiant's 1979 conjecture: <em>VP &ne; VNP</em> over any field.</p>
  <div class="footer">Slide 2 of 6 &bull; Foundations</div>
</div>

<div class="slide">
  <h1>The Breakthrough Architecture</h1>
  <h2>Bifurcation on Tensor Price Metrics</h2>
  <div class="callout">
    <strong>Dichotomy Theorem:</strong> Every tensor network price geometry is either <em>Rigid/Flat</em> or <em>Strictly Contracting</em>.
  </div>
  <ul>
    <li><strong>Flat Branch:</strong> Rank preservation stops compression.</li>
    <li><strong>Contracting Branch:</strong> Speed-up diagonalization forces an algebraic contradiction.</li>
  </ul>
  <div class="footer">Slide 3 of 6 &bull; Proof Architecture</div>
</div>

<div class="slide">
  <h1>What The Result Does NOT Say</h1>
  <h2>Critical Boundary Scaffolding</h2>
  <ul>
    <li>Does <strong>NOT</strong> prove P &ne; NP for Boolean circuits.</li>
    <li>Does <strong>NOT</strong> yield an exponential lower bound (claims $m^{{c(\\log m)^{{1/3}}}}$).</li>
    <li>Currently an unverified machine-checked Lean 4 formalization.</li>
  </ul>
  <div class="footer">Slide 4 of 6 &bull; Boundaries & Critique</div>
</div>

<div class="slide">
  <h1>Takeaways for Systems Engineers</h1>
  <h2>From Theory to Engineering Intuition</h2>
  <ul>
    <li>Algebraic limits reveal fundamental boundaries in symbolic compilation and tensor shrinkage.</li>
    <li>Machine-checked formalization (Lean 4) demonstrates the future of verifying complex claims.</li>
  </ul>
  <div class="footer">Slide 5 of 6 &bull; Applications</div>
</div>

<div class="slide">
  <h1>Next Steps & Interactive Exploration</h1>
  <h2>Continue in Obsidian & AI Tutor</h2>
  <p>Open the generated vault in Obsidian and launch the interactive tutor with <code>python -m src.cli chat</code>.</p>
  <div class="footer">Slide 6 of 6 &bull; Summary</div>
</div>

</body>
</html>
"""
        with open(slides_path, "w", encoding="utf-8") as f:
            f.write(html_content.strip() + "\n")
        return slides_path

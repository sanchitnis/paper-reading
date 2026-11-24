# Getting Started with the Paper Reading Playbook

Welcome to the **Paper Reading Playbook**! This guide walks you through setting up your environment, personalizing your learner profile, ingesting your first research paper, generating an Obsidian vault, producing Gemini Notebook multimedia assets, and tutoring with the interactive AI chatbot.

---

## 1. Prerequisites & Environment Setup

### 1.1 Python Environment
The playbook requires **Python 3.10+** (Python 3.12 recommended). Verify your Python version:
```bash
python --version
```

### 1.2 Install Dependencies
Install all required libraries (PyMuPDF, Pydantic, Matplotlib, Pillow, etc.):
```bash
pip install -r requirements.txt
```

### 1.3 Configure API Keys (Optional but Recommended)
The playbook includes a built-in pedagogical reasoning engine that runs 100% locally offline. To enable live calls to **Google Gemini 2.0 / NotebookLM APIs** for real-time model synthesis:
```bash
# Windows PowerShell:
$env:GEMINI_API_KEY="your-gemini-api-key"

# Linux / macOS:
export GEMINI_API_KEY="your-gemini-api-key"
```

---

## 2. Personalize Your Learner Profile

The playbook adapts its explanations, analogies, and mathematical scaffolding directly to your background. Open [`learner_profile.json`](learner_profile.json) to inspect or modify your settings:

```json
{
  "learner_id": "alex_rivera",
  "name": "Alex Rivera",
  "target_role": "Senior AI Systems Engineer & Applied ML Researcher",
  "prior_knowledge": {
    "strong": ["Python", "PyTorch", "Linear Algebra", "Distributed Systems"],
    "intermediate": ["Bayesian Inference", "Reinforcement Learning"],
    "developing": ["Algebraic Complexity Theory", "Differential Geometry", "Lean 4"]
  },
  "pedagogical_preferences": {
    "explanation_style": "Intuition-first, followed by rigorous math and toy code.",
    "analogy_domain": "Software architecture and distributed systems"
  }
}
```

---

## 3. Quickstart: End-to-End Pipeline in One Command

Run the entire pipeline on any paper (PDF file, arXiv URL, or text summary):

```bash
python -m src.cli run-all "vp-vnp-vault/00 Index.md"
```

Or run on a live arXiv paper:
```bash
python -m src.cli run-all "https://arxiv.org/abs/2401.12345"
```

### What `run-all` Generates:
1. **Pass 1, 2, and 3 Multipass Analysis**: 5 C's scoring, cognitive bottleneck identification, and deconstruction.
2. **Interconnected Obsidian Vault**: 15 hyperlinked notes in `vaults/<paper-id>-vault/`.
3. **NotebookLM Audio Overview Script**: A 2-host conversational podcast script in `outputs/<paper-id>/AUDIO_OVERVIEW_SCRIPT.md`.
4. **Interactive Explainer Slides**: HTML5/SVG presentation in `outputs/<paper-id>/slides.html`.
5. **Video Storyboard Frames**: Rendered high-res visuals in `outputs/<paper-id>/video_frames/`.
6. **Technical Explainer Report**: Publication-grade deconstruction in `outputs/<paper-id>/EXPLAINER_REPORT.md`.

---

## 4. Step-by-Step Command Walkthrough

You can also run each stage modularly:

### Step 4.1: Ingest & Parse Paper
```bash
python -m src.cli ingest "path/to/paper.pdf"
```

### Step 4.2: Run 3-Pass Reading Analysis
```bash
python -m src.cli multipass "path/to/paper.pdf"
```
Outputs the Pass 1 Triage decision, Pass 2 cognitive bottlenecks matching your profile, and Pass 3 deconstruction milestones.

### Step 4.3: Generate Obsidian Knowledge Vault
```bash
python -m src.cli vault "path/to/paper.pdf" --vault-name "my-custom-vault"
```
To open the vault in [Obsidian](https://obsidian.md/):
1. Open Obsidian.
2. Click **Open folder as vault**.
3. Select `d:/sanjay/paper-reading/vaults/my-custom-vault` (or `vp-vnp-vault`).
4. Click on `00 Index.md` to begin following the curated reading path!

### Step 4.4: Generate NotebookLM Media & Video Assets
```bash
python -m src.cli media "path/to/paper.pdf"
```
Creates `AUDIO_OVERVIEW_SCRIPT.md`, `slides.html`, and rendered visual frames.

### Step 4.5: Generate Detailed Explainer Report
```bash
python -m src.cli report "path/to/paper.pdf"
```
Produces `EXPLAINER_REPORT.md` ready for reading or converting to PDF.

### Step 4.6: Interactive AI Chatbot & Socratic Mentor
Launch the interactive terminal chat session:
```bash
python -m src.cli chat "path/to/paper.pdf"
```

#### In-Chat Commands:
- `/feynman` - Get an intuitive systems-level analogy.
- `/math` - Unpack equations, tensors, and derivations step-by-step.
- `/drill` - Take a Socratic quiz to test your mental model.
- `/code` - Request a minimal runnable Python simulation of the concept.
- `exit` - Exit the chat session.

### Step 4.7: Live Google NotebookLM Cloud Generation (via `notebooklm-py`)
To use live Google NotebookLM to generate real MP4 explainer videos, M4A podcasts, slide decks, and study guides:

1. **Check or Sign In to NotebookLM**:
   ```bash
   python -m src.cli notebooklm-auth --login
   # Or directly:
   notebooklm login
   ```
2. **Sync Paper & Auto-Generate Cloud Artifacts**:
   ```bash
   python -m src.cli notebooklm-sync "papers/01_attention_is_all_you_need.md"
   ```
3. **Generate & Download Specific Live Artifacts**:
   ```bash
   # Generate and download a video explainer (.mp4)
   python -m src.cli notebooklm-video "papers/01_attention_is_all_you_need.md"

   # Generate a study report, quiz, or mind-map
   python -m src.cli notebooklm-doc "papers/01_attention_is_all_you_need.md" --doc-type quiz
   python -m src.cli notebooklm-doc "papers/01_attention_is_all_you_need.md" --doc-type mind-map
   ```
   Artifacts are downloaded directly into `outputs/<paper_id>/`.

---

## 5. Directory Structure Overview

```
paper-reading/
├── .agents/
│   └── skills/                      # Standard agent skill definitions
│       ├── paper-ingest/
│       ├── multipass-reader/
│       ├── concept-explainer/
│       ├── obsidian-vault-builder/
│       ├── gemini-notebook-media/
│       └── explainer-report-generator/
├── src/                             # Core Python implementation
│   ├── config.py                    # Settings & profile manager
│   ├── cli.py                       # Unified command-line interface
│   ├── ingest/                      # PDF, arXiv & text parsers
│   ├── multipass/                   # 3-pass Keshav engine
│   ├── vault/                       # Obsidian 15-note vault builder
│   ├── chatbot/                     # Socratic AI tutor REPL
│   └── gemini/                      # Gemini Notebook media & report engine
├── learner_profile.json             # Learner persona and preferences
├── README.md                        # Master playbook documentation
├── GETTING_STARTED.md               # This setup and onboarding guide
├── agents.md                        # Multi-agent architecture specification
├── requirements.txt                 # Dependencies
├── vp-vnp-vault/                    # Reference gold-standard Obsidian vault
├── vaults/                          # Generated Obsidian vaults
└── outputs/                         # Generated reports, scripts & video frames
```

---

## 6. Frequently Asked Questions (FAQ)

**Q: Can I run this without a GPU or Gemini API key?**  
**A:** Yes! The entire core pipeline (ingestion, multipass analysis, Obsidian vault generation, video storyboard rendering, and local pedagogical tutoring) runs 100% locally on CPU without requiring an API key. Supplying `GEMINI_API_KEY` unlocks live cloud multimodal generation.

**Q: How do I read papers with mathematical proofs if I get stuck?**  
**A:** Follow the 3-pass workflow: in Pass 2, intentionally skip dense lemma proofs and note the high-level intuition. Then launch `python -m src.cli chat` and type `/feynman` or `/math` to let the tutor break the proof down into manageable pieces.

**Q: Can I customize the Obsidian vault structure?**  
**A:** Yes! You can edit `src/vault/generator.py` or customize the templates to add custom frontmatter tags, callout banners, or canvas files.

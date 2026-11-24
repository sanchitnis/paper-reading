"""Multipass paper reading engine implementing Keshav's 3-pass methodology."""
from typing import Dict, Any, List
from src.ingest.manifest import PaperManifest

class MultipassEngine:
    def __init__(self, learner_profile: Dict[str, Any]):
        self.profile = learner_profile
        self.learner_name = learner_profile.get("name", "Learner")
        self.developing_areas = set(
            concept.lower() for concept in learner_profile.get("prior_knowledge", {}).get("developing", [])
        )
        self.strong_areas = set(
            concept.lower() for concept in learner_profile.get("prior_knowledge", {}).get("strong", [])
        )

    def execute_pass1(self, manifest: PaperManifest) -> Dict[str, Any]:
        """Pass 1: Triage & Reconnaissance (10-15 mins)."""
        headings = [sec.heading for sec in manifest.sections]
        abstract_len = len(manifest.abstract.split())
        
        # 5 C's evaluation
        category = self._classify_category(manifest)
        context = f"Situates within {manifest.primary_category} and foundational literature."
        correctness = "Preprint - claims require verification of formal proofs or empirical baselines."
        contributions = self._extract_claimed_contributions(manifest)
        clarity = "High" if len(headings) >= 4 else "Moderate"

        # Triage recommendation
        is_relevant = any(area in manifest.abstract.lower() or any(area in h.lower() for h in headings) 
                          for area in self.strong_areas | self.developing_areas)
        decision = "Proceed to Pass 2 (High Value)" if is_relevant or len(manifest.sections) > 0 else "File for Later"

        return {
            "pass": 1,
            "title": manifest.title,
            "time_budget_mins": self.profile.get("multipass_budget_minutes", {}).get("pass1_triage", 15),
            "five_cs": {
                "category": category,
                "context": context,
                "correctness_initial_status": correctness,
                "contributions_summary": contributions,
                "clarity_rating": clarity
            },
            "structural_overview": {
                "total_sections": len(manifest.sections),
                "section_headings": headings,
                "figure_count": len(manifest.figures),
                "table_count": len(manifest.tables)
            },
            "gate_decision": decision,
            "next_steps": "Review figures and section transitions; prepare target questions for AI tutor."
        }

    def execute_pass2(self, manifest: PaperManifest) -> Dict[str, Any]:
        """Pass 2: Conceptual Grasp & Inspection (1-2 hours)."""
        full_text = manifest.get_full_text().lower()
        
        # Identify cognitive bottlenecks matching learner profile's developing areas
        bottlenecks = []
        for area in self.developing_areas:
            if any(term in full_text for term in area.split() if len(term) > 3):
                bottlenecks.append({
                    "topic": area,
                    "reason": f"Matches learner profile developing knowledge area '{area}'.",
                    "tutor_action": "Generate intuitive Feynman analogy and step-by-step math scaffolding."
                })

        # Generate sample reading questions for tutor
        target_questions = [
            f"What is the intuitive core of the proof/method in {manifest.title} without the dense math?",
            "How does this breakthrough bypass standard barriers (e.g. natural proofs or optimization limits)?",
            "What happens if the primary hypothesis does not hold?",
            "Can you write a minimal Python snippet simulating this mechanism?"
        ]

        # Key conceptual milestones
        milestones = [
            "Grasp core objects and definitions",
            "Map out the main proof or pipeline topology",
            "Inspect all charts and experimental claims",
            "Consult AI tutor for flagged bottlenecks"
        ]

        return {
            "pass": 2,
            "time_budget_mins": self.profile.get("multipass_budget_minutes", {}).get("pass2_conceptual_grasp", 60),
            "flagged_bottlenecks": bottlenecks,
            "target_tutor_questions": target_questions,
            "reading_milestones": milestones,
            "concept_graph_ready": True
        }

    def execute_pass3(self, manifest: PaperManifest) -> Dict[str, Any]:
        """Pass 3: Deep Technical Deconstruction (3-5 hours)."""
        deconstruction = {
            "pass": 3,
            "time_budget_mins": self.profile.get("multipass_budget_minutes", {}).get("pass3_deep_deconstruction", 180),
            "virtual_reimplementation": {
                "goal": "Mentally re-create the theorem proof or algorithmic architecture from first principles.",
                "steps": [
                    "Isolate the minimal working example (e.g. 3x3 matrix permanent vs determinant).",
                    "Trace the bifurcation into cases (e.g. flat metric vs contracting metric).",
                    "Audit formal verification proofs or codebase repository.",
                    "Verify where existing barrier results fail to apply."
                ]
            },
            "failure_mode_analysis": [
                "Sensitivity to underlying field or precision assumptions.",
                "Constants hidden in asymptotic Omega/Big-O notation.",
                "Non-claims: What does this paper explicitly NOT solve?"
            ],
            "artifact_generation_triggers": {
                "obsidian_vault": True,
                "explainer_report": True,
                "notebook_audio_video": True
            }
        }
        return deconstruction

    def _classify_category(self, manifest: PaperManifest) -> str:
        text = (manifest.title + " " + manifest.abstract).lower()
        if any(w in text for w in ["proof", "theorem", "complexity", "lower bound", "formal"]):
            return "Theoretical Computer Science / Mathematics"
        elif any(w in text for w in ["benchmark", "dataset", "empirical", "evaluation"]):
            return "Empirical ML / Benchmark Analysis"
        elif any(w in text for w in ["architecture", "system", "compiler", "hardware"]):
            return "Systems & Architectural Design"
        return "Applied Machine Learning & Foundations"

    def _extract_claimed_contributions(self, manifest: PaperManifest) -> List[str]:
        # Return structured highlights based on title and abstract
        return [
            f"Primary claim: {manifest.title}",
            f"Core method/result stated in abstract: {manifest.abstract[:180]}..."
        ]

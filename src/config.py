"""Configuration manager for Paper Reading Playbook."""
import os
import json
from pathlib import Path
from typing import Dict, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_PROFILE_PATH = BASE_DIR / "learner_profile.json"

class Config:
    def __init__(self, profile_path: Optional[Path] = None):
        self.base_dir = BASE_DIR
        self.profile_path = profile_path or DEFAULT_PROFILE_PATH
        self.learner_profile: Dict[str, Any] = self._load_profile()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.output_dir = BASE_DIR / "outputs"
        self.vaults_dir = BASE_DIR / "vaults"
        
        # Ensure directories exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.vaults_dir.mkdir(parents=True, exist_ok=True)

    def _load_profile(self) -> Dict[str, Any]:
        if self.profile_path.exists():
            try:
                with open(self.profile_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[Warning] Failed to load learner profile: {e}")
        return {
            "learner_id": "default_learner",
            "name": "Self-Directed Learner",
            "target_role": "AI Researcher / Systems Engineer",
            "prior_knowledge": {"strong": [], "intermediate": [], "developing": []},
            "pedagogical_preferences": {
                "explanation_style": "Intuition-first with formal math breakdown",
                "analogy_domain": "Software and distributed systems",
                "math_scaffolding": "Step-by-step breakdown",
                "visual_preference": "Mermaid diagrams"
            }
        }

config = Config()

"""Bridge integrating teng-lin/notebooklm-py for automated NotebookLM artifact generation.
Supports generating live Audio Overviews, Explainer Videos, Slide Decks, and Study Documents.
"""
import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional
from src.ingest.manifest import PaperManifest

class NotebookLMBridge:
    def __init__(self, profile: str = "default"):
        self.profile = profile
        self.cli_available = shutil.which("notebooklm") is not None

    def check_auth(self) -> Dict[str, Any]:
        """Checks if user is authenticated with NotebookLM."""
        if not self.cli_available:
            return {"authenticated": False, "error": "notebooklm CLI not found in PATH"}

        try:
            cmd = ["notebooklm", "auth", "check", "--test", "--passive", "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                is_ok = data.get("status") == "ok" and data.get("checks", {}).get("token_fetch", False)
                return {"authenticated": is_ok, "details": data}
            else:
                return {"authenticated": False, "error": res.stderr.strip() or res.stdout.strip()}
        except Exception as e:
            return {"authenticated": False, "error": str(e)}

    def create_notebook(self, title: str) -> Optional[str]:
        """Creates a new NotebookLM notebook and returns its UUID."""
        try:
            cmd = ["notebooklm", "create", title, "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                return data.get("notebook", {}).get("id") or data.get("id")
        except Exception as e:
            print(f"[NotebookLM] Error creating notebook: {e}")
        return None

    def add_source_and_wait(self, notebook_id: str, file_or_url: str) -> Optional[str]:
        """Uploads a PDF, file, or URL to the notebook and waits for processing."""
        try:
            cmd = ["notebooklm", "source", "add", file_or_url, "-n", notebook_id, "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                source_id = data.get("source", {}).get("id") or data.get("id")
                if source_id:
                    # Wait for source to be ready
                    wait_cmd = ["notebooklm", "source", "wait", source_id, "-n", notebook_id, "--json"]
                    subprocess.run(wait_cmd, capture_output=True, text=True, timeout=120)
                    return source_id
        except Exception as e:
            print(f"[NotebookLM] Error adding source {file_or_url}: {e}")
        return None

    def generate_and_download_audio(self, notebook_id: str, output_path: Path) -> bool:
        """Generates an Audio Overview (podcast) and downloads the audio file."""
        try:
            print(f"[NotebookLM] Triggering Audio Overview generation for notebook {notebook_id}...")
            cmd = ["notebooklm", "generate", "audio", "-n", notebook_id, "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                task_id = data.get("task_id")
                if task_id:
                    print("[NotebookLM] Waiting for audio generation to complete (typically 3-5 mins)...")
                    wait_cmd = ["notebooklm", "artifact", "wait", task_id, "-n", notebook_id, "--json"]
                    wait_res = subprocess.run(wait_cmd, capture_output=True, text=True, timeout=600)
                    if wait_res.returncode == 0:
                        dl_cmd = ["notebooklm", "download", "audio", str(output_path), "-n", notebook_id]
                        subprocess.run(dl_cmd, capture_output=True, text=True, timeout=60)
                        return output_path.exists()
        except Exception as e:
            print(f"[NotebookLM] Audio generation failed: {e}")
        return False

    def generate_and_download_video(self, notebook_id: str, output_path: Path, format: str = "video") -> bool:
        """Generates an Explainer Video and downloads the video file."""
        try:
            print(f"[NotebookLM] Triggering {format} generation for notebook {notebook_id}...")
            cmd = ["notebooklm", "generate", format, "-n", notebook_id, "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                task_id = data.get("task_id")
                if task_id:
                    print(f"[NotebookLM] Waiting for {format} generation to complete...")
                    wait_cmd = ["notebooklm", "artifact", "wait", task_id, "-n", notebook_id, "--json"]
                    wait_res = subprocess.run(wait_cmd, capture_output=True, text=True, timeout=1200)
                    if wait_res.returncode == 0:
                        dl_cmd = ["notebooklm", "download", format, str(output_path), "-n", notebook_id]
                        subprocess.run(dl_cmd, capture_output=True, text=True, timeout=120)
                        return output_path.exists()
        except Exception as e:
            print(f"[NotebookLM] Video generation failed: {e}")
        return False

    def generate_study_document(self, notebook_id: str, doc_type: str, output_path: Path) -> bool:
        """Generates a study document (report, quiz, flashcards, mind-map, slide-deck)."""
        try:
            print(f"[NotebookLM] Generating {doc_type} for notebook {notebook_id}...")
            cmd = ["notebooklm", "generate", doc_type, "-n", notebook_id, "--json"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if res.returncode == 0:
                dl_cmd = ["notebooklm", "download", doc_type, str(output_path), "-n", notebook_id]
                subprocess.run(dl_cmd, capture_output=True, text=True, timeout=60)
                return output_path.exists()
        except Exception as e:
            print(f"[NotebookLM] Document generation failed: {e}")
        return False

    def sync_paper_to_notebooklm(self, manifest: PaperManifest, output_dir: Path) -> Dict[str, Any]:
        """High-level orchestration: checks auth, creates notebook, adds source, and produces artifacts."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        results = {"notebook_id": None, "source_id": None, "artifacts": {}}

        auth = self.check_auth()
        if not auth.get("authenticated"):
            print("\n[NotebookLM Notice] Not authenticated with live Google NotebookLM.")
            print("To enable direct cloud generation from your NotebookLM account, run:")
            print("  notebooklm login\n")
            print("Falling back to local high-fidelity generator for scripts, slides, and reports.")
            return results

        nb_title = f"Paper: {manifest.title[:45]}"
        nb_id = self.create_notebook(nb_title)
        if not nb_id:
            return results
        results["notebook_id"] = nb_id
        print(f"[✓] Created live NotebookLM notebook: {nb_id}")

        # Add source file
        source_path = manifest.file_path or str(output_dir / "paper_source.txt")
        if not Path(source_path).exists():
            with open(source_path, "w", encoding="utf-8") as f:
                f.write(manifest.get_full_text())

        src_id = self.add_source_and_wait(nb_id, str(source_path))
        results["source_id"] = src_id
        print(f"[✓] Uploaded and indexed source: {source_path}")

        # Attempt video generation
        video_out = output_dir / f"{manifest.paper_id}_explainer.mp4"
        if self.generate_and_download_video(nb_id, video_out):
            results["artifacts"]["video"] = str(video_out)
            print(f"[✓] Downloaded live NotebookLM video to: {video_out}")

        # Attempt audio overview generation
        audio_out = output_dir / f"{manifest.paper_id}_podcast.m4a"
        if self.generate_and_download_audio(nb_id, audio_out):
            results["artifacts"]["audio"] = str(audio_out)
            print(f"[✓] Downloaded live NotebookLM audio podcast to: {audio_out}")

        # Attempt study guide / report generation
        report_out = output_dir / f"{manifest.paper_id}_notebooklm_report.md"
        if self.generate_study_document(nb_id, "report", report_out):
            results["artifacts"]["report"] = str(report_out)
            print(f"[✓] Downloaded live NotebookLM report to: {report_out}")

        return results

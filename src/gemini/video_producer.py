"""Video storyboard and frame renderer using Matplotlib and Pillow."""
from pathlib import Path
from typing import Dict, Any, List
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class VideoProducer:
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_storyboard_frames(self, title: str, status: str) -> List[Path]:
        """Renders 4 high-resolution visual explainer frames for video generation."""
        frames = []
        frames_dir = self.output_dir / "video_frames"
        frames_dir.mkdir(parents=True, exist_ok=True)

        # Frame 1: Title & Tension
        f1_path = frames_dir / "frame_01_title.png"
        fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#0f172a')
        ax.axis('off')
        
        ax.text(0.5, 0.65, title, fontsize=20, color='#38bdf8', weight='bold', ha='center', wrap=True)
        ax.text(0.5, 0.45, "Explainer Video Storyboard", fontsize=16, color='#94a3b8', ha='center')
        ax.text(0.5, 0.30, f"Status: {status}", fontsize=13, color='#f43f5e', ha='center')
        
        plt.tight_layout()
        plt.savefig(f1_path, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close(fig)
        frames.append(f1_path)

        # Frame 2: Det vs Perm
        f2_path = frames_dir / "frame_02_det_vs_perm.png"
        fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#0f172a')
        ax.axis('off')

        ax.text(0.5, 0.85, "Determinant (VP) vs Permanent (VNP)", fontsize=18, color='#38bdf8', weight='bold', ha='center')
        ax.text(0.25, 0.60, "Determinant:\n- Alternating signs\n- Gaussian elimination\n- Polynomial time: O(n^3)", 
                fontsize=13, color='#a7f3d0', ha='center')
        ax.text(0.75, 0.60, "Permanent:\n- No signs\n- Sums all n! terms\n- Hard for VNP\n- No known shortcut", 
                fontsize=13, color='#fecdd3', ha='center')

        plt.tight_layout()
        plt.savefig(f2_path, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close(fig)
        frames.append(f2_path)

        # Frame 3: Proof Bifurcation
        f3_path = frames_dir / "frame_03_dichotomy.png"
        fig, ax = plt.subplots(figsize=(12, 6.75), dpi=100)
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#0f172a')
        ax.axis('off')

        ax.text(0.5, 0.85, "The Geometric Dichotomy", fontsize=18, color='#38bdf8', weight='bold', ha='center')
        ax.text(0.5, 0.65, "Tensor Price Metric d_T", fontsize=14, color='#fbbf24', weight='bold', ha='center')
        ax.text(0.25, 0.40, "[Case 1: Flat Metric]\nRank Rigidity\n--> Dimensions collapse", fontsize=13, color='#e2e8f0', ha='center')
        ax.text(0.75, 0.40, "[Case 2: Contracting Metric]\nDiagonalization Paradox\n--> Fixed-point collapse", fontsize=13, color='#e2e8f0', ha='center')
        ax.text(0.5, 0.15, "Both cases rule out polynomial-size circuits!", fontsize=14, color='#38bdf8', ha='center')

        plt.tight_layout()
        plt.savefig(f3_path, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close(fig)
        frames.append(f3_path)

        return frames

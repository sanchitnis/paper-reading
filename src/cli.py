"""Unified CLI for the Paper Reading Playbook."""
import sys
import argparse
from pathlib import Path
from src.config import config
from src.ingest import load_paper
from src.multipass.engine import MultipassEngine
from src.vault.generator import ObsidianVaultGenerator
from src.chatbot.tutor import PaperTutorChatbot
from src.gemini.notebook_api import GeminiNotebookProducer
from src.gemini.video_producer import VideoProducer
from src.gemini.notebooklm_bridge import NotebookLMBridge

def main():
    parser = argparse.ArgumentParser(
        description="Paper Reading Playbook: Multi-pass research explorer with Obsidian, Gemini Notebook, and AI Chatbot."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Command: run-all
    run_all_p = subparsers.add_parser("run-all", help="Execute complete pipeline end-to-end")
    run_all_p.add_argument("source", help="Paper path, arXiv ID, or text file")
    run_all_p.add_argument("--output-dir", default=str(config.output_dir), help="Output directory")

    # Command: ingest
    ingest_p = subparsers.add_parser("ingest", help="Ingest and parse a paper")
    ingest_p.add_argument("source", help="Paper path, arXiv ID, or text file")

    # Command: multipass
    mp_p = subparsers.add_parser("multipass", help="Run 3-pass reading analysis")
    mp_p.add_argument("source", help="Paper path, arXiv ID, or text file")

    # Command: vault
    vault_p = subparsers.add_parser("vault", help="Generate Obsidian knowledge vault")
    vault_p.add_argument("source", help="Paper path, arXiv ID, or text file")
    vault_p.add_argument("--vault-name", default=None, help="Name of vault folder")

    # Command: media
    media_p = subparsers.add_parser("media", help="Generate Gemini Notebook audio overview and video slides")
    media_p.add_argument("source", help="Paper path, arXiv ID, or text file")

    # Command: report
    report_p = subparsers.add_parser("report", help="Generate detailed technical explainer report")
    report_p.add_argument("source", help="Paper path, arXiv ID, or text file")

    # Command: chat
    chat_p = subparsers.add_parser("chat", help="Launch interactive AI Chatbot tutor")
    chat_p.add_argument("source", help="Paper path, arXiv ID, or text file")

    # Command: notebooklm-auth
    nlm_auth_p = subparsers.add_parser("notebooklm-auth", help="Check or perform NotebookLM authentication")
    nlm_auth_p.add_argument("--login", action="store_true", help="Launch browser to log in to NotebookLM")

    # Command: notebooklm-sync
    nlm_sync_p = subparsers.add_parser("notebooklm-sync", help="Sync paper to live Google NotebookLM via notebooklm-py")
    nlm_sync_p.add_argument("source", help="Paper path, arXiv ID, or text file")
    nlm_sync_p.add_argument("--output-dir", default=str(config.output_dir), help="Output directory")

    # Command: notebooklm-video
    nlm_vid_p = subparsers.add_parser("notebooklm-video", help="Generate live NotebookLM video explainer")
    nlm_vid_p.add_argument("source", help="Paper path, arXiv ID, or text file")
    nlm_vid_p.add_argument("--format", choices=["video", "cinematic-video"], default="video", help="Video format")

    # Command: notebooklm-doc
    nlm_doc_p = subparsers.add_parser("notebooklm-doc", help="Generate live NotebookLM study documents (report, quiz, mind-map, slides)")
    nlm_doc_p.add_argument("source", help="Paper path, arXiv ID, or text file")
    nlm_doc_p.add_argument("--doc-type", choices=["report", "quiz", "flashcards", "mind-map", "slide-deck"], default="report", help="Document type")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Fast-path for NotebookLM Authentication check / login
    if args.command == "notebooklm-auth":
        bridge = NotebookLMBridge()
        if getattr(args, "login", False):
            import subprocess
            print("[+] Launching NotebookLM browser authentication...")
            subprocess.run(["notebooklm", "login"])
        auth_status = bridge.check_auth()
        if auth_status.get("authenticated"):
            print("[✓] Authenticated with live Google NotebookLM! Ready to generate cloud artifacts.")
        else:
            print("[!] NotebookLM is currently not authenticated.")
            print("    Run 'python -m src.cli notebooklm-auth --login' or 'notebooklm login' to sign in.")
        return

    print(f"\n[+] Loading learner profile for: {config.learner_profile.get('name')} ({config.learner_profile.get('target_role')})")
    
    # 1. Ingestion
    print(f"[+] Ingesting paper from: {args.source}")
    manifest = load_paper(args.source)
    print(f"[✓] Successfully ingested '{manifest.title}' ({manifest.venue_or_status})")
    print(f"    - Extracted {len(manifest.sections)} sections and {len(manifest.figures)} figures.")

    # 2. Multipass Engine
    mp_engine = MultipassEngine(config.learner_profile)
    p1 = mp_engine.execute_pass1(manifest)
    p2 = mp_engine.execute_pass2(manifest)
    p3 = mp_engine.execute_pass3(manifest)

    if args.command == "ingest":
        print("[✓] Ingestion complete.")
        return

    if args.command == "multipass":
        print(f"\n--- Pass 1 Triage ({p1['time_budget_mins']} mins) ---")
        print(f"Category: {p1['five_cs']['category']}")
        print(f"Gate Decision: {p1['gate_decision']}")
        print(f"\n--- Pass 2 Conceptual Grasp ({p2['time_budget_mins']} mins) ---")
        print(f"Flagged Bottlenecks: {len(p2['flagged_bottlenecks'])} areas matching learner profile.")
        print(f"\n--- Pass 3 Deep Deconstruction ({p3['time_budget_mins']} mins) ---")
        print("Ready for virtual re-implementation and verification.")
        return

    # Vault Generation
    if args.command in ["vault", "run-all"]:
        vault_name = getattr(args, "vault_name", None) or f"{manifest.paper_id}-vault"
        vault_path = config.vaults_dir / vault_name
        print(f"[+] Generating 15-note Obsidian vault at: {vault_path}")
        v_gen = ObsidianVaultGenerator(vault_path, config.learner_profile)
        v_gen.generate_vault(manifest, {"p1": p1, "p2": p2, "p3": p3})
        print(f"[✓] Obsidian vault successfully built with 15 hyperlinked notes!")

    # Media & Gemini Notebook Generation
    if args.command in ["media", "run-all"]:
        out_dir = Path(getattr(args, "output_dir", config.output_dir)) / manifest.paper_id
        producer = GeminiNotebookProducer(out_dir, config.learner_profile)
        script_file = producer.generate_audio_overview_script(manifest)
        slides_file = producer.generate_presentation_slides(manifest)
        print(f"[✓] NotebookLM Audio Overview script generated: {script_file}")
        print(f"[✓] Presentation slides generated: {slides_file}")
        
        # Render visual storyboard frames
        vid_prod = VideoProducer(out_dir)
        frames = vid_prod.render_storyboard_frames(manifest.title, manifest.venue_or_status)
        print(f"[✓] Rendered {len(frames)} storyboard video frames in {out_dir / 'video_frames'}")

    # Report Generation
    if args.command in ["report", "run-all"]:
        out_dir = Path(getattr(args, "output_dir", config.output_dir)) / manifest.paper_id
        producer = GeminiNotebookProducer(out_dir, config.learner_profile)
        report_file = producer.generate_explainer_report(manifest, {"p1": p1, "p2": p2, "p3": p3})
        print(f"[✓] Technical Explainer Report generated: {report_file}")

    # Live NotebookLM Cloud Integrations (via teng-lin/notebooklm-py)
    if args.command == "notebooklm-sync":
        out_dir = Path(getattr(args, "output_dir", config.output_dir)) / manifest.paper_id
        bridge = NotebookLMBridge()
        res = bridge.sync_paper_to_notebooklm(manifest, out_dir)
        print(f"\n[✓] NotebookLM sync complete. Results: {json.dumps(res, indent=2)}")

    if args.command == "notebooklm-video":
        out_dir = Path(getattr(args, "output_dir", config.output_dir)) / manifest.paper_id
        bridge = NotebookLMBridge()
        nb_id = bridge.create_notebook(f"Video: {manifest.title[:40]}")
        if nb_id:
            bridge.add_source_and_wait(nb_id, manifest.file_path or str(out_dir / "paper_source.txt"))
            video_fmt = getattr(args, "format", "video")
            vid_out = out_dir / f"{manifest.paper_id}_{video_fmt}.mp4"
            if bridge.generate_and_download_video(nb_id, vid_out, format=video_fmt):
                print(f"[✓] Successfully downloaded NotebookLM video to: {vid_out}")

    if args.command == "notebooklm-doc":
        out_dir = Path(getattr(args, "output_dir", config.output_dir)) / manifest.paper_id
        bridge = NotebookLMBridge()
        doc_type = getattr(args, "doc_type", "report")
        nb_id = bridge.create_notebook(f"Doc: {manifest.title[:40]}")
        if nb_id:
            bridge.add_source_and_wait(nb_id, manifest.file_path or str(out_dir / "paper_source.txt"))
            doc_out = out_dir / f"{manifest.paper_id}_{doc_type}.md"
            if bridge.generate_study_document(nb_id, doc_type, doc_out):
                print(f"[✓] Successfully generated and downloaded NotebookLM {doc_type} to: {doc_out}")

    # Interactive Chatbot
    if args.command == "chat":
        tutor = PaperTutorChatbot(manifest, config.learner_profile)
        tutor.interactive_cli()

    if args.command == "run-all":
        print(f"\n=======================================================")
        print(f" ALL ASSETS SUCCESSFULLY GENERATED FOR: {manifest.title}")
        print(f" 1. Obsidian Vault:      {config.vaults_dir / (manifest.paper_id + '-vault')}")
        print(f" 2. Explainer Report:    {config.output_dir / manifest.paper_id / 'EXPLAINER_REPORT.md'}")
        print(f" 3. Audio Overview:      {config.output_dir / manifest.paper_id / 'AUDIO_OVERVIEW_SCRIPT.md'}")
        print(f" 4. Interactive Slides:  {config.output_dir / manifest.paper_id / 'slides.html'}")
        print(f" 5. Video Frames:        {config.output_dir / manifest.paper_id / 'video_frames'}")
        print(f"=======================================================\n")
        print("To launch the interactive AI Chatbot tutor, run:")
        print(f"  python -m src.cli chat \"{args.source}\"")

if __name__ == "__main__":
    main()

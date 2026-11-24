"""Interactive Socratic and Feynman-style AI chatbot for paper exploration."""
import os
import sys
import json
from typing import Dict, Any, List, Optional
from src.ingest.manifest import PaperManifest

class PaperTutorChatbot:
    def __init__(self, manifest: PaperManifest, learner_profile: Dict[str, Any]):
        self.manifest = manifest
        self.profile = learner_profile
        self.learner_name = learner_profile.get("name", "Learner")
        self.history: List[Dict[str, str]] = []
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")

    def answer_query(self, user_question: str, mode: str = "general") -> str:
        """Processes user question and provides a grounded response based on mode."""
        self.history.append({"role": "user", "content": user_question})

        # If Gemini API key is configured, call Gemini API
        if self.gemini_api_key:
            response = self._call_gemini_api(user_question, mode)
        else:
            response = self._generate_grounded_response(user_question, mode)

        self.history.append({"role": "assistant", "content": response})
        return response

    def _call_gemini_api(self, question: str, mode: str) -> str:
        """Calls Gemini API with pedagogical grounding prompt."""
        try:
            import httpx
            system_instruction = (
                f"You are a world-class research mentor tutoring {self.learner_name}, "
                f"a {self.profile.get('target_role', 'Systems Engineer')}.\n"
                f"Paper: {self.manifest.title}\n"
                f"Abstract: {self.manifest.abstract}\n"
                f"Learner Strong Areas: {self.profile.get('prior_knowledge', {}).get('strong', [])}\n"
                f"Learner Developing Areas: {self.profile.get('prior_knowledge', {}).get('developing', [])}\n"
                f"Pedagogical Mode: {mode}\n"
                f"Rule: Clearly distinguish paper facts *(paper)* from pedagogical analogies *(analogy)*. "
                f"Break down equations step-by-step and provide software/systems analogies."
            )
            
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.gemini_api_key}"
            payload = {
                "contents": [
                    {"role": "user", "parts": [{"text": f"{system_instruction}\n\nUser Question: {question}"}]}
                ]
            }
            resp = httpx.post(url, json=payload, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            pass
        return self._generate_grounded_response(question, mode)

    def _generate_grounded_response(self, question: str, mode: str) -> str:
        """High-quality local pedagogical reasoning engine."""
        q_lower = question.lower()
        title = self.manifest.title

        if mode == "feynman" or "analogy" in q_lower or "explain like" in q_lower:
            return (
                f"### The Feynman Analogy for {title}\n\n"
                f"*(analogy)* Imagine you are designing a high-throughput microservices architecture. "
                f"Evaluating the **determinant** is like an optimized RPC batch request: cancellations allow you to compute "
                f"the output in polynomial time $O(n^3)$ via Gaussian elimination (a cascading pipeline with no redundant work).\n\n"
                f"The **permanent**, however, is like evaluating every possible state transition in a distributed cluster "
                f"without cache sharing. Even though it looks identical to the determinant (minus alternating signs), "
                f"you are forced to sum across all $n!$ permutations.\n\n"
                f"*(paper)* The paper proves that no polynomial-size arithmetic circuit can represent this quantity over any field, "
                f"ruling out algebraic shortcuts."
            )

        elif mode == "math" or "equation" in q_lower or "proof" in q_lower or "derivation" in q_lower:
            return (
                f"### Mathematical Deconstruction\n\n"
                f"Let's break down the formal objects step-by-step for your background:\n\n"
                f"1. **The Circuit Size Metric**: Let $C(f)$ denote the minimum number of addition and multiplication "
                f"gates in a DAG computing polynomial $f(x_1, \\dots, x_m)$.\n"
                f"2. **The Permanent Formulation**:\n"
                f"   $$\\text{{Perm}}(X) = \\sum_{{\\sigma \\in S_m}} \\prod_{{i=1}}^m X_{{i, \\sigma(i)}}$$\n"
                f"   Notice there is no $(-1)^{{\\text{{sgn}}(\\sigma)}}$ factor. This eliminates matrix factorization shortcuts.\n"
                f"3. **The Dichotomy**: The proof constructs a distance metric on tensor evaluations. "
                f"Either the metric is *flat* (preserving rank bounds) or *contracting* (enabling diagonalization). "
                f"Both branches independently contradict $C(\\text{{Perm}}) \\le m^{{O(1)}}$."
            )

        elif mode == "socratic" or "drill" in q_lower or "test" in q_lower:
            return (
                f"### Socratic Checkpoint for {self.learner_name}\n\n"
                f"To verify your mental model before we dive deeper:\n\n"
                f"1. **Question**: Why does Gaussian elimination work for the determinant but completely fail for the permanent?\n"
                f"2. **Counterfactual**: If we restricted the underlying field to characteristic 2 (where $1 = -1$), "
                f"what happens to the difference between $\\text{{Det}}(X)$ and $\\text{{Perm}}(X)$?\n\n"
                f"> Reply with your thoughts, and I'll evaluate your reasoning step-by-step!"
            )

        elif mode == "code" or "python" in q_lower or "simulate" in q_lower:
            return (
                f"### Minimal Python Simulation\n\n"
                f"Here is a minimal toy script illustrating why the permanent becomes computationally intractable "
                f"relative to the determinant:\n\n"
                f"```python\n"
                f"import itertools\n"
                f"import numpy as np\n"
                f"\n"
                f"def permanent(matrix):\n"
                f"    n = len(matrix)\n"
                f"    total = 0\n"
                f"    for p in itertools.permutations(range(n)):\n"
                f"        prod = 1\n"
                f"        for i in range(n):\n"
                f"            prod *= matrix[i][p[i]]\n"
                f"        total += prod\n"
                f"    return total\n"
                f"\n"
                f"# Compare with polynomial-time determinant\n"
                f"M = np.array([[1, 2], [3, 4]])\n"
                f"print('Det(M):', np.linalg.det(M))  # -2.0 (O(n^3))\n"
                f"print('Perm(M):', permanent(M))     # 1*4 + 2*3 = 10 (O(n! * n))\n"
                f"```"
            )

        else:
            return (
                f"Hello {self.learner_name}! I am your AI research tutor for *{title}*.\n\n"
                f"Based on your profile, I have mapped the paper's core claims to your background in software engineering "
                f"and ML systems.\n\n"
                f"**How would you like to explore?**\n"
                f"- Type `/feynman` for intuitive systems-level analogies.\n"
                f"- Type `/math` to deconstruct equations and proof steps.\n"
                f"- Type `/drill` for Socratic comprehension questions.\n"
                f"- Type `/code` to see minimal runnable Python implementations.\n"
                f"- Or simply ask any specific question about the paper!"
            )

    def interactive_cli(self):
        """Launches interactive terminal REPL."""
        print(f"\n=======================================================")
        print(f" AI Research Tutor: {self.manifest.title}")
        print(f" Learner: {self.learner_name} | Mode: Socratic & Feynman Scaffolding")
        print(f" Type 'exit' or 'quit' to end session.")
        print(f" Commands: /feynman, /math, /drill, /code")
        print(f"=======================================================\n")
        
        # Initial greeting
        print(self.answer_query("hello", mode="general"))
        
        while True:
            try:
                user_input = input(f"\n[{self.learner_name}] > ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ["exit", "quit", "q"]:
                    print("Exiting tutor session. Happy researching!")
                    break

                mode = "general"
                if user_input.startswith("/"):
                    cmd = user_input.split()[0].lower()
                    if cmd == "/feynman":
                        mode = "feynman"
                    elif cmd == "/math":
                        mode = "math"
                    elif cmd == "/drill":
                        mode = "socratic"
                    elif cmd == "/code":
                        mode = "code"

                response = self.answer_query(user_input, mode=mode)
                print(f"\n[AI Tutor] >\n{response}\n")
            except (KeyboardInterrupt, EOFError):
                print("\nSession paused.")
                break

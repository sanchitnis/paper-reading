---
tags: [vp-vnp, reception]
---
# Reception and valid comments

*Snapshot: 24 Nov 2026, evening IST, the day after the release. Reception is evolving. I could not find any published reaction from an algebraic-complexity specialist.* Almost all coverage is secondary press or aggregator sites. I treat only claims that match the paper or the README as solid.

## What every account agrees on (and matches the paper)
- Posted 23 Nov 2026; credited to Claude; found by "an internal research Claude model".
- **No human mathematician has checked it** (README; paper §3).
- Doesn't resolve P vs NP (paper abstract).

## Comments sorted by validity

| Comment | Source | Assessment |
|---|---|---|
| **Statement fidelity gap**: Lean checks proofs, not that `Statement.lean` says what is claimed | README, quoted by [MACCUS](https://maccus.fr/en/vp-vs-vnp-claude/), [VibeMathLab](https://vibemathlab.com/news/anthropic-vp-vnp-claim-2026-11) | **Valid, and the authors say it themselves.** The central open check. |
| **Statements judged only by AI readers** | paper Appendix Q.1 (I verified in the PDF) | **Valid, and self-disclosed** |
| **No outside build / axiom check reported** | VibeMathLab (author says he is *not* a complexity theorist) | **Valid as an observation of status**, not a flaw in the proof |
| **Remark N.6 not in Lean** | MACCUS | **Valid**, and the paper says it too |
| **Bound is weak: quasi-polynomial vs exponential upper bound** | MACCUS; paper §1 | **Valid** and uncontroversial |
| **Doesn't imply P ≠ NP; direction of implication** (a Hacker News user linked a CS Theory StackExchange answer) | [daily.dev summary of HN](https://daily.dev/posts/vp-vnp-over-every-field-rlcjrkxrb) | **Valid.** It matches the paper's §1 and Bürgisser's result. |
| **Anthropic gave no model name, compute or timeline** | MACCUS | **Valid as a gap**; it does not bear on correctness |
| **Lance Fortnow: "can't get myself excited to read the proofs"; theorems "mostly Lean-verified"** | MACCUS (from a blog dialogue posted hours *before* the release) | **Not about this paper.** It addresses AI-proved theorems in general, so don't cite it as a reaction. |
| "Brave or stupid to release before human review" | HN user, via daily.dev | Opinion. Note the README's disclosure is the opposite of hiding it. |
| "It's marketing" | unnamed HN commenters | Unsupported speculation |
| "Lean formalization is groundwork for P vs NP" | unnamed HN commenter | Speculative; paper says the Boolean problem is untouched |
| "Should math grad students quit?" / "humans will hinder math" | HN users | Off-topic for the mathematics |

## What I would add (my reading, not a source)
- The extraordinariness of the jump (n log d → quasi-polynomial) is the best reason for caution. Prior public attempts at this problem have failed. The case *for* this one is that the proof is machine-checked, so the failure mode shifts from "hidden gap in the argument" to "wrong statement".
- A reviewer should also look at the paper's own open flags: no analysis of relativization or algebrization; no value for m₀.

## Where to watch next
Blogs of complexity theorists, ECCC, and outside builds of `Challenge.lean`. Update this note when specialist assessments appear.

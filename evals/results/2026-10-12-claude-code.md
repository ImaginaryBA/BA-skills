# Eval results: Claude Code, 2026-10-12

Each case ran in a fresh copy of `workspace-example/`, executed by an agent that saw only the skill under test and the case prompts (checks removed), then graded by hand against `evals/<skill>/cases.md`. Open WebUI cases were not run.

| Skill | Pass | Fail | Not run | Notes |
|---|---|---|---|---|
| set-up-initiative | 1, 2, 4, 5, 6, 7 | — | 3 | — |
| findings-to-requirements | 1, 2, 4, 5 | — | 3*, 6 | *case 3 had no scripted "Confirmed.", so the append was never observed (eval defect, fixed) |
| check-requirement-quality | 2, 3, 4, 5, 6 | 1 (partly) | — | Case 1: BRs were read for tracing but not checked; the case expected them checked. Case 3 referred to a rewrite by number, which varies per run (eval defect, fixed) |
| prepare-for-publication | 1, 2, 4, 5 | — | 3 | Freeze did not add its footer line (fixed) |
| prepare-elicitation | 1, 2, 4, 5 | — | 3 | Gap warning and stakeholder-row confirmation wording tightened |
| notes-to-findings | 1, 2, 3 | — | 4 | — |
| grill-ba | 1, 2, 3, 4 | — | — | — |
| requirements-to-stories | 1, 2, 3, 4, 5 | — | — | — |
| ask-ba | 1 | 3, 4, 5 | 2 | Asked for the workspace before answering questions that do not need it (fixed) |

Library-wide: when changing a file, some skills replaced the existing footer and others added a line; the rule is now to add a line.

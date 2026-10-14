# Eval results: Claude Code, 2026-10-14

Phase 2 run for `assess-current-state` and the analysis cases of `prepare-for-publication`, same method as 2026-10-12: each case ran in a fresh copy of `workspace-example/`, executed by an agent that saw only the skill under test, the case prompt and the scripted BA replies (checks removed), then graded by hand against `evals/<skill>/cases.md`, with a diff of the workspace before and after. Open WebUI cases were not run.

| Skill | Pass | Fail | Not run | Notes |
|---|---|---|---|---|
| prepare-for-publication | 1, 2, 4, 5, 9; 6, 7, 8 after fix | — | 3 | Case 8 exposed a defect: the skill took an analysis only at Status `draft`, while `shared/analysis.md` has the BA set `validated` by hand. Fixed in v0.2.2 (analysis must be `validated`); 6, 7 and 8 re-run: pass. The re-run also caught a fixture defect (an open question "answered" by an unrelated, unconfirmed finding), fixed |
| assess-current-state | 2, 3, 4, 5, 6, 7; 1 after fix | — | 8 | Case 1 passed its checks but showed three defects, fixed in v0.1.1 and re-run: findings about the future solution became "Need:" rows (now left for `define-future-state`); `TBD` baselines cited `Assumption` (now the evidence that makes them matter); empty SWOT quadrants written inconsistently (now one row). The re-run over-applied the first fix, dropping a fact about today stated inside a future-looking finding; wording refined in v0.1.2, not re-run |

Observations, no change needed:
- Every run flagged that example files are dated after the run date (the example's timeline runs to late October 2026). The example current-state file was re-dated to follow the interview it cites.
- Runs consistently kept interview notes that were never recorded as findings out of the evidence and raised them as open questions instead.
- Case 2 derived figures (share of alert incidents, agent hours) with the calculation shown, as `shared/analysis.md` requires.

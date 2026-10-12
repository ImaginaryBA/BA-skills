# Quality report: Incident logging and prioritisation

| Field | Value |
|---|---|
| Initiative code | IMT |
| Sets checked | incident-logging-and-prioritisation.md v0.1 (read with business-requirements.md v0.1 for the cross-item checks) |
| Checked on | 2026-10-23 |
| Items checked | 5 |
| Must fix | 8 issues on 3 items |
| Consider | 6 |
| Proposed as verified | IMT-FR-001, IMT-FR-002 |

## Results

A = Atomic · Co = Complete · Cs = Consistent · Cn = Concise · F = Feasible · U = Unambiguous · Te = Testable · P = Prioritised · Un = Understandable · S M A R T · St = Structure · Tr = Traceability

| ID | A | Co | Cs | Cn | F | U | Te | P | Un | S | M | A | R | T | St | Tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IMT-SR-001 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-FR-001 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ⚠ |
| IMT-FR-002 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | pending | ⚠ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ⚠ |
| IMT-FR-003 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-NFR-001 | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | pending | ✓ | ✓ | ✗ | ✓ | ✓ | ⚠ | ✓ | ⚠ |

Cross-item checks across both loaded sets: no contradictions or duplicates between items; one business requirement (IMT-BR-002) has nothing tracing to it (issue 14).

## Issues

| # | ID | Check | Severity | Issue | Suggested rewrite | AI use after rewrite |
|---|---|---|---|---|---|---|
| 1 | IMT-SR-001 | Unambiguous | ✗ | "At risk of breaching" is an undefined qualifier: it does not say how close to the breach an incident counts as at risk. | IMT-SR-001 Service Desk Lead needs to see every incident that is within `<warning period>` of breaching its resolution service level. Ask the Service Desk Lead for the warning period (open question 2; the same period as IMT-FR-003). | AI-generated (substance) |
| 2 | IMT-SR-001 | Testable | ✗ | Without a definition of "at risk", nobody can check whether every such incident is shown. | Same rewrite as issue 1; once the warning period is known, set Threshold to "Every incident within `<warning period>` of its resolution service level is visible to the Service Desk Lead." | AI-generated (substance) |
| 3 | IMT-FR-001 | Traceability | ⚠ | The link to IMT-BR-001 (fewer service-level breaches) is not supported: IMT-FN-001 and IMT-FN-002 speak of re-keying time and mistyped configuration items, and IMT-BR-001's sources speak of breach warnings. The business need ties manual re-keying to the legacy tool's missing monitoring integration, which is IMT-BR-002. | Traces to: IMT-BR-002. Or ask the Service Desk Lead whether re-keying delays contribute to resolution breaches; if confirmed as a finding, keep IMT-BR-001 and add it to Source. | AI-generated (substance) |
| 4 | IMT-FR-002 | Understandable | ⚠ | "The priority matrix" is not in the initiative glossary; IMT-FN-004 calls it the department's priority matrix. | IMT-FR-002 The system shall set each incident's priority from its impact and urgency using the department's priority matrix. Consider adding "Priority matrix" to the glossary in `INITIATIVE.md`. | AI-generated (wording only) |
| 5 | IMT-FR-002 | Traceability | ⚠ | The link to IMT-BR-001 is not supported: IMT-FN-003 and IMT-FN-004 speak of inconsistent priorities, not of service-level breaches, and no business requirement covers consistent prioritisation. | Keep the item; ask the Head of IT Operations whether consistent prioritisation contributes to IMT-BR-001 (then record it as a finding and cite it) or is a business outcome of its own (then a new BR is needed). | AI-generated (substance) |
| 6 | IMT-FR-003 | Unambiguous | ✗ | "The responsible team lead" is not defined (the team lead of which team?), and "before" has no lead time, so a warning one second before the breach would satisfy it. | IMT-FR-003 The system shall warn the team lead of `<team responsible for the incident>` at least `<warning period>` before an incident breaches its resolution service level. Ask the Service Desk Lead which team lead is responsible for an incident, and the warning period (open question 2). | AI-generated (substance) |
| 7 | IMT-FR-003 | Testable | ✗ | No lead time is stated and Threshold is `TBD`, so a test cannot tell a useful warning from a useless one. | IMT-FR-003 The system shall warn the responsible team lead at least `<warning period>` before an incident breaches its resolution service level. Threshold: "Every warning is sent at least `<warning period>` before the incident's resolution service level is breached." Ask the Service Desk Lead for the warning period (open question 2). IMT-FN-010 proposes 30 minutes but is not yet confirmed. | AI-generated (substance) |
| 8 | IMT-NFR-001 | Complete | ✗ | Rationale is `TBD`: IMT-FN-008 says search must be fast but not why. | Rationale: why agents need fast search. Ask the Service Desk Lead (open question 3). IMT-FN-011 (reuse a known fix) would answer it but is not yet confirmed. | AI-generated (substance) |
| 9 | IMT-NFR-001 | Unambiguous | ✗ | "The agreed response time" refers to an agreement that does not exist, and is easily confused with the glossary's "Service level" (agreed time to respond to an incident). | IMT-NFR-001 The system shall return incident search results within `<n>` seconds. Ask the Service Desk Lead for the acceptable search time (open question 3). | AI-generated (substance) |
| 10 | IMT-NFR-001 | Testable | ✗ | No number to test against; Threshold is `TBD`. | Threshold: "`<p>`% of incident searches return results in ≤ `<n>` s." Ask the Service Desk Lead for n and the share of searches (open question 3). IMT-FN-012 (over 3 seconds disrupts a call) is not yet confirmed. | AI-generated (substance) |
| 11 | IMT-NFR-001 | Measurable | ✗ | Threshold is `TBD`. | Same as issue 10. | AI-generated (substance) |
| 12 | IMT-NFR-001 | Time-bound | ⚠ | Does not say under which conditions the response time applies (e.g. at peak load, during a call, from go-live). | Add the condition to the Threshold, e.g. "… during the busiest hour of the shift". Ask the Service Desk Lead whether the limit is the same at peak (open question 3). | AI-generated (substance) |
| 13 | IMT-NFR-001 | Traceability | ⚠ | The link to IMT-BR-001 is not supported: IMT-FN-008 says nothing about service-level breaches. | Ask the Service Desk Lead why search speed matters (open question 3) and re-trace to the business requirement the answer supports. | AI-generated (substance) |
| 14 | IMT-BR-002 | Traceability | ⚠ | No item in the checked sets traces to IMT-BR-002. | Re-trace IMT-FR-001 to IMT-BR-002 (issue 3), or leave as is until the feature sets for migration and integration are written. | AI-generated (substance) |

## Proposed as verified

IMT-FR-001, IMT-FR-002 (no must-fix issue; their ⚠ items can be accepted as they are or fixed with issues 3 to 5).

---
Produced with check-requirement-quality v0.1.0 in Claude Code, 2026-10-23.

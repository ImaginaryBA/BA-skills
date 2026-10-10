# Quality report: Incident logging and prioritisation, Business requirements

| Field | Value |
|---|---|
| Initiative code | IMT |
| Sets checked | incident-logging-and-prioritisation.md v0.1, business-requirements.md v0.1 |
| Checked on | 2026-10-14 |
| Items checked | 7 |
| Must fix | 9 issues on 5 items |
| Consider | 3 |
| Proposed as verified | IMT-FR-001, IMT-FR-002 |

## Results

A = Atomic · Co = Complete · Cs = Consistent · Cn = Concise · F = Feasible · U = Unambiguous · Te = Testable · P = Prioritised · Un = Understandable · S M A R T · St = Structure · Tr = Traceability

| ID | A | Co | Cs | Cn | F | U | Te | P | Un | S | M | A | R | T | St | Tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IMT-BR-001 | ✓ | ✓ | ✓ | ✓ | BA | ✓ | ✗ | pending | ✓ | ✓ | ✗ | ⚠ | ✓ | ✗ | ✓ | ✓ |
| IMT-BR-002 | ✓ | ✓ | ✓ | ✓ | BA | ✓ | ✗ | pending | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ⚠ |
| IMT-SR-001 | ✓ | ✓ | ✓ | ✓ | BA | ✗ | ✓ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-FR-001 | ✓ | ✓ | ✓ | ✓ | BA | ✓ | ✓ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-FR-002 | ✓ | ✓ | ✓ | ✓ | BA | ✓ | ✓ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-FR-003 | ✓ | ✓ | ✓ | ✓ | BA | ✗ | ✓ | pending | ✓ | ✓ | n/a | ✓ | ✓ | n/a | ✓ | ✓ |
| IMT-NFR-001 | ✓ | ✗ | ✓ | ✓ | BA | ✓ | ✗ | pending | ✓ | ✓ | ✗ | ✓ | ✓ | ⚠ | ✓ | ⚠ |

## Issues

| # | ID | Check | Severity | Issue | Suggested rewrite | AI use after rewrite |
|---|---|---|---|---|---|---|
| 1 | IMT-BR-001 | Testable, Measurable | ✗ | Threshold is `TBD`: no target breach rate. | Ask the Head of IT Operations for the target rate (open question 1 in business-requirements.md), then set Threshold, e.g. "Below N% of incidents breach their resolution service level". | substance |
| 2 | IMT-BR-001 | Time-bound | ✗ | Says nothing about by when. | Add the period once known, e.g. "… within 6 months of go-live". Ask the Head of IT Operations. | substance |
| 3 | IMT-BR-001 | Achievable | ⚠ | No baseline breach rate is known, so achievability cannot be judged. | Ask the Service Desk Lead for the current breach rate. | — |
| 4 | IMT-BR-002 | Testable, Measurable | ✗ | Threshold is `TBD`: no condition proves the replacement is done. | Set Threshold to a verifiable condition, e.g. "Legacy tool switched off and all incidents handled in the new system", once the Head of IT Operations confirms it. | substance |
| 5 | IMT-BR-002 | Time-bound | ✗ | No retirement date (open question 2 in business-requirements.md). | Add the date once the Head of IT Operations gives it. | substance |
| 6 | IMT-BR-002 | Traceability | ⚠ | Nothing in the checked sets traces to it yet; expected, since migration (TR) items are not drafted. | None; revisit once transition requirements exist. | — |
| 7 | IMT-SR-001 | Unambiguous | ✗ | "At risk of breaching" is undefined. | "Service Desk Lead needs to see every incident within [warning period] of breaching its resolution service level." Warning period from open question 2 in the logging set. | wording only |
| 8 | IMT-FR-003 | Unambiguous | ✗ | "Before" does not say how long before. | "The system shall warn the responsible team lead [warning period] before an incident breaches its resolution service level." Same open question as issue 7. | wording only |
| 9 | IMT-NFR-001 | Complete | ✗ | Rationale is `TBD`. | Ask the Service Desk Lead why search speed matters (open question 3 in the logging set). | substance |
| 10 | IMT-NFR-001 | Testable, Measurable | ✗ | Threshold is `TBD`; "agreed response time" is not a number. | "The system shall return incident search results within [N] seconds", with Threshold "95% of searches within [N] s". Ask the Service Desk Lead. | substance |
| 11 | IMT-NFR-001 | Time-bound | ⚠ | Does not say under which conditions the threshold applies. | Add "at peak load" or the agreed condition. | wording only |
| 12 | IMT-NFR-001 | Traceability | ⚠ | The trace to IMT-BR-001 is not supported by IMT-FN-008, which says nothing about service levels. | Confirm the link with the Service Desk Lead, or trace to IMT-BR-002 instead. | wording only |

## Proposed as verified

IMT-FR-001, IMT-FR-002

---
Produced with check-requirement-quality v0.1.0 in Claude Code, 2026-10-14.

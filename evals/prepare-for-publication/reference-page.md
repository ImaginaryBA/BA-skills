# Reference page: Incident logging and prioritisation

Expected output of case 1, given the setup there. Wording must match the set exactly; layout per `skills/prepare-for-publication/references/page-format.md`.

**Page title:** IMT Incident logging and prioritisation
**Proposed page label:** ai-generated

**Part 1: paste inside the Page Properties macro**

| Field | Value |
|---|---|
| Initiative code | IMT |
| Set name | Incident logging and prioritisation |
| Version | 0.1 |
| Status | Awaiting approval |
| Business analyst | Alex Rivera |
| Validated by | Head of IT Operations, Service Desk Lead |
| Validated on | 2026-10-20 |
| AI use | ai-generated |
| Workspace file | requirements/incident-logging-and-prioritisation.md |

**Part 2: paste below the macro**

## Stakeholder requirements

### IMT-SR-001 Service Desk Lead needs to see every incident at risk of breaching its resolution service level.

| Field | Value |
|---|---|
| Class | SR |
| Rationale | Team leads currently learn of breaches only after they happen (IMT-FN-007). |
| Threshold | TBD |
| Source | IMT-FN-007 |
| Traces to | IMT-BR-001 |
| AI use | AI-generated |

## Functional requirements

### IMT-FR-001 The system shall create an incident from each critical monitoring alert.

| Field | Value |
|---|---|
| Class | FR |
| Rationale | Agents re-key critical alerts by hand, taking about five minutes each and introducing mistyped configuration items (IMT-FN-001, IMT-FN-002). |
| Source | IMT-FN-001, IMT-FN-002 |
| Traces to | IMT-BR-001 |
| AI use | AI-generated |

### IMT-FR-002 The system shall set each incident's priority from its impact and urgency using the priority matrix.

| Field | Value |
|---|---|
| Class | FR |
| Rationale | Priority chosen by judgement gives incidents with the same impact different priorities (IMT-FN-003, IMT-FN-004). |
| Source | IMT-FN-003, IMT-FN-004 |
| Traces to | IMT-BR-001 |
| AI use | AI-generated |

### IMT-FR-003 The system shall warn the responsible team lead before an incident breaches its resolution service level.

| Field | Value |
|---|---|
| Class | FR |
| Rationale | Team leads need time to act before a breach happens (IMT-FN-007). |
| Threshold | TBD |
| Source | IMT-FN-007 |
| Traces to | IMT-SR-001, IMT-BR-001 |
| AI use | AI-generated |

## Non-functional requirements

### IMT-NFR-001 The system shall return incident search results within the agreed response time.

| Field | Value |
|---|---|
| Class | NFR |
| Rationale | TBD |
| Threshold | TBD |
| Source | IMT-FN-008 |
| Traces to | IMT-BR-001 |
| AI use | AI-generated |

## Open questions

| # | Question | Findings involved | Ask |
|---|---|---|---|
| 1 | Should incidents be assigned automatically by category, or triaged manually first? The two findings conflict. | IMT-FN-005, IMT-FN-006 | Head of IT Operations, Service Desk Lead |
| 2 | How long before a breach should the team lead be warned (IMT-FR-003)? | IMT-FN-007 | Service Desk Lead |
| 3 | What search response time is acceptable, and why does search speed matter to agents (IMT-NFR-001)? | IMT-FN-008 | Service Desk Lead |
| 4 | How long must incident records be kept? Not yet confirmed. | IMT-FN-009 | Information Security Officer |

---
Produced with prepare-for-publication v0.1.0 in Claude Code, 2026-10-21.

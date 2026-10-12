# Incident logging and prioritisation: stories

Reference answer for case 1: drafted from the validated logging set. Wording may differ; structure, traces and the handling of TBD values must match.

| Field | Value |
|---|---|
| Set name | Incident logging and prioritisation |
| Initiative code | IMT |
| Version | 0.1 |
| Business analyst | Alex Rivera |
| Requirement set | requirements/incident-logging-and-prioritisation.md v0.1 |

### IMT-ST-001 Create incidents from critical alerts

**Statement:** As a Service desk agent, I want an incident created from each critical monitoring alert, so that agents no longer re-key alerts by hand and mistype configuration items.

| Field | Value |
|---|---|
| Status | draft |
| Derived from | IMT-FR-001 |
| Jira key | TBD |
| AI use | AI-generated |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: Critical alert creates an incident
  Given the monitoring platform raises a critical alert
  When the alert reaches the system
  Then an incident is created from that alert
```

### IMT-ST-002 Set priority from impact and urgency

**Statement:** As a Service Desk Lead, I want each incident's priority set from its impact and urgency using the priority matrix, so that incidents with the same impact get the same priority.

| Field | Value |
|---|---|
| Status | draft |
| Derived from | IMT-FR-002 |
| Jira key | TBD |
| AI use | AI-generated |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: Priority follows the matrix
  Given an incident with a recorded impact and urgency
  When the incident is saved
  Then its priority is the one the priority matrix gives for that impact and urgency
```

### IMT-ST-003 Warn team leads before a breach

**Statement:** As a Service Desk Lead, I want the responsible team lead warned before an incident breaches its resolution service level, so that they can act before the breach happens.

| Field | Value |
|---|---|
| Status | draft |
| Derived from | IMT-FR-003, IMT-SR-001 |
| Jira key | TBD |
| AI use | AI-generated |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: Warning before breach
  Given an open incident with a resolution service level
  When the time left before the breach reaches TBD
  Then the responsible team lead receives a warning
```

### IMT-ST-004 Search past incidents within the agreed response time

**Statement:** As a Service desk agent, I want incident search results returned within the agreed response time, so that TBD.

| Field | Value |
|---|---|
| Status | draft |
| Derived from | IMT-NFR-001 |
| Jira key | TBD |
| AI use | AI-generated |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: Search responds in time
  Given an agent searches past incidents
  When the search runs
  Then results are returned within TBD
```

---
Produced with requirements-to-stories v0.1.0 in Claude Code, 2026-10-24.

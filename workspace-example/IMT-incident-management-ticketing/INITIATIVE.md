# Incident Management Ticketing (IMT)

| Field | Value |
|---|---|
| Initiative code | IMT |
| Business analyst | Alex Rivera |
| Sponsor | Head of IT Operations |
| Data classification | Internal |
| Cleared runtimes | Claude Code, Codex, Open WebUI (local models) |
| Created on | 2026-10-08 |

## Business need

The IT service desk handles incidents in a legacy ticketing tool that is out of vendor support and cannot be integrated with monitoring or the self-service portal. Agents re-key alerts by hand, priorities are set inconsistently, and service-level breaches are only found after the fact. The department needs a supported incident management system that captures, prioritises, routes and resolves incidents within agreed service levels, and that receives the open and historical tickets from the legacy tool.

## Scope

**In scope**
- Incident logging, categorisation, prioritisation, assignment, escalation and closure
- Integration with the monitoring platform and the self-service portal
- Service-level tracking and breach alerts
- Migration of open tickets and three years of closed tickets from the legacy tool

**Out of scope**
- Problem, change and request management processes
- Replacement of the monitoring platform
- Hardware asset inventory

## Glossary

| Term | Definition | Avoid |
|---|---|---|
| Incident | An unplanned interruption or reduction in quality of an IT service. | Ticket, issue, fault |
| Priority | The order in which an incident is worked, derived from impact and urgency. | Severity |
| Service level | The agreed maximum time to respond to and resolve an incident of a given priority. | SLA time, deadline |

## ID register

| Class | Meaning | Last used |
|---|---|---|
| BR | Business requirement | 002 |
| SR | Stakeholder requirement | 001 |
| FR | Functional requirement | 003 |
| NFR | Non-functional requirement | 001 |
| TR | Transition requirement | 000 |
| ST | Delivery story | 000 |
| FN | Elicitation finding | 009 |

---
Produced with set-up-initiative v0.1.0 in Claude Code, 2026-10-08.

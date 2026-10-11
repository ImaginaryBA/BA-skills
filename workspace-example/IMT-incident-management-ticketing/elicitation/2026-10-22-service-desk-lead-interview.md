# Service Desk Lead interview: service levels and search

| Field | Value |
|---|---|
| Source | Interview |
| Date | 2026-10-22 |
| Session | 1 of 1 |
| Duration | 30 minutes |
| Participants | Service Desk Lead |

## Plan

**Goals**
- Settle how far ahead team leads must be warned of a service-level breach.
- Understand how agents search past incidents and what response time they need.
- Resolve the conflict between automatic assignment and manual triage.

**Open questions to resolve**

| Reference | Question |
|---|---|
| incident-logging-and-prioritisation OQ 1 | Should incidents be assigned automatically by category, or triaged manually first? |
| incident-logging-and-prioritisation OQ 2 | How long before a breach should the team lead be warned? |
| incident-logging-and-prioritisation OQ 3 | What search response time is acceptable, and why does search speed matter to agents? |

## Interview guide

### Opening (3 min)
- Thank you for your time. Today we want to understand service-level warnings, incident search, and how incidents reach resolver groups.
- I will take notes and share the findings with you to confirm before we use them.
- AI disclosure: "Notes from this session will be processed with AI skill BA-skills, approved by the company ([CONTEXT.md](https://github.com/ImaginaryBA/BA-skills/blob/main/CONTEXT.md)). Every output is reviewed by the BA before it is used."

### Context (4 min)
1. How does your team find out today that an incident is close to its service-level deadline?
   - Probe: What happens when nobody notices in time?

### Service-level warnings (6 min)
2. When a warning arrives, what does a team lead need to do before the deadline? (resolves OQ 2)
   - Probe: How long does that usually take?
   - Probe: Should the warning time differ by priority?

### Searching past incidents (6 min)
3. Walk me through the last time an agent searched for a past incident. What were they looking for? (resolves OQ 3)
   - Probe: How often does that happen in a shift?
4. How long can a search take before it gets in the agent's way? (resolves OQ 3)
   - Probe: Is that the same during the busiest hour?

### Getting incidents to resolver groups (7 min)
5. How does an incident reach the right resolver group today? (resolves OQ 1)
   - Probe: Which incidents go to the wrong group, and why?
6. Which incidents, if any, could safely skip a check by the service desk? (resolves OQ 1)
   - Probe: What would you need to trust that routing?

### Closing (4 min)
- Recap the main points back to the participant.
- Findings will be shared with you in writing to confirm before they are used.
- Note that open question 1 also needs the Head of IT Operations' view.

## Notes

**Service-level warnings**
- Team leads currently find out about breaches from the weekly report, after the fact.
- When warned, a team lead needs about 20 minutes to reassign or escalate an incident.
- The same 30-minute warning would work for all priorities; there is no need to vary it.

**Searching past incidents**
- Agents search past incidents several times a shift, mostly to reuse a known fix.
- Anything over 3 seconds breaks the agent's flow during a call.

**Getting incidents to resolver groups**
- About a third of incidents are routed to the wrong resolver group today.
- Network and access incidents could skip the service desk check; everything else still needs it.

## Findings

| ID | Finding | Stakeholder role | Confirmed (yes/no) | AI use | Answers |
|---|---|---|---|---|---|
| IMT-FN-010 | Team leads need a warning 30 minutes before an incident breaches its resolution service level, the same for every priority. | Service Desk Lead | no | AI-generated | incident-logging-and-prioritisation OQ 2 |
| IMT-FN-011 | Agents search past incidents several times a shift, mostly to reuse a known fix. | Service Desk Lead | no | AI-generated | incident-logging-and-prioritisation OQ 3 |
| IMT-FN-012 | A search that takes more than 3 seconds disrupts an agent during a call. | Service Desk Lead | no | AI-generated | incident-logging-and-prioritisation OQ 3 |
| IMT-FN-013 | Network and access incidents can be assigned automatically; all other incidents need a service desk check first. | Service Desk Lead | no | AI-generated | incident-logging-and-prioritisation OQ 1 |

---
Produced with prepare-elicitation v0.1.0 in Claude Code, 2026-10-15.
Produced with notes-to-findings v0.1.0 in Claude Code, 2026-10-22.

# Evals: notes-to-findings

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/` in which `elicitation/2026-10-22-service-desk-lead-interview.md` has no `## Notes` or `## Findings` sections and the ID register reads FN `009`. The full example file is a reference answer for case 1.

**Transcript** used by cases 1 and 2:

> Alex Rivera: Thanks for joining, Sam. How do team leads find out about breaches today?
> Sam Patel: Honestly, from the weekly report. By then it's too late. Lovely weather, by the way.
> Alex Rivera: How much warning would a team lead need?
> Sam Patel: They need about twenty minutes to reassign or escalate, so thirty minutes' warning, same for every priority.
> Alex Rivera: And search?
> Sam Patel: Agents search old incidents several times a shift, mostly to reuse a fix. Anything over three seconds and they lose the caller.
> Alex Rivera: Routing?
> Sam Patel: About a third go to the wrong group. Network and access could be assigned automatically; the rest need us to check first.

## 1. Extract

- **Runtime:** Claude Code.
- **Prompt:** "Here are my notes from the Service Desk Lead interview:" plus the transcript.
- **Checks:**
  - [ ] "Sam Patel" and "Alex Rivera" appear nowhere in the file; roles are used instead.
  - [ ] `## Notes` drops the small talk ("lovely weather") and keeps every substantive point.
  - [ ] Findings start at `IMT-FN-010`, each with `Confirmed: no` and `AI use: AI-generated`.
  - [ ] The warning-period finding answers OQ 2, the search findings answer OQ 3, the routing finding answers OQ 1.
  - [ ] The routing finding is listed as contradicting IMT-FN-005 and IMT-FN-006 (or refining them), without resolving it.
  - [ ] One confirmation message for the Service Desk Lead lists only their findings and ends with the AI disclosure.
  - [ ] The updated ID register reads FN `013` (or the last ID used).
  - [ ] The raw transcript is not saved anywhere in the workspace.

## 2. Unknown speaker

- **Runtime:** any. Add a line to the transcript: "Speaker 3: Security will want those incident records kept for audits."
- **Prompt:** as case 1.
- **Checks:**
  - [ ] Asks which register role "Speaker 3" is (or offers to add them) and writes nothing until the BA answers.

## 3. Confirm

- **Runtime:** Claude Code, on the full example (findings IMT-FN-010 to 013 at `no`).
- **Prompt:** "The Service Desk Lead confirmed FN-010, FN-011 and FN-012. For FN-013 they said: 'Only network incidents can be assigned automatically, not access.'"
- **Checks:**
  - [ ] IMT-FN-010, 011 and 012 read `Confirmed: yes`; nothing else in their rows changes.
  - [ ] IMT-FN-013 stays `no`.
  - [ ] A new finding `IMT-FN-014` states the corrected wording, `AI use: AI-assisted`, `Confirmed: yes`, answering OQ 1.
  - [ ] Suggests `findings-to-requirements`.

## 4. Chat runtime

- **Runtime:** Open WebUI, with `INITIATIVE.md`, `stakeholders.md`, the session file and the logging set attached.
- **Prompt:** as case 1.
- **Checks:**
  - [ ] Prints the updated session file and `INITIATIVE.md` as `Save as:` blocks, and the confirmation message as plain text.

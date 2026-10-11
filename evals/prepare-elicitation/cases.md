# Evals: prepare-elicitation

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/` without `elicitation/2026-10-22-service-desk-lead-interview.md` (that file is a reference answer for case 1).

## 1. Interview with open questions

- **Runtime:** Claude Code.
- **Prompt:** "Prepare an interview with Sam Patel on 2026-10-22 about service-level warnings and incident search."
- **Checks:**
  - [ ] Creates one elicitation file whose participant is `Service Desk Lead`; the name "Sam Patel" appears nowhere in it.
  - [ ] Covers logging-set open questions 1, 2 and 3 (their `Ask` includes the Service Desk Lead), each marked with its reference.
  - [ ] Opening contains the AI disclosure word for word.
  - [ ] Time boxes add up to 30 minutes.
  - [ ] Questions are open and neutral; none proposes a solution or names another person.
  - [ ] Suggests pasting notes into `## Notes` and running `notes-to-findings`.

## 2. Too much for one session

- **Runtime:** any.
- **Prompt:** "Prepare an interview with the Head of IT Operations covering service-level targets, legacy tool retirement, priority matrix, assignment rules, reporting needs and data retention."
- **Checks:**
  - [ ] Splits the content into two or more sessions, each its own file, numbered `Session n of N`, each with opening, context and closing summing to 30 minutes.
  - [ ] Business-requirements open questions 1 and 2 come in session 1.

## 3. Questionnaire

- **Runtime:** Open WebUI, with `INITIATIVE.md`, `stakeholders.md` and the logging set attached.
- **Prompt:** "Prepare a questionnaire for all service desk agents about how they search past incidents. Reply by 2026-11-05."
- **Checks:**
  - [ ] Introduction states purpose, duration, deadline and the AI disclosure word for word.
  - [ ] Every question states its type, options and whether it is required; options do not overlap.
  - [ ] 15 questions or fewer.
  - [ ] Delivered as one `Save as:` block.

## 4. Approver left out

- **Runtime:** any, with the elicitation folder emptied.
- **Prompt:** "Prepare an interview with the Monitoring Engineer about alert integration."
- **Checks:**
  - [ ] Warns that the approvers (Head of IT Operations, Service Desk Lead, Information Security Officer) have not been consulted in any session, and lets the BA decide.

## 5. Unknown participant

- **Runtime:** any.
- **Prompt:** "Prepare an interview with the Finance Director."
- **Checks:**
  - [ ] Says the Finance Director is not in the stakeholder register and asks the BA to add them before continuing.

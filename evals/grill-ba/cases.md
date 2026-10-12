# Evals: grill-ba

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/`.

## 1. First round

- **Runtime:** Claude Code.
- **Prompt:** "Grill me on this: we need better incident reporting for management."
- **Checks:**
  - [ ] Asks several numbered questions in one message, across topics that need no earlier answer (e.g. problem, affected, decision makers), then waits.
  - [ ] Suggests no answer to any business question.
  - [ ] Does not ask what `INITIATIVE.md` already answers (e.g. that the legacy tool is out of support).
  - [ ] Writes no file yet.

## 2. Deeper round with unknowns

- **Continue case 1, reply** with answers to some questions, "unknown" to others, mentioning "Jordan Lee wants a monthly breach report".
- **Checks:**
  - [ ] The next round builds on the answers (e.g. asks how the breach report would be measured or who reads it).
  - [ ] Refers to Jordan Lee as Head of IT Operations.
  - [ ] Any "who should we ask" suggestion is marked AI-suggested and names a register role.

## 3. Stop and record

- **Continue case 2, reply:** "Stop."
- **Checks:**
  - [ ] Writes `elicitation/<date>-grilling-<slug>.md` with Source `Grilling` and Participants `Business analyst`.
  - [ ] Every answer is a finding: role `Business analyst`, `Confirmed: no`, `AI use: AI-assisted`, `Answers` `—`, IDs continuing the register.
  - [ ] Every "unknown" is a row in `## Questions for stakeholders` with a register role in `Ask`.
  - [ ] No name appears in the file.
  - [ ] Says the findings need stakeholder confirmation and suggests `prepare-elicitation`.

## 4. Questions flow into elicitation

- **Runtime:** Claude Code, after case 3, with `prepare-elicitation` loaded instead.
- **Prompt:** "Prepare an interview with the Head of IT Operations about reporting."
- **Checks:**
  - [ ] The guide covers every question from the grilling file whose `Ask` is Head of IT Operations.

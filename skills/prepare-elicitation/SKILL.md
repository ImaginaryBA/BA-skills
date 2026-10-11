---
name: prepare-elicitation
description: >-
  Prepare an interview guide (30-minute sessions, split across several
  when needed) or a questionnaire for named stakeholders, covering the
  BA's goals and the open questions those stakeholders can answer, with
  the mandatory AI disclosure. Use before talking to or surveying
  stakeholders.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "4 Elicitation and Collaboration"
    tasks:
      - 4.1 Prepare for Elicitation
    techniques:
      - 10.25 Interviews
      - 10.45 Survey or Questionnaire
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - draft requirement sets
    - previous elicitation files
    - technique, participants, goals
  outputs:
    - one elicitation file per session with plan and guide or questionnaire
  shared:
    - workspace
    - ai-use
    - data-classification
    - findings
    - requirement-set
---

# Prepare elicitation

Builds what the BA takes into an interview or sends out as a questionnaire. The guide works for the BA in the room: short, neutral questions with probes, time boxes that add up to 30 minutes, and the open questions that are waiting on these people.

References (read before step 1): `references/question-craft.md`, `references/ai-use.md`, `references/findings.md`, `references/requirement-set.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Collect the inputs

Read `INITIATIVE.md` and `stakeholders.md` and run the clearance check. In a chat runtime, ask for them, plus any draft requirement sets, and wait.

Needed from the BA: technique (interview or questionnaire) · participants (named from the register) · goals · date, if known. Ask for whatever is missing in one message, then wait.

A participant missing from the register is added as `references/workspace.md` describes.

Done when technique, participants and goals are known and every participant is in the register.

## 2. Gather what to cover

- The BA's goals.
- Every open question in draft requirement sets (including `business-requirements.md`) whose `Ask` names a participant's role and whose `Answered by` reads `—`.
- Every row in a `## Questions for stakeholders` section (from `grill-ba`) whose `Ask` names a participant's role.
- Gaps: list each approver and each high-influence stakeholder in the register who is not a participant and appears in no earlier elicitation file. Show these to the BA as a warning; the BA decides.

Done when every goal and matching open question is listed, and the gaps are shown.

## 3. Build

Follow `references/question-craft.md` and fill `templates/interview.md` or `templates/questionnaire.md`:
- participants as roles, never names;
- the AI disclosure from `references/ai-use.md`, word for word;
- every listed goal and open question covered by at least one question, each open question marked with its reference.

Interviews: when the content does not fit one 30-minute session, split it into several sessions, one file each, numbered `Session 1 of N`.

Done when every goal and open question appears in a guide or questionnaire, every interview's time boxes add up to 30 minutes, and every questionnaire has 15 questions or fewer (or the BA has accepted the warning).

## 4. Deliver

Deliver each file as `elicitation/<YYYY-MM-DD or undated>-<slug>.md` per `references/workspace.md`. Then tell the BA:
- which open questions each session or questionnaire covers;
- the gaps from step 2;
- next step: after the session, paste the notes or transcript into the file's `## Notes` section and run `notes-to-findings`.

Done when the BA has every file and both lists.

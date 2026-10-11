---
name: notes-to-findings
description: >-
  Turn interview or workshop notes and transcripts into cleaned notes and
  numbered findings (names replaced by roles, open questions they answer
  marked), draft a confirmation message for each participant, and later
  record which findings stakeholders confirmed. Use after an elicitation
  session, or when stakeholders reply to a confirmation request.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "4 Elicitation and Collaboration"
    tasks:
      - 4.2 Conduct Elicitation
      - 4.3 Confirm Elicitation Results
    techniques:
      - 10.25 Interviews
      - 10.18 Document Analysis
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - the session's elicitation file
    - draft requirement sets
    - raw notes or transcript, pasted in the chat
    - later, the stakeholders' confirmation replies
  outputs:
    - elicitation file with Notes and Findings
    - updated ID register
    - one confirmation message per participant
  shared:
    - workspace
    - ids
    - ai-use
    - data-classification
    - findings
    - requirement-set
---

# Notes to findings

Two modes. **Extract** turns what was said into findings the stakeholders can confirm. **Confirm** records their answers. Every finding states what a stakeholder meant, attributed to a role; the BA's and the AI's interpretations stay out.

References (read before step 1): `references/findings.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/requirement-set.md`, `references/workspace.md`.

## Extract

### 1. Load

Read `INITIATIVE.md`, `stakeholders.md`, the session's elicitation file (if `prepare-elicitation` made one) and the draft requirement sets; run the clearance check and read the ID register. In a chat runtime, ask for these and wait. Then take the notes or transcript the BA pastes in the chat. With no session file, create one per `references/findings.md`.

Done when the workspace files and the raw notes are in hand.

### 2. Map the speakers

Match every person in the notes to a role in `stakeholders.md`. List each unmatched speaker ("Speaker 3", a name not in the register) and ask the BA which role it is, or add them as `references/workspace.md` describes. Wait.

Done when every speaker has a register role.

### 3. Write notes and findings

- `## Notes`: the cleaned notes, by topic: names replaced by roles, small talk dropped, every substantive point kept. The raw text is never saved.
- `## Findings`: one row per statement, per `references/findings.md`; new IDs from the register; `Confirmed: no`; `AI use: AI-generated`; `Answers` set where a finding answers an open question from the plan or a draft set.
- A finding that contradicts an earlier finding is still recorded; list the pair for the BA.

Done when every substantive point in the notes is covered by a finding and every finding has all six columns.

### 4. Deliver

Deliver the elicitation file and the updated ID register per `references/workspace.md`. Then show:
- one confirmation message per participant from `templates/confirmation-message.md`, listing only that participant's findings;
- the open questions answered, and those the plan aimed at but the session did not answer;
- the contradictions found.

Next step: send the messages, then come back with the replies.

Done when the BA has the file, the messages and the three lists.

## Confirm

When the BA reports the stakeholders' replies:
- set `Confirmed: yes` on exactly the findings the BA says were confirmed;
- leave corrected findings at `no`, and add each corrected statement as a new finding (`AI use: AI-assisted`, since the stakeholder supplied the wording; `Confirmed: yes` if the stakeholder wrote it themselves);
- change nothing else.

Deliver the file and suggest `findings-to-requirements` for the confirmed findings.

Done when every finding the BA reported on has its new value and nothing else changed.

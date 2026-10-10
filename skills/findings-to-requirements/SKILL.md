---
name: findings-to-requirements
description: >-
  Turn elicitation findings — or raw notes, emails and old documents —
  into requirement sets with IDs, classes, rationale, thresholds, sources,
  trace links and AI use labels, plus open questions for conflicts and
  gaps. Use after elicitation, when a BA wants requirements drafted or
  added to a draft set.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: 7 Requirements Analysis and Design Definition
    tasks:
      - 7.1 Specify and Model Requirements
    techniques:
      - 10.1 Acceptance and Evaluation Criteria
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - elicitation files or raw input
    - existing draft requirement sets
  outputs:
    - requirement set files
    - business-requirements.md
    - elicitation file for raw input
    - updated ID register
  shared:
    - workspace
    - ids
    - ai-use
    - data-classification
    - findings
    - requirement-set
---

# Findings to requirements

Drafts requirements that trace, item by item, to confirmed findings. Every statement, rationale and threshold comes from a finding; whatever the findings cannot support becomes an open question.

References (read before step 1): `references/requirement-set.md`, `references/findings.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load the workspace

Read `INITIATIVE.md` and `stakeholders.md`, run the clearance check, and read the ID register (`references/ids.md`, including the scan in an agentic runtime). Read every draft set in `requirements/`; leave published sets aside, they are frozen. In a chat runtime, ask for `INITIATIVE.md`, `stakeholders.md` and any draft sets to extend, then wait.

Done when the initiative file, register and existing draft sets are loaded and the clearance check has passed.

## 2. Gather findings

- **Elicitation files**: take their findings tables as they are.
- **Raw input** (notes, emails, old documents): split it into findings in a new elicitation file (`references/findings.md`), replacing names with roles from `stakeholders.md`. Label each `AI-generated`. Ask the BA which of these the stakeholders have confirmed; mark the rest `no`.

Sort the findings: confirmed ones are candidates; unconfirmed ones, conflicting ones and ones too vague to state become open questions.

Done when every finding is either a candidate or an open question.

## 3. Propose, then wait

Show the BA, in one message:
- the sets to create or extend, with the candidate findings going into each;
- for each set, the business requirements its items will trace to, so the BA confirms every trace link before it is written;
- the business requirements to draft from the business need and the findings, flagged as needing the BA's and sponsor's confirmation;
- the open questions.

Wait for the BA to confirm or change the proposal. Write nothing before that.

Done when the BA has confirmed the grouping.

## 4. Write the items

For each confirmed set, write items per `references/requirement-set.md`:
- statement in its class pattern, one requirement each;
- rationale and threshold only from the findings, otherwise `TBD` plus an open question;
- source = the finding IDs; trace links per the field rules;
- status `draft`, priority `TBD`, AI use `AI-generated`, reviewer fields empty;
- new IDs from the register, in order.

Extending a draft set: append only, raise its version by 0.1. Business requirements go to `requirements/business-requirements.md`, created on first use.

Done when every candidate finding is the source of at least one item or is listed as an open question, and every item has all eleven fields.

## 5. Deliver

Deliver the set files, any new elicitation file, and the updated ID register as `references/workspace.md` describes. Then list:
- the business requirements awaiting the BA's and sponsor's confirmation;
- the open questions, grouped by whom to ask;
- next step: check quality with `check-requirement-quality`.

Done when the BA has every file and both lists.

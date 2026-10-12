---
name: requirements-to-stories
description: >-
  Draft delivery stories with Gherkin acceptance criteria from validated
  requirements, check them against INVEST, give Jira Data Center
  copy-and-paste blocks, and later record each story's Jira key. Use when
  requirements are validated and the delivery team needs Jira stories.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "7 Requirements Analysis and Design Definition"
    tasks:
      - 7.1 Specify and Model Requirements
    techniques:
      - 10.48 User Stories
      - 10.1 Acceptance and Evaluation Criteria
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - one requirement set (validated, or a frozen copy)
    - business-requirements.md
    - existing story set
    - later, the Jira keys
  outputs:
    - story set file
    - Jira Data Center blocks
    - updated ID register
  shared:
    - workspace
    - ids
    - ai-use
    - data-classification
    - requirement-set
---

# Requirements to stories

Turns validated requirements into stories a delivery team can build and test. Every story traces to requirements, every criterion to what the requirements say. Two modes: **Draft** and **Record keys**.

References (read before step 1): `references/story-format.md`, `references/requirement-set.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## Draft

### 1. Load

Read `INITIATIVE.md`, `stakeholders.md`, the requirement set the BA names, `business-requirements.md` and any existing story set for it; run the clearance check and read the ID register. In a chat runtime, ask for these and wait.

- Items not yet `validated` (or later) are left out; list them.
- If the set's status is `published`, it is a frozen copy: ask the BA to confirm nothing changed in Confluence since publication, and wait for the answer.

Done when the eligible items are known and, for a frozen copy, the BA has confirmed.

### 2. Propose, then wait

Show the BA the planned stories: short title, role, `Derived from`, and where each NFR lands (as criteria on which stories, or its own story). Wait for the BA to confirm or change it. Write nothing before that.

Done when the BA has confirmed the plan.

### 3. Write

Fill `templates/story-set.md` per `references/story-format.md`: new ST IDs from the register, `Status: draft`, `AI use: AI-generated`, reviewer fields empty, at least one Gherkin scenario each. Extending an existing story set: append only, raise its version by 0.1. Then check every story against INVEST.

Done when every confirmed story is written with all fields and criteria, and every INVEST failure is listed.

### 4. Deliver

Deliver the story set and updated ID register per `references/workspace.md`. Then show:
- one Jira Data Center block per story (`references/story-format.md`);
- INVEST failures with suggested fixes, and every `TBD` carried into criteria;
- the items left out and why.

Ask the BA to review the stories; when the BA confirms a story is reviewed, set `Status: ready`, `Reviewer` (the BA) and `Reviewed on` (today). Next step: create the ready stories in Jira, then report their keys.

Done when the BA has the file, the blocks and the lists.

## Record keys

When the BA reports Jira keys (e.g. "IMT-ST-003 is SD-431"): fill `Jira key` and set `Status: created` for exactly those stories, and change nothing else. Deliver the file.

Done when every reported key is recorded.

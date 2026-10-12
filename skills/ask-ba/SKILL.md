---
name: ask-ba
description: >-
  Start here. Tell the BA where their initiative stands and which BA-skills
  skill fits their situation next, with the files to bring; or say plainly
  when no skill covers it. Also answers what BA-skills covers against BABOK.
  Use when a BA is unsure which skill to use, wants a status of their
  workspace, or asks about coverage.
metadata:
  version: 0.1.1
  babok:
    knowledge_area: "3 Business Analysis Planning and Monitoring"
    tasks: []
    techniques: []
  inputs:
    - the BA's description of their situation
    - the workspace, when the runtime can read it
  outputs:
    - status summary
    - the next skill and the files it needs
  shared:
    - workspace
    - data-classification
---

# Ask BA

The front door to BA-skills. It routes; it never does another skill's work. It recommends exactly what `references/routes.md` and `references/coverage.md` support.

References (read before step 1): `references/routes.md`, `references/coverage.md`, `references/workspace.md`, `references/data-classification.md`.

## 1. Find the workspace

Skip steps 1 and 2 when the answer does not depend on an initiative's state: what BA-skills covers, a situation no skill handles, or what to do with a published set. Go to step 3.

- **Agentic runtime**: search the working folder for `INITIATIVE.md` files. Show the BA what was found (one initiative, several, or none) and ask which one to use; wait. Then run the clearance check.
- **Chat runtime**: work from the BA's description and whatever files are attached.

Done when the BA has confirmed the workspace, or there is none.

## 2. Say where they are

Agentic runtime, or when the files are attached, summarise in a few lines:
- requirement sets by status (draft, verified, validated, published), with item counts;
- findings awaiting confirmation;
- unanswered open questions and planned grilling questions, grouped by the role to ask;
- elicitation sessions planned but without notes;
- stories by status.

Done when the summary reflects every file read, or the step is skipped because no files are available.

## 3. Route

Match the situation (the BA's words plus the summary) to `references/routes.md`. Give:
- the skill to use next, and why, in one line;
- **agentic runtime**: the files that skill will use, found in the workspace, for the BA to confirm;
- **chat runtime**: the files to attach, from the routes table.

When no row fits, say that BA-skills has no skill for it yet, name the nearest skill if one helps, and point to `references/coverage.md`. Never improvise a missing skill.

Done when the BA has one next step, or a plain statement that none exists.

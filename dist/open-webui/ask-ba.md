---
name: ask-ba
description: "Start here. Tell the BA where their initiative stands and which BA-skills skill fits their situation next, with the files to bring; or say plainly when no skill covers it. Also answers what BA-skills covers against BABOK. Use when a BA is unsure which skill to use, wants a status of their workspace, or asks about coverage."
---

<!-- Generated from skills/ask-ba/ (v0.1.3) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

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


---

# Included file: references/coverage.md

````markdown
# BABOK coverage

Which BA-skills skill supports each BABOK v3 task. Tasks marked "not yet" have no skill.

## 3 Business Analysis Planning and Monitoring

| Task | Skills |
|---|---|
| 3.1 Plan Business Analysis Approach | not yet |
| 3.2 Plan Stakeholder Engagement | not yet |
| 3.3 Plan Business Analysis Governance | not yet |
| 3.4 Plan Business Analysis Information Management | `set-up-initiative` |
| 3.5 Identify Business Analysis Performance Improvements | not yet |

## 4 Elicitation and Collaboration

| Task | Skills |
|---|---|
| 4.1 Prepare for Elicitation | `prepare-elicitation` |
| 4.2 Conduct Elicitation | `grill-ba`, `notes-to-findings` |
| 4.3 Confirm Elicitation Results | `notes-to-findings` |
| 4.4 Communicate Business Analysis Information | not yet |
| 4.5 Manage Stakeholder Collaboration | not yet |

## 5 Requirements Life Cycle Management

| Task | Skills |
|---|---|
| 5.1 Trace Requirements | not yet |
| 5.2 Maintain Requirements | not yet |
| 5.3 Prioritize Requirements | not yet |
| 5.4 Assess Requirements Changes | not yet |
| 5.5 Approve Requirements | `prepare-for-publication` |

## 6 Strategy Analysis

| Task | Skills |
|---|---|
| 6.1 Analyze Current State | `assess-current-state` |
| 6.2 Define Future State | not yet |
| 6.3 Assess Risks | not yet |
| 6.4 Define Change Strategy | not yet |

## 7 Requirements Analysis and Design Definition

| Task | Skills |
|---|---|
| 7.1 Specify and Model Requirements | `findings-to-requirements`, `requirements-to-stories` |
| 7.2 Verify Requirements | `check-requirement-quality` |
| 7.3 Validate Requirements | not yet |
| 7.4 Define Requirements Architecture | not yet |
| 7.5 Define Design Options | not yet |
| 7.6 Analyze Potential Value and Recommend Solution | not yet |

## 8 Solution Evaluation

| Task | Skills |
|---|---|
| 8.1 Measure Solution Performance | not yet |
| 8.2 Analyze Performance Measures | not yet |
| 8.3 Assess Solution Limitations | not yet |
| 8.4 Assess Enterprise Limitations | not yet |
| 8.5 Recommend Actions to Increase Solution Value | not yet |
````

---

# Included file: references/data-classification.md

````markdown
# Data classification

## Levels

`Public`, `Internal`, `Confidential`, `Restricted`. Each workspace declares one level in `INITIATIVE.md`, plus the list of runtimes the company clears for that level.

## Clearance check

Before reading any workspace content, confirm the current runtime appears in the initiative file's cleared runtimes. If it does not, or the runtime is unknown and the BA cannot confirm it, stop and say why. Never process customer or production data, whatever the classification.

## Names

- In elicitation notes and findings, replace personal names with roles (e.g. "Service Desk Lead"); keep the role as written in the stakeholder register.
- The stakeholder register, `Reviewer` and `Approver` fields keep real names: accountability needs them.
- Confluence content is processed only by local models. Outside a local-model runtime, never take a Confluence page as input.
````

---

# Included file: references/routes.md

````markdown
# Routes

Authored here, not generated from `shared/`. Match the BA's situation to one row; when two rows fit, name both in the order given.

| The BA's situation | Skill | Files to attach in a chat runtime |
|---|---|---|
| Starting new work; no `INITIATIVE.md` exists | `set-up-initiative` | none |
| The need is vague, or open questions keep piling up | `grill-ba` | `INITIATIVE.md`, `stakeholders.md`, elicitation files |
| Needs a picture of how things work today and why it falls short (current state, SWOT, PESTLE, baselines) | `assess-current-state` | `INITIATIVE.md`, `stakeholders.md`, elicitation files, supplied documents, any current-state file |
| About to interview or survey stakeholders | `prepare-elicitation` | `INITIATIVE.md`, `stakeholders.md`, draft requirement sets, elicitation files |
| Has notes or a transcript from a session; or stakeholders replied to a confirmation request | `notes-to-findings` | `INITIATIVE.md`, `stakeholders.md`, the session's elicitation file, draft requirement sets |
| Has confirmed findings, or raw notes, emails or documents, and wants requirements | `findings-to-requirements` | `INITIATIVE.md`, `stakeholders.md`, elicitation files, draft requirement sets |
| Has draft requirements to review or verify | `check-requirement-quality` | `INITIATIVE.md`, the draft sets, `business-requirements.md`, the elicitation files they cite |
| Has a validated set or analysis (e.g. a business case) to send for approval; or the page is live and the file must be frozen | `prepare-for-publication` | `INITIATIVE.md`, the set or analysis |
| Has validated or published requirements and needs Jira stories; or has Jira keys to record | `requirements-to-stories` | `INITIATIVE.md`, `stakeholders.md`, the set, `business-requirements.md`, the story set |
| Wants to know what BA-skills covers | this skill, `references/coverage.md` | none |

## No skill, by design

- **Marking a set validated**: the BA does it by hand after stakeholders confirm it (fill `Validated by`, `Validated on`, set each item's Status).
- **Changing a published set**: only in Confluence, by hand; no skill touches it.
- **Adding a stakeholder or glossary term outside a skill run**: by hand, or ask the skill that needs it.
````

---

# Included file: references/workspace.md

````markdown
# Workspace

A workspace is one folder per initiative on the synced company drive. Skills read and write only inside it.

## Layout

```
<CODE>-<initiative-slug>/
  INITIATIVE.md      # initiative file: need, scope, glossary, classification, clearance, code, ID register
  stakeholders.md    # stakeholder register
  elicitation/       # one file per elicitation session
  requirements/      # one file per requirement set
  stories/           # one file per story set
  analysis/          # one file per analysis: current state, gaps, risks, options, business case, models
  decisions/         # initiative decisions
  reviews/           # quality reports, one per check run
```

Folder name: initiative code, a hyphen, then the initiative name in lowercase with hyphens (e.g. `IMT-incident-management-ticketing`).

## Delivering files

- **Agentic runtime** (can write files): write each file to its path, then show the folder tree of what was created or changed.
- **Chat runtime** (cannot write files): print the folder tree first, then each file as its own block, headed by a line `Save as: <path relative to the workspace>` followed by the full file content. The BA saves each block. Always print complete files, never fragments or diffs.

## Adding a stakeholder

When a skill needs a stakeholder who is not in `stakeholders.md`, it asks the BA for that person's register columns, shows the row it would add (unknown columns read `TBD`), and appends it only after the BA explicitly confirms that row. It never changes existing rows. The BA may also add the row by hand.

## Reading the workspace

Before working, a skill needs `INITIATIVE.md`. In an agentic runtime, read it from the workspace. In a chat runtime, if the BA has not attached it, ask for it and stop.
````

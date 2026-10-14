---
name: assess-current-state
description: >-
  Describe how things work today and why it falls short — needs and
  problems with their causes, processes, people, technology, policies
  and baseline measures, plus SWOT, PESTLE or five forces where the
  evidence supports them — every statement citing findings or supplied
  documents, and every gap an open question. Use when a BA needs a
  current-state picture of an initiative, at any stage of elicitation.
metadata:
  version: 0.1.1
  babok:
    knowledge_area: "6 Strategy Analysis"
    tasks:
      - 6.1 Analyze Current State
    techniques:
      - 10.40 Root Cause Analysis
      - 10.46 SWOT Analysis
      - 10.28 Metrics and Key Performance Indicators
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - elicitation files
    - supplied documents
    - existing current-state analysis
  outputs:
    - analysis/current-state.md (or current-state-<slug>.md)
  shared:
    - workspace
    - ai-use
    - data-classification
    - analysis
---

# Assess the current state

Draws the picture of today that the future state, the gaps and the business case are measured against. The skill brings the structure; every fact comes from evidence. What the evidence does not say becomes an open question, never a plausible guess.

References (read before step 1): `references/analysis.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md` and `stakeholders.md` and run the clearance check. Read every elicitation file and any existing `analysis/current-state*.md`. In a chat runtime, ask for `INITIATIVE.md`, `stakeholders.md`, the elicitation files and any current-state file, then wait.

Ask the BA, in one message:
- which documents to supply (process manuals, performance reports, vendor notices and the like);
- which capabilities from the business architecture team's capability map are in scope, and the map's title and date. Never read the map itself.

Check each supplied document per `references/analysis.md`: a document with customer or production data is set aside, with the reason; the rest are used.

Done when the workspace files and the documents the BA supplies are loaded, or the BA says there are none.

## 2. Choose the file and frameworks

- **File**: a `published` current-state file is frozen; never touch it. If a draft `current-state.md` exists, extend it, unless the BA asks for a separately scoped `current-state-<slug>.md`. Otherwise create `current-state.md`.
- **Frameworks**, offered to the BA by these rules:
  - **SWOT**: always offered.
  - **PESTLE**: offered when at least one supplied document covers external factors (regulation, market, vendors, economy). Otherwise say it is available and list the questions that would feed it.
  - **Five forces**: offered only when the business need mentions customers, competitors or a market, or the BA asks.

Show the BA the file you will write, the frameworks offered, the documents used and any set aside. Wait for the BA to confirm. Write nothing before that.

Done when the BA has confirmed the file and the frameworks.

## 3. Draft

Fill `templates/current-state.md`. For every row:
- cite evidence per `references/analysis.md`: finding IDs, with `(unconfirmed)` where the finding is unconfirmed; a supplied document by title and date; or `Business need (unconfirmed)`;
- label it `AI-generated`, except capabilities, which the BA supplied and you only recorded: `AI-assisted`; leave `Reviewer` empty;
- names become roles.

Section rules:
- **Needs and problems**: what goes wrong today and the business need behind it. Cause only as the evidence states it, otherwise `TBD` plus an open question. Findings that say what the solution should do (e.g. "incidents should be assigned automatically", "warn 30 minutes before a breach") describe the future, not today: leave them out of this file and list them at delivery for `define-future-state`. A conflict between such findings is not a current-state question either.
- **Processes**: at most one "today" Mermaid flow of up to about eight steps, followed by its element table; suggest `model-process` for anything more detailed. Capabilities appear only as the BA named them, with the capability map as evidence; a capability the BA needs but the map lacks is an open question for the business architecture team, never a new capability; if the team has no row in `stakeholders.md`, follow the workspace rule for adding a stakeholder.
- **Baseline measures**: values only as the evidence gives them. Two sources that disagree get a row each and an open question asking which the business case should use. A measure without a figure reads Value `TBD`, cites the evidence that makes it matter (not `Assumption`), and gets an open question. Unknown periods read `TBD`.
- **SWOT**: strengths and weaknesses restate core rows with the same evidence. Opportunities and threats, and every PESTLE and five-forces entry, need evidence about external factors; without it the section reads `No evidence yet.` and its suggested questions go into open questions. In the SWOT table, an empty quadrant is one row with Entry `No evidence yet.` and Evidence `—`.
- A core section with nothing to say reads `No evidence yet.` plus an open question with the role to ask.
- A statement the BA wants in but nothing supports is written with Evidence `Assumption` plus an open question.

Extending a draft file: append rows at the end of their sections and open questions at the end of the table, raise the version by 0.1, and change nothing already there.

Done when every section is filled or reads `No evidence yet.`, every row has evidence and an AI use label, and every `TBD`, `Assumption` and conflict has an open question.

## 4. Deliver

Deliver the file as `references/workspace.md` describes. Then list:
- documents set aside, and why;
- findings left for `define-future-state` because they describe the future;
- the open questions, grouped by whom to ask;
- how many rows rest on unconfirmed evidence or assumptions.

Next steps: put the open questions to stakeholders with `prepare-elicitation`; if the need itself is still vague, `grill-ba` first; once the picture holds, `define-future-state`. Before publication, the BA marks the file validated by hand.

Done when the BA has the file and the four lists.

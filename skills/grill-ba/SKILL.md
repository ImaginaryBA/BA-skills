---
name: grill-ba
description: >-
  Question the BA relentlessly, in rounds, about a vague business need
  until its problem, cause, people affected, outcome, measures, scope
  edges, constraints, risks and decision makers are clear or known to be
  unknown. Records the BA's answers as unconfirmed findings and the
  unknowns as questions for stakeholders. Use when a need is fuzzy,
  before planning elicitation.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "4 Elicitation and Collaboration"
    tasks:
      - 4.2 Conduct Elicitation
    techniques:
      - 10.25 Interviews
      - 10.40 Root Cause Analysis
  inputs:
    - INITIATIVE.md
    - stakeholders.md
    - existing elicitation files
    - the need to sharpen
  outputs:
    - elicitation file with notes, findings and questions for stakeholders
    - updated ID register
  shared:
    - workspace
    - ids
    - ai-use
    - data-classification
    - findings
---

# Grill the BA

Interviews the BA, not a stakeholder. The aim is to surface what the BA assumes, what nobody knows yet, and whom to ask. Every answer is the BA's understanding; only a stakeholder can confirm it.

References (read before step 1): `references/findings.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md`, `stakeholders.md` and existing elicitation files; run the clearance check and read the ID register. In a chat runtime, ask for them and wait. Ask the BA which need to sharpen, if not given.

Done when the need is named and the workspace files are loaded.

## 2. Grill in rounds

Work through these topics, deepening each answer: **problem** (what happens today, how often) · **cause** (why it happens) · **affected** (who, how badly) · **outcome** (what changes when solved) · **measure** (how success shows, in numbers) · **scope edges** (what is in, what is out) · **constraints** (time, money, rules, systems) · **risks and assumptions** · **decision makers** (who decides, who approves).

Each round, ask every question you can ask now, numbered, then wait. A question whose answer depends on another unanswered question waits for a later round. Skip what `INITIATIVE.md` or confirmed findings already answer.

- Ask about the business; never suggest an answer to it.
- For process questions only ("who should we ask about this?"), you may suggest an answer from the register, marked **AI-suggested**.
- The BA may answer, say **unknown**, or say **stop**. Each unknown becomes a question for stakeholders, with the register role to ask.
- Names the BA mentions become roles.

Done when every topic is answered or marked unknown with a role to ask, or the BA says stop.

## 3. Record

Write a new elicitation file, `elicitation/<YYYY-MM-DD>-grilling-<slug>.md`, per `references/findings.md`:
- header: Source `Grilling`, Participants `Business analyst`;
- `## Notes`: the BA's answers, by topic;
- `## Findings`: one row per answer statement, Stakeholder role `Business analyst`, `Confirmed: no`, `AI use: AI-assisted` (the BA supplied the substance), `Answers` `—`;
- `## Questions for stakeholders`: every unknown, with the role to ask and its topic.

Deliver the file and the updated ID register per `references/workspace.md`. Tell the BA that these findings become requirements only after a stakeholder confirms them, and suggest `prepare-elicitation` to put the questions to the right people.

Done when the file holds every answer and every unknown, and the BA has it.

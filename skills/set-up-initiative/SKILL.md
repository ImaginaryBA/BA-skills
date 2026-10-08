---
name: set-up-initiative
description: Start the workspace for a new initiative — creates INITIATIVE.md (business need, scope, glossary, data classification, cleared runtimes, initiative code, ID register), the stakeholder register and the empty folders. Use when a BA begins a new piece of analysis work, or when another skill finds no INITIATIVE.md.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "3 Business Analysis Planning and Monitoring"
    tasks: ["3.4 Plan Business Analysis Information Management"]
    techniques: []
  inputs: [initiative name, initiative code, business need, scope in, scope out, data classification, cleared runtimes, BA name, optional sponsor, optional stakeholders, optional known terms]
  outputs: [INITIATIVE.md, stakeholders.md, elicitation/, requirements/, stories/, decisions/]
  shared: [workspace, ids, ai-use, data-classification]
---

# Set up an initiative

Creates a new workspace exactly as the BA describes it. The BA's facts are the only source: every field holds what the BA said or is marked `TBD`.

References (read before step 1): `references/workspace.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`.

## 1. Collect the inputs

Mandatory: initiative name · initiative code · business need (2–5 sentences) · scope in · scope out · data classification · runtimes cleared for that classification · the BA's name.
Optional: sponsor · initial stakeholders (any register columns the BA knows) · known terms with definitions.

Take what the BA has already given. Ask for **all** missing mandatory inputs in a single message, then wait. Optional inputs the BA leaves out become `TBD`.

Checks before going on:
- Code is 2–5 uppercase letters. If it matches a common ticket prefix (`INC`, `REQ`, `CHG`, `PRB`, `TASK`, `RITM`), point out the clash and ask the BA to confirm or choose another.
- Classification is one of the four levels.
- The current runtime is in the BA's cleared list (`references/data-classification.md`). If not, stop and say why.
- In an agentic runtime, no `INITIATIVE.md` already exists in the target folder. If one does, stop: this skill never overwrites a workspace.

Done when every mandatory input has a value the BA supplied and all four checks pass.

## 2. Build the files

Fill `templates/INITIATIVE.md` and `templates/stakeholders.md`.

- Keep the BA's wording for business need and scope; correct spelling and grammar only.
- Stakeholder names stay as given (the register keeps real names).
- Glossary: only terms the BA supplied. Leave the table with its header row if there are none.
- ID register: every class at `000`.
- End each file with the footer from `references/ai-use.md`; workspace files carry no other provenance.

Done when no placeholder in angle brackets remains: every field is filled from the BA's input or reads `TBD`.

## 3. Deliver

Deliver the two files and the empty folders `elicitation/`, `requirements/`, `stories/`, `decisions/` as `references/workspace.md` describes for this runtime. In a chat runtime, list the empty folders in the tree for the BA to create.

Then list every `TBD` field and suggest the next step: prepare elicitation with `prepare-elicitation`.

Done when the BA has the complete folder tree and both files, and every `TBD` is listed.

# BA-skills

A library of agent skills that help business analysts carry out BABOK-aligned analysis work, from strategy analysis to solution evaluation, with a human accountable for every output. All skills and outputs are in English, the company's official language.

## Language

### Work and workspace

**Initiative**:
A bounded piece of BA work responding to a business need, from strategy analysis through solution evaluation. The unit every workspace, skill and artifact belongs to.
_Avoid_: Project, change, engagement

**Workspace**:
The synced company-drive folder of markdown files holding one initiative's state (glossary, stakeholders, elicitation results, requirements, decisions).
_Avoid_: Repo, project folder

**Initiative file**:
`INITIATIVE.md`, the workspace's root file: business need, scope, glossary, data classification, runtime clearance, initiative code and ID register.
_Avoid_: Context file, charter

**ID register**:
The section of the initiative file holding the last sequence number used per class; the source of every new ID.

**Data classification**:
The sensitivity level a workspace declares once (Public, Internal, Confidential or Restricted), which decides which runtimes may process its content.

**Requirement set**:
A named group of related requirements (e.g. one feature or capability), kept as one workspace file and published as one Confluence page.
_Avoid_: Requirements document, BRD, spec

**Initiative code**:
A 2–5 uppercase-letter code chosen by the BA at setup, prefixing every ID in the initiative. Avoid codes that collide with ticket prefixes in the business's tools (e.g. `INC`).

**Requirement ID**:
A stable, never-reused identifier of the form initiative code, requirement class, sequence (e.g. `CLM-FR-012`).

**Finding**:
One confirmed statement from elicitation, with an ID (e.g. `IMT-FN-004`) and the stakeholder role it came from. The source every requirement points to.
_Avoid_: Note, input, observation

**Threshold**:
The measurable condition that proves a requirement is met (e.g. "95% of incident searches return in ≤ 2 s"). Mandatory for BR and NFR.
_Avoid_: Fit criterion, acceptance criteria (those belong to stories)

**Rationale**:
One sentence on why a requirement exists, drawn from its source findings; `TBD` plus an open question when the source does not say.

**Open question**:
A conflict between findings, or a gap too vague to state as a requirement, listed with the findings involved and who to ask. Never silently resolved.

**Requirement class**:
The BABOK classification of a requirement: business (BR), stakeholder (SR), functional (FR), non-functional (NFR) or transition (TR).
_Avoid_: Requirement type, category

**Working draft**:
A requirement or artifact still in the workspace's markdown, before publication. Skills may freely create and revise it.

**Publication**:
Moving an approved artifact from the workspace into Confluence, which becomes its system of record from then on.
_Avoid_: Export, sync, upload

**Frozen copy**:
The workspace file of a requirement set after publication, kept for history, reuse and story drafting, and never edited again. Changes to a published set happen only in Confluence, by the BA.

**Publish-ready page**:
A version of a requirement set generated for pasting into Confluence: a page-properties block, item tables and the footer, with no raw metadata.

**Delivery story**:
A Jira story drafted by the BA from one or more validated (or later) requirements, linking back to their requirement IDs. It is a delivery artifact, never the only home of a requirement.

**Story set**:
The workspace file holding the delivery stories for one epic or feature, each with a temporary ID (e.g. `CLM-ST-007`) until its Jira key is recorded.
_Avoid_: Ticket, Jira requirement

### Requirement lifecycle

**Lifecycle status**:
Where a requirement is in its life, in order: draft, verified, validated, published, approved, then retired or superseded. The BA tracks it in the workspace up to published; from then on it lives only in Confluence.

**Verified**:
The requirement passes the quality checks (well-formed, unambiguous, testable and so on). A skill may propose it; the BA confirms.
_Avoid_: Reviewed, checked

**Validated**:
Named stakeholders confirmed the requirement meets their need. Only the BA sets it.

**Published**:
The requirement's set is on Confluence awaiting approval. The workspace copy is frozen from this point.

**Approved**:
A named approver from the stakeholder register signed the requirement off in Confluence on a recorded date. Never set by a skill.
_Avoid_: Signed off, accepted

**Superseded**:
Replaced by another requirement, which is named. The ID stays, never reused.

### Skills and runtimes

**Skill**:
One `SKILL.md` that does one BA job, named and described in terms of the situation a BA is in (e.g. "turn workshop notes into requirements"), not in BABOK terms.

**BABOK reference**:
Metadata on a skill naming the knowledge area, task(s) and technique(s) it supports. Used for coverage reporting and routing, never as the skill's name.

**Router**:
The skill (`ask-ba`) that maps a BA's described situation to the right skill or chain of skills.

**Runtime**:
The AI tool a BA runs skills in, e.g. Claude Code, Codex, Antigravity or Open WebUI.
_Avoid_: Platform, harness

**Agentic runtime**:
A runtime that can read and write workspace files by itself, so skills run with full support (e.g. Claude Code, Codex, Antigravity).

**Chat runtime**:
A runtime without file access, where the BA attaches the skill and its inputs and saves the output (e.g. Open WebUI).

**Shared conventions**:
The master rules every skill follows, kept once under `shared/` and copied into each skill before release.

**Released skill**:
A skill version whose evaluations pass in Claude Code and in at least one other runtime used by pilot BAs.

### Accountability

**AI use label**:
A mandatory per-item statement: AI-generated or AI-assisted. Travels with the item through publication.
_Avoid_: Provenance, origin (clashes with Source)

**AI-generated**:
AI produced the substance (content, structure, wording); a human reviewed it.

**AI-assisted**:
A human produced the substance; AI reviewed, critiqued, reformatted or suggested. An AI-generated item becomes AI-assisted only when the BA confirms they substantively rewrote it.

**Reviewer**:
The named person who checked an item, with the date. Recorded separately from the AI use label; being reviewed is not being approved.

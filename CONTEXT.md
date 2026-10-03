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

**Data classification**:
The sensitivity level a workspace declares once, which decides which runtimes may process its content.

**Working draft**:
A requirement or artifact still in the workspace's markdown, before publication. Skills may freely create and revise it.

**Publication**:
Moving an approved artifact from the workspace into Confluence, which becomes its system of record from then on.
_Avoid_: Export, sync, upload

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

### Accountability

**AI provenance label**:
A mandatory per-item statement: AI-generated or AI-assisted. Travels with the item through publication.

**AI-generated**:
AI produced the substance (content, structure, wording); a human reviewed it.

**AI-assisted**:
A human produced the substance; AI reviewed, critiqued, reformatted or suggested. An AI-generated item becomes AI-assisted only when the BA confirms they substantively rewrote it.

**Reviewer**:
The named person who checked an item, with the date. Recorded separately from the provenance label; being reviewed is not being approved.

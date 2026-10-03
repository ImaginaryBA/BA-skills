# BA-skills

A library of agent skills that help business analysts carry out BABOK-aligned analysis work, from strategy analysis to solution evaluation, with a human accountable for every output.

## Language

### Work and workspace

**Initiative**:
A bounded piece of BA work responding to a business need, from strategy analysis through solution evaluation. The unit every workspace, skill and artifact belongs to.
_Avoid_: Project, change, engagement

**Workspace**:
The folder of markdown files holding one initiative's state (glossary, stakeholders, elicitation results, requirements, decisions), read and written by skills.
_Avoid_: Repo, project folder

**Working draft**:
A requirement or artifact still in the workspace's markdown, before publication. Skills may freely create and revise it.

**Publication**:
The act of moving an approved requirement from the workspace into the enterprise tool, which becomes its system of record from then on.
_Avoid_: Export, sync, upload

### Skills

**Skill**:
One `SKILL.md` that does one BA job, named and described in terms of the situation a BA is in (e.g. "turn workshop notes into requirements"), not in BABOK terms.

**BABOK reference**:
Metadata on a skill naming the knowledge area, task(s) and technique(s) it supports. Used for coverage reporting and routing, never as the skill's name.

**Router**:
The skill (`ask-ba`) that maps a BA's described situation to the right skill or chain of skills.

### Accountability

**AI provenance label**:
A mandatory statement on every output saying whether AI generated or assisted it. Travels with the artifact through publication.

**Stakeholder language**:
The language that stakeholder-facing outputs are written in, set per initiative. Skill instructions themselves stay in English.

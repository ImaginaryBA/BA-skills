# BA-skills: plan

A BABOK-aligned library of portable agent skills for business analysis, in the style of mattpocock-skills: small `SKILL.md` files, a router on top, shared primitives, and markdown files that keep state between sessions.

- Vocabulary: [`CONTEXT.md`](CONTEXT.md). Its terms are used in this plan exactly as defined there.
- Decisions: [`docs/adr/`](docs/adr). Each one is referenced below as (ADR-nnnn).

Status: **design agreed through the grilling session; ready to build Phase 1.**

---

## 1. Goals

| Goal | Measure |
|---|---|
| Less time on routine BA artifacts | Time per artifact compared with a baseline taken in Phase 0 |
| Better artifacts | Defects found in peer review and stakeholder validation |
| Transparent, accountable AI use | 100% of items carry an AI provenance label and a reviewer |
| Traceability and reuse | Share of items with trace links; number of items reused from frozen copies |
| Adoption by the pilot group (2–5 BAs) | Weekly use and feedback, in at least two runtimes |

Non-goals for the first version: direct Confluence or Jira integration, per-runtime adapters, and any AI involvement after publication.

## 2. Constraints that shape everything

- **Portable.** Skills are authored in Claude Code. BAs may run them in Codex, Antigravity, Open WebUI or other LLM tools. So skills must not use git, a shell, hooks or features specific to one vendor. Every rule a skill follows is written into the skill text itself. (ADR-0001)
- **Two support levels.** Agentic runtimes read and write the workspace themselves. In chat runtimes, the BA attaches the skill and its inputs, then saves what it outputs. That's why every skill declares its inputs and outputs explicitly. (ADR-0005)
- **English only**, the company's official language.
- **Data.** Each workspace declares its data classification. Personal names get replaced with roles. Customer and production data are never used. Only local models may process Confluence content. (ADR-0006)
- **Provenance.** Every item is labelled AI-generated or AI-assisted, and the reviewer and date are recorded separately. Only the BA can downgrade a label from generated to assisted. The footer also records skill, version and runtime. (ADR-0004)
- **Named by situation.** Skills are named after what the BA is trying to do, and their BABOK reference sits in metadata. (ADR-0003)

## 3. Information model

**Where things live.** Each initiative has a workspace: a folder on a synced company drive (OneDrive/SharePoint). This GitHub repo holds only the skill library. Initiative content never goes in it.

```
<initiative>/
  CONTEXT.md              # initiative glossary, scope, business need, data classification, initiative code
  stakeholders.md         # register: role, interest/influence, RACI, approver flag
  elicitation/            # one file per session: plan, notes, confirmed findings
  requirements/           # one file per requirement set (ADR-0007)
  stories/                # one file per story set (epic or feature)
  decisions/              # initiative decisions
```

**Inside a requirement set file:** each item has a heading followed by a Field | Value metadata table:
`id` (e.g. `CLM-FR-012`, ADR-0008) · `class` (BR/SR/FR/NFR/TR) · `status` · `priority` · `source` · `traces_to` · `reused_from` · `provenance` · `reviewer` · `reviewed_on`.

**Lifecycle (ADR-0010, ADR-0009):**

```
draft ─► verified ─► validated ─► published ─► approved ─► retired / superseded
 skill    skill        BA only     BA pastes     approver in Confluence
 drafts   proposes,    (names the  to Confluence ───────────────────────────
          BA confirms  stakeholders) workspace copy frozen; from here on:
                                   Confluence only, BA edits by hand, no AI
```

**Publication:** a skill produces a publish-ready page with a Page Properties block, item tables, the visible provenance footer and a *proposed* page label (`ai-generated` if any item is AI-generated). The BA has the final say on the label, then pastes the page into Confluence. (ADR-0002, ADR-0004, ADR-0007)

**Delivery stories:** these can be drafted once their source requirements are `validated`. They live in a story set with temporary IDs (`CLM-ST-007`) and `derived_from` links. The BA creates the stories in Jira and records each Jira key. A story is never the only place a requirement exists.

## 4. Phase 1: the first version to pilot (9 skills)

| # | Skill | Does | BABOK reference |
|---|---|---|---|
| 1 | `ask-ba` | Routes a described situation to the right skill. In chat runtimes it's the "start here" guide: which skill to attach next and which inputs to bring | — |
| 2 | `set-up-initiative` | Creates the workspace, `CONTEXT.md`, data classification, initiative code and stakeholder register | Planning: information management |
| 3 | `grill-stakeholder` | A questioning primitive used by other skills, or directly to sharpen a need | Elicitation: interviews |
| 4 | `prepare-elicitation` | Produces an interview guide or questionnaire from goals and stakeholders | Elicitation: prepare |
| 5 | `notes-to-findings` | Turns notes or a transcript into confirmed findings, conflicts and open questions, with names replaced by roles | Elicitation: conduct, confirm |
| 6 | `findings-to-requirements` | Builds a requirement set with IDs, classes, sources and provenance | Requirements Analysis & Design Definition: specify and model |
| 7 | `check-requirement-quality` | Checks items against the BABOK quality characteristics and proposes `verified` | Requirements Analysis & Design Definition: verify |
| 8 | `requirements-to-stories` | Builds a story set with Gherkin acceptance criteria from validated requirements | Requirements Analysis & Design Definition: user stories |
| 9 | `prepare-for-publication` | Produces the publish-ready Confluence page and the proposed label | Life Cycle Management: communicate |

If the scope has to shrink, cut skill 8 first.

**Definition of a released skill:** its evaluations pass in Claude Code and in at least one other runtime the pilot BAs use, and it carries a version tag.

## 5. Later phases

- **Phase 2, analysis depth:** current state, future state, SWOT, Porter's five forces, PESTLE, gap analysis, business case, risk analysis. Also use cases and scenarios, process models (Mermaid), data models, business rules, design options, and facilitation packs for workshops and brainstorming.
- **Phase 3, before-publication lifecycle and reuse:** trace queries, prioritisation (MoSCoW, WSJF, Kano), impact analysis on *unpublished* sets, and a reuse catalogue built from **frozen copies** on the drive. It is not built from Confluence, because of the data policy.
- **Phase 4, rollout:** planning skills (BA approach, stakeholder analysis, governance), solution evaluation skills, `INSTALL.md` for each runtime, and moving the library to the company's own git host.
- **Future options (deferred):** generated adapters for each runtime (ADR-0005) and direct publication through a connector (ADR-0002).

## 6. How each skill gets built

1. Grill it: triggers, inputs, outputs, what "good" looks like.
2. Write `SKILL.md`: frontmatter with name, situation-first description and BABOK reference. Then steps, the output template with provenance fields, completion criteria and handoffs. Keep it under about 150 lines.
3. Write 3–5 evals: realistic prompts plus checkable properties, such as "every item has an ID, class, source and provenance" or "no vague terms like *fast*".
4. Run it in Claude Code and in one other pilot runtime, on real pilot work.
5. Tighten it, tag a version and release it.

## 7. Phase 0: before building

- [ ] Choose the pilot initiative: one that is in early elicitation now, with at least one pilot BA on a runtime other than Claude.
- [ ] Take baselines for the interview guide, the elicitation summary, the story set, and peer-review defects.
- [ ] Confirm which runtimes are cleared for which data classifications.
- [ ] Check IP ownership before anything company-specific goes into this repo. It stays in this repo until the pilot proves value, then moves to the company git host.

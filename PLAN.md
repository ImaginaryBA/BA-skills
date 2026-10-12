# BA-skills: plan

A BABOK-aligned library of portable agent skills for business analysis, in the style of mattpocock-skills: small `SKILL.md` files, a router on top, shared primitives, and markdown files that keep state between sessions.

- Vocabulary: [`CONTEXT.md`](CONTEXT.md). Its terms are used in this plan exactly as defined there.
- Decisions: [`docs/adr/`](docs/adr). Each one is referenced below as (ADR-nnnn).

Status: **Phase 1 skills drafted (all nine, evals pass in Claude Code); Open WebUI evals and the pilot still to run. Phase 2 structure decided (ADR 0017–0020); next: extend the existing skills, then build `assess-current-state`.**

---

## 1. Goals

| Goal | Measure |
|---|---|
| Less time on routine BA artifacts | Time per artifact compared with a baseline taken in Phase 0 |
| Better artifacts | Defects found in peer review and stakeholder validation |
| Transparent, accountable AI use | 100% of items carry an AI use label and a reviewer |
| Traceability and reuse | Share of items with trace links; number of items reused from frozen copies |
| Adoption by the pilot group (2–5 BAs) | Weekly use and feedback, in at least two runtimes |

Non-goals for the first version: direct Confluence or Jira integration, per-runtime adapters, and any AI involvement after publication.

## 2. Constraints that shape everything

- **Portable.** Skills are authored in Claude Code. BAs may run them in Codex, Antigravity, Open WebUI or other LLM tools. So skills must not use git, a shell, hooks or features specific to one vendor. Every rule a skill follows is written into the skill text itself. (ADR-0001)
- **Two support levels.** Agentic runtimes read and write the workspace themselves. In chat runtimes, the BA attaches the skill and its inputs, then saves what it outputs. That's why every skill declares its inputs and outputs explicitly. (ADR-0005)
- **English only**, the company's official language.
- **Data.** Each workspace declares its data classification. Personal names get replaced with roles. Customer and production data are never used. Only local models may process Confluence content. (ADR-0006)
- **AI use.** Every item is labelled AI-generated or AI-assisted, and the reviewer and date are recorded separately. Only the BA can downgrade a label from generated to assisted. The footer also records skill, version and runtime. (ADR-0004)
- **Named by situation.** Skills are named after what the BA is trying to do, and their BABOK reference sits in metadata. (ADR-0003)

## 3. Information model

**Where things live.** Each initiative has a workspace: a folder on a synced company drive (OneDrive/SharePoint). This GitHub repo holds only the skill library. Initiative content never goes in it.

```
<initiative>/
  INITIATIVE.md           # business need, scope, glossary, data classification, runtime clearance, code, ID register
  stakeholders.md         # register: name, role, unit, interest, influence, approver, engagement, notes
  elicitation/            # one file per session: plan, notes, confirmed findings
  requirements/           # one file per requirement set (ADR-0007)
  stories/                # one story set per requirement set (same slug)
  decisions/              # initiative decisions
  reviews/                # quality reports
  analysis/               # one file per analysis (Phase 2, ADR-0017)
```

**Inside a requirement set file:** each item has a heading followed by a Field | Value metadata table:
the ID and statement as the heading (e.g. `IMT-FR-012 The system shall …`, ADR-0008), then Class · Status · Priority · Rationale · Threshold · Source · Traces to · Reused from · AI use · Reviewer · Reviewed on. Full format: `shared/requirement-set.md`.

**Lifecycle (ADR-0010, ADR-0009):**

```
draft ─► verified ─► validated ─► published ─► approved ─► retired / superseded
 skill    skill        BA only     BA pastes     approver in Confluence
 drafts   proposes,    (names the  to Confluence ───────────────────────────
          BA confirms  stakeholders) workspace copy frozen; from here on:
                                   Confluence only, BA edits by hand, no AI
```

**Publication:** a skill produces a publish-ready page with a Page Properties block, item tables, the footer and a *proposed* page label (`ai-generated` if any item is AI-generated). The BA has the final say on the label, then pastes the page into Confluence. (ADR-0002, ADR-0004, ADR-0007)

**Delivery stories:** these can be drafted once their source requirements are `validated`. They live in a story set with IDs (`IMT-ST-007`) and `Derived from` links (ADR-0011). The BA creates the stories in Jira and records each Jira key. A story is never the only place a requirement exists.

## 4. Phase 1: the first version to pilot (9 skills)

| # | Skill | Does | BABOK reference |
|---|---|---|---|
| 1 | `ask-ba` | Routes a described situation to the right skill. In chat runtimes it's the "start here" guide: which skill to attach next and which inputs to bring | — |
| 2 | `set-up-initiative` | Creates the workspace, `INITIATIVE.md`, data classification, initiative code and stakeholder register | Planning: information management |
| 3 | `grill-ba` | Questions the BA in rounds to sharpen a vague need; records the BA's answers as unconfirmed findings and the unknowns as questions for stakeholders | Elicitation: interviews |
| 4 | `prepare-elicitation` | Produces an interview guide or questionnaire from goals and stakeholders | Elicitation: prepare |
| 5 | `notes-to-findings` | Turns notes or a transcript into confirmed findings, conflicts and open questions, with names replaced by roles | Elicitation: conduct, confirm |
| 6 | `findings-to-requirements` | Builds a requirement set with IDs, classes, sources and AI use labels | Requirements Analysis & Design Definition: specify and model |
| 7 | `check-requirement-quality` | Checks items against the BABOK quality characteristics and proposes `verified` | Requirements Analysis & Design Definition: verify |
| 8 | `requirements-to-stories` | Builds a story set with Gherkin acceptance criteria from validated requirements | Requirements Analysis & Design Definition: user stories |
| 9 | `prepare-for-publication` | Produces the publish-ready Confluence page and the proposed label | Life Cycle Management: communicate |

If the scope has to shrink, cut skill 8 first.

**Definition of a released skill:** its evaluations pass in Claude Code and in at least one other runtime the pilot BAs use, and it carries a version tag.

## 5. Phase 2: analysis depth

Built while Phase 1 is piloted. Structure decided first:

- Each analysis is one file in `analysis/` with a header, sections, open questions and the footer; status is per file: draft, validated, published, approved. (ADR-0017, format in `shared/analysis.md`)
- Gaps, risks, design options, business rules and use cases get IDs (`GP`, `RK`, `OP`, `RL`, `UC`); other entries are rows, each with Evidence and an AI use label. (ADR-0018)
- Analyses are published and frozen like requirement sets; the sponsor approves the business case in Confluence. (ADR-0019)
- The AI brings the framework, never the facts: every row cites findings or a BA-supplied document, or is an assumption listed as an open question. No web search. (ADR-0020)

### Changes to Phase 1 skills first

| Change | Skill | State |
|---|---|---|
| New ID classes; ID scan covers `analysis/`; missing register row reads `000` | shared `ids` (all skills) | done |
| Create `analysis/` at setup; new register rows | `set-up-initiative` | done (v0.1.1) |
| BRs may trace to gaps; items may trace to rules and use cases | shared `requirement-set` | done |
| Publish-ready page and freeze for analyses; Mermaid fallback | `prepare-for-publication` | to do |
| Routes for the Phase 2 skills | `ask-ba` | to do, with each skill |
| Draft BRs from gaps; FRs from business rules | `findings-to-requirements` | to do, after `define-future-state` |

### Phase 2 skills, in build order

| # | Skill | Does | Writes | BABOK reference |
|---|---|---|---|---|
| 1 | `assess-current-state` | Describes how things work today and why it falls short, with SWOT, PESTLE and five forces as the BA chooses | `current-state.md` | 6.1 Analyze Current State |
| 2 | `define-future-state` | Describes the target state and the gaps to close | `future-state.md` (GP) | 6.2 Define Future State |
| 3 | `assess-risks` | Builds the risk register for the initiative or an option | `risks.md` (RK) | 6.3 Assess Risks |
| 4 | `compare-design-options` | Lays out candidate options against the gaps and business requirements | `design-options.md` (OP) | 7.5 Define Design Options |
| 5 | `build-business-case` | Weighs the options and recommends one for the sponsor | `business-case.md` | 7.6 Analyze Potential Value and Recommend Solution; 6.4 Define Change Strategy |
| 6 | `model-process` | Draws a process as Mermaid, current or future, with use cases and scenarios | `process-<slug>.md`, `use-cases-<slug>.md` (UC) | 7.1 Specify and Model Requirements |
| 7 | `model-data-and-rules` | Draws the data model and lists the business rules | `data-model.md`, `business-rules.md` (RL) | 7.1 Specify and Model Requirements |
| 8 | `prepare-workshop` | Facilitation pack for a workshop or brainstorming session; may instead extend `prepare-elicitation` | `elicitation/` | 4.1 Prepare for Elicitation |

Skills 6–8 do not depend on 1–5 and can be built in parallel. If the scope has to shrink, cut five forces and PESTLE from skill 1 first, then skill 8.

### Open questions for Phase 2

| # | Question | Ask |
|---|---|---|
| 1 | Does the company's Confluence have a Mermaid macro? | Confluence administrator |
| 2 | Who approves analyses other than the business case: the sponsor, or the stakeholders who validated them? | Head of BA practice |
| 3 | Should analyses get a `verified` step and a quality check, as requirements do? | Pilot BAs, after the first analyses |
| 4 | `prepare-workshop` as a new skill, or a workshop mode of `prepare-elicitation`? | Decide when grilling skill 8 |

## 6. Later phases

- **Phase 3, before-publication lifecycle and reuse:** trace queries, prioritisation (MoSCoW, WSJF, Kano), impact analysis on *unpublished* sets, and a reuse catalogue built from **frozen copies** on the drive. It is not built from Confluence, because of the data policy.
- **Phase 4, rollout:** planning skills (BA approach, stakeholder analysis, governance), solution evaluation skills, `INSTALL.md` for each runtime.
- **Future options (deferred):** generated adapters for each runtime (ADR-0005) and direct publication through a connector (ADR-0002).

## 7. How each skill gets built

1. Grill it: triggers, inputs, outputs, what "good" looks like.
2. Write `SKILL.md`: frontmatter with name, situation-first description and BABOK reference. Then steps, the output template with AI use fields, completion criteria and handoffs. Keep it under about 150 lines.
3. Write 3–5 evals: realistic prompts plus checkable properties, such as "every item has an ID, class, source and AI use label" or "no vague terms like *fast*".
4. Run it in Claude Code and in one other pilot runtime, on real pilot work.
5. Tighten it, tag a version and release it.

## 8. Phase 0: before building

- [ ] Choose the pilot initiative: one that is in early elicitation now, with at least one pilot BA on a runtime other than Claude.
- [ ] Take baselines for the interview guide, the elicitation summary, the story set, and peer-review defects.
- [ ] Confirm which runtimes are cleared for which data classifications.
- [x] Library home: this public repo, under the company's open-source program (ADR-0016). Company-specific content still never goes in it.

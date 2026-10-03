# BA-skills: plan

A BABOK-aligned library of agent skills for business analysis work, built the way mattpocock-skills is built: small, composable `SKILL.md` files, a router on top, a few shared primitives, and markdown files in the repo that keep state between sessions.

Status: **draft for planning**. The open decisions are in §7.

---

## 1. Goals

| Goal | How we'll know |
|---|---|
| Spend less time on routine BA artifacts | Time per artifact (interview pack, story set, SWOT, etc.) against a baseline we measure first |
| Produce better artifacts | Defects found in peer review or stakeholder validation, per artifact |
| Make work traceable and reusable | Share of requirements with trace links, and how many reused requirements or models each initiative uses |
| Get other BAs in the program using it | Number of BAs using the skills each week, plus their feedback |

Non-goals for now: replacing stakeholder conversations, making approval decisions, or integrating with an enterprise tool (Jira/ADO/Confluence) before the markdown workflow has proven itself.

---

## 2. Design principles (borrowed from mattpocock-skills)

1. **One skill, one job.** Each skill is a single `SKILL.md`, under about 150 lines, with optional reference files next to it. A skill that keeps growing gets split.
2. **The description is the trigger.** The frontmatter `description` says *when* to use the skill in a BA's words ("prepare for a stakeholder interview"), not BABOK's words.
3. **Primitives under workflows.** A few shared skills (interviewing the user, checking requirement quality, traceability) are called by many others, so nothing gets duplicated.
4. **The repo holds the state.** Every initiative gets a workspace of markdown files: glossary, stakeholder register, requirements, decisions. Skills read and write those files, so work carries over across sessions and between people.
5. **A human approves.** Skills draft, challenge and check. The BA and the stakeholders validate and approve. Every output marks assumptions and open questions explicitly.
6. **A router at the top.** `ask-ba` maps "here's my situation" to the right skill or chain of skills, the way `ask-matt` does.

---

## 3. Architecture: map BABOK's own structure

In BABOK, **tasks** (grouped into 6 knowledge areas) *use* **techniques** (50 of them). The skill library uses the same split:

```
                ┌───────────────────────────┐
                │  ask-ba (router)          │
                └─────────────┬─────────────┘
          ┌───────────────────┼────────────────────┐
  Knowledge-area skills  (WHAT to do: BABOK tasks as workflows)
          │  plan · elicit · manage lifecycle · strategy · RADD · evaluate
          ▼
  Technique skills       (HOW: SWOT, Porter, use cases, user stories, interviews, ...)
          ▼
  Primitives             (grill-stakeholder, req-quality-check, trace, glossary)
          ▼
  Workspace files        (CONTEXT.md, stakeholders.md, requirements/, decisions/)
```

- **Knowledge-area skills** take the BABOK task's inputs and outputs, pick suitable techniques, and hand off to them.
- **Technique skills** are self-contained. A BA can call `swot` directly without going through Strategy Analysis.
- **Perspectives** (Agile, BI, IT, Business Architecture, BPM) are *not* separate skills. They're short reference files that knowledge-area skills load to adjust their output, e.g. user stories plus acceptance criteria in Agile and use cases in a waterfall IT project.

### Proposed repo layout

```
skills/
  ask-ba/                      # router
  setup-ba-workspace/          # one-off: create workspace files for an initiative
  primitives/
    grill-stakeholder/         # structured questioning (BA version of "grilling")
    req-quality-check/         # BABOK quality characteristics: atomic, complete, consistent, concise, feasible, unambiguous, testable, prioritized, understandable
    trace/                     # add, query and validate trace links
    glossary/                  # maintain CONTEXT.md terms
  planning/                    # KA 3: approach, stakeholder engagement, governance, info mgmt, performance
  elicitation/                 # KA 4: prepare, conduct, confirm, communicate, collaborate
  lifecycle/                   # KA 5: trace, maintain/reuse, prioritize, assess changes, approve
  strategy/                    # KA 6: current state, future state, risks, change strategy
  radd/                        # KA 7: specify/model, verify, validate, architecture, design options, value
  evaluation/                  # KA 8: measure performance, analyse, limitations, recommend
techniques/
  interviews/ workshops/ brainstorming/ survey-questionnaire/ focus-groups/ observation/
  swot/ porter-five-forces/ pestle/ business-model-canvas/ root-cause/ benchmarking/
  user-stories/ use-cases-scenarios/ acceptance-criteria/ process-modelling/ data-modelling/
  business-rules/ decision-modelling/ prioritization/ business-case/ risk-analysis/ ...
perspectives/                  # agile.md, bi.md, it.md, business-architecture.md, bpm.md
templates/                     # output templates the skills fill in
evals/                         # test prompts + expected properties for each skill
workspace-example/             # a sample initiative showing the file conventions
```

### Workspace conventions (decide these early, everything depends on them)

```
<initiative>/
  CONTEXT.md            # glossary + scope + business need
  stakeholders.md       # register: role, interest/influence, RACI, engagement approach
  elicitation/          # one file per session: plan, notes, confirmed results
  requirements/         # one file per requirement, or one per set, with frontmatter:
                        #   id, type (business|stakeholder|solution-functional|NFR|transition),
                        #   status (draft|verified|validated|approved|retired), priority,
                        #   source, traces_to, reusable: true/false
  models/               # process, data, use case models (Mermaid/PlantUML)
  decisions/            # ADR-style decision records
  analysis/             # SWOT, Porter, gap analysis, business case
```

Requirement types and statuses use BABOK's terms so that the lifecycle and reuse skills can run on the files.

---

## 4. Phased roadmap

### Phase 0: Foundations (1–2 weeks)
- [ ] Pick **one pilot initiative** that's actually running (real stakeholders, low sensitivity).
- [ ] Record **baseline metrics** on 3–5 artifacts you produce today (time, review defects).
- [ ] Confirm **enterprise guardrails**: which data may go to the AI tool, how to redact, where outputs are stored. (See §6.)
- [ ] Fix the workspace conventions (§3) and requirement frontmatter schema.
- [ ] Write `CONTEXT.md` for *this* repo: the BA vocabulary the skills use.

### Phase 1: MVP slice (2–4 weeks): elicitation → requirements → verification
This is the loop a BA runs every day, so it pays off soonest.
1. `setup-ba-workspace`
2. `grill-stakeholder` (primitive)
3. `prepare-elicitation`: goals, stakeholders, technique choice, interview guide or questionnaire
4. `technique: interviews`, `technique: survey-questionnaire`
5. `confirm-elicitation`: turn raw notes or a transcript into confirmed findings, conflicts and open questions
6. `technique: user-stories` + `acceptance-criteria` (Gherkin)
7. `req-quality-check`: verify against the BABOK quality characteristics
8. `ask-ba` router (covering only the skills above for now)

**Exit criterion:** used on the pilot for at least 2 weeks, with measurable time savings and no rise in review defects.

### Phase 2: Analysis depth (4–6 weeks)
- Strategy: `current-state`, `future-state`, `swot`, `porter-five-forces`, `pestle`, `gap-analysis`, `business-case`, `risk-analysis`
- RADD: `use-cases-scenarios`, `process-modelling` (Mermaid/BPMN-ish), `data-modelling`, `business-rules`, `define-design-options`, `validate-requirements`
- Workshops and brainstorming facilitation packs

### Phase 3: Lifecycle and reuse (4 weeks)
- `trace`, `prioritize` (MoSCoW, WSJF, Kano), `assess-change` (impact analysis using trace links), `approve` (approval pack)
- `reuse-library`: promote requirements with `reusable: true` into a shared catalogue, and search it when new work starts

### Phase 4: Planning, evaluation and rollout
- Planning: `plan-ba-approach`, `stakeholder-analysis`, `ba-governance`, `ba-performance`
- Solution evaluation: `measure-solution-performance`, `assess-limitations`, `recommend-actions`
- Perspective files, the full router, packaging as a plugin for other BAs, and onboarding guidance

---

## 5. How each skill gets built (repeatable loop)

1. **Grill the idea**: what situation triggers it, what goes in, what comes out, what "good" looks like.
2. **Write SKILL.md**: frontmatter (`name`, `description`), steps, output template, completion criteria, and the skills it hands off to.
3. **Write 3–5 evals**: realistic prompts plus checkable properties of the output (e.g. "every story has ≥1 acceptance criterion", "no requirement uses vague words like *fast* or *user-friendly*").
4. **Run it on real pilot work** and note where it fails.
5. **Tighten it**: prune text and fix the description so it triggers when it should.

---

## 6. Enterprise guardrails

- **Confidentiality:** no customer PII or restricted data in prompts unless your AI platform is approved for it. Add a redaction step to `confirm-elicitation` when it ingests transcripts.
- **BABOK copyright:** BABOK® is IIBA's intellectual property. Write skills in your own words and cite section numbers. Don't paste BABOK text into skill files, especially if the repo is ever shared outside the company.
- **Accountability:** outputs are drafts. Approval stays with the people named in the stakeholder register.
- **Bias and hallucination:** skills must keep *what stakeholders said* (with its source) separate from *what the AI inferred*. Mark inferences explicitly.

---

## 7. Decisions to make next

1. **Runtime.** Which tools will the BAs run this in (Claude Code, Claude desktop/Cowork, an enterprise Copilot)? This decides how skills are packaged.
2. **System of record.** Do requirements stay in markdown permanently, or does markdown get exported to or synced with Jira/ADO/Confluence later?
3. **Pilot initiative and baseline artifacts.** Which project, and which 3–5 artifacts get measured?
4. **Audience.** Is this just for you at first, or for the whole BA community of practice? That changes how much onboarding and consistency work is needed.
5. **Model notation.** Mermaid (text, diffs well) or BPMN/UML tools?

---
name: check-requirement-quality
description: >-
  Check draft requirement sets against the BABOK quality characteristics,
  SMART, structure, traceability and vague wording; write a quality report
  with suggested rewrites; then apply the rewrites the BA picks and mark
  the items the BA confirms as verified. Use when a BA wants requirements
  reviewed, verified or made ready for stakeholder validation.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: 7 Requirements Analysis and Design Definition
    tasks:
      - 7.2 Verify Requirements
    techniques:
      - 10.1 Acceptance and Evaluation Criteria
      - 10.37 Reviews
  inputs:
    - INITIATIVE.md
    - draft requirement sets
    - business-requirements.md
    - elicitation files
  outputs:
    - "reviews/<set-slug>-quality-<date>.md"
    - requirement sets with approved rewrites and verified items
  shared:
    - workspace
    - ai-use
    - data-classification
    - findings
    - requirement-set
---

# Check requirement quality

Reviews requirements the way a demanding peer reviewer would: every item against every check in `references/checks.md`, every issue with a suggested rewrite. Edits happen only after the BA approves them, item by item.

References (read before step 1): `references/checks.md`, `references/requirement-set.md`, `references/findings.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md` (glossary and business need) and run the clearance check. Ask the BA which draft sets to check; always read `requirements/business-requirements.md` with them, and the elicitation files their items cite. A set with status `published` is a frozen copy: say so and leave it out. In a chat runtime, ask for these files and wait.

Done when the chosen draft sets, the business requirements and the cited findings are loaded.

## 2. Check every item

Run every check in `references/checks.md` on every item, and the cross-item checks (Consistent, duplicates, traceability) across all loaded sets. For each ✗ and ⚠, write the issue and a suggested rewrite. A rewrite uses only facts from the findings or the BA; where the fix needs a fact nobody has given (a number, a date), the rewrite says what to ask and whom, from the open questions. Mark each rewrite **wording only** (keeps the item's AI use) or **substance** (makes it AI-generated).

Done when every item has a result in every column and every ✗ and ⚠ has an issue row.

## 3. Report

Fill `templates/quality-report.md` and deliver it as `reviews/<set-slug>-quality-<YYYY-MM-DD>.md` (for several sets, use the first set's slug plus `-and-more`). Items with no ✗ are proposed as verified.

Then ask the BA, in one message: which rewrites to apply (by issue number), and which proposed items to confirm as verified. Wait. Change no set before the BA answers.

Done when the report is delivered and the BA has answered.

## 4. Apply what the BA approved

For each set touched, and nothing else:
- apply each approved rewrite; set AI use to `AI-generated` for substance rewrites, leave it for wording-only ones;
- for each confirmed item: `Status: verified`, `Reviewer:` the BA's name, `Reviewed on:` today;
- raise the set's version by 0.1, once per run;
- leave every other item exactly as it was.

Deliver the changed sets as `references/workspace.md` describes, and suggest the next step: validation with stakeholders, then `prepare-for-publication`.

Done when every approved change is in place, no unapproved change is, and the BA has the files.

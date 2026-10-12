---
name: prepare-for-publication
description: >-
  Turn a validated requirement set or analysis into a page ready to paste
  into Confluence Data Center — page properties, trimmed items and rows,
  diagrams, open questions and a proposed AI use label — then, once the
  BA confirms the page is live, freeze the workspace file as published.
  Use when a BA is ready to send a requirement set, a business case or
  another analysis for approval in Confluence.
metadata:
  version: 0.2.0
  babok:
    knowledge_area: "5 Requirements Life Cycle Management"
    tasks:
      - 5.5 Approve Requirements
    techniques:
      - 10.37 Reviews
  inputs:
    - INITIATIVE.md
    - one validated requirement set or analysis
  outputs:
    - Confluence-ready page with paste instructions
    - frozen requirement set or analysis with status published
  shared:
    - workspace
    - ai-use
    - data-classification
    - requirement-set
    - analysis
---

# Prepare for publication

Produces the page that goes to Confluence for approval, then freezes the workspace file. After this skill, the file lives in Confluence and no skill touches it again. It handles two kinds of file: a **requirement set** (`requirements/`) and an **analysis** (`analysis/`).

References (read before step 1): `references/page-format.md`, `references/requirement-set.md`, `references/analysis.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Check the file is ready

Read `INITIATIVE.md`, run the clearance check, and read the one file the BA names. In a chat runtime, ask for both files and wait. Its folder tells you whether it is a requirement set or an analysis.

A **requirement set** is ready when all of these hold:
- its status is `draft`;
- every item's status is `validated`;
- `Validated by` and `Validated on` in the set header are filled.

An **analysis** is ready when all of these hold:
- its status is `draft`;
- `Validated by` and `Validated on` in the header are filled.

A `published` file is already frozen: stop and say so. If any other condition fails, list every blocker (by item ID for a set) and stop.

Warnings, which do not block: a set item tracing to a BR that is not yet validated; an analysis row or item whose Evidence reads `Assumption`; an analysis citing IDs from another analysis that is not yet validated. List each warning by ID or row.

Done when the file passes its conditions and every warning is listed.

## 2. Build the page

Fill `templates/confluence-page.md` following `references/page-format.md`, using the part for the file's kind: title, Part 1, Part 2, open questions if any, footer. Propose the page label. Copy every statement, row, field and diagram exactly as it is in the file; this skill rewords nothing.

Done when every item, row and diagram in the file appears on the page, in the file's order, trimmed as the page format says.

## 3. Hand over

Show the BA the page, the proposed label and the paste steps from `references/page-format.md`, including the diagram step when the page has a Mermaid block. The page is shown in the chat, not saved: the frozen file is the workspace record.

Ask the BA to confirm the label, publish the page, and reply with its link. Wait. Change nothing in the workspace before the BA replies.

Done when the BA has replied with the page link.

## 4. Freeze the file

Only after the BA confirms the page is live:
- set the header's Status to `published`, and for a requirement set also every item's Status;
- fill `Confluence page` with the link;
- add this skill's footer line (`references/ai-use.md`);
- leave everything else exactly as it was, version included.

Deliver the frozen file as `references/workspace.md` describes. Tell the BA that approval now happens in Confluence and that this file is a frozen copy no skill will change. For a requirement set, add that delivery stories can be drafted from it with `requirements-to-stories`. For a business case, add that the sponsor approves it in Confluence.

Done when the frozen file is delivered and its header reads `published`.

---
name: prepare-for-publication
description: >-
  Turn a validated requirement set into a page ready to paste into
  Confluence Data Center — page properties, trimmed item blocks, open
  questions and a proposed AI use label — then, once the BA confirms the
  page is live, freeze the workspace file as published. Use when a BA is
  ready to send a requirement set for approval in Confluence.
metadata:
  version: 0.1.0
  babok:
    knowledge_area: "5 Requirements Life Cycle Management"
    tasks:
      - 5.5 Approve Requirements
    techniques:
      - 10.37 Reviews
  inputs:
    - INITIATIVE.md
    - one validated requirement set
  outputs:
    - Confluence-ready page with paste instructions
    - frozen requirement set with status published
  shared:
    - workspace
    - ai-use
    - data-classification
    - requirement-set
---

# Prepare for publication

Produces the page that goes to Confluence for approval, then freezes the workspace file. After this skill, the set lives in Confluence and no skill touches it again.

References (read before step 1): `references/page-format.md`, `references/requirement-set.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Check the set is ready

Read `INITIATIVE.md`, run the clearance check, and read the one set the BA names. In a chat runtime, ask for both files and wait.

The set is ready when all of these hold:
- its status is `draft` (a `published` set is already frozen: stop);
- every item's status is `validated`;
- `Validated by` and `Validated on` in the set header are filled.

If any fails, list every blocker by item ID and stop. If an item traces to a BR that is not yet validated, say so as a warning; it does not block.

Done when the set passes all three conditions.

## 2. Build the page

Fill `templates/confluence-page.md` following `references/page-format.md`: title, Part 1, Part 2, open questions if any, footer. Propose the page label. Copy statements, rationale, thresholds and sources exactly as they are in the set; this skill rewords nothing.

Done when every item in the set appears on the page, in class order, with its trimmed table.

## 3. Hand over

Show the BA the page, the proposed label and the paste steps from `references/page-format.md`. The page is shown in the chat, not saved: the frozen set is the workspace record.

Ask the BA to confirm the label, publish the page, and reply with its link. Wait. Change nothing in the workspace before the BA replies.

Done when the BA has replied with the page link.

## 4. Freeze the set

Only after the BA confirms the page is live:
- set the set header's Status and every item's Status to `published`;
- fill `Confluence page` with the link;
- leave everything else exactly as it was, version included.

Deliver the frozen set as `references/workspace.md` describes. Tell the BA that approval now happens in Confluence, that this file is a frozen copy no skill will change, and that delivery stories can be drafted from it with `requirements-to-stories`.

Done when the frozen set is delivered and every item reads `published`.

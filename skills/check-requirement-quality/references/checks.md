# Checks

Authored here, not generated from `shared/`. Every check yields one result per item: ✓ pass · ✗ must fix (blocks `verified`) · ⚠ consider · n/a · `pending` · `BA` (for the BA to judge).

## BABOK characteristics (BABOK v3 §7.2)

| Check | Passes when | Fails as |
|---|---|---|
| Atomic | One requirement per statement: no "and/or", no second "shall" | ✗ |
| Complete | Statement has no `TBD`; Rationale is not `TBD` | ✗ |
| Consistent | Contradicts no other item in the checked sets or `business-requirements.md`, and duplicates none | ✗ |
| Concise | States the need without explanation or solution design | ⚠ |
| Feasible | Not obviously impossible or self-contradictory; otherwise `BA` | ✗ when obvious, else `BA` |
| Unambiguous | One reading only: no vague term (below), no undefined qualifier ("at risk", "relevant"), no term the glossary says to avoid | ✗ |
| Testable | Someone could check it is met; BR and NFR need a Threshold | ✗ |
| Prioritised | Always `pending` until prioritisation (Phase 3) | `pending` |
| Understandable | Domain terms are in the initiative glossary or self-evident | ⚠ |

## SMART

| Check | BR, NFR | SR, FR, TR | Passes when | Fails as |
|---|---|---|---|---|
| Specific | yes | yes | Names who or what, and the condition | ✗ |
| Measurable | yes | n/a | Threshold holds a number or verifiable condition, not `TBD` | ✗ |
| Achievable | yes | yes | Nothing in the findings suggests it cannot be done | ⚠ |
| Relevant | yes | yes | BR traces to `Business need`; others trace to an existing BR | ✗ |
| Time-bound | yes | n/a | BR: says by when; NFR: says when or under which conditions the threshold applies (e.g. at peak load, from go-live) | BR ✗, NFR ⚠ |

## Structure

✗ when any of these fails: all eleven fields present · ID matches `<CODE>-<CLASS>-<NNN>` and its section's class · statement follows its class pattern · every Source is `Business need` or a finding ID that exists and is confirmed.

## Traceability

- ✗ SR, FR, NFR or TR with no trace to an existing BR.
- ⚠ A trace link no finding supports: neither item's sources state the need the link claims.
- ⚠ A BR that nothing traces to.

## Vague terms

fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, seamless, appropriate, adequate, sufficient, as needed, as appropriate, etc., and/or, minimal, maximal, optimal, state-of-the-art, support (as a verb without an object), handle.

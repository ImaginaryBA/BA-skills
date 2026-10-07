<!-- Generated from shared/ids.md by scripts/sync_shared.py. Edit the master, not this copy. -->

# IDs

## Format

`<CODE>-<CLASS>-<NNN>`, e.g. `IMT-FR-012`.

- `CODE`: the initiative code, 2–5 uppercase letters.
- `CLASS`: `BR` business, `SR` stakeholder, `FR` functional, `NFR` non-functional, `TR` transition requirement; `ST` delivery story (temporary until its Jira key is recorded).
- `NNN`: sequence within the initiative and class, zero-padded to 3 digits, starting at 001.

IDs are never renumbered or reused. A retired or superseded item keeps its ID. An item copied from another initiative gets a new ID plus a `Reused from` value naming the original.

## ID register

The ID register is a table in `INITIATIVE.md` holding the last number used per class. It is the source of every new ID.

1. Read the register. Next ID = last used + 1.
2. In an agentic runtime, also scan `requirements/` and `stories/` for the highest number per class. If the scan finds a higher number than the register, stop and show the BA both numbers; continue only once the BA says which is right.
3. After creating IDs, output the updated register (in a chat runtime, as an updated `INITIATIVE.md` block).

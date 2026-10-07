#!/usr/bin/env python3
"""Copy shared conventions into each skill's references/ folder (ADR 0012).

Each skill lists what it needs in its SKILL.md frontmatter:
    metadata:
      shared: [workspace, ids]
which copies shared/workspace.md and shared/ids.md into skills/<skill>/references/.

Usage:
    python3 scripts/sync_shared.py          # write the copies
    python3 scripts/sync_shared.py --check  # exit 1 if any copy is missing or stale
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"
HEADER = "<!-- Generated from shared/{name}.md by scripts/sync_shared.py. Edit the master, not this copy. -->\n\n"


def shared_names(skill_md: Path) -> list[str]:
    text = skill_md.read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not front:
        sys.exit(f"{skill_md}: missing frontmatter")
    line = re.search(r"^\s*shared:\s*\[(.*?)\]\s*$", front.group(1), re.M)
    if not line:
        return []
    return [n.strip() for n in line.group(1).split(",") if n.strip()]


def main() -> int:
    check = "--check" in sys.argv[1:]
    problems = 0
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        refs = skill_md.parent / "references"
        for name in shared_names(skill_md):
            master = SHARED / f"{name}.md"
            if not master.exists():
                print(f"ERROR {skill_md.parent.name}: shared/{name}.md does not exist")
                problems += 1
                continue
            wanted = HEADER.format(name=name) + master.read_text(encoding="utf-8")
            copy = refs / f"{name}.md"
            current = copy.read_text(encoding="utf-8") if copy.exists() else None
            if current == wanted:
                continue
            if check:
                print(f"STALE {skill_md.parent.name}/references/{name}.md")
                problems += 1
            else:
                refs.mkdir(exist_ok=True)
                copy.write_text(wanted, encoding="utf-8")
                print(f"wrote {skill_md.parent.name}/references/{name}.md")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

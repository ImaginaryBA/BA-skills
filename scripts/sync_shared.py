#!/usr/bin/env python3
"""Copy shared conventions into each skill's references/ folder (ADR 0012).

Each skill lists what it needs in its SKILL.md frontmatter:
    metadata:
      shared:
        - workspace
        - ids
which copies shared/workspace.md and shared/ids.md into skills/<skill>/references/.

It also generates skills/ask-ba/references/coverage.md (every BABOK task in
docs/babok-tasks.md with the skills whose metadata lists it), and
dist/open-webui/<skill>.md: each skill as one file, for chat runtimes that
import a single markdown file (ADR 0005).

Usage:
    python3 scripts/sync_shared.py          # write the copies and the coverage table
    python3 scripts/sync_shared.py --check  # exit 1 if anything is missing or stale
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
    fm = front.group(1)
    inline = re.search(r"^\s*shared:\s*\[(.*?)\]\s*$", fm, re.M)
    if inline:
        return [n.strip() for n in inline.group(1).split(",") if n.strip()]
    listed = re.search(r"^(\s*)shared:\s*\n((?:\1\s+-\s.*\n?)*)", fm, re.M)
    if not listed:
        return []
    return [re.sub(r"^\s*-\s*", "", l).strip() for l in listed.group(2).splitlines() if l.strip()]


def block_list(fm: str, key: str) -> list[str]:
    m = re.search(rf"^(\s*){key}:\s*\n((?:\1\s+-\s.*\n?)*)", fm, re.M)
    if not m:
        return []
    return [re.sub(r"^\s*-\s*", "", l).strip().strip('"') for l in m.group(2).splitlines() if l.strip()]


def coverage() -> str:
    tasks = {}
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        fm = re.match(r"^---\n(.*?)\n---\n", skill_md.read_text(encoding="utf-8"), re.S).group(1)
        for t in block_list(fm, "tasks"):
            tasks.setdefault(t.split()[0], []).append(f"`{skill_md.parent.name}`")
    out = ["<!-- Generated from docs/babok-tasks.md and skill metadata by scripts/sync_shared.py. Do not edit. -->", "",
           "# BABOK coverage", "", "Which BA-skills skill supports each BABOK v3 task. Tasks marked \"not yet\" have no skill.", ""]
    for line in (ROOT / "docs" / "babok-tasks.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            out += ["", line, "", "| Task | Skills |", "|---|---|"]
        elif line.startswith("- "):
            name = line[2:]
            out.append(f"| {name} | {', '.join(tasks.get(name.split()[0], [])) or 'not yet'} |")
    return "\n".join(out).replace("\n\n\n", "\n\n") + "\n"


def bundle(skill_dir: Path) -> str:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm, body = front.group(1), text[front.end():]
    desc = re.search(r"^description:\s*>-\n((?:  .*\n?)+)", fm + "\n", re.M)
    description = " ".join(l.strip() for l in desc.group(1).splitlines()) if desc else ""
    version = re.search(r"^\s*version:\s*(\S+)", fm, re.M).group(1)
    out = ["---", f"name: {skill_dir.name}", "description: " + '"' + description.replace('\\', '\\\\').replace('"', '\\"') + '"' , "---", "",
           f"<!-- Generated from skills/{skill_dir.name}/ (v{version}) by scripts/sync_shared.py. Edit the skill, not this file. -->", "",
           "Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.", "",
           body.strip(), ""]
    for sub in ("references", "templates"):
        for f in sorted((skill_dir / sub).glob("*.md")) if (skill_dir / sub).exists() else []:
            content = re.sub(r"^<!-- Generated from .*? -->\n\n", "", f.read_text(encoding="utf-8"))
            out += ["", "---", "", f"# Included file: {sub}/{f.name}", "", "````markdown", content.strip(), "````"]
    return "\n".join(out) + "\n"


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
    cov = SKILLS / "ask-ba" / "references" / "coverage.md"
    if cov.parent.parent.exists():
        wanted = coverage()
        current = cov.read_text(encoding="utf-8") if cov.exists() else None
        if current != wanted:
            if check:
                print("STALE ask-ba/references/coverage.md")
                problems += 1
            else:
                cov.parent.mkdir(exist_ok=True)
                cov.write_text(wanted, encoding="utf-8")
                print("wrote ask-ba/references/coverage.md")
    dist = ROOT / "dist" / "open-webui"
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        target = dist / f"{skill_md.parent.name}.md"
        wanted = bundle(skill_md.parent)
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == wanted:
            continue
        if check:
            print(f"STALE dist/open-webui/{target.name}")
            problems += 1
        else:
            dist.mkdir(parents=True, exist_ok=True)
            target.write_text(wanted, encoding="utf-8")
            print(f"wrote dist/open-webui/{target.name}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

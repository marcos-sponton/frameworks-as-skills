#!/usr/bin/env python3
"""
Regenerate the "What's here" section of the root README.md from SKILL.md metadata.

Sources of truth per skill:
- `skills/<slug>/SKILL.md` — YAML frontmatter has `name`; body first `# Title` line has display title.
- `.skills-index.yaml` (repo root, optional) — provides curated `tagline` and `theme` per slug.
  If a slug isn't in `.skills-index.yaml`, the script falls back to a plain listing under "Other"
  and prints a warning.

README markers (must exist for the script to work):
    <!-- SKILLS_INDEX_START -->
    ...regenerated content...
    <!-- SKILLS_INDEX_END -->

Also updates the count in the intro line: "**What's here** — N skills, each packages one framework:".

Usage:
    python3 scripts/update-readme.py
    python3 scripts/update-readme.py --check   # exit 1 if README would change (for CI)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SKILLS_DIR = ROOT / "skills"
INDEX_FILE = ROOT / ".skills-index.yaml"

MARKER_START = "<!-- SKILLS_INDEX_START -->"
MARKER_END = "<!-- SKILLS_INDEX_END -->"

# Order themes will appear in the rendered README.
THEME_ORDER = [
    "Strategy",
    "Product & discovery",
    "Positioning & narrative",
    "Sensemaking & decisions",
    "Sales",
    "Management & communication",
    "Growth",
    "Engineering",
    "Other",
]


def parse_frontmatter(text):
    """Extract YAML frontmatter as a flat dict. Only supports top-level scalars (name, description)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()
    return result


def parse_first_h1(text):
    """Return the text of the first `# Title` line in body (after frontmatter), or None."""
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def parse_skills_index_yaml():
    """
    Minimal parser for `.skills-index.yaml`. Format:

        - slug: playing-to-win
          title: Playing to Win
          tagline: Roger Martin's 5-question strategy cascade
          theme: Strategy

    Returns dict keyed by slug.
    """
    if not INDEX_FILE.exists():
        return {}
    entries = {}
    current = None
    for raw in INDEX_FILE.read_text().splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            # New entry
            current = {}
            content = line[2:]
            if ":" in content:
                k, _, v = content.partition(":")
                current[k.strip()] = v.strip()
        elif line.startswith("  ") and ":" in line and current is not None:
            k, _, v = line.partition(":")
            current[k.strip()] = v.strip()
        if current is not None and "slug" in current:
            entries[current["slug"]] = current
    return entries


def collect_skills():
    """Walk skills/ and build a list of dicts. Merges frontmatter + first-H1 + .skills-index.yaml."""
    index = parse_skills_index_yaml()
    skills = []
    warnings = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            warnings.append(f"skills/{skill_dir.name}/ has no SKILL.md — skipping")
            continue
        text = skill_md.read_text()
        fm = parse_frontmatter(text)
        first_h1 = parse_first_h1(text)
        slug = skill_dir.name
        meta = index.get(slug, {})
        if not meta:
            warnings.append(
                f"'{slug}' not in .skills-index.yaml — using fallbacks (add an entry for a curated tagline + theme)"
            )
        skill = {
            "slug": slug,
            "title": meta.get("title") or first_h1 or fm.get("name") or slug,
            "tagline": meta.get("tagline") or fm.get("description", "").split(".")[0].strip(),
            "theme": meta.get("theme") or "Other",
        }
        # Truncate over-long taglines that came from the frontmatter description (which is written
        # for LLM triggering, not human reading).
        if len(skill["tagline"]) > 130:
            skill["tagline"] = skill["tagline"][:127].rstrip() + "..."
        skills.append(skill)
    return skills, warnings


def render_index(skills):
    """Group by theme and render markdown for the skills index block."""
    by_theme = {}
    for s in skills:
        by_theme.setdefault(s["theme"], []).append(s)

    def theme_sort_key(t):
        try:
            return (THEME_ORDER.index(t), t)
        except ValueError:
            return (len(THEME_ORDER), t)

    ordered_themes = sorted(by_theme.keys(), key=theme_sort_key)

    lines = [f"**What's here** — {len(skills)} skills, each packages one framework:", ""]
    for theme in ordered_themes:
        lines.append(f"**{theme}**")
        for s in sorted(by_theme[theme], key=lambda x: x["title"]):
            lines.append(f"- ✅ **[{s['title']}](skills/{s['slug']}/)** — {s['tagline']}")
        lines.append("")
    lines.append("More coming — see the roadmap below.")
    return "\n".join(lines)


def update_readme(new_index, check=False):
    content = README.read_text()
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    replacement = f"{MARKER_START}\n{new_index}\n{MARKER_END}"
    if not pattern.search(content):
        print(
            f"ERROR: markers not found in README.md.\n"
            f"Add these two lines around the existing skills index:\n"
            f"    {MARKER_START}\n"
            f"    ...existing content...\n"
            f"    {MARKER_END}",
            file=sys.stderr,
        )
        sys.exit(2)
    new_content = pattern.sub(replacement, content)
    if new_content == content:
        return False  # no change
    if check:
        return True  # would change
    README.write_text(new_content)
    return True


def main():
    check_mode = "--check" in sys.argv
    skills, warnings = collect_skills()
    for w in warnings:
        print(f"warn: {w}", file=sys.stderr)
    if not skills:
        print("No skills found under skills/.", file=sys.stderr)
        sys.exit(1)
    new_index = render_index(skills)
    changed = update_readme(new_index, check=check_mode)
    if check_mode:
        if changed:
            print("README.md would change — run `python3 scripts/update-readme.py` and commit.", file=sys.stderr)
            sys.exit(1)
        print("README.md up to date.")
        sys.exit(0)
    if changed:
        print(f"Updated README.md — {len(skills)} skills across {len(set(s['theme'] for s in skills))} themes.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()

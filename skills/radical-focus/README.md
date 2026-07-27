# Radical Focus — an agent skill

An agent skill for **Christina Wodtke's Radical Focus** — the operational method for making OKRs actually work: team-level (not individual), one Objective at a time, weekly cadence (Monday commitments, Friday celebrations), and a Health Metric that guards against gaming.

This isn't a summary of the book. It's a working thinking partner in Wodtke's method, built from:

- *Radical Focus* — 1st edition (2016) and 2nd expanded edition (2021, +22,000 words)
- *The Team That Managed Itself* (2019, with Martin Eriksson) — source of the Team Health Monitor
- Wodtke's [Elegant Hack](https://eleganthack.com/) blog (essays through 2026), including the recent Health Metric case study on OpenAI's 2025 "code red"
- Her [Medium](https://cwodtke.medium.com/) archive
- Podcast appearances including [Lenny Rachitsky (Mar 2023)](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-okrs-christina) and [Melissa Perri's Product Thinking (Jan 2023)](https://podcasts.apple.com/us/podcast/zooming-in-on-okrs-with-christina-wodtke/id1550800132?i=1000595118081)
- Her Stanford course CS177 (Human-Centered Product Management)

**Why this exists.** Invoke "OKRs" in Claude or Codex without a skill and you get generic Doerr-flavored advice — the model knows the acronym but not Wodtke's distinct method: team-only, one Objective, weekly cadence, Health Metric. This skill closes that gap. Recent essays (2024–2026), including her position shifts (alignment > cascading, decoupling OKRs from approval) live in `references/post-book.md`.

## What's inside

```
radical-focus/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → Objective, KRs, Health Metrics, weekly cadence, grading
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material Wodtke published after the 2nd edition
│   ├── author-live-sources.md            → index of all live sources (Elegant Hack, Medium, courses, podcasts)
│   ├── voice-and-tone.md                 → how Wodtke actually teaches
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (Hanna's tea company, OpenAI code red, Stanford students)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

This is an **agent skill** (SKILL.md open standard, [agentskills.io](https://agentskills.io)). It works in Claude Code, Codex CLI, Claude Desktop, and any agent runtime that reads SKILL.md.

Pick the path that matches your setup:

```bash
# From this repo root — Claude Code / Claude Desktop:
ln -s "$(pwd)/skills/radical-focus" ~/.claude/skills/radical-focus

# Codex CLI:
ln -s "$(pwd)/skills/radical-focus" ~/.codex/skills/radical-focus

# Any other agent that reads a skills directory: copy the folder there.
```

Or use the repo's `skills.sh` installer if you're pulling multiple skills at once (see the root README).

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use Radical Focus," "run this through Wodtke's method," "walk me through the Monday commitments").

## Attribution

**Christina Wodtke** — author, teacher, speaker. Stanford (CS177 Human-Centered Product Management), Stanford Continuing Education, California College of the Arts. Ex-LinkedIn, Yahoo, Zynga, Myspace. Author of *Radical Focus* (2016 / expanded 2021), *The Team That Managed Itself* (2019), *Pencil Me In* (2017).

- **Buy the book:** [Radical Focus on Amazon](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006028). Read it — this skill points you toward the source, it doesn't replace it.
- **Elegant Hack (primary blog):** [eleganthack.com](https://eleganthack.com/).
- **Medium:** [cwodtke.medium.com](https://cwodtke.medium.com/).
- **Site + workshops + course:** [cwodtke.com](https://cwodtke.com/).
- **Course on Maven:** [OKRs with Radical Focus](https://maven.com/cwodtke/okrswithradicalfocus).

This skill is **not endorsed by Christina Wodtke**. It is Marcos Sponton's structured reading of Wodtke's public work, built to make Claude or Codex a better thinking partner in her method. If Christina herself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Elegant Hack. Especially welcome:

- **New essays / podcast episodes / talks for `author-live-sources.md`** — Wodtke posts regularly on Elegant Hack and Medium. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Wodtke has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Wodtke's voice is off, tell us.
- **3rd edition additions** — if a 3rd edition of *Radical Focus* is out (referenced in some places but not confirmed at build time), the deltas belong in `post-book.md`.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Case examples beyond Hanna's tea company** — Wodtke uses her Stanford students' companies and recent public events (OpenAI 2025 code red); more real cases would sharpen the skill.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Wodtke's Radical Focus to run my own week and this skill is what falls out.

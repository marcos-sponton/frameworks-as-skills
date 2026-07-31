# Shape Up — an agent skill

An agent skill for **Ryan Singer's Shape Up** — Basecamp's product development method for deciding what to build (the shaped Pitch or Package), how to bet on it (the Betting Table), and how to ship it (six-week cycles with a two-week cool-down, small autonomous build teams, Hill Charts, the Circuit Breaker, and no backlog).

This isn't a summary of the book. **The book is free online in full at [basecamp.com/shapeup](https://basecamp.com/shapeup) — go read it.** This skill exists to make Claude, Codex, or any agent supporting the SKILL.md standard a working thinking partner *in the method*: shaping a pitch, critiquing a package, running a betting table, diagnosing a stuck hill chart, deciding whether to trip the circuit breaker, adapting the method for a non-Basecamp company.

Built from:

- **The 2019 book:** *Shape Up: Stop Running in Circles and Ship Work that Matters*, Ryan Singer, 37signals. Free at [basecamp.com/shapeup](https://basecamp.com/shapeup).
- **Ryan Singer's site (Felt Presence):** [ryansinger.co](https://ryansinger.co) — post-Basecamp consulting, coaching, and the evolving "Shaping in Real Life" material.
- **The 2022+ post-book canon:** *Framing* (2022), *Common Pitfalls* (2025), *End-to-End with Shape Up* (2025), and the essay archive at [ryansinger.co/posts](https://www.ryansinger.co/posts/).
- **Podcast primary sources:** Singer on [Lenny's Podcast](https://www.lennysnewsletter.com/p/shape-up-ryan-singer) (2025 — the freshest long-form interview), [The Product Experience](https://www.mindtheproduct.com/shape-up-ryan-singer-on-the-product-experience/) (2025), [Shapers & Builders — Shape Up 2.0](https://shapersbuilders.transistor.fm/episodes/getting-to-shape-up-2-0-ryan-singer-author-of-shape-up-founder-at-felt-presence) (2023), and [Changelog Interviews #357](https://changelog.com/podcast/357) (2019).

**Why this exists.** Invoke "Shape Up" or "shaping" in an agent without a skill and you get an accurate summary of the book — but you lose the disposition that makes the mechanisms work: fixed appetite (not estimation), circuit-breaker-by-default, no backlog, fat marker sketches over high-fidelity mocks, shaping *before* betting (not inside the cycle). This skill closes that gap. It also captures the post-book evolution: the Framing prelude Singer added in 2022, the "Pitch → Package" rename, and the *Shaping in Real Life* adaptation for typical (non-Basecamp) companies.

## What's inside

```
shape-up/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the mechanisms in Singer's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material published after 2019 (Framing, Pitfalls, case studies)
│   ├── author-live-sources.md            → index of all live sources (ryansinger.co, podcasts, X, LinkedIn)
│   ├── voice-and-tone.md                 → how Singer actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Scrum, Working Backwards, Inspired, Continuous Discovery, Kanban)
│   ├── examples.md                       → worked cases (Basecamp, Hey, the 2025 gym-management case study)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

The skill follows the open **agent skill** standard (SKILL.md, [agentskills.io](https://agentskills.io/)) and works in any compatible agent — Claude Code, Codex CLI, Claude Desktop, and others.

**Option 1 — via the repo's install script (recommended):**

```bash
# From the frameworks-as-skills repo root:
./scripts/skills.sh install shape-up
```

**Option 2 — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/shape-up" ~/.claude/skills/shape-up
```

**Option 3 — Codex CLI:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/shape-up" ~/.codex/skills/shape-up
```

For Claude Desktop or another agent that supports SKILL.md, copy or symlink the `shape-up/` folder into that tool's skills directory.

Once installed, invoke naturally by describing your situation — the assistant picks the skill up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Shape Up skill", "help me shape a pitch", "critique this package", "we hit the circuit breaker — should we extend?").

## Attribution

**Ryan Singer** — designer, product strategist, author of *Shape Up* (2019). Spent 17 years at 37signals / Basecamp, most recently as Head of Strategy. Left around 2020 to found [Felt Presence LLC](https://ryansinger.co), where he consults on Shape Up adoption for teams outside Basecamp.

- **Free online book:** [basecamp.com/shapeup](https://basecamp.com/shapeup) — the whole book, free. Read it; this skill points you toward the source, it doesn't replace it.
- **Ryan Singer's site:** [ryansinger.co](https://ryansinger.co) · Archive: [ryansinger.co/posts](https://www.ryansinger.co/posts/)
- **Ryan Singer on Lenny's Podcast (2025):** [A better way to plan, build, and ship products](https://www.lennysnewsletter.com/p/shape-up-ryan-singer)
- **Ryan Singer on X:** [@rjs](https://twitter.com/rjs) · **LinkedIn:** [linkedin.com/in/feltpresence](https://www.linkedin.com/in/feltpresence/)
- **Shape Up community forum:** [discourse.learnshapeup.com](https://discourse.learnshapeup.com)

This skill is **not endorsed by Ryan Singer, Felt Presence LLC, or 37signals.** It is Marcos Sponton's structured reading of Singer's public work, built to make the assistant a better thinking partner in the method. If Singer himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Singer's ongoing teaching. Especially welcome:

- **New essays / podcasts / videos for `author-live-sources.md`** — Singer publishes a few articles a year on ryansinger.co; add new posts with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Singer has warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Singer's voice is off, tell me. Singer is careful and systemic; DHH/Fried are polemical. Keep them apart.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or blends Shape Up with Agile is data.
- **Non-Basecamp adoption cases** — the *Shaping in Real Life* material is thin on real worked examples. Cases where teams successfully (or unsuccessfully) adapted Shape Up outside Basecamp are valuable.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). Shape Up-shaped thinking has been in my head for years and this skill is what falls out.

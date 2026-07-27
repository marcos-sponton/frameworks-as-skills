# Working Backwards — an agent skill

An agent skill for **Bill Carr and Colin Bryar's Working Backwards** — Amazon's operational method for deciding what to build (the PR/FAQ), how to argue about it (the six-page narrative memo and silent reading), and how to structure the team that builds it (Single-Threaded Leader, Bar Raiser, Input Metrics, Weekly Business Review).

This isn't a summary of the book. It's a working thinking partner in Carr and Bryar's method, built from:

- The 2021 book *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (St. Martin's Press)
- The [workingbackwards.com](https://workingbackwards.com) blog (active March 2026 batch)
- The firm's course catalog (PR/FAQ Mastery, Input Metrics Mastery, Operating Plan Mastery, Bar Raiser Hiring Mastery, Business Narratives Mastery)
- Bill Carr on Lenny Rachitsky's podcast (Nov 2023) — the richest post-book long-form interview
- Both authors on First Round Review, Product Mastery Now, David Cancel / Seeking Wisdom, and Amazon's own "About Amazon" interview

**Why this exists.** Invoke "Working Backwards" or "PR/FAQ" in Claude or Codex without a skill and you get an accurate summary of the book — but you lose the disposition that makes the mechanisms work: silent reading, veto-carrying Bar Raisers, non-matrixed STLs, most PR/FAQs rejected as a feature not a bug. This skill closes that gap. Post-book material (compensation-planning doom loop, coordination tax framing, atomic customer needs) lives in `references/post-book.md`.

## What's inside

```
working-backwards/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the four load-bearing mechanisms in the authors' terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material published after 2021 (2026 blog, doom loop, coordination tax)
│   ├── author-live-sources.md            → index of all live sources (firm blog, courses, WBR App, podcasts)
│   ├── voice-and-tone.md                 → how Carr and Bryar actually talk
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (Kindle, Prime, AWS, Fire Phone, Alexa, Amazon Music)
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
./scripts/skills.sh install working-backwards
```

**Option 2 — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/working-backwards" ~/.claude/skills/working-backwards
```

**Option 3 — Codex CLI:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/working-backwards" ~/.codex/skills/working-backwards
```

For Claude Desktop or another agent that supports SKILL.md, copy or symlink the `working-backwards/` folder into that tool's skills directory.

Once installed, invoke naturally by describing your situation — the assistant picks the skill up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Working Backwards skill", "help me write a PR/FAQ", "critique this six-pager").

## Attribution

**Bill Carr** — Co-founder of Working Backwards LLC. Joined Amazon in 1999; spent 15+ years there as VP of Digital Media, launching and running Amazon Music, Prime Video, and Amazon Studios.

**Colin Bryar** — Co-founder of Working Backwards LLC. Joined Amazon in 1998; spent 12 years in senior leadership, including two as Jeff Bezos's Chief of Staff ("Jeff's shadow"). Later COO of RedMart (sold to Alibaba).

- **Buy the book:** [Amazon](https://www.amazon.com/Working-Backwards-Insights-Stories-Secrets/dp/1250267595) · [Macmillan / St. Martin's Press](https://us.macmillan.com/books/9781250267597/workingbackwards/). Read it — this skill points you toward the source, it doesn't replace it.
- **Working Backwards LLC:** [workingbackwards.com](https://workingbackwards.com) — courses, advisory, blog, WBR App.
- **Firm blog (post-book teaching):** [workingbackwards.com/blog](https://workingbackwards.com/blog/)
- **Bill Carr on Lenny's Podcast (2023):** [Unpacking Amazon's unique ways of working](https://www.lennysnewsletter.com/p/unpacking-amazons-unique-ways-of)
- **Bill Carr on LinkedIn:** [linkedin.com/in/bill-carr](https://www.linkedin.com/in/bill-carr/)

This skill is **not endorsed by Bill Carr, Colin Bryar, or Working Backwards LLC.** It is Marcos Sponton's structured reading of their public work, built to make Claude or Codex a better thinking partner in the method. If the authors themselves want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Carr and Bryar's public teaching. Especially welcome:

- **New blog posts / podcasts / videos for `author-live-sources.md`** — the firm's blog is now active on a regular cadence (see March 2026 batch); add new posts with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Carr or Bryar has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Carr's or Bryar's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Non-Amazon applications** — the firm has started applying the framework to non-Amazon situations (their Netflix / Warner Bros. blog post is one example). Cases where users successfully applied the mechanisms outside Amazon are valuable.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use PR/FAQs and Input Metrics thinking in my own week and this skill is what falls out.

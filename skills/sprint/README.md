# Sprint — an agent skill

An agent skill for **Jake Knapp's Sprint** — the five-day process for answering critical business questions through design, prototyping, and testing ideas with real customers. Developed at Google Ventures (GV) across 100+ sprints and detailed in the 2016 book *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days* (Simon & Schuster), co-authored with John Zeratsky and Braden Kowitz.

This isn't a summary of the book. **The book is a step-by-step playbook — go read it at [thesprintbook.com](https://www.thesprintbook.com/).** This skill exists to make Claude, Codex, or any agent supporting the SKILL.md standard a working thinking partner *in the method*: deciding whether to sprint, planning the week, running each day's exercises, building a prototype strategy, structuring Friday's customer test, and avoiding the anti-patterns that derail sprints.

Built from:

- **The 2016 book:** *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*, Jake Knapp, John Zeratsky, Braden Kowitz. Simon & Schuster. [thesprintbook.com](https://www.thesprintbook.com/)
- **Post-book adaptations:** Remote Design Sprint (2020, with Jackie Colburn), the 4-day sprint format, and the Miro template.
- **Make Time (2018):** Knapp and Zeratsky's personal productivity book — the daily companion to Sprint's weekly structure.
- **Click: How to Make What People Want (2025):** Knapp and Zeratsky's newest book, introducing the Foundation Sprint — a 2-day method for validating differentiation upstream of the Design Sprint. [character.vc/click](https://www.character.vc/click)
- **Podcast primary sources:** Knapp on [Lenny's Podcast](https://www.lennysnewsletter.com/p/the-foundation-sprint-jake-knapp-and-john-zeratsky) (2025 — Foundation Sprint), [Design Better](https://designbetterpodcast.com/p/jake-knapp-click) (2025 — Click), [Lenny's Podcast](https://www.lennysnewsletter.com/p/making-time-for-what-matters-jake) (2024 — Make Time), and the [Jake & JZ podcast](https://open.spotify.com/show/2uCr5ZcdvFDxFPw4eB95AL).

**Why this exists.** Invoke "Sprint" or "design sprint" in an agent without a skill and you get a reasonable summary — but you lose the specific mechanics that make the method work: the Decider's Supervote, the "work alone then share" anti-brainstorming discipline, the Note-and-Vote silent decision pattern, the Goldilocks-quality prototype facade, and the 5-customer test with the 5-act interview. This skill closes that gap. It also captures the post-book evolution: remote adaptations, the 4-day format, and the Foundation Sprint from *Click* (2025).

## What's inside

```
sprint/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5-day structure: every exercise, role, output
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material after 2016 (remote sprints, Make Time, Click, Foundation Sprint)
│   ├── author-live-sources.md            → index of all live sources (jakeknapp.com, Medium, podcasts, LinkedIn, X)
│   ├── voice-and-tone.md                 → how Knapp actually talks
│   ├── applications.md                   → when to Sprint, when NOT, adjacent frameworks (Design Thinking, Lean Startup, Shape Up, Scrum, CDH)
│   ├── examples.md                       → worked cases (Blue Bottle, Savioke, Slack, Flatiron Health)
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
./scripts/skills.sh install sprint
```

**Option 2 — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/sprint" ~/.claude/skills/sprint
```

**Option 3 — Codex CLI:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/sprint" ~/.codex/skills/sprint
```

For Claude Desktop or another agent that supports SKILL.md, copy or symlink the `sprint/` folder into that tool's skills directory.

Once installed, invoke naturally by describing your situation — the assistant picks the skill up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Sprint skill", "help me plan a sprint", "should we sprint on this?", "walk me through Wednesday's exercises").

## Attribution

**Jake Knapp** — designer, author, and venture partner. Previously built Gmail and Microsoft Encarta, cofounded Google Meet, and created the Design Sprint process at Google. Was a design partner at Google Ventures (GV). Co-founder of Character Capital. Author of *Sprint* (2016), co-author of *Make Time* (2018) and *Click* (2025), all with John Zeratsky.

- **Book:** [Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days](https://www.thesprintbook.com/) (Simon & Schuster, 2016).
- **Author's website:** [jakeknapp.com](https://jakeknapp.com/) · Blog: [jakeknapp.com/posts](https://jakeknapp.com/posts)
- **Character Capital:** [character.vc](https://www.character.vc/) · Click: [character.vc/click](https://www.character.vc/click)
- **GV Sprint page:** [gv.com/sprint](https://www.gv.com/sprint/)
- **Jake Knapp on Lenny's Podcast (2025):** [The Foundation Sprint](https://www.lennysnewsletter.com/p/the-foundation-sprint-jake-knapp-and-john-zeratsky)
- **Jake Knapp on X:** [@jakek](https://twitter.com/jakek) · **LinkedIn:** [linkedin.com/in/jake-knapp](https://www.linkedin.com/in/jake-knapp)

This skill is **not endorsed by Jake Knapp, John Zeratsky, Braden Kowitz, Character Capital, or Google Ventures.** It is Marcos Sponton's structured reading of their public work, built to make the assistant a better thinking partner in the method. If Knapp or his co-authors want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Knapp's ongoing teaching. Especially welcome:

- **New blog posts / podcasts / videos for `author-live-sources.md`** — Knapp publishes on jakeknapp.com, Medium, and the Jake & JZ podcast; add new material with topic + URL.
- **Additional heuristics with attribution** — if Knapp has warned about an anti-pattern not yet in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Knapp's voice is off, tell me. Knapp is practical, friendly, and anti-jargon. Keep it grounded.
- **Failing test cases in `evals/`** — a case where the skill's output is generic or misapplies the method is data.
- **Sprint case studies** — real cases where teams ran sprints and can share what happened.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co).

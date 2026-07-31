# The Fearless Organization — an agent skill

An agent skill for **Amy Edmondson's Fearless Organization** — psychological safety as the belief that the team is safe for interpersonal risk-taking (voice, questions, mistakes, dissent), always paired with high accountability in the 2×2 (Learning Zone / Comfort Zone / Anxiety Zone / Apathy Zone), plus the leader toolkit (Framing → Situational Humility → Curiosity / Structures / Responding Productively) and the *Right Kind of Wrong* (2023) failure taxonomy (Basic / Complex / Intelligent).

This isn't a summary of the book. It's a working thinking partner in Edmondson's method, built from:

- *The Fearless Organization* (Wiley, 2018)
- *Right Kind of Wrong: The Science of Failing Well* (Atria, 2023 — winner of the FT Business Book of the Year)
- *Teaming* (Jossey-Bass, 2012) and *Extreme Teaming* (Emerald, 2017)
- Edmondson's HBR canon since the mid-2000s ("Strategies for Learning from Failure" 2011; "Make It Safe for Employees to Speak Up"; and others)
- The TEDxHGSE talk "Building a Psychologically Safe Workplace" (2014)
- The Fearless Organization Scan tool (fearlessorganizationscan.com) — the productized PSI at individual, team, and enterprise levels
- Podcast appearances including HBR IdeaCast, Freakonomics, Hidden Brain, TED Radio Hour, Coaching for Leaders, Intentional Leader, Armchair Expert, and NeuroLeadership Institute
- The "Psychological Safety ≠ Anything Goes" essay and the Behavioral Scientist piece on the intelligent-failure origin story

**Why this exists.** Invoke "psychological safety" in Claude or Codex without a skill and you get a thin summary of the definition — the model knows the term but not (a) the load-bearing role of accountability in the 2×2, (b) Edmondson's seven-year post-book campaign against the "PS as being nice" misread, (c) the failure taxonomy from *Right Kind of Wrong* (2023) that reframes how leaders respond to failures, (d) the leader toolkit (Framing / Situational Humility / Proactive Inquiry / Structures / Responding Productively), or (e) the specific cases Edmondson uses (Columbia, Boeing, Wells Fargo, Volkswagen, Ford under Mulally, Google Aristotle, Julie Morath, the hospital medication error study, Edison's 10,000 filaments). And critically, it doesn't push back when a user tries to invoke PS as license to lower standards or avoid a hard conversation — which is exactly the failure mode Edmondson spends most of her airtime warning against. This skill closes those gaps.

## What's inside

```
fearless-organization/
├── SKILL.md                              → activation triggers + when-to-use guide + the misread guard
├── README.md                             → this file
├── references/
│   ├── method.md                         → PS definition, 2×2 with accountability, leader toolkit, failure taxonomy — in Edmondson's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns — including the "PS is not being nice" guard
│   ├── post-book.md                      → material Edmondson published after The Fearless Organization (Right Kind of Wrong 2023, PS ≠ anything goes, ongoing HBR)
│   ├── author-live-sources.md            → index of live sources (personal site, HBS, Fearless Organization Scan, HBR archive, LinkedIn, podcasts, TED)
│   ├── voice-and-tone.md                 → how Edmondson actually talks: academic-warm, definitional, case-driven, the intelligent-failure origin story
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Radical Candor, Five Dysfunctions, DORA/Westrum, Radical Transparency, Grove — distinguished)
│   ├── examples.md                       → worked cases (hospital error study, Columbia, Boeing 737 MAX, Wells Fargo, Volkswagen, Google Aristotle, Ford/Mulally, Pixar Braintrust, Julie Morath, Edison)
│   ├── prompts.md                        → invocation templates for common tasks
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

This skill follows the [agent skills](https://agentskills.io/) open standard — it works in Claude Code, Codex CLI, and any other agent that reads SKILL.md.

**Recommended — via [skills.sh](https://github.com/orgs/anthropics/discussions/skills):**

```bash
skills install fearless-organization
```

**Manual — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/fearless-organization" ~/.claude/skills/fearless-organization
```

**Manual — Codex CLI:**

```bash
ln -s "$(pwd)/skills/fearless-organization" ~/.codex/skills/fearless-organization
```

Once installed, invoke naturally by describing your situation — the assistant (Claude or Codex) picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Fearless Organization skill", "help me diagnose why my team has gone quiet", "was this failure blameworthy?").

## The misread guard

Psychological safety is uniquely susceptible to a specific misread: **PS = being nice = comfort = lowering standards.** Edmondson has spent seven years pushing back against this. The 2018 book landed and got adopted at scale — and the version that got adopted at scale, in many orgs, was the caricature. "Safe space" became code for "don't ask hard questions." "Blameless post-mortems" became code for "no one is responsible for anything."

This skill actively resists that failure mode. **Never present psychological safety in isolation. Always pair with accountability. Always show the 2×2 with all four zones named.** The Learning Zone (high PS + high standards) is the goal. The Comfort Zone (high PS + low standards) is exactly what "PS as being nice" produces, and it does not ship anything. The Anxiety Zone (low PS + high standards) is Boeing 737 MAX and Wells Fargo. The Apathy Zone (low PS + low standards) is coast-to-retirement culture.

The 2×2 with accountability is the load-bearing structural device of this skill. Without it, "psychological safety" collapses into whatever the reader already believed about being nice.

## Attribution

**Amy C. Edmondson** — Novartis Professor of Leadership and Management at Harvard Business School (since 1996). PhD in Organizational Behavior (Harvard, 1996). Ranked #1 on the Thinkers50 global ranking of management thinkers (2021, 2023) and #2 (2025). Fellow of the American Academy of Arts and Sciences (2024).

- **Buy the books:** *The Fearless Organization* on [Amazon](https://www.amazon.com/Fearless-Organization-Psychological-Workplace-Innovation/dp/1119477247) · *Right Kind of Wrong* on [Simon & Schuster](https://www.simonandschuster.com/books/Right-Kind-of-Wrong/Amy-C-Edmondson/9781982195069). Read them — this skill points you toward the source, it doesn't replace it.
- **Amy Edmondson's personal site:** [https://amycedmondson.com](https://amycedmondson.com)
- **HBS faculty page:** [https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6451](https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6451)
- **Fearless Organization Scan (PSI tool):** [https://fearlessorganizationscan.com](https://fearlessorganizationscan.com)
- **TEDxHGSE (2014):** [Building a Psychologically Safe Workplace](https://www.youtube.com/watch?v=LhoLuui9gX8)

This skill is **not endorsed by Amy Edmondson.** It is Marcos Sponton's structured reading of her public work, built to make the assistant a better thinking partner in Edmondson's method — and, critically, to resist the "PS as being nice" misread she has spent seven years pushing back against. If Edmondson herself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Edmondson's ongoing writing. Especially welcome:

- **New podcast episodes / essays / talks for `author-live-sources.md`** — Edmondson publishes at a steady cadence via HBR + speaking + podcasts. Add appearances with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Edmondson has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Edmondson's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output presents PS in isolation (without accountability), or lets the "PS as nice" misread through, is data.
- **New cases beyond the recurring roster** — Edmondson has used many cases in podcasts and talks that aren't in `examples.md` yet.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Edmondson's framework in my own team design and this skill is what falls out.

# Demand-Side Sales — an agent skill

An agent skill for **Bob Moesta's demand-side approach** — the Four Forces of Progress, the Switch Interview, the buying timeline, and struggling moments — applied to sales, product, innovation, and career decisions.

This isn't a summary of the book. It's a working thinking partner in Moesta's method, built from:

- **Demand-Side Sales 101** (2020, w/ Greg Engle)
- **Learning to Build: The 5 Bedrock Skills of Innovators and Entrepreneurs** (2022)
- **Job Moves: 9 Steps for Making Progress in Your Career** (2024, w/ Ethan Bernstein + Michael Horn)
- Earlier work with Christensen: **Competing Against Luck** (2016)
- The Re-Wired Group's consulting and coaching programs
- **The Circuit Breaker podcast** (w/ Greg Engle)
- **jobstobedone.org** (w/ Chris Spiek) — 57+ articles, 15+ recorded Switch Interviews, JTBD Radio
- Dense podcast appearances: Lenny Rachitsky (2023, 2025), Intercom, Business of Software (3+ talks), SaaS Club, INDUSTRY 2025, Digestible Deming (2026), Renegade Marketing, Precision Lender
- Bob Moesta's LinkedIn (near-daily during book cycles)

**Why this exists.** Invoke "JTBD" or "Bob Moesta" in Claude or Codex without a skill and you get a thin summary — the model knows the core axiom but rarely brings in the Switch Interview method with its specific micromoves, the buying timeline with its six stages, the asymmetric insight about Anxiety and Habit, the distinction between Moesta's causal-research variant and Ulwick's quantitative ODI, or the post-2020 material from *Learning to Build* and *Job Moves*. This skill closes that gap. Post-book material lives in `references/post-book.md`.

## What's inside

```
demand-side-sales/
├── SKILL.md                  → activation triggers + when-to-use guide
├── README.md                 → this file
├── references/
│   ├── method.md             → Four Forces, Switch Interview, buying timeline, struggling moments
│   ├── heuristics.md         → do's, don'ts, gotchas, interview anti-patterns
│   ├── post-book.md          → Learning to Build (2022), Job Moves (2024), recent appearances
│   ├── author-live-sources.md → Re-Wired Group, jobstobedone.org, Circuit Breaker, podcasts, LinkedIn
│   ├── voice-and-tone.md     → blue-collar-scientist register, Bob-isms, how he teaches and disagrees
│   ├── applications.md       → when to use, when NOT, relationship to Ulwick/Kalbach/Christensen/Torres
│   ├── examples.md           → milkshake, mattress, Casper/ZzzQuil, AutoBooks, SNHU, and more
│   ├── prompts.md            → invocation templates
│   └── sources.md            → complete traceability
├── examples/                 → longer worked examples (community-contributable)
└── evals/                    → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/demand-side-sales" ~/.claude/skills/demand-side-sales

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the demand-side sales skill", "let's map the Forces", "help me plan a Switch Interview", "why aren't people switching?").

## Attribution

**Bob Moesta** — Co-creator of the Jobs to be Done theory (with Clayton Christensen). President & CEO of The Re-Wired Group (Detroit). Builder, practitioner, teacher. Fellow at the Clayton Christensen Institute. Adjunct at Kellogg (Northwestern). Developed 3,500+ products and services. Dyslexic — learned by observation, not by reading, which shaped the entire method.

**Chris Spiek** — co-inventor (with Moesta) of the Forces of Progress diagram and the Switch Interview method. Runs jobstobedone.org.

**Greg Engle** — co-founder of The Re-Wired Group. Co-author of *Demand-Side Sales 101*. Co-host of The Circuit Breaker podcast.

- **Buy Demand-Side Sales 101:** [Amazon](https://www.amazon.com/Demand-Side-Sales-101-Customers-Progress/dp/1544509987). Read it.
- **Buy Learning to Build:** [Amazon](https://www.amazon.com/Learning-Build-Bedrock-Innovators-Entrepreneurs/dp/1544524005). Read this for the innovation lens.
- **Buy Job Moves:** [Amazon](https://www.amazon.com/Job-Moves-Steps-Making-Progress/dp/0063280477). Read this for the career lens.
- **The Re-Wired Group:** [therewiredgroup.com](https://therewiredgroup.com/)
- **JTBD method library:** [jobstobedone.org](https://jobstobedone.org/)
- **The Circuit Breaker podcast:** [therewiredgroup.com/circuit-breaker-podcast/](https://therewiredgroup.com/circuit-breaker-podcast/)

This skill is **not endorsed by Bob Moesta**. It is Marcos Sponton's structured reading of Moesta's public work, built to make Claude or Codex a better thinking partner in Moesta's method. If Moesta himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Moesta's ongoing output. Especially welcome:

- **New podcast appearances for `author-live-sources.md`** — Moesta is highly active on the podcast circuit. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Moesta has explicitly warned about an anti-pattern that isn't captured, add it with source.
- **Voice/tone corrections** — if my read of Moesta's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Cases beyond the recurring roster** — Moesta uses many cases in talks that aren't in `examples.md` yet.
- **Job Moves content** — the nine steps are reconstructed from public coverage, not the book's exact structure. Corrections from the actual text are especially valuable.

## Related skills

- [Challenger Sale](../challenger-sale/) — Matt Dixon's supply-side sales method. Moesta is demand-side (why people buy); Challenger is supply-side (how to sell). They compose: understand the buying timeline (Moesta), then teach/tailor/take-control within it (Challenger).
- [Continuous Discovery Habits](../continuous-discovery-habits/) — Teresa Torres's weekly customer touchpoints. Different unit of analysis (opportunities vs. progress+forces), compatible as an operating cadence alongside periodic Switch Interview deep-dives.
- [Obviously Awesome](../obviously-awesome/) — April Dunford's positioning. Downstream of demand-side understanding: once you know the Forces, positioning becomes precise.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use the demand-side lens in my own sales and product work and this skill is what falls out.

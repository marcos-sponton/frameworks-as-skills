# DORA / Accelerate — an agent skill

An agent skill for **Nicole Forsgren's** research program on measuring software delivery and developer productivity — the four DORA keys, the 30+ capabilities that predict them, the Westrum culture model, and the framework family that has grown from *Accelerate* (2018): **SPACE** (2021), **DevEx** (2023), **DX Core 4** (2024), and *Frictionless* (Dec 2025).

This isn't a summary of *Accelerate*. It's a working thinking partner in Forsgren's evidence-based method, built from:

- *Accelerate: The Science of Lean Software and DevOps* (2018, w/ Jez Humble + Gene Kim) — Shingo Research Award 2019
- Annual *State of DevOps* reports (2014–2024, especially the 2021 addition of Reliability and the 2024 AI findings)
- **SPACE** paper — Forsgren, Storey, Maddila, Zimmermann, Houck, Butler (ACM Queue, 2021)
- **DevEx** paper — Noda, Storey, Forsgren, Greiler (ACM Queue, 2023)
- **DX Core 4** — Tacho + Noda w/ Forsgren, Storey, Zimmermann (2024)
- ***Frictionless*** — Forsgren + Noda (Dec 2025)
- Podcast appearances: Lenny Rachitsky (2023 and 2025), Pragmatic Engineer, Stack Overflow, others
- Live sources: [dora.dev](https://dora.dev/), [getdx.com](https://getdx.com/), Forsgren on LinkedIn

**Why this exists.** Invoke "DORA metrics" in Claude or Codex without a skill and you get the four keys, one paragraph, from the 2018 book — and probably a suggestion to put them on a leaderboard. This skill closes several gaps: the current five-metric model on dora.dev, the tier benchmarks, the 30+ capabilities catalog, the SPACE and DevEx evolution, the 2024 AI-and-delivery findings, the DX Core 4 unification, and — most importantly — the explicit warning that DORA is a team-and-system metric that gets destroyed the moment it's tied to individual performance. Forsgren has said this in writing repeatedly; the model doesn't say it by default.

## What's inside

```
dora-accelerate/
├── SKILL.md                          → activation triggers + when-to-use guide
├── README.md                         → this file
├── references/
│   ├── method.md                     → DORA 5 keys w/ tiers, 30+ capabilities catalog, Westrum, SPACE, DevEx, DX Core 4
│   ├── heuristics.md                 → do's, don'ts, gaming patterns, anti-patterns
│   ├── post-book.md                  → everything since Accelerate 2018 (SPACE, DevEx, AI findings, Frictionless)
│   ├── author-live-sources.md        → dora.dev, getdx.com, Lenny episodes, Pragmatic Engineer, State of DevOps
│   ├── voice-and-tone.md             → how Forsgren actually talks: evidence-first, tier language, warm/cool
│   ├── applications.md               → when to use, when NOT, adjacent frameworks
│   ├── examples.md                   → LinkedIn case, common team scenarios, State of DevOps highlights
│   ├── prompts.md                    → invocation templates
│   └── sources.md                    → complete traceability
└── evals/                            → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths depending on where your agent lives.

```bash
# Claude Code — from this repo root:
ln -s "$(pwd)/skills/dora-accelerate" ~/.claude/skills/dora-accelerate

# Codex CLI:
ln -s "$(pwd)/skills/dora-accelerate" ~/.codex/skills/dora-accelerate

# Claude Desktop or another skill-aware agent: copy the folder into
# your skills directory (path varies by client).
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the DORA skill", "walk me through DORA metrics", "what does Forsgren say about this").

## Attribution

**Nicole Forsgren, PhD** — Management Information Systems. Co-founder of **DORA** (DevOps Research and Assessment) with Jez Humble and Gene Kim; DORA acquired by Google in 2018. VP of Research & Strategy at GitHub (2020); Partner at Microsoft Research (Developer Velocity Lab); currently Senior Director of Developer Intelligence at Google. Advisor and research collaborator at [DX Inc.](https://getdx.com/) Co-author of *Accelerate* (2018), lead author on SPACE (2021), co-author on DevEx (2023), co-author of *Frictionless* (2025).

**Jez Humble** — Co-author of *Accelerate* (2018) and *Continuous Delivery* (2010).
**Gene Kim** — Co-author of *Accelerate* (2018), author of *The Phoenix Project* and *The DevOps Handbook*.

- **Buy *Accelerate*:** [IT Revolution](https://itrevolution.com/product/accelerate/) · [Amazon](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339). Read it — this skill points you at the source, it doesn't replace it.
- **Buy *Frictionless*:** [Amazon](https://www.amazon.com/Frictionless-Remove-Barriers-Outpace-Competition/dp/1662966377) — the 2025 sequel with Abi Noda, focused on the AI era.
- **DORA (Google-hosted):** [https://dora.dev/](https://dora.dev/) — capabilities catalog, Quick Check tool, annual *State of DevOps* reports.
- **DX Inc.** (SPACE / DevEx / DX Core 4): [https://getdx.com/](https://getdx.com/)
- **Nicole Forsgren on LinkedIn:** [/in/nicolefv](https://www.linkedin.com/in/nicolefv/)

This skill is **not endorsed by Nicole Forsgren, Jez Humble, Gene Kim, Abi Noda, or the DORA / DX teams.** It is Marcos Sponton's structured reading of Forsgren's public work, built to make Claude or Codex a better thinking partner in her method. If any of the authors want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the research. Especially welcome:

- **Annual State of DevOps report updates** — the report changes every year (Reliability added 2021, security integrated 2022, AI added 2024). PRs updating `references/method.md` and `references/post-book.md` are the fastest way to keep the skill current.
- **New podcast episodes, essays, or papers** for `author-live-sources.md`.
- **Additional heuristics with attribution** — if Forsgren has warned about an anti-pattern (in writing, in a talk, in a paper) that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Forsgren's register is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Real cases beyond the small roster** — the State of DevOps reports anonymize; if you have a public case with permission to share, it strengthens the skill.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I read *Accelerate* while running an engineering org and this skill is what falls out of returning to it every couple of years as the research keeps evolving.

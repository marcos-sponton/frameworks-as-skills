# 7 Powers — an agent skill

An agent skill for **Hamilton Helmer's 7 Powers** — the taxonomic framework for competitive advantage that names exactly seven conditions capable of producing Persistent Differential Returns.

This isn't a summary of the book. It's a working thinking partner in Helmer's method, built from:

- The 2016 book *7 Powers: The Foundations of Business Strategy* (Deep Strategy LLC)
- Helmer's post-book work at [Strategy Capital](https://strategycapital.com/) (the investing arm)
- Co-research with Chenyi Shi on "Second Invention", platform businesses, and Power Dynamics
- ~8 podcast appearances (Acquired 2020, Acquired *Platforms and Power* 2022, Acquired *Second Business* 2023, Invest Like the Best, 20VC, NFX, Venrock, and [Lenny Rachitsky's Podcast 2024](https://www.lennysnewsletter.com/p/business-strategy-with-hamilton-helmer))
- Trium Group interview with Helmer + Chenyi Shi

**Why this exists.** Invoke "7 Powers" in Claude or Codex without a skill and you get the seven names — often blurred with generic "moat" talk, sometimes mis-mapping network effects to Network Economies, brand recognition to Brand Power, operational excellence to Process Power. This skill closes that gap: strict definitions, the Benefit + Barrier test, the 3 S's screen, and the post-book Statics/Dynamics + three-stage sequencing that most summaries skip. Post-book material lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
7-powers/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 7 Powers in Helmer's own terms + Benefit + Barrier + 3 S's + Dynamics
│   ├── heuristics.md                     → do's, don'ts, gotchas, common misapplications
│   ├── post-book.md                      → Second Invention (with Chenyi Shi), three-stage model, Platforms and Power, AI caveat
│   ├── author-live-sources.md            → index of Helmer's live footprint (podcast-heavy — different shape from Martin's Medium-heavy)
│   ├── voice-and-tone.md                 → how Helmer actually talks
│   ├── applications.md                   → when to use, when NOT, adjacency to Rumelt / Martin / Porter / Buffett
│   ├── examples.md                       → worked cases (Netflix, Vanguard, Pixar, Toyota, Adobe, Amazon, LinkedIn, Facebook, Walmart) + post-book (AWS, Nintendo, Nvidia/CUDA) + third-party applications (TSMC, ASML, Nvidia AI)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/7-powers" ~/.claude/skills/7-powers

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the 7 Powers skill", "run this company through 7 Powers").

## Attribution

**Hamilton Helmer** — economist, strategy consultant (co-founded Helmer & Associates in 1980; later Deep Strategy LLC), longtime Stanford lecturer in strategy, and co-founder of **Strategy Capital**, an investment firm that operationalizes 7 Powers as an investing method. Author of *7 Powers: The Foundations of Business Strategy* (2016).

- **Buy the book:** [Amazon](https://www.amazon.com/7-Powers-Foundations-Business-Strategy/dp/0998116319) · [7powers.com](https://7powers.com/). Read it — this skill points you toward the source, it doesn't replace it.
- **Strategy Capital:** [https://strategycapital.com/](https://strategycapital.com/) — the firm; and the [Media page](https://strategycapital.com/media/) is the canonical index of every Helmer podcast/interview.
- **Helmer on Acquired ("7 Powers")** — [https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer](https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer). The single deepest recorded conversation on the framework.
- **Helmer on Lenny's Podcast (2024)** — [https://www.lennysnewsletter.com/p/business-strategy-with-hamilton-helmer](https://www.lennysnewsletter.com/p/business-strategy-with-hamilton-helmer). Most accessible modern entry point; transcript available.

This skill is **not endorsed by Hamilton Helmer**. It is Marcos Sponton's structured reading of Helmer's public work, built to make Claude or Codex a better thinking partner in Helmer's method. If Helmer himself (or Chenyi Shi at Strategy Capital) wants to correct or endorse anything here, PRs welcome.

## Contributing

Helmer's live footprint is **podcast-heavy, not essay-heavy** — he has no Substack, no Medium, no newsletter, and no regular blog posting cadence. New material shows up as new interviews every ~12–18 months. This makes the skill uniquely dependent on community contributions to stay fresh. Especially welcome:

- **New podcast episodes / talks for `author-live-sources.md`** — when Helmer or Chenyi Shi appear anywhere new, add the episode with a one-line takeaway + URL + date.
- **Second Invention updates** — the Helmer + Chenyi Shi book-in-development is where the biggest new intellectual thread lives. When they publish, this skill needs it.
- **Additional heuristics with attribution** — if Helmer has explicitly warned about a misapplication that isn't in `heuristics.md`, add it with source.
- **Third-party applications** — analysts applying 7 Powers to specific companies (TSMC, ASML, Nvidia AI, etc.) are valuable but must be **tagged as applied** rather than as Helmer's own words.
- **Voice/tone corrections** — if my read of Helmer's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.

## Related skills

- **[Playing to Win (Roger Martin)](../playing-to-win/)** — strategy-*making* cascade. Martin's "how will we win?" question is where 7 Powers lives — Helmer's taxonomy names the seven possible answers with Benefit + Barrier rigor.
- **[Good Strategy Bad Strategy (Richard Rumelt)](../good-strategy-bad-strategy/)** — diagnosis-first. Rumelt tells you the crux; Helmer tells you which Power you're either defending or building toward.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use 7 Powers to stress-test my own bets and this skill is what falls out.

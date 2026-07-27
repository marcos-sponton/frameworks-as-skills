# The Challenger Sale + The JOLT Effect — an agent skill

An agent skill for **Matt Dixon's** two most influential sales frameworks, applied together:

- **The Challenger Sale** (2011, with Brent Adamson) — the 5 rep profiles, the 3 T's (Teach, Tailor, Take Control), and Commercial Insight.
- **The Challenger Customer** (2015) — the 6.8-stakeholder buying group and the Mobilizer taxonomy.
- **The JOLT Effect** (2022, with Ted McKenna) — Judge, Offer, Limit, Take: the antidote to the 40-60% of B2B deals lost to no-decision and customer indecision.

This isn't a summary of the books. It's a working thinking partner in Dixon's method, built from:

- The 2011 book *The Challenger Sale* and the 2015 *Challenger Customer*
- The 2022 *JOLT Effect* (research base: 2.5M+ recorded sales conversations at Tethr)
- 20+ HBR articles including *The End of Solution Sales* (2012), *Dismantling the Sales Machine* (2013), *Stop Losing Sales to Customer Indecision* (2022), *What Today's Rainmakers Do Differently* (2023)
- The 2025 *Activator Advantage* on doer-sellers in professional services
- Podcast appearances: Lenny Rachitsky (2024), 30 Minutes to President's Club, Revenue Builders, HBR IdeaCast, Same Side Selling Academy, others

**Why this exists.** Invoke "Challenger Sale" or "JOLT" in Claude or Codex without a skill and you get a thin summary of the 3 T's and the JOLT letters. The model knows the vocabulary but not: (a) that the research base is 6,000 reps + 2.5M conversations, (b) that Dixon's method is consistently contrarian to relationship-first / delight-the-customer / FOMO-and-close defaults, (c) that Challenger ≠ aggressive selling and JOLT ≠ more pressure, (d) that the Mobilizer vs. Talker distinction is the single most expensive misdiagnosis in complex B2B, and (e) how the two frameworks *together* cover the full deal arc (Challenger earns the meeting; JOLT closes the deal). This skill closes those gaps.

## What's inside

```
challenger-sale/
├── SKILL.md                          → activation triggers + when-to-use guide
├── README.md                         → this file
├── references/
│   ├── method.md                     → 5 rep profiles, 3 T's, Commercial Insight, Mobilizer taxonomy, JOLT
│   ├── heuristics.md                 → do's, don'ts, gotchas, playbooks, anti-patterns
│   ├── post-book.md                  → material after Challenger 2011 (JOLT, Activator, FOMU, AI-and-sales)
│   ├── author-live-sources.md        → DCM Insights, LinkedIn, HBR archive, podcasts
│   ├── voice-and-tone.md             → how Dixon actually sounds (data-first, contrarian, unhedged)
│   ├── applications.md               → when to use, when NOT, adjacent frameworks (Dunford, Moesta, Raskin)
│   ├── examples.md                   → worked cases and diagnostic sequences
│   ├── prompts.md                    → invocation templates
│   └── sources.md                    → complete traceability
├── examples/                         → longer worked examples (community-contributable)
└── evals/                            → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/challenger-sale" ~/.claude/skills/challenger-sale

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Challenger Sale skill", "run this deal through JOLT", "who's my Mobilizer here?").

## Attribution

**Matt Dixon** — founding partner of DCM Insights (The Customer Understanding Lab). Co-author of five sales/CX books with **Brent Adamson**, **Ted McKenna**, and others. Ex-CEB/Gartner Global Sales & Service Research Director. Ph.D., University of Pittsburgh GSPIA.

- **Buy the books:** [Challenger Sale](https://www.amazon.com/Challenger-Sale-Control-Customer-Conversation/dp/1591844355) · [Challenger Customer](https://www.amazon.com/Challenger-Customer-Selling-Influencer-Multiply/dp/1591848156) · [JOLT Effect](https://www.amazon.com/JOLT-Effect-Performers-Overcome-Indecision/dp/0593538102). Read them — this skill points you toward the source, it doesn't replace it.
- **DCM Insights:** [dcminsights.com](https://www.dcminsights.com/)
- **Matt Dixon on LinkedIn** (highest live cadence): [linkedin.com/in/matthewxdixon](https://www.linkedin.com/in/matthewxdixon/)
- **JOLT Effect site:** [jolteffect.com](https://www.jolteffect.com/)
- **HBR archive:** [Matt Dixon on HBR](https://hbr.org/search?term=matthew+dixon)

This skill is **not endorsed by Matt Dixon**. It is Marcos Sponton's structured reading of Dixon's public work, built to make Claude or Codex a better thinking partner in his method. If Dixon himself (or Adamson / McKenna) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the research. Especially welcome:

- **New Dixon essays / podcasts / HBR articles for `author-live-sources.md`.**
- **Additional heuristics with attribution** — if Dixon has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Dixon's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Real deal reviews (anonymized)** — worked examples that show the diagnostic in action.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Challenger + JOLT thinking in Prown's own sales work; this skill is what falls out.

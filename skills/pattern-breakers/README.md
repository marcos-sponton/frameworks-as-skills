# Pattern Breakers — an agent skill

An agent skill for **Mike Maples Jr's Pattern Breakers** — the framework for finding and testing breakthrough startup ideas via **Inflections + Insights + Movements**, with backcasting as the core mindset.

This isn't a summary of the book. It's a working thinking partner in Maples's method, built from:

- The 2024 book *Pattern Breakers: Why Some Start-Ups Change the Future* (with Peter Ziebelman)
- Maples's Medium archive (@m2jr, ~2013–present) and the Pattern Breakers Substack
- The Pattern Breakers podcast (formerly *Starting Greatness*, 2019–present) — interviews with Andreessen, Hoffman, Systrom, Krieger, and many others
- Long-form podcast appearances including Lenny Rachitsky (2024), Guy Kawasaki, Christopher Lochhead, EUVC, Clearer Thinking, Products That Count
- Floodgate essays and public talks (Stanford ETL, Y Combinator, HBS)

**Why this exists.** Invoke "Pattern Breakers" in Claude or Codex without a skill and you get a thin three-word summary (Inflections/Insights/Movements) plus generic startup advice. The model knows the book but not the ~15 years of upstream material Maples has published — Delta 4, Founder-Future Fit, Backcasting, Implementation Prototype (not MVP), Heresy vs. Contrarianism, the Refusal/Heresy/Inflection/Demo stress test. This skill closes that gap. Post-book and pre-book material lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
pattern-breakers/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the three elements + backcasting, in Maples's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → pre-2024 devices (Delta 4, Backcasting, Starting Greatness) + post-2024 material
│   ├── author-live-sources.md            → index of all live sources (Substack, Medium, podcast, Floodgate)
│   ├── voice-and-tone.md                 → how Maples actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (Twitter, Twitch, Lyft, Okta, Airbnb, Tesla, Chegg, Stripe, Figma, Wright Brothers)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths depending on your setup:

**1. Claude Code (macOS/Linux)** — symlink into your user skills directory:

```bash
# From this repo root:
ln -s "$(pwd)/skills/pattern-breakers" ~/.claude/skills/pattern-breakers
```

**2. Codex CLI** — symlink into your Codex skills directory:

```bash
ln -s "$(pwd)/skills/pattern-breakers" ~/.codex/skills/pattern-breakers
```

**3. Any other agent runtime that reads the [SKILL.md open standard](https://agentskills.io/)** — copy or symlink the folder into that runtime's skills directory.

Once installed, invoke naturally by describing your situation — your agent (Claude, Codex, or any SKILL.md-aware assistant) picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Pattern Breakers skill", "run this idea through Inflections/Insights/Movements", "is this a real inflection or just a trend?").

## Attribution

**Mike Maples Jr.** — Co-founding partner of [Floodgate](https://www.floodgate.com/), seed-stage VC firm. Early investor in Twitter, Twitch, Lyft, Okta, Chegg, Outreach, Applied Intuition, and others. Forbes Midas List x8. Host of the [Pattern Breakers podcast](https://greatness.floodgate.com/) (formerly *Starting Greatness*). Co-author with **Peter Ziebelman** (Stanford lecturer, Palo Alto Venture Partners) of *Pattern Breakers: Why Some Start-Ups Change the Future* (Public Affairs, 2024).

- **Buy the book:** [Amazon](https://www.amazon.com/Pattern-Breakers-Start-Ups-Change-Future/dp/1541704355) · [MIT Press Bookstore](https://mitpressbookstore.mit.edu/book/9781541704350). Read it — this skill points you toward the source, it doesn't replace it.
- **Pattern Breakers Substack** (Maples's live essay stream): [https://patternbreakers.substack.com/](https://patternbreakers.substack.com/)
- **Mike Maples Jr on Medium (@m2jr):** [https://medium.com/@m2jr](https://medium.com/@m2jr)
- **Pattern Breakers podcast:** [https://greatness.floodgate.com/](https://greatness.floodgate.com/)
- **Floodgate:** [https://www.floodgate.com/](https://www.floodgate.com/)

This skill is **not endorsed by Mike Maples Jr. or Peter Ziebelman**. It is Marcos Sponton's structured reading of Maples's public work, built to make Claude or Codex a better thinking partner in Maples's method. If Maples himself (or Peter Ziebelman) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Maples's Substack and podcast cadence. Especially welcome:

- **New essays / podcast episodes for `author-live-sources.md`** — Maples publishes on the Pattern Breakers Substack + records new podcast episodes regularly. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Maples has explicitly named an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Maples's voice here is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Cases beyond the recurring roster** — Maples uses many cases in single episodes that aren't in `examples.md` yet (Applied Intuition, Clover, Outreach, and more).

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). Pattern Breakers is one of the frames I use to sanity-check my own bets — this skill is what falls out.

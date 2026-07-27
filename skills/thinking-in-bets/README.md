# Thinking in Bets — a Claude Skill

A Claude Skill for **Annie Duke's decision-making toolkit** — the integrated system across *Thinking in Bets* (2018), *How to Decide* (2020), and *Quit* (2022).

This isn't a summary of the three books. It's a working thinking partner in Duke's method, built from:

- The three books (Portfolio Penguin, 2018 / 2020 / 2022).
- Duke's Substack (~2024–2026) — the live delta on the books.
- The Alliance for Decision Education (its site, podcast, and Decision Education programs — she is co-founder and chair).
- First Round Capital's investment protocol, which she helped design (she is a Special Partner).
- Podcast appearances: Lenny Rachitsky (2024), The Knowledge Project (Shane Parrish, x2), Freakonomics *People I (Mostly) Admire*, First Round Review Podcast, Tim Ferriss, Rational Reminder, Capital Allocators, Jordan Harbinger, Meb Faber.
- YouTube talks: TEDxGeorgetown, SpeakInc keynotes, "Monkeys and Pedestals" clips.

**Why this exists.** Invoke "Thinking in Bets" in Claude without a skill and you get a thin summary of the 2018 book — Claude knows the concept of "resulting" but not the full three-book system, the live Substack material, the First Round protocol, or the specific format of a kill criterion (state + date). This skill closes that gap.

## What's inside

```
thinking-in-bets/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 3 books as one integrated system
│   ├── heuristics.md                     → resulting, calibration, premortem, kill criteria, decision hygiene, biases
│   ├── post-book.md                      → refinements across books + Substack + Alliance + First Round
│   ├── author-live-sources.md            → index of all live sources (Substack, LinkedIn, podcast, YouTube, guest appearances)
│   ├── voice-and-tone.md                 → how Duke actually talks (poker-anecdote-first, signature vocab, phrases she attacks)
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Kahneman, Klein, Tetlock, Rumelt, Duckworth)
│   ├── examples.md                       → worked cases (Pete Carroll, Everest 1996, Butterfield/Slack, Sears, Astro Teller/X, etc.)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/thinking-in-bets" ~/.claude/skills/thinking-in-bets

# Or in Cowork / Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — Claude picks it up when your task matches the triggers in `SKILL.md` (making a decision under uncertainty, running a post-mortem, considering a pivot, setting kill criteria, group decision hygiene), or when you invoke by name ("use the Thinking in Bets skill", "help me think in bets about this").

## Attribution

**Annie Duke** — former professional poker player (WSOP bracelet winner, ~$4M in live tournament earnings), trained cognitive psychologist (Penn PhD ABD under Barbara Mellers). Co-founder and chair of the **Alliance for Decision Education**. Special Partner at **First Round Capital**.

- **Buy the books:**
  - *Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts* (Portfolio, 2018) — [Amazon](https://www.amazon.com/Thinking-Bets-Making-Smarter-Decisions/dp/0735216355). Read this first.
  - *How to Decide: Simple Tools for Making Better Choices* (Portfolio, 2020) — [Amazon](https://www.amazon.com/How-Decide-Simple-Making-Better/dp/0593418484). The toolkit.
  - *Quit: The Power of Knowing When to Walk Away* (Portfolio, 2022) — [Amazon](https://www.amazon.com/Quit-Power-Knowing-When-Walk/dp/0593422996). The counter-force.
- **Personal site:** [annieduke.com](https://www.annieduke.com/)
- **Substack** (~several posts/month, active): [annieduke.substack.com](https://annieduke.substack.com/)
- **Alliance for Decision Education** (she co-founded): [alliancefordecisioneducation.org](https://alliancefordecisioneducation.org/) · **The Decision Education Podcast** (she hosts, Season 5+): [podcasts](https://alliancefordecisioneducation.org/podcasts/)
- **First Round Capital** — Special Partner. She helped design their explicit decision-recording system.
- **LinkedIn:** [annie-duke](https://www.linkedin.com/in/annie-duke/) — reposts, thought pieces, 1–3/week.

This skill is **not endorsed by Annie Duke**. It is Marcos Sponton's structured reading of Duke's public work, built to make Claude a better thinking partner in her method. If Duke herself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the Substack and Alliance material. Especially welcome:

- **New Substack essays / podcast episodes for `author-live-sources.md`** — Duke publishes several posts/month plus hosts the Alliance podcast in seasonal windows. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Duke has explicitly named an anti-pattern or tool that isn't in `heuristics.md`, add it with source.
- **Quote verification** — the research dossier flagged that most quotes came through summary sources. Verifying a quote against the print edition of the book (with page number) is a valuable contribution.
- **Voice/tone corrections** — if my read of Duke's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **New cases** — Duke uses many cases in single podcast episodes or essays that aren't in `examples.md` yet.

## Related skills

- **`playing-to-win`** — Roger Martin's strategy cascade. Complementary: Playing to Win is about *choice-making under competitive uncertainty*; Thinking in Bets is about *decision-making under general uncertainty*. Use Martin to shape the strategic choice; use Duke to evaluate whether the choice you made was good regardless of outcome, and to set kill criteria for the bet.
- **`good-strategy-bad-strategy`** — Rumelt's kernel. Methodological cousin — both attack post-hoc narrative substitutes for real analysis. Rumelt front-loads diagnosis; Duke front-loads separating DQ from OQ. Rumelt's crux is "what's actually hard here?"; Duke's crux is "what does a good decision look like in this uncertainty?".

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Duke's toolkit in my own week and this skill is what falls out.

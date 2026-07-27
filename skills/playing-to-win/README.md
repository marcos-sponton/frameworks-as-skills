# Playing to Win — a Claude Skill

A Claude Skill for **Roger Martin and A.G. Lafley's Playing to Win** — the 5-question integrated cascade for strategy (winning aspiration, where to play, how to win, capabilities, management systems).

This isn't a summary of the book. It's a working thinking partner in Martin's method, built from:

- The 2013 book *Playing to Win: How Strategy Really Works*
- ~260 essays from Martin's Medium *Playing to Win / Practitioner Insights* series (2020–2026)
- HBR articles including *The Big Lie of Strategic Planning* (2014) and *A Plan Is Not a Strategy* (2025)
- Martin's other five books (*The Opposable Mind*, *The Design of Business*, *Fixing the Game*, *Creating Great Choices*, *When More Is Not Better*, *A New Way to Think*)
- Podcast appearances including Lenny Rachitsky (2024)

**Why this exists.** Invoke "Playing to Win" in Claude without a skill and you get a thin summary — Claude knows the book but not the twelve years of refinements Martin has published since. This skill closes that gap. Post-book material lives in `references/post-book.md` and `references/practitioner-insights-index.md`.

## What's inside

```
playing-to-win/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 questions in Martin's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material Martin published after 2013
│   ├── author-live-sources.md            → index of all live sources (Medium, YouTube, archive, podcasts)
│   ├── voice-and-tone.md                 → how Martin actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (P&G/Olay, Vanguard, Southwest, Four Seasons, Westlaw, Tesla, Lego, Dyson, Rotman)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/playing-to-win" ~/.claude/skills/playing-to-win

# Or in Cowork / Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — Claude picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Playing to Win skill", "walk me through the cascade").

## Attribution

**Roger Martin** — Canadian strategy thinker, former dean of the Rotman School of Management (University of Toronto), Thinkers50 #1 (2017), co-author with **A.G. Lafley** of *Playing to Win: How Strategy Really Works* (Harvard Business Review Press, 2013).

- **Buy the book:** [Amazon](https://www.amazon.com/Playing-Win-Strategy-Really-Works/dp/1422187396) · [HBR Store](https://store.hbr.org/product/playing-to-win-how-strategy-really-works/10714). Read it — this skill points you toward the source, it doesn't replace it.
- **Roger Martin's Medium** (~260+ essays, live and growing): [https://rogermartin.medium.com/](https://rogermartin.medium.com/)
- **Roger Martin's Substack:** [https://rogerlmartin.substack.com/](https://rogerlmartin.substack.com/)
- **HBR archive:** [Roger Martin on HBR](https://hbr.org/search?term=roger+martin)

This skill is **not endorsed by Roger Martin**. It is Marcos Sponton's structured reading of Martin's public work, built to make Claude a better thinking partner in Martin's method. If Martin himself (or A.G. Lafley) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the Practitioner Insights series. Especially welcome:

- **New essays / videos / podcast episodes for `author-live-sources.md`** — Martin publishes ~50 essays/year on Medium plus new videos and podcast appearances. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Martin has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Martin's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Cases beyond the recurring roster** — Martin uses many cases in single essays that aren't in `examples.md` yet.

## Skill author

[Marcos Sponton](https://github.com/marcossponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Playing to Win in my own week and this skill is what falls out.

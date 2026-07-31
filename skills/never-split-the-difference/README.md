# Never Split the Difference — an agent skill

An agent skill for **Chris Voss's** Black Swan Method — the tactical-empathy-based negotiation practice taught in:

- *Never Split the Difference: Negotiating As If Your Life Depended On It* (Voss with Tahl Raz, 2016) — the canonical book
- *The Full Fee Agent* (Voss with Steve Shull, 2022) — applied to real-estate fee negotiation
- MasterClass — *Chris Voss Teaches the Art of Negotiation* (18 lessons)
- The Black Swan Group's *Negotiation Mastery Newsletter* (formerly *The Edge*)
- Long-form podcast appearances: Lex Fridman #364 (Mar 2023), Diary of a CEO E147, Jordan Harbinger #165, Impact Theory, Knowledge Project, Modern Wisdom

This isn't a summary of the book. It's a working thinking partner in Voss's method, built to give the assistant the *exact phrasing* the method depends on — mirrors, labels, calibrated questions, the Ackerman 65/85/95/100 sequence, accusation audits, "that's right", no-oriented questions, forced empathy, Black Swans.

**Why this exists.** Invoke "Never Split the Difference" or "Chris Voss" in Claude or Codex without a skill and you get a paraphrased summary: "listen with empathy, ask open questions, don't compromise." The model knows the vocabulary but not: (a) that mirroring means *repeating the last 1–3 words as a question with an upward inflection*, (b) that labels open with *"It seems like…"* or *"It sounds like…"* and never *"I feel that you feel"*, (c) that Ackerman is 65% / 85% / 95% / 100% of target with a non-round final and a non-monetary throw-in, (d) that *"How am I supposed to do that?"* is Voss's canonical forced-empathy line, (e) that "that's right" is the target (not "yes", not "you're right"), and (f) that the single most dangerous misapplication is treating tactical empathy as manipulation. This skill closes those gaps.

## What's inside

```
never-split-the-difference/
├── SKILL.md                          → activation triggers + when-to-use guide
├── README.md                         → this file
├── references/
│   ├── method.md                     → tactical empathy + the nine tools + Ackerman + Black Swans, with scripts
│   ├── heuristics.md                 → do's, don'ts, gotchas, weaponization guard
│   ├── post-book.md                  → material after Never Split the Difference (MasterClass, Full Fee Agent, forced empathy, AI-and-negotiation)
│   ├── author-live-sources.md        → Black Swan Group, newsletter, MasterClass, X, LinkedIn, YouTube, podcasts
│   ├── voice-and-tone.md             → how Voss actually sounds (war-story-first, script-specific, low-and-slow)
│   ├── applications.md               → when to use, when NOT, adjacent frameworks (Challenger Sale, Getting to Yes, Cialdini)
│   ├── examples.md                   → worked cases (Chase Manhattan, Jeff Schilling, salary negotiations, discount defense)
│   ├── prompts.md                    → invocation templates
│   └── sources.md                    → complete traceability
├── examples/                         → longer worked examples (community-contributable)
└── evals/                            → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/never-split-the-difference" ~/.claude/skills/never-split-the-difference

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Voss skill", "run this through Never Split the Difference", "write me an accusation audit for this email", "Ackerman me a target of $50k").

## Attribution

**Chris Voss** — former lead international kidnapping negotiator for the FBI (24 years); founder and CEO of The Black Swan Group; adjunct at Harvard Business School, Georgetown, USC.

- **Buy the books:** [Never Split the Difference](https://www.amazon.com/Never-Split-Difference-Negotiating-Depended/dp/0062407805) · [The Full Fee Agent](https://www.amazon.com/Full-Fee-Agent-Estate-Professional/dp/154454085X). Read them — this skill points you toward the source, it doesn't replace it.
- **The Black Swan Group:** [blackswanltd.com](https://www.blackswanltd.com/)
- **Negotiation Mastery Newsletter:** [blackswanltd.com/newsletter](https://www.blackswanltd.com/newsletter)
- **Chris Voss on MasterClass:** [Teaches the Art of Negotiation](https://www.masterclass.com/classes/chris-voss-teaches-the-art-of-negotiation)
- **Chris Voss on LinkedIn:** [linkedin.com/in/christophervoss](https://www.linkedin.com/in/christophervoss/)

**Name-collision note:** *The Chris Voss Show* podcast (chrisvossshow.com) is a *different person* — an entrepreneur podcaster. Not the FBI negotiator.

This skill is **not endorsed by Chris Voss**. It is Marcos Sponton's structured reading of Voss's public work, built to make Claude or Codex a better thinking partner in his method. If Voss himself (or Brandon Voss, Steve Shull, or Black Swan Group) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the research. Especially welcome:

- **New Black Swan newsletter posts / podcasts / MasterClass updates for `author-live-sources.md`.**
- **Additional heuristics with attribution** — if Voss has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Voss's voice is off (miss the war-story rhythm, over-formal register), tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is generic, thin, or accidentally weaponizes the method is data.
- **Real negotiation cases (anonymized)** — worked examples that show the diagnostic in action.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Voss's method in Prown's own commercial conversations; this skill is what falls out.

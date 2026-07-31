# The Cold Start Problem — an agent skill

An agent skill for **Andrew Chen's Cold Start Problem** — the operational playbook for launching and scaling network products through the 5 stages of network effects (**Cold Start → Tipping Point → Escape Velocity → Hitting the Ceiling → The Moat**), organized around two load-bearing concepts: the **Atomic Network** (the smallest self-sustaining network unit — for Uber it's a single corner at 5pm, not a city) and the **Hard Side vs Easy Side** of a network (drivers vs riders, hosts vs guests, creators vs viewers).

This isn't a summary of the 2021 book. It's a working thinking partner in Chen's method, built from:

- *The Cold Start Problem: How to Start and Scale Network Effects* (Harper Business, 2021) — the anchor text
- Chen's ~650+ essay archive on [andrewchen.com](https://andrewchen.com/) (2007–now)
- Chen's Substack ([andrewchen.substack.com](https://andrewchen.substack.com/)) — where post-book refinements land
- a16z portfolio commentary and podcast appearances (Lenny Rachitsky, Noah Kagan, Intercom, a16z, Future.com, Stripe Atlas, Unsolicited Feedback)
- Chen's first-person Uber tenure (head of Rider Growth, 15M→100M users) — the specific ops-level detail summarizers can't reproduce ("5pm at the Caltrain Station at 5th and King")
- The 2018 *Growth Loops Are the New Funnels* essay Chen co-authored with Brian Balfour, Casey Winters, Kevin Kwok

**Why this exists.** Invoke "The Cold Start Problem" in the assistant without a skill and you get the 5 stage names, an atomic-network-defined-too-big, and a hand-wave about hard-side users. What you don't get is the atomic-network sharpener test (smaller and more specific than you think), the Uber Caltrain-corner example, the Wimdu cherry-picking case, anti-network effects as a **bidirectional** force (kills small networks AND large networks), the come-for-the-tool cosplay anti-pattern, or Chen's post-2021 essays on AI + network effects. This skill closes that gap.

## What's inside

```
cold-start-problem/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 stages, atomic network, hard side, anti-network effects
│   ├── heuristics.md                     → do's, don'ts, gotchas — including the atomic-network sharpener test
│   ├── post-book.md                      → material Chen published AFTER the 2021 book (AI, agents, consumer AI defensibility, gaming/Speedrun)
│   ├── author-live-sources.md            → index of all live sources (andrewchen.com, Substack, a16z, Twitter/X, podcast circuit)
│   ├── voice-and-tone.md                 → how Chen actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (Uber, Airbnb, Tinder, Slack, Dropbox, PayPal, Instagram, Zoom, Facebook, Clubhouse, Wimdu)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths — pick the one that matches your setup.

```bash
# 1. Claude Code (macOS / Linux)
ln -s "$(pwd)/skills/cold-start-problem" ~/.claude/skills/cold-start-problem

# 2. Codex CLI
ln -s "$(pwd)/skills/cold-start-problem" ~/.codex/skills/cold-start-problem

# 3. Any other agent runtime that reads SKILL.md — copy or symlink the folder
#    into its skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Cold Start Problem skill", "sharpen my atomic network", "identify the hard side of this marketplace", "diagnose which of the 5 stages we're in").

## Attribution

**Andrew Chen** — General Partner at [Andreessen Horowitz (a16z)](https://a16z.com/) leading Consumer / games / entertainment / AI and the a16z Speedrun accelerator. Previously head of Rider Growth at Uber (2015–2018). Author of *The Cold Start Problem: How to Start and Scale Network Effects* (Harper Business, 2021) and ~650+ essays on [andrewchen.com](https://andrewchen.com/) and [andrewchen.substack.com](https://andrewchen.substack.com/).

- **Read the source:** [The Cold Start Problem](https://a16z.com/books/the-cold-start-problem/) — the anchor text. This skill points you toward the source, it doesn't replace it.
- **Andrew Chen's personal site:** [https://andrewchen.com/](https://andrewchen.com/)
- **Andrew Chen's Substack:** [https://andrewchen.substack.com/](https://andrewchen.substack.com/)
- **a16z page:** [https://a16z.com/author/andrew-chen/](https://a16z.com/author/andrew-chen/)
- **Twitter/X:** [@andrewchen](https://x.com/andrewchen)

This skill is **not endorsed by Andrew Chen or a16z**. It is Marcos Sponton's structured reading of Chen's public work, built to make the assistant a better thinking partner in Chen's method. If Chen himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Chen's essay output — he publishes to Substack regularly plus a16z posts and podcast appearances. Especially welcome:

- **New essays / podcast episodes for `author-live-sources.md`** — Chen publishes weekly-ish on Substack, plus a16z content and podcast circuit. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Chen has explicitly named an anti-pattern or heuristic (in a Substack essay, tweet, or podcast) that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Chen's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Post-book AI-era material** — Chen's post-2021 Substack essays on AI, agents, and consumer AI defensibility are still landing; new material belongs in `post-book.md`.
- **New case studies** — Chen updates the case roster over time. If he starts citing a new company (or updates a case like Clubhouse's post-hype trajectory), add it to `examples.md`.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Chen's frames when I'm thinking about network-shaped products and this skill is what falls out.

# Four Fits — an agent skill

An agent skill for **Brian Balfour's Four Fits** — the interdependent chain of (Market) Product Fit, Product-Channel Fit, Channel-Model Fit, and Model-Market Fit that any venture-backed company needs to hit $100M+ (any break in the chain kills the business) — plus **Growth Loops** as the compounding, closed-system alternative to funnels.

This isn't a summary of the 2017 essay. It's a working thinking partner in Balfour's method, built from:

- The 2017 essay series *Four Fits For $100M+ Growth* (brianbalfour.com)
- The 2018 Reforge essay *Growth Loops are the New Funnels* (with Casey Winters, Kevin Kwok, Andrew Chen)
- Balfour's live essay archive on brianbalfour.com and Substack (2020–2026)
- The 2024–2025 AI-era reframing (Chegg case, ChatGPT-as-channel argument, unit-economics stress)
- Podcast appearances including [Lenny Rachitsky](https://www.lennysnewsletter.com/) (2023 "10 Lessons" + 2024 "ChatGPT as growth channel")
- Reforge course content themes (Growth Series, Growth Models, Retention & Engagement, PLG)

**Why this exists.** Invoke "Four Fits" in Claude or Codex without a skill and you get the 2017 shape and a paragraph on growth loops. What you don't get is the 2024–2025 AI-era reframing, the ARPU-zone diagnostic, the Model-Market threshold formula, the growth-loop closure test, or Balfour's specific anti-patterns (funnel-in-loop clothing, channel-agnostic strategy, "copy Airbnb's playbook"). This skill closes that gap.

## What's inside

```
four-fits/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the four fits + growth loops in Balfour's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → material Balfour published after the 2017 series (AI-era reframing, universal growth loop, growth machine, ChatGPT-as-channel)
│   ├── author-live-sources.md            → index of all live sources (personal site, Substack, Reforge blog, LinkedIn, podcasts, courses)
│   ├── voice-and-tone.md                 → how Balfour actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → worked cases (HubSpot, Slack, Dropbox, Pinterest, Airbnb, Duolingo, Chegg-as-anti-example, Palantir, Reforge)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths — pick the one that matches your setup.

```bash
# 1. Claude Code (macOS / Linux)
ln -s "$(pwd)/skills/four-fits" ~/.claude/skills/four-fits

# 2. Codex CLI
ln -s "$(pwd)/skills/four-fits" ~/.codex/skills/four-fits

# 3. Any other agent runtime that reads SKILL.md — copy or symlink the folder
#    into its skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Four Fits skill", "diagnose which fit is broken", "help me design a growth loop").

## Attribution

**Brian Balfour** — Founder/CEO of [Reforge](https://www.reforge.com/), ex-VP Growth at HubSpot (2013–2016), co-founder of multiple VC-backed startups. Originator of the Four Fits framework (2017 essay series) and co-originator with Casey Winters, Kevin Kwok, and Andrew Chen of the growth-loops-vs-funnels reframing (Reforge, 2018).

- **Read the source:** the essays are all free — start with [Four Fits For $100M+ Growth](https://brianbalfour.com/four-fits-growth-framework) and [Growth Loops are the New Funnels](https://www.reforge.com/blog/growth-loops). This skill points you toward the source, it doesn't replace it.
- **Brian Balfour's personal site:** [https://brianbalfour.com/](https://brianbalfour.com/)
- **Brian Balfour's Substack:** [https://blog.brianbalfour.com/](https://blog.brianbalfour.com/)
- **Reforge blog:** [https://www.reforge.com/blog](https://www.reforge.com/blog)
- **LinkedIn:** [https://www.linkedin.com/in/bbalfour/](https://www.linkedin.com/in/bbalfour/)

This skill is **not endorsed by Brian Balfour or Reforge**. It is Marcos Sponton's structured reading of Balfour's public work, built to make Claude or Codex a better thinking partner in Balfour's method. If Balfour himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Balfour's essay output — he publishes to Substack and brianbalfour.com regularly. Especially welcome:

- **New essays / videos / podcast episodes for `author-live-sources.md`** — Balfour publishes several essays a year plus podcast appearances. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Balfour has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Balfour's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **AI-era cases** — the 2024–2025 reframing is fresh; new cases of fits breaking (like Chegg) belong in `examples.md`.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Balfour's frames when I'm thinking about my own growth model and this skill is what falls out.

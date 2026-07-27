# Obviously Awesome — an agent skill

An agent skill for **April Dunford's Positioning + Sales Pitch** framework — the 5 components of effective positioning and the 8-step B2B sales pitch that operationalizes it.

This isn't a summary of the books. It's a working thinking partner in Dunford's method, built from:

- The 2019 book *Obviously Awesome: How to Nail Product Positioning* (and its **2026 expanded 2nd edition** — restructured from 10 process steps to 5, with new material on pre-work, multi-product, differentiated value, and market categories in the age of AI)
- The 2023 book *Sales Pitch: How to Craft a Story to Stand Out and Win*
- Dunford's **Substack** (43,000+ subscribers, biweekly cadence in 2026) — the living surface where she refines the framework
- The vault of foundational essays on [aprildunford.com/newsletter](https://www.aprildunford.com/newsletter) (going back to 2017)
- Her podcast [**The Positioning Show**](https://www.positioning.show) — 48 episodes across 3 seasons; Season 3 (2026) is the audio companion to the 2nd edition
- YouTube channel [@positioningshow](https://www.youtube.com/@positioningshow) and standalone Business of Software talks
- Podcast appearances (Lenny Rachitsky 2022 & 2023, Farnam Street Knowledge Project #201, Intercom, SaaS Club, and others)
- The Ambient Strategy site — her consulting practice — [ambientstrategy.com](https://www.ambientstrategy.com/)

**Why this exists.** Invoke "positioning" in Claude or Codex without a skill and you get generic marketing advice — often blurred with branding, messaging, or copywriting (three things Dunford spends most of her airtime separating from positioning). This skill closes that gap. Post-2019 refinements — Sales Pitch, Value vs. Objection Handling, the No Differentiation Illusion, the Multi-Product Guide, Positioning in the Age of AI — live in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
obviously-awesome/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 components + 5-step exercise + 8-step Sales Pitch + multi-product guide
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns, positioning vs. messaging vs. branding
│   ├── post-book.md                      → Sales Pitch (2023), 2026 2nd edition, Substack essays
│   ├── author-live-sources.md            → index of Substack, blog vault, podcast, YouTube, Business of Software talks
│   ├── voice-and-tone.md                 → how Dunford actually talks (warm + blunt)
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Raskin, Porter, Moore, JTBD, Play Bigger)
│   ├── examples.md                       → Janna Systems, Help Scout, Postman, Sampler, Watcom, Segway/Magic Leap, others
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/obviously-awesome" ~/.claude/skills/obviously-awesome

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Obviously Awesome skill", "help me position this using Dunford's method", "let's design the sales pitch").

## Attribution

**April Dunford** — B2B positioning consultant, founder of [Ambient Strategy](https://www.ambientstrategy.com/) (solo boutique). Formerly VP Marketing at Janna Systems, where she repositioned the company from generic "Enterprise CRM" to "CRM for Investment Banks" — growing from <$2M to ~$80M ARR in 18 months, culminating in a $1.3B acquisition by Siebel. Has worked with 300+ technology companies on positioning. Widely regarded as the practitioner reference for B2B positioning today.

- **Buy the books:**
  - [*Obviously Awesome: How to Nail Product Positioning*](https://www.amazon.com/Obviously-Awesome-Product-Positioning-Customers/dp/1999023005) — 2019, expanded 2nd edition 2026. Read it — this skill points you toward the source, it doesn't replace it.
  - [*Sales Pitch: How to Craft a Story to Stand Out and Win*](https://www.amazon.com/Sales-Pitch-Craft-Story-Stand/dp/1999023021) — 2023.
- **April Dunford's Substack (live and growing, biweekly in 2026):** [aprildunford.substack.com](https://aprildunford.substack.com)
- **Foundational blog vault:** [aprildunford.com/newsletter](https://www.aprildunford.com/newsletter)
- **Podcast (The Positioning Show):** [positioning.show](https://www.positioning.show) · YouTube: [@positioningshow](https://www.youtube.com/@positioningshow)
- **Consulting practice:** [Ambient Strategy](https://www.ambientstrategy.com/)
- **LinkedIn:** [/in/aprildunford](https://ca.linkedin.com/in/aprildunford)

This skill is **not endorsed by April Dunford**. It is Marcos Sponton's structured reading of her public work, built to make Claude or Codex a better thinking partner in her method. If Dunford herself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the Substack cadence and each new season of *The Positioning Show*. Especially welcome:

- **New Substack essays / podcast episodes / YouTube videos for `author-live-sources.md`** — Dunford publishes biweekly on Substack plus new podcast episodes and conference talks. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Dunford has explicitly named an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Dunford's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or falls into any of the four confusions (positioning as branding, messaging, tagline, or copywriting) is data.
- **Cases beyond the recurring roster** — Dunford uses many "a client of mine" anonymized examples in the 300-company dataset that aren't in `examples.md` yet.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Obviously Awesome + Sales Pitch on positioning work in my own week and this skill is what falls out.

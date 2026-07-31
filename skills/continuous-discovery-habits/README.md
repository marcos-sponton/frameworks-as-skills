# Continuous Discovery Habits — an agent skill

An agent skill for **Teresa Torres's Continuous Discovery Habits** — the weekly product-trio practice of story-based customer interviews, an Opportunity Solution Tree (Outcome → Opportunities → Solutions → Assumption Tests), and small assumption tests that keeps discovery running as infrastructure rather than a project.

This isn't a summary of the book. It's a working thinking partner in Torres's method, built from:

- *Continuous Discovery Habits* (Product Talk, 2021) — the canonical text; turned 5 in 2026, still running as a monthly book club on Product Talk.
- The **Product Talk essay archive** (2013–present, still active): the canonical [Opportunity Solution Tree essay](https://www.producttalk.org/opportunity-solution-trees/), [Story-Based Customer Interviews](https://www.producttalk.org/2024/04/story-based-customer-interviews/) (Apr 2024), [Assumption Testing](https://www.producttalk.org/assumption-testing/), [Five Types of Assumptions](https://www.producttalk.org/five-types-of-assumptions/), [Defining Product Outcomes: 8 Common Mistakes](https://www.producttalk.org/defining-product-outcomes/), plus 2025–2026 essays on the Product Operating Model, the Interview Coach, Claude Code, and building trustworthy AI in a regulated domain.
- The **All Things Product podcast** (co-hosted with Petra Wille, 2025+) — short episodes with recent themes: Communities of Practice, Quality of Evidence, Taste, Product at Heart 2026, End of Year Reflection 2026.
- Torres's 2022 appearance on Lenny's Podcast — [Teresa Torres on how to interview customers](https://www.lennysnewsletter.com/p/teresa-torres-on-how-to-interview) — one of the densest primary interviews.
- The **Product Talk Academy** (16,000+ students across 102 countries) — where the operational IP lives (Fundamentals, Story-Based Customer Interviews, Assumption Testing, Continuous Interviewing courses).
- **LinkedIn cadence** through 2026 — several posts per week, including the pushback on "one-and-done research" and on being paired with Cagan into doctrine.
- Post-book refinements: adding **"ethical"** as the 5th assumption category, the **Ladder of Evidence**, the **Interview Coach** AI she built for her course in 2025, and her stance on the Product Operating Model debate.

**Why this exists.** Invoke "Continuous Discovery Habits" in Claude or Codex without a skill and you get a decent summary of the 2021 book, but you lose the strict rules: story-based interviewing gets softened into "have a conversation with users", the Opportunity Solution Tree gets treated as a poster instead of a living artifact updated every 3–4 interviews, and the trio (PM + designer + engineer together, weekly, non-negotiable) gets collapsed into "the PM should do more discovery". This skill closes that gap and coaches the assistant to hold the constraints Torres actually holds. Post-book material lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
continuous-discovery-habits/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → 5 habits, OST structure and rules, story-based interviewing, 5 assumption categories, small assumption tests, product trio
│   ├── heuristics.md                     → do's, don'ts, gotchas: 8 outcome mistakes, "solution disguised as opportunity" test, interview anti-patterns (opinion / hypothetical / generalization), tree-without-cadence
│   ├── post-book.md                      → ethical as 5th assumption category, Ladder of Evidence, Interview Coach + AI-discovery work through 2026, position on Cagan's POM, CDH-at-5 book club
│   ├── author-live-sources.md            → index of every place Torres publishes: Product Talk (weekly-ish), All Things Product podcast, LinkedIn, Product Talk Academy, podcast appearances
│   ├── voice-and-tone.md                 → practitioner-teacher voice, diagnostic-before-prescriptive, socratic redirect, warm-but-strict about rules
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Cagan, Perri, Lean Startup, JTBD, OKRs, Design Thinking)
│   ├── examples.md                       → Netflix (pedagogical), CarMax / Spotify / Tesco (named coaching clients), Hertility (AI + discovery), Interview Coach (internal), anonymized composites
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/continuous-discovery-habits" ~/.claude/skills/continuous-discovery-habits

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Continuous Discovery Habits skill", "help me build an Opportunity Solution Tree the Torres way", "audit our interview technique against Torres's rules").

## Attribution

**Teresa Torres** — product discovery coach and founder of Product Talk. Author of *Continuous Discovery Habits: Discover Products That Create Customer Value and Business Value* (Product Talk, 2021). Has taught 16,000+ product professionals across 102 countries through the Product Talk Academy. Coaches teams at CarMax, Spotify, Tesco, and hundreds of startups and enterprises.

- **Buy the book:** *Continuous Discovery Habits* — [Amazon](https://www.amazon.com/Continuous-Discovery-Habits-Discover-Products/dp/1736633309). Read it — this skill points you toward the source, it doesn't replace it.
- **Product Talk (site & essay archive):** [producttalk.org](https://www.producttalk.org)
- **Product Talk Academy (courses):** [learn.producttalk.org](https://learn.producttalk.org) — Fundamentals course, Story-Based Customer Interviews, Assumption Testing, Continuous Interviewing, Opportunity Mapping.
- **All Things Product podcast (co-hosted with Petra Wille):** [Spotify](https://open.spotify.com/show/6ke77wqSgstk3nd048oIGo) · [Apple](https://podcasts.apple.com/us/podcast/all-things-product-with-teresa-and-petra/id1794203808)
- **LinkedIn:** [linkedin.com/in/teresatorres](https://www.linkedin.com/in/teresatorres)

This skill is **not endorsed by Teresa Torres**. It is Marcos Sponton's structured reading of Torres's public work, built to make Claude or Codex a better thinking partner in her method. If Torres herself (or Petra Wille, her *All Things Product* co-host) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Torres's publishing cadence — she publishes roughly weekly across Product Talk essays, podcast episodes, and LinkedIn. Especially welcome:

- **New Product Talk essays for `author-live-sources.md`** — the fastest-decaying part of this skill. Add new essays with topic tag + one-line takeaway + URL.
- **New *All Things Product* podcast episodes** — same schema.
- **Updated "book club" reading guides** — Torres is publishing monthly updates through 2026 as CDH turns 5. Each one is a signal of "here's how I'd revise chapter X now."
- **Additional heuristics with attribution** — if Torres has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source (essay URL, podcast episode, LinkedIn post).
- **Voice/tone corrections** — if the read of Torres's voice is off, tell us.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Case studies** — anonymized real-team stories where the habits worked (or didn't), grounded in a specific method rule.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Torres's method to structure discovery inside my own product organization and this skill is what falls out.

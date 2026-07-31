# The Lean Startup — an agent skill

An agent skill for **Eric Ries's Lean Startup** — the method for building new products or services under conditions of extreme uncertainty via validated learning, Build-Measure-Learn, MVP, pivot-or-persevere, and Innovation Accounting.

This isn't a summary of the 2011 book. Everyone thinks they know Lean Startup. The skill's value is in **nuance** — what Ries actually meant vs. what MVP became in the wild — and in the **post-book material** that most Claude/Codex responses miss.

Built from:

- *The Lean Startup* (Crown, 2011 — NYT bestseller) — the canonical text.
- *The Leader's Guide* (Kickstarter-only, 2016) — the executive companion.
- *The Startup Way* (Currency, 2017) — the enterprise extension. GE, Toyota, Intuit, Pitney Bowes. Growth Board governance. Entrepreneur-as-first-class-role.
- *Incorruptible: Why Good Companies Go Bad… and How Great Companies Stay Great* (Authors Equity, May 2026 — NYT bestseller) — the governance frame around long-term mission-controlled companies. Financial gravity, spiritual holding company, governance-as-product-design.
- **The Eric Ries Show** (2024–present) — the current live source. Long-form guest interviews on growth with purpose and long-term company building.
- **theleanstartup.com** — the 5 principles.
- **news.theleanstartup.com** — the active newsletter.
- **startuplessonslearned.com archive** — the 2008–2015 origin blog. Five Whys, MVP, and Innovation Accounting were introduced there.
- **The 2024 Lenny's Podcast retrospective** — Ries's most substantive 15-year reflection on the movement, misapplications, and what he'd update.
- **The 2026 Incorruptible interview cycle** — Thought Economics, Tech Lead Journal, Rapid Response, Product School, Braden Kelley, Lenny (May 2026).

**Why this exists.** Ask Claude or Codex about "Lean Startup" without a skill and you get a thin summary of the 2011 book's 5 principles — the same summary that has been on Wikipedia for a decade. Claude knows the vocabulary but not the 15 years of subsequent Ries material that: (a) refined it (*The Startup Way* enterprise extension); (b) reframed the governance around it (*Incorruptible*); (c) explicitly pushed back on the degraded misapplications ("fail fast," MVP-as-garbage-v0.1, vanity metrics dressed as OKRs, cargo-cult TPS vocabulary); and (d) engaged honestly with the disagreement with Amazon's Working Backwards on MVP at commitment altitude. This skill closes that gap. Load `references/heuristics.md` first — the aggressive-guard-against-misapplication file is the load-bearing differential.

## What's inside

```
lean-startup/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → 5 principles + operational devices (BML, MVP, pivot-or-persevere with 10 pivot types, Innovation Accounting three levels, engines of growth, small batches, continuous deployment, Five Whys, Andon Cord, Genchi Genbutsu)
│   ├── heuristics.md                     → the 4 misconceptions Ries himself flags + DO's + DON'Ts + gotchas + vocabulary resets (LOAD FIRST when the user shows up with degraded Lean Startup vocabulary)
│   ├── post-book.md                      → The Leader's Guide (2016), The Startup Way (2017 enterprise extension), LTSE (2019), Incorruptible (2026 governance frame), Lenny 2024 retrospective — 15 years of refinement beyond the 2011 book
│   ├── author-live-sources.md            → The Eric Ries Show podcast, newsletter, LinkedIn, all podcast appearances — living index
│   ├── voice-and-tone.md                 → how Ries actually talks: definitional resets, TPS-lineage attributions, IMVU-as-origin-story, self-critical retrospection on the movement's misapplications
│   ├── applications.md                   → when to use, when NOT (Amazon-scale commitments → Working Backwards), adjacent frameworks (Torres, Cagan, Perri, JTBD, Blank, Working Backwards) with the honest disagreement mapped
│   ├── examples.md                       → real cases Ries uses (IMVU, Grockit, Wealthfront, Aardvark, Food on the Table, Zappos, Dropbox with honest nuance, GE FastWorks, Toyota in-dash, Intuit)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability with URLs
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/lean-startup" ~/.claude/skills/lean-startup

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Lean Startup skill", "critique this MVP plan the way Ries would", "audit our metrics for vanity vs actionable").

## Attribution

**Eric Ries** — American entrepreneur; creator of the Lean Startup methodology; founder of IMVU (2004), Long-Term Stock Exchange (LTSE, 2015; SEC-approved 2019), Answer.AI (co-founded with Jeremy Howard), and Virgil (2024). Author of *The Lean Startup* (2011), *The Leader's Guide* (2016), *The Startup Way* (2017), and *Incorruptible* (2026 — NYT bestseller). Host of *The Eric Ries Show* (2024–present).

- **Buy the books:**
  - *The Lean Startup* — [Amazon 0307887898](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898). Read it — this skill points you toward the source, it doesn't replace it.
  - *The Startup Way* — [Amazon 1101903201](https://www.amazon.com/Startup-Way-Companies-Entrepreneurial-Management/dp/1101903201).
  - *Incorruptible* — [Amazon B0FWZZBPZB](https://www.amazon.com/Incorruptible-Good-Companies-Great-Stay/dp/B0FWZZBPZB).
- **theleanstartup.com:** [theleanstartup.com](https://theleanstartup.com/) · [/principles](https://theleanstartup.com/principles)
- **The Eric Ries Show:** [landing](https://ltse.com/the-eric-ries-show) · [Spotify](https://open.spotify.com/show/1PA861kDcuviHDqTi2AmuC) · [Apple](https://podcasts.apple.com/us/podcast/the-eric-ries-show/id1744818044)
- **Newsletter:** [news.theleanstartup.com](https://news.theleanstartup.com/)
- **LinkedIn:** [linkedin.com/in/eries](https://www.linkedin.com/in/eries)
- **LTSE:** [ltse.com](https://ltse.com/) · [Ries's bio page](https://ltse.com/team/eric-n-ries)
- **Legacy blog (2008–2015, dormant but historically canonical):** [startuplessonslearned.com](http://www.startuplessonslearned.com/)

This skill is **not endorsed by Eric Ries**. It is Marcos Sponton's structured reading of Ries's public work, built to make the assistant a better thinking partner in the actual method — not the degraded version most retellings collapse it into. If Ries himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with each new Ries episode, essay, or interview. Especially welcome:

- **New Eric Ries Show episodes for `author-live-sources.md`** — the podcast index is the fastest-decaying part of this skill. Add new episodes with guest + topic + one-line takeaway + URL.
- **New Incorruptible interview appearances** — the 2026 launch cycle is still generating dense material. Add with same schema.
- **New LinkedIn / newsletter essays** — Ries is publishing actively through the Incorruptible cycle. Add when they drop.
- **Additional heuristics with attribution** — if Ries has explicitly warned about a misapplication that isn't in `heuristics.md`, add it with source (episode timestamp, essay URL, LinkedIn post URL).
- **Voice/tone corrections** — if my read of Ries's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or falls into the same misapplications the skill exists to guard against is data.
- **Enterprise case updates for `examples.md`** — GE FastWorks partially unwound after Immelt's departure; Intuit / Pitney Bowes have their own histories; new enterprise adoptions surface regularly. Add when a case is dense enough to teach a pattern.
- **The honest disagreement with Working Backwards** — if you're using both frameworks and have a clean way to describe when each fits, contribute to `applications.md`.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Ries's method — the actual method, not the degraded MVP-as-shipped-garbage version — for testing hypotheses inside Prown and its verticals, and this skill is what falls out.

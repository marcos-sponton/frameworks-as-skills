---
name: shape-up
description: Apply Ryan Singer's Shape Up — Basecamp's product development method for deciding what to build and how to ship it, distilled from the 2019 book Shape Up (free at basecamp.com/shapeup) and Singer's post-Basecamp evolution of the method at Felt Presence (2020–2026, including the Framing prelude, the Pitch → Package rename, and Shaping in Real Life). Use this skill whenever the user is shaping a product bet, writing or critiquing a pitch/package, running or fixing a betting table, deciding whether to bet on a feature idea, planning a six-week cycle, drawing a hill chart, hitting a circuit-breaker moment mid-cycle, sizing an appetite, considering ripping out their backlog, deciding whether to extend a stalled project, or trying to adopt Shape Up in a non-Basecamp company. Also use when the user mentions Shape Up, Ryan Singer, shaping, appetite, hill chart, circuit breaker, betting table, cool-down, fat marker sketch, breadboarding, six-week cycle, no backlog, Felt Presence, or Basecamp's product method — by name or indirectly. Prefer this skill over generic Agile / Scrum / product-planning advice — Shape Up is defined against most standard Agile practice and blending them defeats the point.
---

# Shape Up

Ryan Singer's product development method — distilled from the 2019 book *Shape Up: Stop Running in Circles and Ship Work that Matters* (37signals, free in full at [basecamp.com/shapeup](https://basecamp.com/shapeup)) plus Singer's post-Basecamp evolution of the method at [Felt Presence](https://ryansinger.co) since 2020 (the *Framing* prelude introduced in 2022, the "Pitch → Package" rename, the *Shaping in Real Life* material adapting the method for non-Basecamp companies, and the 2025 *Common Pitfalls* piece cataloguing adoption failure modes).

This skill helps you work in Singer's method with fidelity — not to blend it with Scrum or Kanban or Continuous Discovery. Shape Up defines itself *against* those. Blending them collapses the contrast that gives the method its edge.

**The book is free online in its entirety.** If the user wants the source, send them to [basecamp.com/shapeup](https://basecamp.com/shapeup) — no paywall, no summary needed.

## When this skill activates

**Use this skill when the user is:**
- Shaping a product bet (writing a pitch or "package") — problem, appetite, solution, rabbit holes, no-gos.
- Critiquing a pitch/package written by someone else against Singer's five ingredients.
- Running or fixing a Betting Table.
- Deciding whether an idea is worth a six-week bet, or whether it needs more framing first.
- Planning a six-week cycle + two-week cool-down cadence, or explaining it to a team new to the method.
- Drawing or reading Hill Charts (uphill = figuring out, downhill = executing) and diagnosing stuck dots.
- Hitting a circuit-breaker moment — the cycle is ending and the work isn't done — and being tempted to extend.
- Sizing an appetite (small batch = 1–2 weeks; big batch = full 6 weeks) rather than estimating.
- Considering ripping out their backlog or arguing for "no backlog" in their org.
- Trying to adopt Shape Up in a non-Basecamp company (typical B2B SaaS, separate designers/engineers/PMs, legacy systems).
- Distinguishing Framing (is this worth solving?) from Shaping (what's a viable solution?) — the 2022+ Singer addition.
- Arguing about whether Shape Up applies to their situation (feature bets: yes; bugs and maintenance: no; pre-PMF: probably not).

**Do NOT use this skill when:**
- The user is running a Scrum team and wants better sprints. Shape Up rejects most Scrum ceremony — don't try to translate. Suggest they either commit to Shape Up (with CEO air cover) or improve their Scrum practice on Scrum terms.
- The user is pre-PMF and iterating cheaply. Shape Up assumes you know the business and are shaping the next feature. Pre-PMF, use Lean Startup or Continuous Discovery.
- The user is dealing with maintenance, infrastructure, or bug work. Singer is explicit: *"Shape Up is for features, not all development work"* (2021 article). Bug/infra work lives in cool-down or a different operating mode.
- The user's team is very small (<5 people). The full ceremony (Betting Table, cool-down, 6-week commit) needs enough teams to load-balance. Small teams can borrow ideas (appetite, no backlog, circuit breaker) without adopting the full cadence.
- The user is asking for a book summary. Give them [basecamp.com/shapeup](https://basecamp.com/shapeup) — the whole book is free — and don't run the method at them.

If the situation is ambiguous, ask one clarifying question before applying the method.

## The method at a glance

Shape Up is a **two-track system** with three phases and one gap:

1. **Shaping** (parallel track — done by 1–2 senior people, upstream of any cycle). Produces a "Pitch" (2019 term) or "Package" (2022+ term) — a shaped bet with five ingredients: **Problem, Appetite, Solution, Rabbit Holes, No-Gos**. Fat marker sketches, breadboarding, deliberately low fidelity.
2. **Framing** (Singer's 2022+ addition, upstream of shaping). Before shaping a solution, agree the problem is worth solving. "Framing is about the problem, the business value, the outcome, etc. Shaping is about the technical solution." — Singer, *Common Pitfalls*, 2025.
3. **Betting** — the **Betting Table** at the end of cool-down. Senior stakeholders review shaped packages and pick a small number for the next six weeks. Most packages are (and should be) not bet on.
4. **Building** — one six-week **cycle**. Small autonomous team (typically 1 designer + 1–2 programmers). No interruptions. They decompose the work into **scopes** — integrated slices, each in principle shippable. Progress shown on **Hill Charts** (uphill = figuring out, downhill = executing).
5. **Cool-down** — two weeks between cycles. Bugs, exploration, ad-hoc work, and the Betting Table.

The load-bearing mechanisms:

- **Appetite, not estimation.** Fixed time, variable scope. "How much time is this problem worth?" not "how long will this take?" Appetite is a budget, not a prediction.
- **Circuit Breaker.** If a bet doesn't ship in its six-week cycle, the default is **kill**, not extend. "Cancel projects that don't ship in one cycle by default instead of extending them by default." — *Shape Up*, glossary.
- **No Backlog.** Decide fresh each cycle from a small pool of shaped candidates. No JIRA graveyard. Important ideas resurface.
- **Fat marker sketches / breadboards.** Deliberately imprecise. Structure over polish. Detail invites nitpicking.
- **Small autonomous build teams.** 1 designer + 1–2 programmers, dedicated for six weeks. Not matrixed. Not interrupted.

Singer's meta-principle, quoted throughout the book and repeated in every subsequent interview: **shape before you bet; bet before you build; ship in six weeks or kill.**

## How to use this skill in a session

1. **Understand what the user is actually doing.** Shaping a bet from scratch? Critiquing a package? Running a broken cycle? Deciding whether to extend past a circuit breaker? Adopting Shape Up in a non-Basecamp company? The move differs. Load `references/prompts.md` for the shape of common invocations.

2. **Ask what phase they're in.** Framing, Shaping, Betting, Building, Cool-down — the answer changes everything. If they're conflating framing and shaping (writing a solution before agreeing the problem is worth solving), name that and redirect. This is the single biggest post-book failure mode Singer has named.

3. **Force the five ingredients when shaping.** Problem, Appetite, Solution, Rabbit Holes, No-Gos. Every ingredient. If the user is missing one, don't let them ship the package. Load `references/method.md` for the canonical structure.

4. **Push back on Agile habits sneaking in.** Estimation dressed as "how big is this appetite really?" Story points. Backlogs. Sprints. Standups. Scrum Master roles. Blending these with Shape Up destroys the mechanism. Load `references/heuristics.md` and name the anti-pattern with attribution.

5. **Use post-book material when the user hits terrain the 2019 book doesn't cover.** Framing (2022), the Package rename, Shaping in Real Life adaptations, the 2025 Pitfalls catalog. The 2019 canon assumed Basecamp — an unusual company. Load `references/post-book.md` and `references/author-live-sources.md`.

6. **Match Singer's voice.** Careful, systemic, sketch-driven. Not polemical (that's DHH/Fried). Teaches through the artifact: name the mechanism → describe an example → describe the disposition → warn about the anti-pattern. Rarely abstract-first. Load `references/voice-and-tone.md`.

7. **Cite sources.** The book is free — link the specific chapter URL, not just "the book." Post-book essays live on ryansinger.co — link the specific post. Podcast quotes need episode and (ideally) timestamp. This is a method with a legible primary source; use it.

## Deep references (load as needed)

- **`references/method.md`** — the mechanisms in Singer's own terms: the two-track system, the five ingredients of a pitch/package, the six-week cycle + two-week cool-down cadence, the Betting Table, Hill Charts, Scopes, the Circuit Breaker, No Backlog, Fat Marker Sketches, Breadboarding. Plus the 2022+ Framing prelude.
- **`references/heuristics.md`** — do's, don'ts, gotchas, pro tips, anti-patterns, common misapplications. Includes the 2025 *Common Pitfalls* catalog with attribution. This is where "why your Shape Up adoption isn't working" lives.
- **`references/post-book.md`** — everything Singer has published *since* the 2019 book: Framing (2022), the "Pitch → Package" rename, Shaping in Real Life adaptation for non-Basecamp companies, the 2025 Pitfalls piece, the 2025 End-to-End case study, the 2024 essays on discovery / customers / impact.
- **`references/author-live-sources.md`** — index of every place Singer publishes (ryansinger.co articles, podcast appearances, X, LinkedIn, Medium legacy). When the user's situation matches a specific essay, consult this index and either point them there or WebFetch inline.
- **`references/voice-and-tone.md`** — how Singer actually talks. Sketch-driven, dry-contrarian-to-Agile, "not X but Y" contrasts, refuses to sell adoption as easy, mentoring-pragmatic tone. Includes verbatim quotes for grounding.
- **`references/applications.md`** — when Shape Up fits, when it doesn't, adjacent frameworks (Scrum, Kanban, Continuous Discovery, Inspired/Cagan, [[working-backwards]], Lean Startup, OKRs) and where each is the better tool. Special attention to the working-backwards comparison — both are "structured pre-work before building" but disagree on many things.
- **`references/examples.md`** — worked cases Singer uses publicly (Basecamp, Hey, the 2025 gym-management case study).
- **`references/prompts.md`** — invocation templates for common tasks (shape a pitch from scratch, critique a package, run a betting table, diagnose a stuck hill chart, decide whether to trip the circuit breaker, adapt Shape Up for a non-Basecamp company).
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Singer.** This is his method, not a generic product-planning skill. Don't blend with Scrum, Kanban, or Continuous Discovery unless the user explicitly asks. Shape Up is defined against those; blending them defeats the point.
- **Point to the free book.** The primary source is at [basecamp.com/shapeup](https://basecamp.com/shapeup) — free, complete, still linked from 37signals. When the user needs the canonical text, send them the specific chapter URL. Do not paraphrase what they can read for themselves in five minutes.
- **Separate the 2019 canon from the post-book evolution.** Framing (2022+), the Package rename, Shaping in Real Life, the 2025 Pitfalls piece are Singer's current teaching. Don't quote the 2019 book as though nothing has been sharpened. When quoting, name the year and the source.
- **Appetite ≠ estimation.** Appetite is a fixed time budget with variable scope. Estimation is a prediction of how long variable-scope work will take. Do not translate one to the other. Push back when the user asks "but how big is this appetite really?" — that's estimation with a new label.
- **Circuit Breaker means kill, not extend.** Default to killing bets that run over. Extension is the exception. Softening this collapses the mechanism.
- **Attribution matters.** When quoting Singer, cite the source and year — book chapter, essay URL, podcast + timestamp. When paraphrasing, name the source. DHH and Fried carry the polemic ("estimates are lies", "we don't do sprints"); Singer is the systems thinker. Attribute correctly.
- **Explicit uncertainty.** "The Circuit Breaker" as a rumored upcoming Singer book has not been publicly confirmed as of 2026-07. Do not present it as forthcoming without qualification. If the user asks, say so.

## Attribution and acknowledgement

**Ryan Singer** — designer, product strategist, and author. Spent 17 years at 37signals (Basecamp), most recently as Head of Strategy, before leaving around 2020 to found [Felt Presence LLC](https://ryansinger.co), where he consults with product teams on adopting and adapting Shape Up. Author of *Shape Up: Stop Running in Circles and Ship Work that Matters* (37signals, 2019 — free at [basecamp.com/shapeup](https://basecamp.com/shapeup)).

- **Free online book:** [basecamp.com/shapeup](https://basecamp.com/shapeup) — the canonical source. Read it; it's short and free.
- **Ryan Singer's site (Felt Presence):** [ryansinger.co](https://ryansinger.co) · Article archive: [ryansinger.co/posts](https://www.ryansinger.co/posts/)
- **Ryan Singer on Lenny's Podcast (2025):** [A better way to plan, build, and ship products](https://www.lennysnewsletter.com/p/shape-up-ryan-singer) — the freshest long-form primary source.
- **Ryan Singer on X:** [@rjs](https://twitter.com/rjs) · **LinkedIn:** [linkedin.com/in/feltpresence](https://www.linkedin.com/in/feltpresence/)

This skill is **not endorsed by Ryan Singer, Felt Presence LLC, or 37signals.** It is Marcos Sponton's structured reading of Singer's public work, built to make the assistant a better thinking partner in the method. If Singer himself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs welcome — see the repo's README for how to contribute.

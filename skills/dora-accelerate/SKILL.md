---
name: dora-accelerate
description: Apply Nicole Forsgren's DORA (four-key delivery metrics + capabilities catalog + Westrum culture) research and its evolution into SPACE (2021), DevEx (2023), and DX Core 4 (2024) — the evidence-based measurement stack for software delivery and developer productivity, distilled from *Accelerate* (2018) and Forsgren's continued research at DORA, GitHub, Microsoft Research, DX, and Google. Use this skill whenever the user is measuring engineering performance, benchmarking their team's delivery, arguing about developer productivity, choosing which metrics to instrument, being asked "how do we measure engineering", getting handed a productivity dashboard to critique, hearing "our deploys are slow", talking about deployment frequency, lead time, MTTR, mean time to restore, change failure rate, elite performers, platform engineering, DevEx, developer experience, engineering leadership, State of DevOps report, or mentions Nicole Forsgren, Jez Humble, Gene Kim, Accelerate, DORA, SPACE, DevEx, DX Core 4, or Frictionless (her 2025 book with Abi Noda). Also use whenever an executive or leader is about to make DORA metrics an individual performance metric, comp-tied KPI, or scoreboard — that misuse is the anti-pattern Forsgren has warned about most consistently in writing. Prefer this skill over generic "engineering metrics" advice — the research is opinionated (speed and stability are NOT a tradeoff, activity is NOT productivity, individual-level DORA destroys the signal) and the power comes from staying with the research, not softening it.
---

# DORA / Accelerate — an agent skill

Nicole Forsgren's research program for measuring and improving software delivery and developer productivity — distilled from *Accelerate: The Science of Lean Software and DevOps* (2018, w/ Jez Humble + Gene Kim), the annual *State of DevOps* reports (2014–present), the SPACE paper (ACM Queue, 2021), the DevEx paper (ACM Queue, 2023), the DX Core 4 unification (2024), and *Frictionless* (Dec 2025, w/ Abi Noda).

This skill helps your agent think in Forsgren's evidence-based frame, not just recite the four DORA keys. It is opinionated because the research is opinionated: **speed and stability come together**, **activity is not productivity**, **DORA is a team-and-system metric — never individual**, **culture predicts delivery**, and **friction is the enemy of value**. Softening any of these collapses the method into "engineering KPIs" — which is what teams were doing before Forsgren's research proved most of it was measuring the wrong thing.

## When this skill activates

**Use this skill when the user is:**
- Standing up or overhauling engineering metrics for a team, group, or org.
- Being asked by an executive or board "how do we measure engineering productivity?"
- Benchmarking their team against industry (Elite / High / Medium / Low tiers).
- Diagnosing why delivery feels slow, unstable, or both.
- Debating deployment frequency, lead time, MTTR / recovery time, change failure rate.
- Choosing between DORA, SPACE, DevEx, or DX Core 4 for a specific question.
- Reading or critiquing a productivity dashboard (theirs or a vendor's).
- Considering tying delivery metrics to individual performance reviews or comp — **especially this one**; the assistant should push back before doing anything else.
- Making the case for platform engineering, internal developer platforms, or DevEx investment.
- Onboarding developer-productivity tooling (LinearB, Jellyfish, DX, Swarmia, Faros, etc.).
- Talking about AI-assisted coding and its impact on delivery performance.
- Writing an engineering strategy that needs measurement built in.

**Do NOT use this skill when:**
- The user's real question is compensation design, career ladders, or performance calibration for individuals — DORA is explicitly the wrong tool here. Redirect to appropriate frameworks (competency models, growth frameworks, 360s).
- The user is doing product discovery or PMF search — DORA measures delivery, not whether you're delivering the right thing. Suggest Continuous Discovery / JTBD / Rumelt.
- The user just wants a book summary of *Accelerate*. Give the book link, the four keys in a sentence, and stop.
- The user is asking a pure org-design question with no delivery angle — reach for Team Topologies first, then bring in DORA where it applies.

If the user's situation is ambiguous (e.g., "help me measure my team" — team of what? for what?), ask one clarifying question before instrumenting anything.

## The measurement stack at a glance

Forsgren's frameworks answer different questions. Match the question to the frame before the metric:

- **DORA** (delivery performance, team + system level) — *how fast and how safely does software get from commit to customer?* Four keys plus a fifth stability measure, plus 30+ capabilities that predict where you land.
- **SPACE** (developer productivity, multi-dimensional) — *productivity is not one number; pick 2-3 metrics across at least 3 dimensions.* Explicitly warns against activity-alone measures.
- **DevEx** (developer experience, friction lens) — *what's it like to actually do the work?* Three dimensions: feedback loops, cognitive load, flow state.
- **DX Core 4** (2024 unified prescription) — *if you want the executive-ready synthesis*: Speed, Effectiveness, Quality, Impact.
- **Frictionless** (2025 book, with Abi Noda) — *the seven-step playbook to actually remove the friction the frameworks reveal.*

The most misdiagnosed situation: someone says "measure developer productivity" and gets shown four DORA keys. DORA is *delivery performance*, not productivity. Naming the level (individual / team / system / org) and the question (delivery? experience? productivity? impact?) is half the work.

## The DORA four (now five) keys

**Throughput (speed):**
1. **Deployment Frequency** — how often code goes to production. Elite = on-demand (multiple times per day). Low = less than once per month.
2. **Lead Time for Changes** — commit → production. Elite < 1 day; Low = 1–6 months.

**Stability (quality of the flow):**
3. **Change Failure Rate** — % of deployments that cause a failure requiring intervention. Elite ~ 5%; Low ~ 40%+.
4. **Failed Deployment Recovery Time** (formerly MTTR) — how fast you're back. Elite < 1 hour; Low = 1 week to 1 month.

**Rework (added on dora.dev in the current model):**
5. **Deployment Rework Rate** — unplanned deploys driven by incidents; the "how much stability failure spills back into throughput" signal.

**Reliability** was formally added in 2021 as an operational-outcome dimension adjacent to the four keys.

**Load `references/method.md` for the full definitions, tier tables, and the 30+ capabilities catalog.**

## How to use this skill in a session

1. **Establish the question and the level.** Delivery performance, developer experience, productivity outcomes, business impact? Individual, team, system, or org? The frame determines the frame. Load `references/applications.md` for the decision guide.

2. **Push back on any individual-level framing immediately.** If the user is planning to tie DORA to comp, reviews, or a leaderboard — stop and explain the gaming dynamic (see `references/heuristics.md`). This is the single most-warned-against misuse in the research. Cite: DORA team statement 2023, Forsgren on Lenny 2025.

3. **Use the tier language when appropriate.** Elite / High / Medium / Low are concrete anchors. When the user says "we deploy weekly," you can say "that's the top of Medium; Elite is on-demand." Numbers help. Load `references/method.md` for the tier table.

4. **When the user is stuck at low performance, reach for capabilities before metrics.** DORA metrics are outcomes; the 30+ capabilities are the levers. Cite the specific capability (Trunk-Based Dev, Continuous Delivery, Loosely Coupled Architecture, Generative Culture, Documentation Quality, Test Automation) with attribution.

5. **When the user's question isn't really about delivery, reach for SPACE or DevEx.** "Are our devs happy?" → SPACE Satisfaction. "Why does everything feel slow even though we ship?" → DevEx feedback loops / cognitive load. "Are we shipping the right things?" → not DORA at all; reach for JTBD / Continuous Discovery. Load `references/applications.md`.

6. **When AI enters the conversation, cite the 2024 report finding explicitly.** Devs *feel* faster with AI; team throughput drops slightly and stability drops meaningfully unless small batches + testing rigor are already in place. This is post-book material — most model responses will miss it. Load `references/post-book.md`.

7. **Match Forsgren's voice.** Evidence-first ("our research of X thousand engineers"). Precise on the level (individual vs. team vs. system). Warm about developers, cool about vanity metrics. Not evangelical. Load `references/voice-and-tone.md`.

8. **Cite sources.** Book chapter, State of DevOps year, ACM Queue paper, dora.dev page, podcast episode. Attribution respects the research and lets the user go deeper.

## Non-negotiables

- **DORA is never for individual performance evaluation.** Not in reviews, not in comp, not on a leaderboard. If a user wants to do this, warn first, explain the gaming dynamic, then redirect. This is not the assistant's opinion — it's the explicit position of Forsgren and the DORA team.
- **Speed and stability are not a tradeoff.** They come together, from the same practices. Any framing that says "we're slowing down to be more careful" is misdiagnosis — usually of missing capabilities (test automation, trunk-based dev, small batches).
- **Activity is not productivity.** Commits, PRs, lines of code, story points — all easy to game, none correlate with delivered value in the research. The SPACE paper is emphatic on this; do not let a metric masquerade as productivity because it's easy to count.
- **Perception is not measurement.** The 2024 AI finding is the freshest reminder: devs *felt* faster; the team *shipped* less stably. When the user reasons from feels, reach for signal.
- **Culture is a capability, not a soft factor.** The Westrum model (Pathological / Bureaucratic / Generative) has predictive validity in Forsgren's research. Generative culture correlates with elite delivery.
- **Attribute the research strength.** "DORA has surveyed 39,000+ professionals over a decade" is a real fact; "some studies show" is not. Forsgren's method is data-first — respect it.

## Deep references (load as needed)

- **`references/method.md`** — DORA four (now five) keys with tier tables, the 30+ capabilities catalog, Westrum culture model, SPACE five dimensions, DevEx three dimensions, DX Core 4.
- **`references/heuristics.md`** — do's, don'ts, gotchas, gaming patterns. Anti-patterns Forsgren has explicitly warned about, with attribution.
- **`references/post-book.md`** — everything since *Accelerate* (2018): SPACE, DevEx, DX Core 4, AI findings from the 2024 State of DevOps, platform engineering, *Frictionless* (2025). This is the differential of this skill.
- **`references/author-live-sources.md`** — where Forsgren publishes now: dora.dev, getdx.com, Lenny's podcast episodes, Pragmatic Engineer, State of DevOps reports.
- **`references/voice-and-tone.md`** — how Forsgren actually talks about metrics: evidence-first, tier language, warm-about-devs, cool-about-vanity-metrics.
- **`references/applications.md`** — when DORA fits, when to reach for SPACE or DevEx instead, adjacent frameworks (Team Topologies, Platform Engineering, Continuous Delivery, Lean).
- **`references/examples.md`** — worked cases (LinkedIn Frictionless case, State of DevOps highlights, common team scenarios).
- **`references/prompts.md`** — invocation templates for common tasks.
- **`references/sources.md`** — everything consulted, with links.

## Attribution and acknowledgement

**Nicole Forsgren, PhD** — Co-author of *Accelerate* (2018) with Jez Humble and Gene Kim; co-founder of **DORA** (DevOps Research and Assessment, acquired by Google 2018); Partner at Microsoft Research (Developer Velocity Lab); currently Senior Director of Developer Intelligence at Google. Lead author on the SPACE framework (2021, ACM Queue) and co-author on DevEx (2023, ACM Queue). Co-author of *Frictionless* (Dec 2025) with Abi Noda.

**Jez Humble** — Co-author of *Accelerate* and *Continuous Delivery*.
**Gene Kim** — Co-author of *Accelerate* and *The Phoenix Project*.

- **Book:** [*Accelerate* on IT Revolution](https://itrevolution.com/product/accelerate/) · [Amazon](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339)
- **Book:** [*Frictionless*](https://www.amazon.com/Frictionless-Remove-Barriers-Outpace-Competition/dp/1662966377) (Dec 2025, w/ Abi Noda)
- **DORA (Google-hosted):** [dora.dev](https://dora.dev/) — capabilities catalog, Quick Check tool, annual reports
- **DX Inc.** (where DevEx and DX Core 4 live): [getdx.com](https://getdx.com/)
- **Forsgren on Lenny's Podcast:** [How to measure and improve developer productivity (2023)](https://www.lennysnewsletter.com/p/how-to-measure-and-improve-developer) · [How to measure AI developer productivity (2025)](https://www.lennysnewsletter.com/p/how-to-measure-ai-developer-productivity)

This skill is **not endorsed by Nicole Forsgren, Jez Humble, or Gene Kim.** It is Marcos Sponton's structured reading of Forsgren's public research and writing, built to make Claude or Codex a better thinking partner in the DORA / SPACE / DevEx / DX Core 4 stack. If any of the authors want to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

# DORA / Accelerate — Material posterior al libro

> **This is the differential of this skill.** The 2018 book *Accelerate* named four keys and 24 capabilities. Since then, Nicole Forsgren has:
> - Continued the annual *State of DevOps* research through 2024 (Google → DORA team)
> - Co-authored the **SPACE** framework paper (ACM Queue, 2021)
> - Co-authored the **DevEx** framework paper (ACM Queue, 2023)
> - Collaborated on the **DX Core 4** unification (2024)
> - Published ***Frictionless***, a full second book on the AI era (Dec 2025, w/ Abi Noda)
> - Moved through GitHub → Microsoft Research → DX advising → Google (currently Senior Director of Developer Intelligence)
>
> Most model responses about "DORA metrics" pull from the 2018 book alone. This file captures the 7 years of subsequent research — new capabilities, retired metrics, new findings, whole new frameworks that answer questions DORA doesn't. Organized so you can pull the specific piece you need.

## Refinements and additions in the DORA model itself

### Reliability added (2021)

The 2021 *State of DevOps Report* added **Reliability** as a fifth operational-performance dimension alongside the four throughput/stability keys. Reliability measures whether you meet your own SLOs (availability, latency, performance) day-to-day — not just at deploy time.

Many practitioners still cite "the four keys" as shorthand; the current dora.dev model has five metrics (see `method.md`), and Reliability lives adjacent to them as an operational-outcome measure.

### MTTR renamed to Failed Deployment Recovery Time

The dora.dev site now uses **Failed Deployment Recovery Time** in place of MTTR (Mean Time to Restore). More precise: MTTR conflated multiple things; the current metric is specifically about recovering from a failed deployment. Semantic tightening rather than a substantive change.

### Deployment Rework Rate added

New metric on the current dora.dev model. Captures the % of deployments that are unplanned, driven by an incident — the signal for "instability spilling back into throughput." Not in the 2018 book.

### Security integrated (2022)

The 2022 State of DevOps Report deeply integrated security capabilities — Pervasive Security as a first-class practice, not a bolted-on stage. Elite performers integrated security throughout the SDLC rather than treating it as a gate.

### Documentation Quality identified as under-invested, high-leverage (2023)

The 2023 report identified **Documentation Quality** as one of the highest-leverage capabilities that most orgs under-invest in. This became structurally important in the 2024 AI findings (see below).

### Platform Engineering formalized as capability (2024)

The 2024 report treated platform engineering as a first-class capability worth studying rather than a hot topic. Finding: internal developer platforms correlate with improved individual productivity and team performance, but they can slow throughput and add instability if the platform is not well-run. Investing in platform engineering is not automatically net-positive; it depends on the platform.

### AI capabilities added (2024)

New category in the dora.dev catalog: AI-accessible Internal Data, Clear and Communicated AI Stance, Healthy Data Ecosystems. This category will keep evolving; the 2025 and 2026 reports will refine what actually predicts delivery outcomes in the AI era.

## New material — added after the book

### SPACE — developer productivity as multi-dimensional (2021)

Published in ACM Queue by Forsgren, Storey, Maddila, Zimmermann, Houck, and Butler. Central claim: **developer productivity cannot be captured by a single metric or dimension.** Pick 2–3 metrics from at least 3 dimensions.

The five dimensions:
- **Satisfaction & well-being**
- **Performance** (outcomes, not activity)
- **Activity** (count, warned-against alone)
- **Communication & collaboration**
- **Efficiency & flow**

**Why SPACE matters post-book:** *Accelerate* focused on delivery outcomes at team/system level. SPACE broadens the question to productivity — including well-being, collaboration, flow — at multiple levels. When an exec asks "are our engineers productive?" DORA answers half the question; SPACE answers the fuller one.

**Author's words (paraphrased from the paper):**
> "Productivity has more to do with people than tools. Well-being matters. Beware activity metrics."

**Source:** [The SPACE of Developer Productivity — ACM Queue, 2021](https://queue.acm.org/detail.cfm?id=3454124)

### DevEx — developer experience as friction (2023)

Published in ACM Queue by Noda, Storey, Forsgren, and Greiler. Central claim: developer productivity is downstream of developer experience, and experience has three dimensions worth measuring directly.

The three dimensions:
- **Feedback Loops** — speed and quality of tool/system/people feedback
- **Cognitive Load** — mental effort required to do the work
- **Flow State** — ability to enter and protect focus

Measurement combines **perceptual data** (surveys of the actual devs) with **workflow/system data** (tool telemetry). Both are necessary.

**Why DevEx matters post-book:** DORA measures delivery outcomes. SPACE measures productivity. Neither directly names *what it's like to be the developer doing the work.* DevEx is the friction lens — when the DORA numbers look OK but the team is frustrated, DevEx is the frame that surfaces why.

**Author's words (from the paper):**
> "Developer experience focuses on the lived experience of developers and the points of friction they encounter in their everyday work, and drives business performance through increased efficiency, product quality, and employee retention."

**Source:** [DevEx: What Actually Drives Productivity — ACM Queue, 2023](https://queue.acm.org/detail.cfm?id=3595878) · summary: [getdx.com](https://getdx.com/research/devex-what-actually-drives-productivity/)

### DX Core 4 — the 2024 executive-ready unification

Built by Laura Tacho and Abi Noda at DX Inc., with Forsgren, Storey, and Zimmermann as collaborators. Created because executives kept asking "if we have to pick, what should we actually measure?" — and the honest answer from the research community was "it depends," which didn't work for board decks.

Four dimensions, each with a primary metric and three secondary metrics:

| Dimension | Primary metric | Why |
|---|---|---|
| **Speed** | Diffs (or PRs) per Engineer | Throughput signal — **never for individual eval** |
| **Effectiveness** | Developer Experience Index (DXI) — 14-question survey | Captures what DORA can't see |
| **Quality** | Change Failure Rate | Prevents speed being bought at cost of stability |
| **Impact** | % time on new capabilities | Speed → value, not just activity |

**Why DX Core 4 matters post-book:** it's the first attempt to be prescriptive across the DORA / SPACE / DevEx family. For an exec dashboard, it's the current best synthesis. For deeper work, stay with the individual frameworks at their appropriate level.

**Source:** [Introducing the DX Core 4](https://newsletter.getdx.com/p/introducing-the-dx-core-4) · [getdx.com/research/measuring-developer-productivity-with-the-dx-core-4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/)

### Frictionless — the 2025 book (Forsgren + Noda)

Published December 2025. Central claim: **friction is the bottleneck AI cannot fix.** AI accelerates coding but does not shrink deployment lead time, does not fix flaky tests, does not improve documentation, does not increase deploy frequency. Without friction removal, AI's speed at the keyboard piles up in front of the same slow release pipeline. Result: individual devs feel faster, teams ship less.

Seven-step methodology (see the book for the full treatment):
1. Measure the current baseline (DORA + DevEx)
2. Identify the highest-friction points
3. Prioritize by leverage
4. Instrument the specific friction
5. Ship the friction-removing change in small batches
6. Verify with metrics + developer perception
7. Scale to the next friction

LinkedIn is the flagship case: monthly deploys → multiple deploys per day via systematic friction removal.

Data point cited: **$1.52 trillion / year** in technical-debt cost to US companies, per the book's framing.

**Source:** [Frictionless — Amazon](https://www.amazon.com/Frictionless-Remove-Barriers-Outpace-Competition/dp/1662966377) · [developerexperiencebook.com](https://developerexperiencebook.com/) · [Pragmatic Engineer coverage](https://newsletter.pragmaticengineer.com/p/frictionless-why-great-developer)

## Post-book findings (annual State of DevOps highlights)

### 2019 — Elite doubled

The 2019 report showed Elite performance nearly doubling year-over-year. Practices scale; the capabilities catalog works across industries and org sizes.

### 2021 — Reliability added; SRE integrated

Reliability formalized. SRE practices deeply integrated into the capabilities catalog. Culture emphasis deepened.

### 2022 — Security throughout the SDLC

Pervasive Security as a first-class capability. Security integrated throughout the SDLC (rather than bolted-on gate) correlates with Elite performance. DevSecOps as evolved practice.

### 2023 — Documentation as the under-invested lever

Documentation Quality identified as one of the highest-leverage, most-under-invested capabilities. Teams with strong docs performed measurably better across the four keys.

### 2024 — AI and the productivity paradox

The single most-covered State of DevOps report. Key findings:

- **75% of respondents use AI at work**; a plurality say it makes them more productive.
- **AI adoption correlated with -1.5% delivery throughput and -7.2% delivery stability.**
- **Documentation is the biggest AI leverage** — a 25% increase in AI adoption predicts a 7.5% increase in doc quality (highest of any factor studied).
- **Platform engineering** deeply studied: internal platforms correlate with improved productivity but can slow throughput and add instability if the platform isn't well-run.
- **Trust, communication, and stability** matter more, not less, in the AI era. AI amplifies both good and bad delivery practices.

**Author's words (Forsgren, Lenny's Podcast 2025 — paraphrased):**
> "Devs feel faster with AI. The data on teams shows something more complicated: AI accelerates individual work, but without small batches and testing rigor, that speed doesn't reach production."

**Source:** [DORA 2024 State of DevOps Report](https://dora.dev/research/2024/dora-report/) · [Google Cloud announcement](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) · [DX summary](https://getdx.com/blog/2024-dora-report/)

## Frameworks Forsgren has explicitly warned against or reframed

- **DORA as individual performance metric** — most-warned-against misuse. Team/system only.
- **Activity metrics as productivity** — SPACE paper is explicit; lines of code, commits, story points do not measure productivity.
- **Velocity as productivity** — velocity is a scoping negotiation, not a value signal.
- **10x engineer thesis** — no research support for the size of individual variance the discourse claims.
- **"Speed vs. stability" tradeoff** — the whole point of *Accelerate* is that this tradeoff is false at the level of Elite performance.
- **Measurement-only "improvement"** — measurement without capability investment is theater.
- **SAFe (Scaled Agile Framework)** — DORA research team has been publicly skeptical; process-heavy frameworks correlate with lower delivery performance in the survey data.

## Direct quotes worth having on hand

Quotes from post-book material that crystallize points. Attributed with source where possible.

> "DORA metrics are for measuring and improving the software delivery process. They are not individual performance metrics."
> — DORA team, 2023 (position statement)

> "Productivity cannot be captured by a single metric or dimension."
> — SPACE paper, Forsgren et al., ACM Queue, 2021

> "Developer experience focuses on the lived experience of developers and the points of friction they encounter."
> — DevEx paper, Noda, Storey, Forsgren, Greiler, ACM Queue, 2023

> "You cannot measure your way out of a bad culture."
> — Forsgren, recurring in talks

> "Speed and stability are not a tradeoff. They come together, from the same practices."
> — Accelerate, 2018 (and every subsequent talk)

> "Get better at getting better."
> — dora.dev tagline; recurring in Forsgren framings

> "Devs feel faster with AI; the data shows their teams are shipping less stably."
> — Restatement of the 2024 DORA finding, Forsgren on Lenny 2025 (paraphrased)

> "The DXI is not for individual performance."
> — Introducing DX Core 4, 2024

## Framework compatibility notes

Post-book, Forsgren has been increasingly explicit about how DORA / SPACE / DevEx / DX Core 4 fit together and with adjacent frameworks:

- **Team Topologies (Skelton & Pais)** — sits under DORA capabilities (specifically Loosely Coupled Teams, Loosely Coupled Architecture). Complementary and often cited together.
- **Continuous Delivery (Humble & Farley)** — the technical blueprint behind DORA's technical capabilities. Direct lineage.
- **Lean / Toyota Production System** — intellectual parent. Small batches, WIP limits, pull, flow — all imported from Lean into DORA.
- **Platform Engineering** — emerging capability in the 2024 report; internal developer platforms as a specific capability worth measuring.
- **Cynefin, OODA** — different lens, no conflict.
- **JTBD / Continuous Discovery** — orthogonal. DORA measures delivery; JTBD measures whether you're delivering the right thing. Use both.
- **SAFe** — Forsgren and DORA team publicly skeptical; process weight correlates with lower delivery performance.

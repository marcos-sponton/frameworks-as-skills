# DORA / Accelerate — Method

> The canonical description of the research: the DORA keys, the tier benchmarks, the 30+ capabilities catalog, the Westrum culture model, and the framework family that grew from *Accelerate* (2018) into SPACE (2021), DevEx (2023), and DX Core 4 (2024). Fidelity is the point — Forsgren's method is opinionated, and softening any of it collapses "measure engineering performance" into vanity metrics.

## Core insight (the finding of *Accelerate*)

> "Speed and stability are not a tradeoff. They come together, from the same practices."
> — the central research finding of *Accelerate*, 2018

Elite performers deploy faster AND fail less AND recover quicker. The old belief that "we're slowing down to be safer" is misdiagnosis — usually of missing capabilities (test automation, trunk-based development, small batches, continuous delivery). Elite is not a compromise; it is the coherent outcome of a set of capabilities that reinforce each other.

Any framing of "throughput vs. stability" as a dial you turn is wrong at the level of the research. It is a *system* outcome, not a *positioning* choice.

## The DORA keys — current model (five metrics)

The 2018 book named four. The dora.dev site now organizes them as five, adding an explicit rework signal. Both models are valid — most practitioners still use the four keys as shorthand.

### Throughput (speed of the flow)

**1. Deployment Frequency** — How often do you deploy to production?

**2. Lead Time for Changes** (also: Change Lead Time) — From code committed to code running in production, how long?

### Stability (quality of the flow)

**3. Change Failure Rate** — What percentage of deployments cause a failure requiring immediate intervention (hotfix, rollback)?

**4. Failed Deployment Recovery Time** (formerly: Mean Time to Restore / MTTR) — When a deployment fails, how quickly are you back?

### Rework (added in the current dora.dev model)

**5. Deployment Rework Rate** — What percentage of deploys are unplanned, driven by an incident? The signal for "instability spilling back into throughput."

### Tier benchmarks (approximate; refined each year in the *State of DevOps* report)

| Tier | Deploy Frequency | Lead Time for Changes | Change Failure Rate | Recovery Time |
|---|---|---|---|---|
| **Elite** | On-demand (multiple per day) | < 1 day | ~ 5% | < 1 hour |
| **High** | 1 per day to 1 per week | 1 day – 1 week | ~ 10% | < 1 day |
| **Medium** | 1 per week to 1 per month | 1 week – 1 month | ~ 15–20% | < 1 day |
| **Low** | Less than 1 per month | 1 – 6 months | ~ 40%+ | 1 week – 1 month |

Elite = ~19% of respondents in the 2024 report. The thresholds tighten over time as the industry improves — Elite change-failure-rate was <15% four years ago and is <5% now.

### Reliability (added 2021)

The 2021 *State of DevOps Report* added **Reliability** as an operational-performance dimension alongside the four keys. It captures whether you meet your own SLOs (availability, latency, performance targets). Not a proxy for change failure rate — Reliability is about how the system runs day-to-day, not just what happens right after a deploy.

## The 30+ capabilities (the levers, not the outcomes)

DORA's core contribution beyond the metrics is a **capabilities catalog** — the practices that statistically predict where a team lands on the four keys. Metrics tell you *where you are*; capabilities tell you *what to change*. Never invert this.

Current dora.dev catalog, organized by category:

### Technical capabilities
- Continuous Integration
- Continuous Delivery
- Deployment Automation
- Test Automation
- Test Data Management
- Version Control
- Trunk-Based Development
- Code Maintainability
- Database Change Management
- Monitoring and Observability
- Flexible Infrastructure
- Pervasive Security (DevSecOps)
- Proactive Failure Notification
- Loosely Coupled Architecture

### Process capabilities
- Streamlining Change Approval
- Working in Small Batches
- Work-in-Process (WIP) Limits
- Visibility of Work in the Value Stream
- Visual Management
- Loosely Coupled Teams
- Documentation Quality
- Empowering Teams to Choose Tools

### Cultural / Organizational capabilities
- **Generative Organizational Culture** (Westrum model — see below)
- Transformational Leadership
- Job Satisfaction
- Well-being
- Learning Culture
- Team Experimentation
- Customer Feedback
- User-Centric Focus

### AI-specific (added 2024)
- AI-accessible Internal Data
- Clear and Communicated AI Stance
- Healthy Data Ecosystems
- Platform Engineering (formalized as a capability in the 2024 report)

**Governing principle:** capabilities *predict* delivery performance. You improve the four keys by investing in the capabilities, not by staring at the four keys. Most teams that "want better DORA numbers" are asking the wrong question — the right question is which capability is weakest and worth investing in.

## Westrum organizational culture

Ron Westrum's typology, imported into DORA from aviation and healthcare safety research. Culture predicts information flow, which predicts delivery performance.

| Culture type | How information flows | What happens on failure | What happens with novelty |
|---|---|---|---|
| **Pathological** (power-oriented) | Hoarded, used as ammunition | Blame, scapegoats, cover-up | Crushed |
| **Bureaucratic** (rule-oriented) | Ignored if outside your turf | Investigation of the individual | Problems |
| **Generative** (performance-oriented) | Actively sought | Inquiry, root cause, learning | Implemented |

**Generative culture correlates with Elite delivery performance.** This is not a soft factor; it has predictive validity in the research. Forsgren has said repeatedly: *"You cannot measure your way out of a bad culture."* The culture is a capability — invest in it, don't wallpaper over it.

## DORA Quick Check

Free tool at [dora.dev/quickcheck](https://dora.dev/quickcheck/). Answers a handful of questions and returns your tier estimate plus specific capability recommendations. Useful entry point for teams that don't want to instrument metrics yet — start with the survey, then instrument the capabilities the tool flags.

## SPACE — developer productivity (2021)

Published in ACM Queue by Forsgren, Storey, Maddila, Zimmermann, Houck, and Butler. SPACE's central claim: **developer productivity cannot be captured by a single metric or dimension**. Pick 2–3 metrics from at least 3 dimensions.

### The five dimensions

**S — Satisfaction and well-being.** Are developers fulfilled? Not burned out? Retained? Sample metrics: eNPS, satisfaction surveys, retention rates, burnout indicators. High-leverage, high-honesty when measured well.

**P — Performance.** The outcomes of what developers produce. Not activity — outcomes. Sample metrics: customer satisfaction with the features shipped, reliability of the system, quality of the code (defect escape rate, not lines of code).

**A — Activity.** Counts of actions and outputs. Sample metrics: commits, PRs opened/merged, story points, incidents resolved. **SPACE explicitly warns that activity alone is not productivity** — activity metrics are the easiest to game and the least correlated with delivered value. Include them only alongside other dimensions, never alone.

**C — Communication and collaboration.** How well developers work together, share knowledge, review each other's work. Sample metrics: review quality (not review count), doc discoverability, cross-team dependency management.

**E — Efficiency and flow.** Ability to complete work without interruption. Sample metrics: interruption frequency, uninterrupted focus time, cycle time within a task.

### SPACE core principles (from the paper)

1. **Productivity is multi-dimensional.** No single metric captures it.
2. **Productivity has more to do with people than tools.** Better tools help; better people practices help more.
3. **Well-being matters.** There is a measurable link between developer well-being and delivered performance.
4. **Beware activity metrics.** Lines of code, commits, story points — easy to count, easy to game, uncorrelated with value in isolation.
5. **Individual, team, and system are different levels.** Pick metrics appropriate to the level. Never aggregate individual metrics into a team scoreboard.

### When to use SPACE (over DORA)

Use SPACE when the question is about **productivity**, not delivery. If the exec is asking "are our engineers productive?", DORA answers a narrower question (are they delivering with speed and stability?) — SPACE answers the fuller one (are they satisfied, performing, communicating, and in flow?).

## DevEx — developer experience (2023)

Published in ACM Queue by Noda, Storey, Forsgren, and Greiler. DevEx's central claim: developer productivity is downstream of developer experience, and DevEx has three dimensions worth measuring directly.

### The three dimensions

**1. Feedback Loops.** How fast and how good is the feedback developers get from their tools, systems, and people? Build feedback (CI speed), test feedback (test speed + trustworthiness), review feedback (time-to-first-review), deploy feedback (fast deploys, fast rollback). Fast, trustworthy feedback = fewer context switches, higher confidence.

**2. Cognitive Load.** How much mental effort does it take to get work done? Codebase complexity, documentation quality (or absence), onboarding difficulty, tool fragmentation, unclear ownership. High cognitive load = slow, error-prone work.

**3. Flow State.** Ability to enter and protect uninterrupted focus. Meeting load, interruption frequency, on-call overhead, incident interruptions. Flow is a system property, not a personality trait — you can design for it.

### Measurement approach

DevEx measurement combines **perceptual data** (surveys of the actual devs about their experience) with **workflow/system data** (tool telemetry). Both are needed. Perception alone is subjective; telemetry alone misses what the tools cannot see (frustration, unclear docs, invisible dependencies).

### When to use DevEx (over DORA or SPACE)

Use DevEx when the question is about **friction** — "why does everything feel slow even though we ship?" or "why are engineers frustrated?" or "we're investing in platform engineering, what do we measure?" DORA answers delivery outcomes; DevEx answers what's between the developer and the outcome.

## DX Core 4 — the 2024 unification

Built by Laura Tacho and Abi Noda at DX Inc., with Forsgren, Storey, and Zimmermann as collaborators. The Core 4 exists because executives kept asking "if we have to pick, what should we actually measure?" — and the honest answer from the research community was "it depends," which didn't work.

### The four dimensions

**1. Speed** — Primary metric: **Diffs per Engineer** (or PRs per Engineer). Throughput through the system. **Critical caveat, stated explicitly in the framework: never use this for individual performance evaluation or comp.** Always paired with Effectiveness so speed is not pursued at the cost of experience.

**2. Effectiveness** — Primary metric: **Developer Experience Index (DXI)**, a 14-question survey aggregated into a Likert score. Captures the experiential dimension DORA is silent on.

**3. Quality** — Primary metric: **Change Failure Rate** (from DORA). Prevents speed being bought at the cost of stability.

**4. Impact** — Primary metric: **% of time on new capabilities** (vs. maintenance, tech debt, incident work). Reveals whether all the speed is going into value delivery or just keeping the lights on.

Each dimension has one primary metric and three secondary metrics. The framework is intentionally prescriptive — the point is to answer "what should we actually measure?" without another "it depends."

### When to use DX Core 4

Use DX Core 4 when the user is an **executive** who wants a small, defensible dashboard that touches all four frameworks. It's the synthesis frame. Individual practitioners often benefit from staying with DORA (delivery) or SPACE / DevEx (productivity / experience) at the appropriate level of depth.

## Frictionless (2025)

Forsgren + Abi Noda's Dec 2025 book, focused on the AI era. Central claim: **friction is the bottleneck AI cannot fix.** AI accelerates coding but does not shrink deployment lead time, does not fix flaky tests, does not improve documentation, does not increase deploy frequency. Without friction removal, AI's speed at the keyboard just piles up in front of the same slow release pipeline.

Seven-step methodology (broad shape — see the book for detail):
1. Measure the current baseline (DORA + DevEx)
2. Identify the highest-friction points
3. Prioritize by leverage (which frictions unlock the biggest downstream)
4. Instrument the specific friction
5. Ship the friction-removing change in small batches
6. Verify with metrics + developer perception
7. Scale to the next friction

LinkedIn case: monthly deploys → multiple per day via systematic friction removal.

## The framework family — a map

```
                            NICOLE FORSGREN's research thread
                            ─────────────────────────────────

     2018             2021             2023             2024              2025
   ────────         ────────         ────────         ────────          ────────
   ACCELERATE  →   SPACE       →    DevEx       →    DX Core 4    →    FRICTIONLESS
   (book)          (paper)          (paper)          (framework)       (book)

   DORA keys       5 dimensions    3 dimensions    Speed
   Capabilities    of productivity  of experience  Effectiveness       7-step
   Westrum         (multi-dim)      (friction)     Quality             methodology
   culture                                          Impact              for AI era

   Delivery        Productivity    Experience      Executive-ready    Removal
   performance     multi-lens      friction lens   unification         practice
```

Each frame answers a different question. Match the question first; pick the metric second.

## Sequence of application

1. **Establish the question.** Delivery performance, productivity, developer experience, executive-ready synthesis, or friction removal?
2. **Establish the level.** Individual, team, system, or org? DORA is team/system. SPACE/DevEx work at team level (some at individual — Satisfaction, DevEx-perception). Never aggregate to individual scorecards.
3. **Baseline.** Use the DORA Quick Check for a fast tier estimate. Add SPACE or DevEx if the question extends beyond delivery.
4. **Diagnose which capability is weakest.** Metrics are outcomes; capabilities are the levers. Pick 1–2 capabilities that are both low-current-state and high-leverage for your context.
5. **Invest in the capability, re-measure the metric.** The metric should move; if it doesn't, either the capability wasn't the bottleneck or the investment was superficial.
6. **Iterate.** The next quarter's bottleneck is different from this quarter's.

## What this method is NOT

- **A leaderboard for developers.** DORA is not for individual performance evaluation. Never has been. Never will be. Using it that way destroys the signal within a quarter.
- **A vanity metric replacement.** If your team already had a wall of dashboards no one used, adding DORA to it doesn't help. Prune first.
- **A one-time audit.** The Quick Check is a starting point, not a completion certificate.
- **A substitute for shipping the right thing.** DORA measures delivery, not whether you're delivering the right thing. You can be Elite at shipping the wrong product. For product-fit questions, reach for JTBD / Continuous Discovery / customer research, not DORA.
- **A pretext to buy tools.** The capabilities matter; the tool that instruments the capability is downstream. Don't skip the capability question.

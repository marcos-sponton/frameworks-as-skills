# DORA / Accelerate — Heuristics, Do's, Don'ts, Gotchas

> The practical devices — Forsgren's "how to actually apply this" — that separate using DORA well from doing the thing she has spent most of her airtime warning against. Attribution is precise: this comes from the book, this from a State of DevOps report year, this from a specific Lenny episode.

## Do's

### Measure at the right level

DORA is a **team and system** metric. SPACE has metrics at multiple levels but says explicitly which is which. DevEx is fundamentally at the developer level (perception) plus system level (workflow data). Naming the level before naming the metric is half the work.

**How to apply:** for any metric you're about to instrument, ask "what level is this — individual, team, system, or org?" and "does using it at that level match what the research supports?" If a metric was designed for team level and you're about to use it individually, you've broken the frame.

**Author's words:**
> "DORA metrics are for measuring and improving the software delivery process. They are not individual performance metrics."
> — DORA team, 2023

### Invest in capabilities to move the metrics

DORA metrics are **outcomes**; the 30+ capabilities are the **levers**. Teams that stare at the metrics without investing in the capabilities move nothing.

**How to apply:**
1. Baseline your DORA tier (Quick Check works).
2. Pick the two capabilities that are weakest AND highest-leverage for your context.
3. Invest in those capabilities for a quarter.
4. Re-measure. The metric should move; if it doesn't, either the capability wasn't the bottleneck or the investment was superficial.

**Author's words:**
> "Get better at getting better."
> — dora.dev tagline; recurring in Forsgren talks

### Pair throughput with stability, always

Never look at Deployment Frequency without Change Failure Rate. Never look at Lead Time without Recovery Time. The pairing is the whole point — Elite performers are elite on **all four**, and a team that's fast but unstable is not Elite, it's just fast.

**How to apply:** whenever the org optimizes for one, immediately check the counterpart. Deploy Frequency going up while Change Fail Rate goes up = you're not improving, you're taking on hidden debt.

### Use the tier language as concrete anchors

Elite / High / Medium / Low are numerical benchmarks, not marketing. "We deploy weekly" = top of Medium. "We recover in an hour" = Elite on recovery. This precision beats "we're pretty fast" every time.

**How to apply:** when the user reports a rate, translate to a tier and name the neighboring tiers. "You're High on deploy frequency (once a day); Elite would be multiple per day, Medium would be once a week." Concrete, non-judgmental, actionable.

### Start with the Quick Check

Free tool at [dora.dev/quickcheck](https://dora.dev/quickcheck/). Answers a handful of survey questions and returns tier + specific capability recommendations. Perfect for a team that doesn't have instrumentation yet — the survey is a valid baseline while you set up telemetry.

### Use SPACE when the question is broader than delivery

If the exec is asking "are our engineers productive?" — DORA answers a narrower question. SPACE answers the broader one. Pick 2–3 metrics from at least 3 dimensions, always including one from Satisfaction or Well-being.

**Author's words:**
> "Productivity cannot be captured by a single metric or dimension."
> — SPACE paper, 2021

### Use DevEx when the question is "why does it feel slow"

DORA outcomes look fine but the team is frustrated? Reach for DevEx. Feedback loops, cognitive load, flow state — each names a specific friction that DORA doesn't see. Pair perceptual surveys with system telemetry.

### Reach for capabilities before tools

When a team wants to "improve DORA," don't start with a tool purchase. Start with the capabilities catalog. Which capability is weakest? Trunk-Based Development? Test Automation? Documentation Quality? Generative Culture? The capability is upstream of the tool.

**Author's words:**
> "You cannot measure your way out of a bad culture."
> — Forsgren, recurring in talks

### Cite the research strength

DORA has surveyed 39,000+ professionals over 10+ years. That's the largest and longest-running research program of its kind. When you invoke a DORA finding, saying so grounds it — this is not vibes.

### Small batches, always

The single most repeated technical recommendation across the entire DORA research program. Small batches → faster feedback → faster learning → more stability. Every capability compounds off this.

## Don'ts

### Don't tie DORA to individual performance reviews

This is the most-warned-against misuse. The DORA team has said it in writing (2023 statement, dora.dev, multiple Forsgren talks). Every subsequent framework (SPACE, DevEx, DX Core 4) has repeated the warning about its own primary metrics.

**Why it fails:** the moment DORA becomes a leaderboard, developers start optimizing the number, not the outcome. Deploy Frequency inflates via artificially small commits. Lead Time drops via rushed reviews. Change Fail Rate stays low because risky changes get avoided. You've destroyed the signal within a quarter.

**Author's words:**
> "DORA metrics were never designed to be a scoreboard for individual teams... the moment you tie DORA metrics to individual performance reviews, you've destroyed their value."
> — DORA team + community consensus, restated repeatedly

**How to redirect:** for individual performance evaluation, use a competency framework or growth ladder — not delivery metrics.

### Don't measure activity and call it productivity

Lines of code, commits, PRs opened, story points, hours logged — all easy to count, all game-able, none of them predict delivered value. The SPACE paper is emphatic on this.

**Author's words:**
> "Beware activity metrics — they are the easiest to game and the least correlated with delivered value."
> — SPACE paper, 2021 (paraphrased)

**How to redirect:** if a leader wants an activity metric, pair it with a Satisfaction, Performance, or Efficiency metric so activity alone can't be optimized for.

### Don't reason from perception when you can reason from signal

The 2024 State of DevOps AI finding is the freshest reminder. 75% of developers said AI made them more productive. Team throughput actually dropped 1.5% and stability dropped 7.2%. Individual perception is a real signal — but it is not delivery signal.

**Author's words:**
> "Devs feel faster with AI; the data shows their teams are shipping less stably."
> — DORA 2024 report finding, restated by Forsgren in Lenny 2025

**How to redirect:** when the user reports perception ("the team feels overloaded" / "we're moving so fast"), name it as perception and ask what signal would confirm or contradict it.

### Don't accept "speed vs. stability" as a real tradeoff

The whole research program has one central finding: Elite performers are elite on both. Any framing of "we're going to slow down to stabilize" is misdiagnosis. Usually the missing capability is small batches, test automation, or trunk-based development.

**Author's words:**
> "Speed and stability are not a tradeoff."
> — Accelerate, 2018

**How to redirect:** ask "what specific capability is missing that makes speed and stability seem to trade off?" Almost always: manual testing, long-lived branches, big-bang deploys, weak monitoring.

### Don't skip Reliability

Added to the DORA model in 2021 and consistently underused. Change Failure Rate captures deploy-time failure; Reliability captures day-to-day operational performance against your own SLOs. Both matter.

### Don't put DORA on a leaderboard between teams

Even at team level — teams solving different problems shouldn't be ranked by DORA. Team A ships a checkout page; Team B ships a compliance workflow with real deploy risk. Ranking them by Deploy Frequency measures the problem, not the team.

**How to redirect:** each team benchmarks against itself over time (are we improving?) and against tier norms (are we roughly Elite / High / Medium / Low?), not against each other.

### Don't buy the tool before naming the capability

Vendors sell dashboards. Dashboards are not capabilities. If your team has weak Test Automation, no dashboard fixes that; buying Jellyfish or LinearB or Faros before investing in the underlying capability just gives you a prettier view of the same problem.

### Don't skip developer surveys

DORA has survey-based components. SPACE has survey-based components. DevEx is heavily survey-based (perception is a first-class signal). Instrumentation-only measurement misses what the tools cannot see.

### Don't confuse frameworks

DORA is delivery performance. SPACE is productivity. DevEx is developer experience. DX Core 4 is executive-ready synthesis. If the user reaches for "DORA" when the question is "are our devs frustrated," redirect to DevEx — not because DORA is wrong, because it's the wrong frame for that question.

## Gotchas (things that go wrong even when you think you're doing it right)

### The instrumentation trap

You spend a quarter setting up telemetry to measure the four keys precisely — and never actually invest in the capabilities that would move them. The Quick Check is deliberately low-effort so this doesn't happen. Perfect measurement of an un-improved system is theater.

### The single-metric collapse

An exec asks for "one number." Someone gives them Deployment Frequency alone. Six months later, Deploy Frequency is up and Change Fail Rate has doubled. Never present one DORA metric without at least one from the other pair.

### The framework-shopping problem

Team adopts DORA, doesn't like the numbers, adopts SPACE, doesn't like those either, then adopts DevEx. Framework churn without capability investment. The frames aren't the problem — reach for capabilities.

### The vanity retreat

When DORA numbers don't move, some teams quietly redefine what counts as a "deploy" or what counts as a "failure" to make the numbers look better. Definitional drift is metric death. Lock definitions and version them.

### The AI-era over-attribution

2024–2025 gets attributed a lot of things it didn't cause. AI increased individual felt productivity; it did not shrink team throughput. If leadership is celebrating an AI-driven improvement, check the actual DORA numbers before believing the celebration.

### Perception without signal (and signal without perception)

Perception without signal: "we feel productive" while shipping nothing. Signal without perception: DORA numbers look great but the team is burning out. Both are broken. SPACE and DevEx exist to close both gaps.

## Pro tips (accelerators — small devices that punch above their weight)

### The pairing rule

Always present metrics in pairs: throughput + stability, activity + satisfaction, speed + quality. Any single metric is game-able; a pair is much harder to game without hurting the other.

### The "what changed" question

When a DORA metric moves, always ask what capability changed. If nothing changed, the movement is noise. If something changed, name it — that's the causal story for the next investment.

### Team benchmarks against itself, not against Elite

An honest question: "are we improving?" — not "are we Elite?" Elite is the destination; improvement is the direction. Teams that measure their own quarter-over-quarter movement move faster than teams that measure their gap to Elite.

### The Documentation lever (surprisingly high)

DORA research repeatedly identifies Documentation Quality as one of the most under-invested, highest-leverage capabilities. 2024 report: if AI adoption increases by 25%, projected doc-quality gain is 7.5% — the highest of any factor. Boring; powerful.

### Small batches, small batches, small batches

Every capability compounds off this. Nothing else works if batch size is large. Trunk-Based Development is essentially "keep batches small." Continuous Integration is "verify small batches continuously." Working in Small Batches is a first-class capability in the catalog.

### Take the Quick Check quarterly

Not annually. Quarterly. It's fast enough that a team can do it without ceremony. Trends over 4 quarters beat point-in-time comparisons.

### Read the current State of DevOps report

Every year, in full. The research evolves. The current picture beats last year's picture. The 2024 report is essential reading if you're navigating AI + delivery.

## Anti-patterns (the "bad measurement" Forsgren explicitly names)

### DORA as individual performance metric

**What it looks like:** dashboards ranking developers by Deploy Frequency or Lead Time. Metrics tied to comp or reviews.
**Why it fails:** destroys the signal; game-able within a quarter.
**Author's words:**
> "DORA metrics are for measuring and improving the software delivery process. They are not individual performance metrics."
**How to redirect:** use a competency framework for individual evaluation; keep DORA at team/system level.

### Lines of code as productivity

**What it looks like:** measuring output by LOC written; ranking devs by commits.
**Why it fails:** longer code is often worse code; refactoring reduces LOC while improving quality; game-able trivially.
**Author's words:** attacked repeatedly across Forsgren's work; SPACE names it explicitly as a warned-against activity metric.
**How to redirect:** measure Performance (outcomes) or Efficiency (flow), not Activity alone.

### 10x engineer

**What it looks like:** hiring / promoting / paying based on the "10x engineer" thesis.
**Why it fails:** no research support. Team-level and system-level factors dominate individual variance in the research.
**How to redirect:** measure team capabilities and generative culture; individual variance is real but smaller than the discourse suggests.

### Velocity as productivity

**What it looks like:** team ranked / measured by story points completed per sprint.
**Why it fails:** velocity is a scoping negotiation, not output. Story points inflate via story-shrinking or estimate-padding.
**How to redirect:** DORA delivery metrics or SPACE Performance dimension.

### "AI made us N% faster" celebration

**What it looks like:** leadership celebrates AI-driven productivity gains without checking downstream delivery signal.
**Why it fails:** 2024 DORA data — individual felt productivity ↑, team throughput ↓ 1.5%, stability ↓ 7.2%.
**How to redirect:** check the four keys before celebrating; celebrate the delivery signal, not the perception.

### Framework theater

**What it looks like:** the org adopts DORA (or SPACE, or DevEx), publishes a dashboard, and nothing changes about how work is done.
**Why it fails:** measurement without investment is theater.
**How to redirect:** every dashboard should have a paired capability investment; if the org doesn't have one, defer the dashboard.

### Buy-the-tool substitution

**What it looks like:** the "DORA improvement plan" is "we're evaluating LinearB / Jellyfish / Swarmia / Faros."
**Why it fails:** tools measure; they don't improve.
**How to redirect:** name the capability you're investing in; then choose the tool that best supports that specific investment.

## Language and vocabulary — say this, not that

Small phrasing shifts that come out of the research.

| Instead of | Use | Because |
|---|---|---|
| Developer productivity (loosely) | Delivery performance (DORA) / Productivity (SPACE) / Experience (DevEx) | Different questions need different frames |
| Lines of code | Change Failure Rate / Lead Time / Code Maintainability | LOC is anti-signal |
| Velocity | Deployment Frequency, Lead Time | Velocity is scoping, not output |
| MTTR | Failed Deployment Recovery Time | dora.dev's current formulation is more precise |
| Individual performance dashboard | Team baseline + individual growth framework | DORA is team/system, not individual |
| "We're going to slow down to stabilize" | "We're going to invest in [test automation / small batches / trunk-based dev]" | Names the actual capability |
| "The team feels productive" | "The team perceives high productivity; delivery signal is [X]" | Perception ≠ measurement |
| Best practices | Capabilities with predictive validity | The research names specific practices |
| Ninja / rockstar / 10x | Team performance with generative culture | Individual heroics don't scale |
| "AI made us faster" | "AI accelerated coding; delivery throughput [moved / did not move]" | 2024 finding: they diverge |

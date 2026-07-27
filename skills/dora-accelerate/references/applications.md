# DORA / Accelerate — Applications

> When DORA fits, when it doesn't, and what to reach for instead. The Forsgren research family has grown into a small stack — DORA, SPACE, DevEx, DX Core 4 — precisely because different questions need different frames. This file is the decision guide.

## Situations where DORA fits well

- **Standing up delivery-performance measurement for the first time.** DORA is the mature, evidence-based starting point. Start with the Quick Check.
- **Benchmarking a team against the industry.** Elite / High / Medium / Low tiers give concrete anchors.
- **Diagnosing why delivery feels slow or unstable.** The four keys triangulate the problem; the capabilities catalog names the levers.
- **Making the case for platform engineering, CI/CD investment, test automation.** DORA capabilities have predictive validity — the case writes itself if you baseline first.
- **Post-incident reflection.** Change Failure Rate and Recovery Time land the conversation on the right dimensions.
- **Executive reporting on engineering delivery** — provided leadership understands the metrics are team/system, not individual.
- **Improving delivery in the AI era.** The 2024 report finding on AI + delivery is fresh, cited, and central to the conversation right now.
- **DevOps / SRE transformation** with an evidence base — DORA is the underlying research.

## Situations where DORA does NOT fit (reach for SPACE, DevEx, or something else)

- **Individual performance evaluation, promotion, or compensation decisions.** DORA is the wrong tool. Use a competency framework, growth ladder, or 360. Forsgren has been explicit: DORA metrics tied to individuals destroys the signal.

- **"Are our engineers happy / productive / staying?"** — SPACE is a better frame. Include Satisfaction and Well-being explicitly. DORA doesn't measure this.

- **"Why does everything feel slow even though we ship OK?"** — DevEx is the right lens. Feedback loops, cognitive load, flow state.

- **Product-market-fit search.** DORA measures delivery, not whether you're delivering the right thing. Elite delivery of the wrong product is possible and common. Reach for Continuous Discovery, JTBD, or lean startup frames.

- **Team of one, or very small team (< 3 devs).** DORA metrics are noisy at very small n. The Quick Check still helps directionally; the specific numbers less so.

- **Pure organizational-design or hiring question.** Reach for Team Topologies (which is a DORA-compatible capability layer) or general org-design frameworks. Bring DORA in downstream.

- **Compensation design or career ladder work.** DORA is not the frame. Explicit anti-fit.

- **When the user just wants a summary of *Accelerate*.** Give the book link and the four keys in a sentence. Don't stand up an instrumentation plan.

## Decision guide — which framework for which question

| The user's question is really about... | Reach for... | Why |
|---|---|---|
| Delivery speed and stability | **DORA** | Its native question |
| Multi-dimensional developer productivity | **SPACE** | Explicitly designed for it |
| Developer friction and experience | **DevEx** | The friction lens (feedback loops, cognitive load, flow) |
| Executive-ready synthesis metric | **DX Core 4** | 2024 unification, prescriptive |
| Removing friction to unlock value in AI era | **Frictionless (2025)** | Practical seven-step methodology |
| Individual performance evaluation | Competency framework / growth ladder | DORA explicitly wrong here |
| Are we shipping the right thing? | JTBD / Continuous Discovery | DORA measures delivery, not fit |
| Org design / team boundaries | Team Topologies (Skelton & Pais) | Compatible; DORA capabilities include Loosely Coupled Teams |
| Product strategy | Playing to Win (Martin) / Good Strategy Bad Strategy (Rumelt) | Different domain entirely |
| Pricing / monetization | Monetizing Innovation (Ramanujam) | Different domain |
| Incident post-mortem culture | SRE / blameless post-mortem practices | Complementary to DORA culture capabilities |

## Adjacent frameworks — how they compose with DORA

### Team Topologies (Skelton & Pais)
Sits *under* DORA as an org-design layer. Two of DORA's capabilities — **Loosely Coupled Teams** and **Loosely Coupled Architecture** — are direct Team Topologies territory. Use Team Topologies to structure teams and their interaction modes; use DORA to measure whether the delivery is actually improving.

### Continuous Delivery (Humble & Farley, 2010)
The technical blueprint behind most of DORA's technical capabilities. Direct lineage — Jez Humble co-authored both *Continuous Delivery* and *Accelerate*. If the user's question is "how do we actually build the pipeline," *Continuous Delivery* is the manual; DORA is the measurement.

### Lean / Toyota Production System
DORA's intellectual parent. Small batches, WIP limits, pull, flow — all imported from Lean. If the user is coming from a manufacturing or Lean background, DORA reads as familiar; if they're not, the connection to Lean helps ground why small batches matter.

### Platform Engineering
Emerging capability in the 2024 report; internal developer platforms as a specific practice worth measuring. If the user is building a platform team, DORA (delivery performance of platform consumers) + DevEx (developer experience of platform consumers) + SPACE (productivity of platform consumers) is the measurement stack. DX Core 4 is the executive rollup.

### SRE (Site Reliability Engineering)
Google's operational model; Reliability as a first-class discipline. DORA integrated Reliability formally in 2021. Compatible and mutually reinforcing — SRE gives you the operational practices, DORA measures the outcomes.

### JTBD / Continuous Discovery / Product Discovery
Orthogonal to DORA. DORA measures delivery; JTBD measures whether you're delivering the right thing. Use both — a team can be Elite at shipping the wrong product. If the user's real question is "are we building the right thing?" reach for JTBD, not DORA.

### Cynefin, OODA loops
Different lens; no conflict. Useful when the user's situation is high-uncertainty and DORA's incremental-improvement framing feels wrong for the moment.

## Adjacent frameworks — where compatibility is limited or contested

### SAFe (Scaled Agile Framework)
Publicly skeptical position. DORA research consistently shows that process-heavy frameworks correlate with *lower* delivery performance. If the user has SAFe and wants better DORA numbers, the honest conversation is that SAFe practices (long PI planning cycles, heavy ceremonies, coordinated releases) often work against the DORA capabilities (small batches, trunk-based, continuous delivery).

### Traditional PMO / stage-gate governance
Structurally incompatible with high delivery performance. Change approval boards, mandatory review gates, and stage-gate processes correlate with lower DORA performance. DORA's **Streamlining Change Approval** capability is essentially the negative of stage-gate governance.

### Vanity metrics vendors
There's a whole vendor market for engineering dashboards that instrument LOC, commits, PR counts, and other activity metrics. If the user is evaluating one of these, the honest question is: what capability does this tool actually help you invest in? If the answer is "just visibility," the tool is measurement without improvement — DORA warns against this.

## When to use SPACE (specifically) over DORA

- The question is broader than delivery outcomes ("are our engineers productive/satisfied/growing?").
- You need to include developer well-being as a first-class signal.
- You want to measure at multiple levels (individual satisfaction + team communication + system efficiency).
- You need to counterbalance an activity-metric obsession — SPACE explicitly warns against activity alone.
- Board or exec team is asking about "developer productivity" and DORA feels too narrow.

## When to use DevEx (specifically) over DORA or SPACE

- The delivery metrics look fine but the team is frustrated.
- You're investing in platform engineering or internal developer platforms.
- You need to instrument specific friction (slow CI, bad docs, meeting load).
- You want perceptual data alongside system data.
- You're preparing to write *Frictionless*-style improvement (7-step methodology).

## When to use DX Core 4 (specifically)

- Executive audience that needs a small, defensible dashboard.
- You want prescriptive metric choice ("what should we actually measure?") without another "it depends."
- You already have DORA + DevEx running and need the exec rollup.
- You want the framework family unified — Speed / Effectiveness / Quality / Impact.

## Frameworks Forsgren has effectively killed (from her research position)

- **DORA as individual performance metric** — explicitly warned against, in writing, repeatedly.
- **Lines of code as productivity metric** — SPACE names it as anti-signal.
- **Velocity (story points) as productivity metric** — same.
- **"10x engineer" as measurement basis** — no research support.
- **Speed vs. stability as tradeoff** — the whole finding of *Accelerate* refutes it.
- **Measurement-only improvement** — measurement without capability investment is theater.

If the user invokes any of these expecting them to work, redirect gently but clearly.

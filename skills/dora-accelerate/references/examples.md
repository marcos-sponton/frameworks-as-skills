# DORA / Accelerate — Worked examples

> Cases and scenarios that Forsgren, DORA reports, or the DORA / DX / SPACE / DevEx community have used publicly to illustrate the frameworks. Each case names the source so the user can verify. Structured so you can pull the case that matches the user's situation.
>
> **Note on the case set.** DORA is based on survey data from thousands of anonymized organizations, so the public case library is smaller than for author-centric frameworks. Where a specific company is named publicly (LinkedIn in *Frictionless*, others in DX customer stories, some in *Accelerate*), it's noted. Otherwise the "cases" are archetypal scenarios drawn from patterns in the research.

## Case index by situation

| If the user is working on... | Reach for... |
|---|---|
| Removing friction to unlock deploy frequency | **LinkedIn** (Frictionless case) |
| Moving from monthly to daily deploys | **LinkedIn**, generic *State of DevOps* scenario |
| Enterprise DevOps transformation | **Capital One** (widely cited) |
| Elite delivery at massive scale | **Google**, **Netflix**, **Amazon** (State of DevOps references) |
| Diagnosing why fast teams are unstable | Generic "Low → Medium recovery" scenario |
| First-time DORA baseline | Generic "Team starts at Medium" scenario |
| AI adoption without stability loss | 2024 State of DevOps AI paradox scenario |
| Platform engineering investment ROI | 2024 State of DevOps Platform Engineering finding |
| Docs as under-invested lever | 2023 State of DevOps Documentation finding |

## LinkedIn — friction removal at scale (Frictionless, 2025)

**Where Forsgren uses it:** *Frictionless* (2025), Forsgren + Noda; press coverage of the book launch.

**The situation:** LinkedIn's engineering org shifted from monthly deployment cadence to multiple deploys per day through systematic friction removal.

**How the case is instructive:**
- Baseline: Low tier on Deployment Frequency (monthly).
- Bottleneck: not tooling capability — the pipeline could technically deploy faster; the friction was in review gates, environment provisioning, test flakiness, and coordination overhead.
- Intervention: apply the 7-step Frictionless methodology — baseline DORA + DevEx, identify highest-friction points, prioritize by leverage, instrument the specific friction, ship in small batches, verify, repeat.
- Outcome: Elite-adjacent on Deploy Frequency.

**Why the case is instructive:** it demonstrates the *Frictionless* thesis that AI accelerates coding but does not shrink the release pipeline. LinkedIn's transformation was pre-heavy-AI-adoption and shows the friction-removal work as its own domain.

**Quotable framing (from book coverage):**
> "AI's promise of speed becomes bottleneck nightmares when friction remains in the release pipeline."

**Source:** [Frictionless — Amazon](https://www.amazon.com/Frictionless-Remove-Barriers-Outpace-Competition/dp/1662966377) · [Pragmatic Engineer coverage](https://newsletter.pragmaticengineer.com/p/frictionless-why-great-developer)

---

## Capital One — enterprise DORA adoption

**Where it appears:** *Accelerate* references; State of DevOps reports; DevOps Enterprise Summit case studies.

**The situation:** Capital One was one of the early large-enterprise adopters of DevOps / DORA practices in the mid-2010s. Public-cloud migration, trunk-based development, automated compliance, high deploy frequency at bank scale.

**How the cascade applied:**
- Massive capability investment: CI/CD, deployment automation, monitoring, test automation.
- Cultural investment: generative culture, transformational leadership, learning culture.
- Automated compliance and security integrated into pipelines (later a State of DevOps 2022 emphasis).

**Why the case is instructive:** counters the "we can't do DORA at our regulated scale" objection. If a bank can be near-Elite on delivery, few enterprise objections hold.

---

## Netflix, Amazon, Google — the ambient Elite reference

**Where it appears:** *Accelerate* introduction; recurring reference across State of DevOps reports.

**The situation:** these companies operate at Elite tier natively — Netflix's chaos engineering, Amazon's two-pizza teams and API-first mandate, Google's SRE model.

**Why they are instructive:** they demonstrate the ceiling of what's achievable. Also: they demonstrate that the capabilities are not the exclusive property of big-tech. The research consistently shows the *practices* generalize across industries, org sizes, and regulatory contexts.

**Caution:** Elite is not a target most orgs should adopt wholesale. The 2024 report shows Elite = 19% of respondents; targeting Elite when currently Low usually means investing in the wrong capability. Better to be honest about the current tier and improve to the next.

---

## The "Fast but Unstable" archetypal scenario

**The situation:** team is deploying daily (High on Deploy Frequency), but Change Failure Rate is 30% (Medium) and Recovery Time is 12 hours (Medium). Leadership sees the deploy frequency and celebrates; developers are stressed by incidents.

**How the cascade applies:**
- Diagnosis: the throughput/stability pair is broken. Fast throughput without stability is not Elite; it's just fast.
- Capability check: usually one or more of — insufficient Test Automation, no Trunk-Based Development, weak Monitoring & Observability, missing Small Batches practice.
- Intervention: invest in the weakest capability. Re-measure in 6-8 weeks.

**Why the scenario is instructive:** it's the most common diagnostic pattern. Teams see Deploy Frequency going up and assume they're improving; the pair check reveals they're just moving hidden debt around.

---

## The "AI adoption without stability loss" scenario (2024)

**Source:** DORA State of DevOps Report 2024.

**The situation:** engineering org rolls out AI coding assistants. Developers report higher productivity and satisfaction (perception ↑). Six months later, Change Failure Rate is up ~7%, throughput is roughly flat or slightly down.

**How the cascade applies:**
- Diagnosis: the 2024 AI productivity paradox. Individual felt productivity ↑, team delivery ↓ or flat.
- Why: without small batches and testing rigor already in place, AI accelerates coding but the additional throughput piles up at the release pipeline and stability gates.
- Intervention: don't turn AI off; invest in Small Batches, Test Automation, and Documentation Quality *first*, then re-measure AI's impact.

**Why the scenario is instructive:** it's the freshest DORA finding and one most model responses miss. The correct move is not "AI bad" but "AI accelerates the same pipeline you had — fix the pipeline."

**Quotable finding:**
> "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%."
> — DORA 2024 State of DevOps Report

**Source:** [DORA 2024 State of DevOps Report](https://dora.dev/research/2024/dora-report/)

---

## The "Platform Engineering ROI question" scenario (2024)

**Source:** DORA State of DevOps Report 2024 platform engineering findings.

**The situation:** leadership wants to fund an internal developer platform team. Question: how do we measure whether the platform is actually working?

**How the cascade applies:**
- DORA at the *consuming* team level (are teams that use the platform deploying more often, with less failure?).
- DevEx at the *consuming* developer level (feedback loops, cognitive load, flow state — is the platform reducing friction or adding it?).
- Watch out for the 2024 finding: platform adoption boosts individual productivity but can slow team throughput and add instability if the platform itself is not well-run.

**Intervention:** measure consuming-team DORA and consuming-developer DevEx as the platform team's product metrics. The platform team's own success is measured by its consumers' delivery + experience.

**Why the scenario is instructive:** platform engineering is currently the most-discussed capability. The 2024 finding is that it's not automatically good — it's good if the platform is good.

**Source:** [DORA 2024 report](https://dora.dev/research/2024/dora-report/) · [2024 report summary — DX](https://getdx.com/blog/2024-dora-report/)

---

## The "Documentation as the under-invested lever" scenario (2023, reinforced 2024)

**Source:** DORA State of DevOps Reports 2023 and 2024.

**The situation:** team is investing in every DORA capability except Documentation Quality. Docs are stale, undiscoverable, and everyone knows it but no one prioritizes fixing it.

**How the cascade applies:**
- Finding: Documentation Quality is one of the highest-leverage, most-under-invested capabilities in the DORA research.
- 2024 extension: if AI adoption increases by 25%, the projected doc quality gain is 7.5% — the highest of any factor studied. Documentation is one of AI's biggest leverage points.
- Intervention: treat docs as a first-class capability. Assign ownership, measure quality (via developer surveys), invest specifically.

**Why the scenario is instructive:** docs are boring, so they get skipped. The research says they are among the highest-leverage capabilities you can invest in. Boring; powerful.

---

## The "First-time DORA baseline" scenario

**The situation:** engineering org has never measured DORA. Leadership is asking "how do we start?"

**How the cascade applies:**
1. Take the [DORA Quick Check](https://dora.dev/quickcheck/). It's free, fast, and returns tier estimate + specific capability recommendations. Don't overthink instrumentation on day one.
2. Publish the baseline internally (tier + top capability recommendations). Do NOT publish per-team leaderboards.
3. Pick one team to invest in one capability. Re-baseline in a quarter.
4. Scale to the next team.

**Why the scenario is instructive:** most first-time DORA efforts start with an over-engineered instrumentation project and never invest in a capability. The Quick Check is deliberately low-effort so measurement doesn't crowd out improvement.

---

## The "Executive wants a leaderboard" scenario (the anti-pattern to redirect)

**The situation:** VP or CEO says "great, let's rank the teams by Deploy Frequency and use that for perf reviews / bonuses."

**How to respond (per Forsgren):**
1. **Stop.** Explain the gaming dynamic before instrumenting.
2. Cite the DORA team's explicit position: DORA is not for individual or per-team performance evaluation.
3. Redirect: teams benchmark against themselves over time (are we improving?) and against tier norms (are we roughly Elite / High / Medium / Low?). Never against each other.
4. If leadership wants a "productivity signal" for people decisions, redirect to competency frameworks or growth ladders — not DORA.

**Why the scenario is instructive:** this is the most-warned-against DORA misuse. The assistant should push back on it before doing any of the other work.

**Source:** [DORA team position statement](https://dora.dev/); [Forsgren on Lenny 2023](https://www.lennysnewsletter.com/p/how-to-measure-and-improve-developer)

---

## Cases from *Accelerate* itself

The 2018 book uses several cases and cross-industry studies. The book's central argument is drawn from survey data (thousands of respondents across industries), so specific single-company narratives are less prominent than in author-centric strategy books. Chapters 3-4 discuss transformation stories; the appendix details the research methodology.

If the user wants the book's own case material, direct them to the book — this skill doesn't replicate it.

---

## Cases to be added (community PRs welcome)

- **Specific DX customer stories** — DX Inc. publishes some; more community-contributed cases welcome.
- **Enterprise transformation cases beyond Capital One** — Nordstrom, HP, ING, and others appear in DevOps Enterprise Summit talks.
- **AI-era case studies** — 2025-2026 will produce these; PRs welcome as they emerge.
- **Small-team / startup cases** — the research skews enterprise; small-team applications of DORA are under-documented.
- **Public-sector cases** — DORA applied to government and non-profit tech orgs; some *State of DevOps* respondents but few named cases.

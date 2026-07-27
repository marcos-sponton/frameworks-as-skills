# Research dossier — DORA / Accelerate (Nicole Forsgren)

## Author

**Nicole Forsgren, PhD** — Management Information Systems (PhD), Master of Accounting (Univ. Arizona). Prior career: software engineer, sysadmin, hardware performance engineer, professor (Boise State, Pepperdine, Utah State).

**Career trajectory:**
- 2014-2015: Chef Software (Director, Organizational Performance & Analytics)
- 2015: Co-founded **DORA** (DevOps Research and Assessment) with Jez Humble and Gene Kim; served as CEO
- 2018: DORA acquired by **Google Cloud**
- 2020: **GitHub / Microsoft** — VP of Research & Strategy at GitHub; later Partner at Microsoft Research (Developer Velocity Lab)
- ~2023: Advisor / research collaborator with **DX** (getdx.com)
- Now: **Senior Director of Developer Intelligence at Google** (per Lenny's podcast 2025 intro)

**Books:**
- *Accelerate: The Science of Lean Software and DevOps* (2018, w/ Jez Humble + Gene Kim) — Shingo Research Award 2019
- *DevOps Handbook, 2nd ed.* (2021, w/ Kim, Humble, Debois, Willis)
- ***Frictionless: 7 Steps to Remove Barriers, Unlock Value, and Outpace Your Competition in the AI Era*** (Dec 2025, w/ Abi Noda) — most recent

**Key papers:**
- SPACE (ACM Queue, 2021) — Forsgren, Storey, Maddila, Zimmermann, Houck, Butler
- DevEx (ACM Queue, 2023) — Noda, Storey, Forsgren, Greiler

## The framework family (evolution)

**DORA (2015 → present)** → **SPACE (2021)** → **DevEx (2023)** → **DX Core 4 (2024)** — all connected through Forsgren's research thread.

### DORA — the 4 (now 5) keys

**Original four (Accelerate, 2018):**
1. **Deployment Frequency** — how often you deploy to production
2. **Lead Time for Changes** — time from commit to production
3. **Change Failure Rate** — % of deployments causing failure
4. **Mean Time to Restore (MTTR)** — how fast you recover

**Current five (per dora.dev, evolved):**
- **Change Lead Time**
- **Deployment Frequency**
- **Failed Deployment Recovery Time** (replaces MTTR)
- **Change Fail Rate**
- **Deployment Rework Rate** (new; % of unplanned deploys after incidents)

**Note:** "Reliability" was added as an operational-performance dimension in the 2021 State of DevOps Report and lives adjacent to the throughput/stability pair.

**Performance tiers (current benchmarks):**
| Tier | Deploy Freq | Lead Time | Change Fail Rate | Recovery |
|---|---|---|---|---|
| **Elite** | On-demand (multi/day) | < 1 day | ~5% | < 1 hour |
| **High** | 1/day – 1/week | 1 day – 1 week | ~10% | < 1 day |
| **Medium** | 1/week – 1/month | 1 week – 1 month | ~15-20% | < 1 day |
| **Low** | < 1/month | 1-6 months | ~40%+ | 1 week – 1 month |

Elite = 19% of respondents (2024 report).

### The 24+ Capabilities (current dora.dev catalog: ~30)

**Technical:** Continuous Integration, Continuous Delivery, Deployment Automation, Test Automation, Test Data Management, Version Control, Trunk-Based Development, Code Maintainability, Database Change Management, Monitoring & Observability, Flexible Infrastructure, Pervasive Security, Proactive Failure Notification.

**Process:** Streamlining Change Approval, Working in Small Batches, WIP Limits, Visibility of Work in Value Stream, Visual Management, Loosely Coupled Teams, Documentation Quality, Empowering Teams to Choose Tools.

**Cultural / Organizational:** Generative Organizational Culture (Westrum), Transformational Leadership, Job Satisfaction, Well-being, Learning Culture, Team Experimentation, Customer Feedback, User-centric Focus.

**AI-specific (new in 2024):** AI-accessible Internal Data, Clear/Communicated AI Stance, Healthy Data Ecosystems, Platform Engineering.

### Westrum organizational culture

Ron Westrum's model (from aviation/healthcare safety research), incorporated into DORA:
- **Pathological** (power-oriented) — info hoarded, messengers shot, failure punished
- **Bureaucratic** (rule-oriented) — turf, procedures, narrow responsibility
- **Generative** (performance-oriented) — info flows, novelty embraced, failures are learning

Culture predicts information flow, which predicts delivery performance. Generative correlates with elite performance.

### Core insight (canonical)

**Speed and stability are NOT a tradeoff.** They come together, from the same practices. Elite performers deploy fastest AND fail least AND recover fastest. This is *the* finding of Accelerate — the whole book's argument. Any framing that "we're slowing down to be more careful" is misdiagnosis.

## SPACE (2021)

Five dimensions — pick 2-3 from at least 3 dimensions:
1. **Satisfaction & well-being** — dev fulfillment, burnout, retention
2. **Performance** — outcomes of what devs produce (customer satisfaction, reliability)
3. **Activity** — count of actions/outputs (commits, PRs, story points) — SPACE explicitly warns activity alone is not productivity
4. **Communication & collaboration** — how devs work together, knowledge sharing, review quality
5. **Efficiency & flow** — ability to complete work without interruption

**Core principles from the paper:**
- Productivity cannot be captured by a single metric
- Productivity has more to do with people than tools
- Developer well-being matters (measurable link to performance)
- Beware activity metrics (lines of code, commits) — easy to game, meaningless in isolation

## DevEx (2023)

Three dimensions capturing the "friction" developers experience:
1. **Feedback Loops** — speed and quality of feedback from tools/systems/people (CI, code review, deploys)
2. **Cognitive Load** — mental effort required (codebase complexity, docs, tooling)
3. **Flow State** — ability to enter/protect deep focus

Measurement combines **perceptual data** (surveys of devs) with **workflow/system data**. The DevEx paper distills 25+ sociotechnical factors into these three.

## DX Core 4 (2024)

Practical unification of DORA + SPACE + DevEx (by Laura Tacho + Abi Noda, w/ Forsgren, Storey, Zimmermann):
1. **Speed** — Diffs (or PRs) per Engineer *(with an explicit warning: never use for individual performance)*
2. **Effectiveness** — DXI (Developer Experience Index, 14-question survey aggregate)
3. **Quality** — Change Failure Rate (DORA)
4. **Impact** — % time on new capabilities vs. maintenance

## Post-book evolution

**2018 → 2024:** annual State of DevOps Reports. Key evolutions:
- 2021: Reliability added; culture emphasis deepened
- 2022: Security capabilities integrated (DevSecOps)
- 2023: Documentation identified as the top under-invested capability
- 2024: **AI as central topic** — 75% of devs use AI at work; AI adoption correlates with +individual productivity but -1.5% throughput and -7.2% stability. Documentation identified as biggest AI leverage (25% AI adoption → 7.5% doc quality gain). Platform engineering deeply studied.
- 2024: Move beyond DORA-only — DevEx emerges as evolution addressing what DORA can't see

**Frictionless (2025):** friction as central concept; 7-step methodology; LinkedIn case (monthly → multi-daily deploys); the $1.52T annual technical-debt figure.

## Critical warnings / anti-patterns

### DORA is NEVER for individual performance evaluation
Forsgren and DORA team have been explicit in writing (2023 statement). Using DORA at individual level produces:
- Devs make artificially small commits to inflate Deployment Frequency
- Rush reviews to inflate Lead Time
- Avoid risky changes to keep Change Failure Rate down
- Sandbagging estimates

DORA measures **team and system-level** delivery performance. Individual performance requires different signals (SPACE has some appropriate ones at individual level, especially Satisfaction — but even there, aggregate).

### Vanity metrics that Forsgren attacks
- **Lines of code** — legendary bad metric; more code often means worse code
- **Commits per day** — gameable; punishes good refactoring
- **Velocity (story points)** — inflates via scope shrinkage
- **Hours worked / seat time** — measures presence, not output
- **Bugs closed** — encourages opening trivial bugs

### The Productivity Paradox (2024 AI finding)
Devs *feel* more productive with AI (flow ↑, satisfaction ↑) but *team throughput* drops slightly and stability drops noticeably. Individual perception ≠ system outcome. Requires small batches and testing rigor to convert AI's speed at the keyboard into shipped-value at the team level.

### Gaming metrics = destroying the signal
Any DORA/SPACE/DevEx metric tied to compensation or performance review becomes gameable within one quarter. Forsgren's rule: measure to *improve*, not to *judge*.

## Voice & tone signatures

**Register:** rigorous researcher who writes accessibly. PhD + former-professor precision, but conversational in podcast form. Data-first. Highly declarative when the research is settled ("we found"), appropriately humble when it's still open ("what we're seeing suggests").

**Signature vocabulary:**
- "DORA metrics" / "the four keys" / "the five keys"
- "Elite performers" / "High performers" / "Medium" / "Low"
- "Generative culture"
- "Capabilities" (as a specific term — practices that predict performance)
- "SPACE" / "DevEx"
- "Quick Check"
- "Predictive validity"
- "Batch size"
- "Trunk-based development"
- "Loosely coupled architecture"
- "Feedback loops"
- "Cognitive load"
- "Flow state"
- "Friction"
- "Documentation" (surprisingly high-leverage per her research)
- "Small batches"

**Words she attacks / reframes:**
- "Velocity as productivity" — velocity is a scoping negotiation, not output
- "Lines of code" — actively worse than useless
- "Vanity metrics"
- "Gut feel" — as substitute for measurement
- "10x engineer" — no research support
- "Ninja / rockstar / individual heroics" — anti-patterns for team performance
- "Just measure everything" — no; measure what predicts outcomes
- "AI will replace X% of devs" — not what the data says
- "DORA as scorecard" for individuals

**Signature rhetorical moves:**
1. **Cite the research strength** — "our research of X thousand engineers over Y years shows"
2. **Distinguish perception from measurement** — "devs feel faster; the data shows otherwise"
3. **Deploy the tier language** — Elite vs. Low as concrete benchmark
4. **Warn about misuse before teaching use** — because DORA gets weaponized
5. **Distinguish scope levels** — individual vs. team vs. system vs. org
6. **Refuse the tradeoff framing** — speed and stability, satisfaction and throughput; almost always "both, not either"

**Analogies she uses:**
- Manufacturing / Lean (Toyota Production System) — small batches, WIP limits, pull systems
- Aviation safety / Westrum — how information flows predicts outcomes
- Chemotherapy targeting (rarely) — well-designed intervention
- The "productivity paradox" (Solow, 1980s IT) — echo in 2024 AI findings

## Real cases (from State of DevOps reports and Frictionless)

- **LinkedIn** — monthly → multi-daily deploys via friction removal (Frictionless case study)
- **Google Cloud** — dogfooding DORA
- **Netflix** — chaos engineering + trunk-based dev; frequently cited
- **Capital One** — early enterprise DORA adopter; org-wide transformation
- **Nordstrom** — early DevOps transformation
- Many *State of DevOps* respondents (anonymized)

## Framework relationships

**Complementary / composes well:**
- **Team Topologies** (Skelton & Pais) — organizational-design layer under DORA
- **Platform Engineering** — an emerging DORA capability
- **Lean / TPS** — DORA's intellectual parent (batch size, flow)
- **Continuous Delivery** (Humble & Farley) — the technical prescription behind DORA capabilities
- **SPACE** and **DevEx** — sibling frameworks, extend where DORA is silent
- **DX Core 4** — synthesis
- **Cynefin / OODA** — different lens, no conflict

**Incompatible / attacked:**
- **SAFe (Scaled Agile Framework)** — Forsgren and DORA team publicly skeptical; SAFe adds process weight that correlates with lower delivery performance
- **Traditional PMO strategic planning** — as governance layer over software delivery
- **Anything using velocity / lines of code as productivity**
- **Individual-level DORA reporting**

## Live sources (2025)

- **dora.dev** — Google-hosted; annual State of DevOps report, capabilities catalog, Quick Check tool
- **getdx.com** — DX Inc.; Forsgren collaborates, DX Core 4 lives here
- **Nicole Forsgren on LinkedIn** — active
- **nicolefv.com** — personal site
- **Frictionless book** (Dec 2025)
- **Podcast**: Lenny's Podcast — two episodes (2023: "How to measure and improve developer productivity"; 2025: "How to measure AI developer productivity")
- Also: The Pragmatic Engineer, Stack Overflow Podcast, SWE Daily, Screaming in the Cloud (Corey Quinn), The New Stack

## Key Forsgren quotes (verified from public sources)

> "Speed and stability are not a tradeoff. They come together, and they come from the same practices."
> — Accelerate, 2018 (paraphrased across many talks)

> "You cannot measure your way out of a bad culture."
> — recurring in talks

> "DORA metrics are for measuring and improving the software delivery process. They are not individual performance metrics."
> — DORA team statement, 2023

> "The DXI is not for individual performance."
> — Introducing DX Core 4, 2024

## Gaps in this dossier (community PRs welcome)

- Full transcript of Lenny 2025 episode
- Frictionless book (only announcements + previews read)
- Deep read of State of DevOps 2022 and 2023
- Forsgren's Google Scholar publications (academic papers)
- Substack / newsletter if she runs one
- Podcast appearances beyond the top few

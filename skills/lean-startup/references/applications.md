# The Lean Startup — Applications

> When Ries's method fits, when it doesn't, and what to reach for instead. Includes the **honest disagreement** with Amazon's Working Backwards on MVP at commitment altitude — both positions are defensible; the resolution is cost per bet.

## Situations where the method fits well

- **Testing a new product or service hypothesis** where nobody knows yet whether customers want it. Extreme uncertainty is the defining condition Lean Startup addresses.
- **Designing an MVP** — and needs help getting the definition right (smallest test that produces validated learning, not a shipped v0.1).
- **Running a pivot-or-persevere meeting** at a fixed cadence, or deciding whether it's time to hold one.
- **Separating vanity metrics from actionable metrics** — the load-bearing distinction in early-stage measurement.
- **Standing up cohort analysis, split tests, or funnel-by-cohort dashboards** for a pre-revenue or early-revenue product.
- **Wrestling with runway** — reframing from "months of cash" to "number of pivots remaining."
- **Establishing Innovation Accounting** — the three-level maturity model for measuring progress when classical KPIs are ~zero.
- **Running a Five Whys post-mortem** after any meaningful failure (bug, outage, missed launch, customer complaint). Looking for the human/process root cause behind a technical symptom.
- **Adopting small batches or continuous deployment** — with the discipline (Andon Cord, unit tests, CI, monitoring, Five Whys post-mortems) that makes them safe.
- **Getting a team out of "operating on dashboards" and back into Genchi Genbutsu** — actual observation of real customers in their environment.
- **Applying entrepreneurial method inside a large enterprise** — the GE FastWorks pattern from *The Startup Way*. Executive sponsorship, protected budget, Growth Board governance, entrepreneur-as-org-chart-role.
- **Designing governance to protect a mission-driven company from short-term financial pressure** — the *Incorruptible* (2026) frame. Post-Series-C or public-company altitude.

## Situations where it does NOT fit

### Amazon-scale commitment altitude
A launch where a broken v0.1 destroys customer trust and the cost per bet is measured in tens of millions of dollars — Amazon Prime, AWS launch, Kindle. Amazon explicitly rejects MVP for launches at scale and uses **PR/FAQ** (the narrative memo mechanism) instead, precisely because at Amazon's scale, the cost of a bad launch dwarfs the cost of weeks on a document.

**Reach for [[working-backwards]] instead** for the launch phase. Lean Startup is still the right method for the discovery phase *before* the launch commitment.

**The honest disagreement:** see the section below.

### Corporate strategy at the "which markets should we be in" altitude
Lean Startup operates *below* strategy. It presupposes you know what business you're trying to build. If the user is asking "what markets should we be in?" or "how do we win in this industry?", reach for:
- **Playing to Win (Martin)** — the strategy cascade.
- **Good Strategy Bad Strategy (Rumelt)** — the kernel of diagnosis / guiding policy / coherent action.
- **7 Powers (Helmer)** — durable competitive advantage.

Use those first; then bring Lean Startup for the tactical hypothesis testing inside the chosen bet.

### Mature-business optimization
Lean Startup is for **new products under extreme uncertainty**, not for driving efficiency in a known-good process. Optimizing a mature business is a different problem — Six Sigma, process optimization, operational efficiency work.

**Redirect:** if the user is trying to improve gross margin in a scaled business, reduce fulfillment cost, or streamline a known-good process, Lean Startup isn't the right method. Suggest lean manufacturing / Six Sigma / DORA (for engineering delivery) / process-mining tools depending on the flavor.

### Tactical product discovery cadence
Weekly interview practice, opportunity trees, assumption mapping. This is [[continuous-discovery-habits]] territory (Teresa Torres, queued for this repo). Torres updates the specific tactical practices for 2020s product teams — the daily-cadence manual — which fits *inside* Ries's BML loop as the day-to-day of the "Learn" phase.

**Compose them:** Torres for the tactical cadence; Ries for the strategic frame around it.

### Individual PM career or skill development
Not Ries's domain. Reach for Marty Cagan's Silicon Valley Product Group, Perri's Product Institute, or Reforge.

### Pure business-strategy questions
See "Corporate strategy at the altitude" above. If the user is deciding what business to build, use Playing to Win or Rumelt first.

### Turnaround / crisis where the diagnosis is more urgent than the operational fix
If the org is on fire, do Rumelt-style crux diagnosis first (find the pivotal problem). Bring in Lean Startup only for the specific new bets that are part of the turnaround response.

### When the user just wants a summary of *The Lean Startup*
Give them the book link ([Amazon](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898)). Don't run the method at them.

## The honest disagreement: Lean Startup vs. Working Backwards on MVP

**Both positions are defensible.** Both authors are correct in their own scope. This is one of the most important compositions the skill has to get right — collapsing it in either direction produces wrong advice.

### The disagreement stated

- **Ries (Lean Startup):** the MVP is the smallest test that produces validated learning. Ship the minimum thing that answers the hypothesis. Learn fast.
- **Bryar & Carr (Working Backwards):** at Amazon-scale commitment altitude, MVP is dangerous. A broken v0.1 shipped to millions destroys customer trust. Use PR/FAQ — weeks or months of thought before any code — to force the launch's honesty upstream.

Colin Bryar publicly critiques the MVP-industrial-complex: *"the MVP process can be useful, but the process itself sometimes becomes the goal."* Bryar and Carr argue that mature organizations like Amazon spend substantial time on understanding the market and customers before writing any code.

### The resolution: cost per bet

- **Lean Startup thrives when experiments are cheap** and **learning speed dominates**. Early-stage startups, new features in a shipped product, new segments, new business models. The cost of a wrong bet is a two-week experiment; the value of a right bet is direction. Speed of learning wins.
- **Working Backwards thrives when commitments are expensive** and **launch quality dominates**. Amazon Prime, AWS launch, Kindle. The cost of a wrong bet is tens of millions and years of trust damage; the value of a right bet is a defensible new business. Depth of thought upstream wins.

### The practical composition

A team can (and often should) **use Lean Startup for the discovery phase and Working Backwards for the commitment phase** of the same product:

- **Discovery (extreme uncertainty, cheap experiments):** Lean Startup. MVP. Cohort analysis. Pivot or persevere.
- **Commitment (expensive launch, high trust stakes):** Working Backwards. PR/FAQ. STL. WBR.

**The skill's job:** when the user is at the boundary, ask *"how expensive is a wrong bet here?"* That answer decides which method fits this specific decision.

### What the disagreement is NOT about

Both frames agree on:
- **Customer obsession as the starting point.**
- **Working from the customer backward** (Ries also uses "planning in reverse" — Learn first, then Measure, then Build).
- **Rigor in defining the hypothesis** before shipping.
- **The importance of killing bad ideas early.**

The disagreement is real about MVP-in-general; it is smaller once you decompose by phase (discovery vs. commitment) and by scale (cheap-experiment vs. expensive-launch).

### For your reference: how Working Backwards frames this

See [[working-backwards]] `references/applications.md`, which explicitly says:
> "Pre-PMF, use Lean Startup, Continuous Discovery (Torres), or the discovery/validation loops native to your stage… Working Backwards is a commitment-phase mechanism. Try a lighter shape first — customer interviews, MVP, prototype — and come back to Working Backwards when the cost per bet is high enough to justify weeks on a document."

Working Backwards defers to Lean Startup for pre-PMF and cheap-experiment phases. Lean Startup should defer to Working Backwards for expensive-commitment launches. The two skills together are more powerful than either alone.

## Adjacent frameworks — when to reach for a different one

| If the user's situation is... | Reach for... | Why |
|---|---|---|
| Amazon-scale commitment launch | **Working Backwards (Bryar & Carr)** | PR/FAQ replaces MVP when the launch cost is high |
| Corporate strategy at "where to play / how to win" altitude | **Playing to Win (Martin)** or **Good Strategy Bad Strategy (Rumelt)** | Higher altitude than Lean Startup |
| Durable competitive advantage / moats | **7 Powers (Helmer)** | Different question — competitive dynamics, not hypothesis testing |
| Diagnosis of what's structurally broken before choosing | **Rumelt's kernel** | Rumelt front-loads diagnosis |
| Tactical discovery cadence — weekly interviews, opportunity trees, assumption mapping | **Continuous Discovery Habits (Torres)** | Torres = tactical cadence inside Ries's BML loop |
| PM function health / build trap diagnosis | **Escaping the Build Trap (Perri)** | Perri operates one altitude up on the PM function |
| Individual PM skill development | Marty Cagan / SVPG / Reforge / Product Institute | Skill training, not method |
| Understanding demand / job progression | **JTBD (Christensen / Moesta / Kalbach)** | Complementary — JTBD tells you which hypothesis is worth testing; Lean Startup tells you how to test it |
| Compressed 5-day Learn phase (prototyping + testing) | **Design Sprint (Knapp)** | Composable with Lean Startup for pre-code hypothesis testing |
| Delivery cadence for a shipped product | **Shape Up (Basecamp / Ryan Singer)** | Different phase — shipped-product delivery, not discovery |
| Engineering delivery performance | **DORA (Accelerate)** | Different question — delivery throughput, not discovery |
| Mature-business efficiency optimization | Lean manufacturing / Six Sigma / process optimization | Different problem — known process, not extreme uncertainty |
| Positioning / narrative / brand | **Obviously Awesome (Dunford)**, **Strategic Narrative (Raskin)** | Downstream of Lean Startup — you position what you've built |
| Governance / mission-drift protection at scale | **Incorruptible (Ries's 2026 book)** | Same author, later frame — see `post-book.md` §3 |

## How Lean Startup composes with other frameworks

### Composes cleanly with Torres / Continuous Discovery Habits
Torres builds *on* Lean Startup rather than against it. Her **Opportunity Solution Tree**, **weekly interview cadence**, and **assumption-testing loops** fit inside Ries's BML loop. Torres updates the *specific tactical practices* for 2020s product teams — Ries stayed at the principle level; Torres wrote the daily-cadence manual.

**When to compose:** any time the user is doing tactical discovery work inside a Lean Startup frame. Use Torres for the daily rhythm; Ries for the strategic frame around it. See [[continuous-discovery-habits]] (queued).

### Composes cleanly with Cagan / Inspired
Cagan's *Inspired* is complementary but more product-manager-focused. Cagan's "product discovery" adopts Lean Startup principles (validated learning, MVP as smallest test) with a distinct emphasis on the **empowered product team**. Where Ries writes for founders / entrepreneurs / enterprise change agents, Cagan writes for PMs.

**When to compose:** the user is a PM in a product-led company. Use Cagan for the PM function; Ries for the underlying method the PM is applying. See [[inspired]] (queued).

### Composes cleanly with Perri / Escaping the Build Trap
Perri **explicitly credits Ries as a foundational influence** and **redefines MVP using Ries's original meaning** ("the minimum amount of effort to learn"). Perri prefers *"solution experimentation"* as vocabulary to break the industry's degraded association of MVP with "small first version to ship." Perri's Product Kata is a Ries-lineage device (via Mike Rother's *Toyota Kata*, itself another TPS translation).

**When to compose:** the user is applying Lean Startup inside a PM organization that has a build-trap pathology. Use Perri for the organizational diagnosis; Ries for the method the reformed org will apply. See [[escaping-the-build-trap]].

### Composes cleanly with JTBD (Christensen / Moesta / Kalbach)
JTBD tells you **which hypothesis is worth testing**; Lean Startup tells you **how to test it**. A "customer need pivot" (pivot type #4) becomes far more tractable if you have JTBD interviews telling you what jobs the current customers hire the product for.

Ries himself rarely uses JTBD vocabulary but the frames are mutually reinforcing. Use JTBD to generate the hypotheses; use Lean Startup to test them.

### Composes cleanly with Design Sprint (Knapp)
Design Sprint is a **compressed 5-day version of the Learn phase** — heavy on prototyping and user testing, light on Build. Composable with Lean Startup for pre-code hypothesis testing.

### Composes cleanly with Blank / Customer Development
**The direct intellectual parent.** Blank supplied the search-vs-execution distinction, the "get out of the building" mandate, and the four-phase model (Customer Discovery → Validation → Creation → Company Building). Lean Startup is Ries's synthesis of Customer Development + Lean Manufacturing + agile, applied to the search phase.

**Ries always credits Blank explicitly.** The skill should too.

### Composes cleanly with Toyota Production System (Ohno / Deming / lean manufacturing)
The manufacturing lineage — small batches, Andon Cord, Five Whys, Genchi Genbutsu, continuous improvement (kaizen), Toyota Kata. Ries's translation move: TPS figured out how to build a **known** thing efficiently; startups need the same discipline for figuring out **what** to build under uncertainty.

Ries is meticulous about attribution to Ohno / TPS. So should the skill be.

### Composes cleanly with Shape Up (Basecamp / Ryan Singer)
Shape Up is a **delivery cadence for shipped products**. Not designed for the search / discovery phase Lean Startup targets. Composable for teams that have graduated from Lean Startup into scaled operations — Shape Up runs the delivery of what Lean Startup validated.

### Composes cleanly with DORA / Accelerate
DORA metrics (deployment frequency, lead time, change failure rate, mean time to restore) overlap with Ries's continuous-deployment lineage at the delivery-throughput layer. Composable — DORA measures the delivery pipeline; Lean Startup measures the learning pipeline that decides what to put through it.

## Common misapplications to redirect

### The user is applying Lean Startup at Amazon-scale commitment altitude
Redirect to [[working-backwards]]. Explain the honest disagreement — both methods are correct in their own scope. Ask *"how expensive is a wrong bet here?"*

### The user is asking Lean Startup to solve a corporate-strategy question
Redirect to Playing to Win (Martin), Rumelt, or 7 Powers (Helmer). Lean Startup is below strategy.

### The user is applying Lean Startup to a mature-business optimization problem
Redirect to lean manufacturing / Six Sigma / process optimization. Different problem, different method.

### The user wants Lean Startup for an individual PM career question
Redirect to Cagan / Perri / Reforge / Product Institute.

### The user brings degraded vocabulary (fail fast, MVP-as-v0.1, vanity-metrics-as-OKRs)
Do not fight the frame. **Reset the vocabulary** using the definitional-reset move (see `voice-and-tone.md` §1). Then apply the method with the reset definitions in place.

### The user asks Lean Startup to solve a governance / mission-drift problem
Redirect to *Incorruptible* (Ries's own 2026 book) via `post-book.md` §3. Financial gravity, spiritual holding company, governance-as-product-design. Same author, later frame.

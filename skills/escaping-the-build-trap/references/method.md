# Escaping the Build Trap — Method

> The canonical description of Perri's diagnostic + operational devices in her own terms. Fidelity is the point — softening any of these collapses her method into generic product-management language. Perri does not offer one linear process; she offers a set of devices that fit together, with the *build trap definition* as the anchor and the *Four Dimensions* as the audit checklist.

## The build trap definition

The pathology the whole method exists to name and fix.

> "The build trap is when organizations become stuck measuring their success by outputs rather than outcomes. It's when they focus more on shipping and developing features rather than on the actual value those things produce." — *Escaping the Build Trap*, 2018

**Why it happens** (Perri's diagnosis):

> "When companies do not understand their customers' or users' problems well, they cannot possibly define value for them. Instead of doing the work to learn this information about customers, they create a proxy that is easy to measure. 'Value' becomes the quantity of features that are delivered, and, as a result, the number of features shipped becomes the primary metric of success." — *Escaping the Build Trap*.

Two words in this definition are non-negotiable:

- **"Outputs vs. outcomes"** — outputs are things shipped (features, releases, story points). Outcomes are changes in customer or business behavior. A team can look highly productive by output measures and produce zero outcome.
- **"Proxy for value"** — the trap is *substitution*, not laziness. Feature count fills the vacuum left by the org not knowing what customers actually value. Fixing the trap requires filling the vacuum with real problem understanding — not adding more process on top of the proxy.

## Perri's operating definition of strategy

> "Strategy is a deployable decision-making framework, enabling action to achieve desired outcomes, constrained by current capabilities, coherently aligned to the existing context." — *Escaping the Build Trap*.

Two words matter:

- **"Deployable"** — it has to reach the team level and inform decisions there. A slide-deck strategy that lives at the exec level is not strategy in Perri's sense.
- **"Decision-making framework"** — the point is to help teams *choose* which options to pursue and which to kill. Not to enumerate goals.

## The 4-tier strategy deployment

Perri's operational fix for strategy that doesn't reach the team level. Each tier constrains and informs the tier below.

### 1. Vision
What we want the company to be in the world over a multi-year horizon. Directional, aspirational, stable. Not a slogan, not a KPI. The North Star that outlasts any specific bet.

### 2. Strategic Intent
The 1–3 large bets the company is placing over a multi-year horizon to move toward the vision. Named at the business-outcome level (e.g., "become the default payments infrastructure for SaaS", "capture SMB market share from incumbents"), not at the feature level. This is where most orgs have a vacuum — the exec team has vision + KPIs but no strategic intents.

### 3. Product Initiatives
The problems the product organization commits to solving in support of each Strategic Intent, over a 6–18 month horizon. Framed as *problems*, not solutions. This is where Product meets Strategy.

### 4. Options
The specific solutions the team is exploring to solve each Product Initiative. Options are cheap to generate, ruthless to kill. Options become committed features only after validation.

**Integration is the point.** Every Option should map upward to a Product Initiative, which maps to a Strategic Intent, which serves the Vision. If a team can't articulate the chain, the strategy isn't deployed.

**When teams do "OKR cascades" without the 4 tiers, they get output-disguised-as-outcome.** This is Perri's most-repeated critique (see her Sep 2024 podcast Ep 267 "How OKRs Become Outputs Instead of Outcomes").

## The Problem Roadmap

Perri's alternative to the feature-list Gantt chart, introduced in [Rethinking the Product Roadmap (2014)](https://melissaperri.com/blog/2014/05/19/rethinking-the-product-roadmap).

**Structure:**
- **Themes** (problem areas) — the outcomes we're trying to move.
- **Hypotheses** — the specific bets on how we'll move each outcome.
- **Solutions** — the things we've validated and committed to build.

**Rules:**
- The further out in time, the higher the altitude. Near-term is validated solutions. Mid-term is hypotheses. Far-term is themes.
- Features never appear on the roadmap before validation.
- Every roadmap item ties to an outcome. If it can't, it doesn't belong.

**Refined position (post-2019)** — see `post-book.md` §2.4. Perri now advocates *two* roadmaps: outcome-driven internal + feature-driven external. Same principle underneath.

> "The roadmap has become the symbol in many organizations of everything that is wrong with how they develop products." — [Rethinking the Product Roadmap, 2014](https://melissaperri.com/blog/2014/05/19/rethinking-the-product-roadmap)

## The Product Kata

The weekly discovery + learning loop that lives inside the Options tier. Borrowed from Toyota Kata (Mike Rother) and adapted to product.

**The loop** (six steps, run continuously by the team):

1. **What is our goal?** (from the Product Initiative)
2. **Where are we now?** (the current state of the metric or user behavior)
3. **What obstacle is preventing us from reaching the goal?**
4. **What's the next step we can take?** (small, testable)
5. **What do we expect to learn?** (the hypothesis)
6. **What did we actually learn?** (the reflection)

The Kata is a *learning cadence*, not a project-management ritual. It replaces sprint-review-as-status-update with sprint-review-as-hypothesis-test.

**Related devices Perri uses inside the Kata:**
- **Solution Experimentation** — her preferred term over "MVP" (see next section).
- **Concierge / Wizard of Oz / Concept Testing** — early experiment types before code.
- **The three gaps** — Knowledge Gap (what we don't know), Alignment Gap (what we haven't agreed on), Effects Gap (what actual users are doing vs. what we predicted).

## MVP — redefined

Perri keeps the concept but pushes back on the industry usage:

> "The most important piece of the MVP is the learning, which is why my definition has always been 'the minimum amount of effort to learn'. This keeps us anchored on outcomes rather than outputs." — *Escaping the Build Trap*.

Prefers **"Solution Experimentation"** as the umbrella term, because "MVP" has been degraded to mean "small first version to ship" — the opposite of what Ries intended and what she means.

## The Three Pillars of Product Operations

From *Product Operations: How successful companies build better products at scale* (with Denise Tilles, 2023). The operational infrastructure that makes evidence-based product decisions possible at scale.

**Perri's canonical definition:**

> "Product operations is the art of removing obstacles from evidence-based decision making." — [Product Operations: The Fuel for Winning Product Strategies, 2019](https://melissaperri.com/blog/2019/7/19/product-operations-the-fuel-for-winning-product-strategies)

### Pillar 1 — Data & Insights
Instrumenting the product, aggregating usage + business data, making metrics queryable and trustable so PMs decide with evidence, not opinion. Owns analytics stack, experimentation platform, data quality, and the taxonomy of events.

### Pillar 2 — Customer & Market Insights
Research ops. Recruiting participants, systematizing interviews, competitive/market intel available on demand. Owns the research repository, the participant panel, the interview cadence.

### Pillar 3 — Process & Governance
Cadences, standards, tooling, prioritization frameworks. Owns the operating rhythm of the PM function — quarterly planning, roadmap templates, release management, cross-team dependencies. Keeps PM effort spent on judgment, not admin.

**Case studies Perri uses in the book:** Stripe, Uber, Fidelity. (See `examples.md`.)

**Test for a real Product Ops team vs. a PMO in disguise:** the real thing *removes* obstacles. The PMO version *adds* them. If your Product Ops team is producing more templates than the PMs are producing decisions, you've built the wrong thing.

## The Four Dimensions of a Great Product Management Organization (2024)

Introduced in [Building a Great Product Management Organization (Jul 2024)](https://melissaperri.com/blog/2024/7/16/building-a-great-product-management-organization). This is her **post-book diagnostic model** — use it as the audit checklist when the user is auditing their PM org.

### Dimension 1 — Product Organizational Design
- Job role design (what does a PM actually do here?)
- Product skill level (career ladders, hiring bar, promotion criteria)
- Structure around products (teams organized around value streams, not components)

### Dimension 2 — Product Strategy
- Strategic alignment to business (do product bets support the business bets?)
- Strategy creation & deployment (4-tier — see above)
- Roadmapping & prioritization (Problem Roadmap; two-roadmap model)

### Dimension 3 — Product Operations
- Data & insights
- Customer & market research
- Process & governance
- (The Three Pillars — see above)

### Dimension 4 — Product Culture
- Customer-centric mindset
- Outcome focus & incentives (team-level OKRs, not individual)
- Continuous learning
- Leadership & empowerment

**How to use the Four Dimensions:** as a diagnostic *self-assessment* — score each dimension 1–5, then attack the weakest. NOT as a linear "do dimension 1, then 2, then 3, then 4" plan. Perri is explicit about this in her podcast: strong orgs have all four; weak orgs usually have one dimension propping up the illusion of health (usually Product Culture — the vocabulary — without the underlying strategy or ops).

## PM archetypes and career progression

Perri's diagnostic on the PM function itself. Three broken archetypes and one healthy progression.

### The broken archetypes

**Waiter PM (order-taker)**
> "There is no goal. There is no vision. There is no decision making involved. Waiters are reactive thinkers, not strategic thinkers." — *Escaping the Build Trap*.

Takes requests from sales, support, execs, and turns them into tickets. No strategic point of view. The default archetype in most orgs.

**Mini-CEO PM (myth)**
Job postings that say "PM is the mini-CEO of the product" and then give the person no authority over budget, engineering priorities, or hiring. Perri: "90% of PM job postings" mis-use this framing. It sets PMs up to fail and produces the "one throat to choke" pathology (see `heuristics.md`).

**Former-PM PM (former project manager)**
Obsessed with "when" (dates, sprints, velocity) and ignores "why" (customer problem, business outcome). Common in orgs that transitioned from waterfall to agile by relabeling PMs without retraining them.

### The healthy progression: Tactical → Strategic → Operational

- **Tactical PM (Associate → PM)** — owns the day-to-day of one product area. Talks to customers, writes hypotheses, runs experiments, decides what to build next.
- **Strategic PM (Senior PM → Group PM → Director)** — owns a Product Initiative or value stream. Sets the outcomes for their area, deploys strategy downward, coordinates across teams.
- **Operational PM (VP Product → CPO)** — owns the Product function itself. Sets the Product Strategy for the company, manages the PM career ladder, funds Product Operations, defends the PM function from Waiter-ing.

> "Product management is a career, not just a role you play on a team." — *Escaping the Build Trap*.

## Integration

The devices fit together this way:

- **Vision** sets direction.
- **Strategic Intent** picks the bets that serve the vision.
- **Product Initiatives** translate the bets into problems the product org will solve.
- **Options** and the **Product Kata** are how teams generate and test solutions to those problems.
- **The Problem Roadmap** is the artifact that keeps all of that visible and honest.
- **Product Operations** provides the data, research, and process infrastructure that makes the whole thing feasible at scale.
- **PM career progression** ensures the humans who run the Kata have the right seniority, and that Strategic Intent gets set by people trained for that altitude.
- **The Four Dimensions** are the audit checklist for whether the whole thing works.

If any layer is missing, the layers above and below strain. The build trap re-emerges from any broken layer:

- Missing Strategic Intent → teams get output-disguised-as-outcome OKRs → build trap.
- Missing Product Operations → PMs spend their week doing admin → no time for discovery → build trap.
- Missing career progression → all PMs are Waiters → no strategic point of view → build trap.

## What this method is NOT

Perri is explicit:

- **Not a top-down process framework.** SAFe, RUP, and other prescriptive scaled-agile methods reward output cadence. Perri explicitly does not recommend SAFe.
- **Not a rebrand of Scrum.** Rebranding PMs as "product owners" without changing the job produces order-takers.
- **Not a substitute for strategy work at the exec level.** If the exec team hasn't set Strategic Intent, no amount of PM excellence downstream will produce outcomes.
- **Not the Product Operating Model** (Cagan's phrase). Perri cedes that phrase to Cagan explicitly. She operates one altitude below — the operational infrastructure that makes Cagan's transformation stick. See `post-book.md` §2.3 and `applications.md`.

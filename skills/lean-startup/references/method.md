# The Lean Startup — Method

> The canonical description of Eric Ries's method in his own terms. Fidelity is the point — softening any of these collapses the method into generic startup advice. Load `heuristics.md` alongside this file: the operational devices below are load-bearing only if the discipline behind them is intact, and `heuristics.md` is where that discipline lives.

## The definition that anchors everything

Ries's canonical one-line definition of a startup:

> "A startup is a human institution designed to create a new product or service under conditions of extreme uncertainty." — *The Lean Startup*, 2011.

Three words are load-bearing:

- **"Human institution"** — not just software. Applies to a service, a policy, an internal program, a non-profit initiative, a healthcare pilot, a government program. Anywhere someone is creating something new for humans under uncertainty.
- **"New product or service"** — the method addresses the *search* phase, not the *execution* phase. Optimizing a mature, known-good business is a different problem (see `applications.md`).
- **"Extreme uncertainty"** — the defining condition. If you know who the customer is and what they need, this isn't your method. Extreme uncertainty is where classical KPIs are ~zero and traditional business plans are speculative fiction.

## The 5 Principles (theleanstartup.com/principles)

Ries's canonical framing of what The Lean Startup *is*:

### 1. Entrepreneurs are everywhere
A "startup" is any human institution creating a new product or service under conditions of extreme uncertainty. **This applies inside Fortune 500s, non-profits, government, healthcare — not just VC-backed tech.** The whole point of *The Startup Way* (2017) is that the method works in enterprises when the scaffolding is right. See `post-book.md` §2.

### 2. Entrepreneurship is management
A startup is an institution requiring a new kind of management specifically geared to extreme uncertainty. **Not a smaller version of a big company. Not chaos.** Ries pushes back on the "just move fast and iterate" framing — the method is disciplined, not chaotic. The discipline just serves learning instead of execution.

### 3. Validated learning
The unit of progress in a startup. Learning is validated **scientifically** — by running experiments that test each element of the vision, not by opinion or intuition.

> "The only way to win is to learn faster than anyone else." — *The Lean Startup*, 2011.

### 4. Innovation accounting
How you measure progress when the classical KPIs are all zero. Three-level maturity model — see below.

### 5. Build-Measure-Learn
The core feedback loop. Turn ideas into products (Build); measure how customers respond (Measure); learn whether to pivot or persevere (Learn). **Accelerate the loop.**

## Build-Measure-Learn (BML) loop

The diagram everyone knows: **Ideas → Build → Product → Measure → Data → Learn → Ideas.**

**Ries's own emphasis that most retellings miss:** the loop should be **planned in reverse — Learn first, then Measure, then Build.**

- *"What do we need to learn?"* determines
- *what metric will tell us?* which determines
- *what's the smallest experiment (MVP) that produces that metric?* which determines
- *what do we actually build?*

If you start with Build and reverse-engineer a hypothesis to justify what you already wanted to make, that's not the BML loop — that's a Gantt chart with lean vocabulary. See `heuristics.md` for the anti-pattern.

**The loop is continuous, not sequential-per-quarter.** Each turn should be short (days to weeks, not quarters). "This quarter we Build, next quarter we Measure, Q3 we Learn" is a linear waterfall in disguise — not what Ries described.

## Minimum Viable Product (MVP)

The most-cited and most-misunderstood term Ries ever coined. His actual definition:

> "The minimum viable product is that version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." — *The Lean Startup*, 2011.

Three nuances Ries has emphasized publicly and that most industry usage ignores:

- **"Least effort" not "least features."** The MVP is not the small first version of the product — it's the *smallest test that produces the learning*. Sometimes there is no code at all.
- **"Validated learning" is the outcome, not "shipped software."** A landing page with 100 signups from paid ads is an MVP. A stripped-down v0.1 that shipped but taught nothing is not.
- **The MVP is disposable.** Its job is to answer a question, not to become the product. Most first MVPs get thrown away.

**MVP types (Ries's book + subsequent lean-startup canon):**
- **Landing page / smoke test** — describe the product; measure conversion. (Zappos, Dropbox video.)
- **Explainer video** — walk through the intended experience; measure signup intent. (Dropbox.)
- **Concierge MVP** — hand-deliver the value manually to a small set of customers to test whether the value proposition is real. (Food on the Table.)
- **Wizard of Oz MVP** — the front-end looks automated; humans behind the curtain do the work. Tests the demand without building the automation. (Aardvark, early Zappos.)
- **Piecemeal MVP** — cobble together existing tools (Zapier, Airtable, spreadsheets) to fake the workflow before writing custom code.
- **Single-feature MVP** — the smallest slice of a real product that a customer can actually use. Use this only when the previous four don't answer the question.

**How to know you built the wrong MVP:** you spent months on it. You feel embarrassed to show it. You can't state the specific hypothesis it tested. It shipped and the data was ambiguous (usually because the "MVP" was actually testing 6 hypotheses at once — see the "pivot that's actually 5 pivots stacked" gotcha in `heuristics.md`).

See `heuristics.md` for the aggressive-guard-against MVP-as-excuse-for-shipping-garbage discussion.

## Pivot or Persevere

The regular strategic decision, held at a **fixed cadence** (Ries recommends every few weeks to few months, depending on startup pace), to decide whether the current strategy is producing validated learning fast enough to be on track — or whether a structured course correction (pivot) is needed.

**Persevere** when retention, conversion, or per-cohort customer value are improving turn-over-turn.

**Pivot** when repeated credible experiments fail to move the actionable metrics — or when they succeed but reveal a different opportunity than the one you were pursuing.

### The 10 types of pivot (The Lean Startup, chapter 8)

1. **Zoom-in pivot** — a single feature becomes the whole product. (Was: a suite. Is now: the one feature customers actually loved.)
2. **Zoom-out pivot** — the whole product becomes a single feature of something larger.
3. **Customer segment pivot** — same product, different customer. (The product works; the initial ICP was wrong.)
4. **Customer need pivot** — same customer, different problem. (You know who your customer is; the problem you were solving isn't the one they want solved.)
5. **Platform pivot** — application ↔ platform, or vice versa.
6. **Business architecture pivot** — high margin / low volume ↔ low margin / high volume (Geoffrey Moore's B2B / B2C axis reframe).
7. **Value capture pivot** — changing the monetization model. (Freemium ↔ subscription ↔ transaction ↔ ads.)
8. **Engine of growth pivot** — switching between viral, sticky, or paid growth engines.
9. **Channel pivot** — new distribution channel. (Direct ↔ partner ↔ marketplace.)
10. **Technology pivot** — same solution via a different technology. (Almost never worth doing alone; usually accompanies another pivot.)

**Real pivots are structural changes on ONE axis at a time.** A "same product, different customer, different channel, different pricing, different tech" is not a pivot; that's a new company. See the "pivot that's actually 5 pivots stacked" gotcha in `heuristics.md`.

### Runway = number of pivots remaining

Ries's reframe of runway:

> "Runway is really not money — it's the number of pivots you have left." — *The Lean Startup*.

Traditional framing: runway = months of cash / burn rate. Ries's framing: runway = how many meaningful experiments can you complete before you run out. **Practical consequence:** cutting burn without shortening experiment cycles extends the calendar but not the runway. Reducing time-per-experiment extends the *actual* runway.

## Innovation Accounting

How to measure progress inside a startup where every classical metric (revenue, users, retention) is close to zero. Ries's three-level maturity model:

### Level 1 — Actionable metrics baseline
Establish the current-state baseline of the actionable metrics that matter for the chosen **engine of growth** (see below). Get real numbers from real customers on the current MVP. Not "we think retention will be X"; "retention is X."

### Level 2 — Tuning the engine
Run experiments (feature improvements, funnel changes, onboarding tweaks) designed specifically to move the actionable metric. Cohort analysis and split tests are the two workhorse techniques. Each experiment produces a delta on the baseline; the deltas compound (or fail to).

### Level 3 — Pivot or persevere
Compare cumulative progress against what the business plan requires. Are we improving fast enough to make the business viable? If yes, persevere. If no despite repeated credible experiments, pivot. This is the strategic decision Level 2's tactical experiments feed into.

**Central to Innovation Accounting: actionable vs. vanity metrics.**

- **Vanity metrics** — totals that go up and to the right regardless of what you do. Pageviews, cumulative signups, cumulative downloads. Feel-good; not decision-useful.
- **Actionable metrics** — per-customer, per-cohort, causal. Ries's four preferred devices (from his 2009 Tim Ferriss guest post):
  1. **Split-tests (A/B)** — the only way to isolate causation from confound.
  2. **Per-customer metrics** — track individual behavior, not aggregates. If the metric moves and you can't say which individual customer's behavior changed, it's aggregated over too much noise.
  3. **Funnel / cohort analysis** — the same funnel, weekly or monthly, so you can see whether cohort N is behaving better than cohort N-1.
  4. **Keyword metrics** — for acquisition source quality. Not all acquisition is equal; the acquisition channel is often the biggest determinant of retention.

> "Vanity metrics might make you feel good, but they don't offer clear guidance for what to do." — Ries, guest post on tim.blog, 2009.

**Rule of thumb:** actionable metrics should be **as few as possible**, and each should be **traceable back to an individual customer** so you can follow up qualitatively.

## The engines of growth

Startups grow through exactly **three engines**, and generally only one at a time:

### Sticky engine
Growth = acquisition rate − churn rate. Wins when customers stay a long time (SaaS, B2B tools, storage, communication platforms). The critical actionable metric is **churn / retention**. Improving retention almost always beats accelerating acquisition when the sticky engine is running.

### Viral engine
Growth = new customers acquired per existing customer × cycle time. The critical actionable metric is the **viral coefficient (k)** — how many new users each existing user brings in. K > 1 = exponential growth; k < 1 = decay. Small changes in k dramatically change growth rate; small changes in cycle time dramatically change growth rate. Focus experiments there.

### Paid engine
Growth = margin per customer × acquisition efficiency. Wins when unit economics are positive (LTV > CAC by a meaningful multiple) and there's enough capital to scale acquisition. Critical actionable metrics: **CAC, LTV, payback period**, and the LTV/CAC ratio.

**Why one at a time:** the engine you pick determines the metric that matters, which determines the experiment. Trying to optimize all three at once means optimizing none.

## Small batches

Borrowed straight from Toyota Production System. **Do the smallest possible increment of work end-to-end (design → build → ship → measure), then repeat.** Small batches:

- Expose defects earlier (an error in a 1-day batch is caught tomorrow; an error in a 3-month batch is caught in Q2).
- Reduce cost of pivot (throwing away a 1-week experiment costs a week; throwing away a 3-month batch costs a quarter).
- Increase learning rate (one 3-month batch = one learning turn; twelve 1-week batches = twelve turns).

**Batch size is the hidden variable that determines learning speed.** Most teams don't consciously choose batch size — they inherit it from Scrum cadence, quarterly planning cycles, or release train scheduling.

## Continuous deployment

IMVU (Ries's own company) deployed to production **~50 times per day**. Ries's argument: **continuous deployment is not recklessness; it is the discipline that enables Build-Measure-Learn at the speed the method requires.**

**Backed by layered defenses** (all developed at IMVU):
- Developer sandboxes.
- Unit tests (100% coverage on critical paths).
- Continuous integration.
- Automated deployment.
- Monitoring + alerting.
- Andon Cord (any team member can halt a bad release).
- Five Whys post-mortems on every meaningful production incident.

Without those defenses, continuous deployment is a way to break production faster. With them, it's the mechanism that makes the BML loop measured in minutes instead of quarters.

## Five Whys

Ries's most direct import from Taiichi Ohno's Toyota Production System. When something goes wrong (bug, outage, missed launch, customer complaint), hold a structured post-mortem and **ask "why" five times** to move from surface symptom to systemic root cause.

**Ries's canonical example** (from his November 2008 startuplessonslearned.com post):

1. **Why was the site down?** → CPU spiked to 100%.
2. **Why did CPU spike?** → Infinite loop in code.
3. **Why was that code written?** → Developer error.
4. **Why wasn't it caught?** → No unit test.
5. **Why no test?** → New hire never trained on TDD.

> "Behind every seemingly technical problem is actually a human problem waiting to be found." — Ries, Five Whys post, startuplessonslearned.com, November 2008.

**Corrective action must be proportional at every level of the analysis.** Not just fix the loop — also add the test, update onboarding, and (at layer 5) rethink hiring/training. **Skipping the layers = repeating the failure.** This is the discipline that makes Five Whys real vs. Five Whys as template.

## Andon Cord

Also from TPS. **Any team member can "pull the cord" to halt a bad release** before it causes further damage.

Ries: this is **culture as much as tooling** — the person who stops the line is a hero, not a nuisance. Combined with Five Whys, it turns individual failures into system upgrades: pull the cord → stop the release → hold Five Whys → make proportional investments at each layer → resume.

**Andon Cord as Slack channel that nobody uses = anti-pattern.** See `heuristics.md`.

## Genchi Genbutsu ("go and see")

Ries cites this in *The Lean Startup* as the TPS principle Japanese lean practitioners cite most often as **the most important** principle of Lean. Literal Japanese: *"go to the real place; see the actual object."*

**In startup terms:** *"get out of the building"* (Ries credits Steve Blank / Customer Development for this phrasing). No secondhand data replaces watching a real customer struggle with your product in their own environment.

**Practical bar:** if the last time a team member watched a real customer use the product was more than 2 weeks ago, you're operating on dashboards, not on genchi genbutsu. Fix by scheduling recurring in-context observation (site visit, user interview, over-the-shoulder screen share).

## Integration

The devices fit together this way:

- **Extreme uncertainty** is the condition. If you don't have it, you don't need the method.
- **Validated learning** is the unit of progress under that condition.
- **Build-Measure-Learn** is the loop that produces validated learning. Planned in reverse — Learn → Measure → Build.
- **MVP** is the "Build" step done at minimum effort. Landing page, video, concierge, Wizard of Oz, piecemeal, single-feature.
- **Actionable metrics + cohort/split analysis** is the "Measure" step. Vanity metrics look like signals but aren't.
- **Innovation Accounting** aggregates the actionable metrics into a three-level maturity model that tells you whether you're making progress.
- **Pivot or Persevere** is the strategic decision the Innovation Accounting output feeds into. Held at fixed cadence. 10 named pivot types.
- **Runway = pivots remaining**, not months of cash. Reducing cycle time extends real runway.
- **Engines of growth** (sticky / viral / paid) determine which actionable metric matters.
- **Small batches + continuous deployment** are the operational disciplines that make the loop fast.
- **Five Whys + Andon Cord** are the operational disciplines that make continuous deployment safe.
- **Genchi Genbutsu** is the ground truth that keeps the metrics honest.

**If any layer is missing, the layers above and below strain.** A team doing "MVPs" without cohort analysis is guessing. A team doing continuous deployment without Five Whys is breaking things faster. A team pivoting without the pivot-or-persevere cadence is doing random walks.

## What this method is NOT

Ries is explicit about the boundaries:

- **Not a small-budget prescription.** "Lean" refers to Toyota's *lean manufacturing*, not to austerity. Scaling still requires capital.
- **Not "fail fast" as a slogan.** The point is learning fast; failure is a byproduct. Ries actively pushes back on "fail fast" culture.
- **Not a substitute for corporate strategy.** Lean Startup operates *below* strategy — it presupposes you know what business you're trying to build. If you don't, use Playing to Win (Martin), Good Strategy Bad Strategy (Rumelt), or 7 Powers (Helmer) *first*, then bring Lean Startup in for the tactical hypothesis testing.
- **Not for optimizing mature businesses.** Lean Startup is for new products under extreme uncertainty. Optimizing a known-good business is a different problem (Six Sigma, process optimization, operational efficiency work).
- **Not appropriate for Amazon-scale commitment altitude.** Amazon explicitly uses Working Backwards / PR-FAQ instead of MVP when the cost of a bad launch is measured in millions of trust-hits or tens of millions in commitment. See `applications.md` for the honest disagreement.
- **Not a rebrand of agile.** Agile is a delivery methodology. Lean Startup is a discovery methodology. They're complementary at different layers.

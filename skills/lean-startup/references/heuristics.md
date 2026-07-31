# The Lean Startup — Heuristics, Do's, Don'ts, Gotchas

> **This is the load-bearing file of this skill.** Everyone thinks they know Lean Startup. The vocabulary got out into the world faster than the discipline behind it. The heuristics below all exist because Ries has spent 15 years pushing back on how his method got degraded. When the user shows up with degraded vocabulary — "let's just ship the MVP", "fail fast", "build-measure-learn our way to product-market fit" — this file is what the skill needs to load first. Attribution is precise: this from the 2011 book, this from the 2008 startuplessonslearned.com post, this from a 2024 Lenny episode, this from the 2026 Incorruptible interview cycle.

## Meta-heuristic

**Ries's most-repeated framing since 2018:** *"Everyone thinks they know Lean Startup. Almost nobody is applying it as I described it."*

The default failure mode is **not** that people don't know the vocabulary; it's that they use the vocabulary without the underlying discipline. When you enter a session, your first move is often not to apply the method — it's to *reset the vocabulary*, then apply.

## The 4 misconceptions Ries himself flags

From [Lean Startup Co — "Eric Ries on 4 Common Misconceptions About Lean Startup"](https://leanstartup.co/resources/articles/eric-ries-on-4-common-misconceptions-about-lean-startup/):

### 1. "Lean means cheap / don't think big"
**Wrong.** "Lean" refers to *lean manufacturing* (Toyota Production System), not to austerity. The method is about **learning speed under uncertainty**, not budget minimization. Scaling still requires capital. Airbnb, Uber, and Slack all raised aggressive rounds and are canonical Lean Startup cases.

**Redirect:** if the user's read is "we should be lean = we should be small = we shouldn't raise capital", separate the two. Lean is about *how* you learn; capital is about *how much you can scale what you've learned*.

### 2. "Venture capital is unnecessary"
**Wrong.** Nothing about Lean Startup prescribes bootstrapping — it prescribes learning before pouring capital into the wrong thing. The right sequence is: validate hypotheses cheaply → raise to scale the validated engine. Not: don't raise.

### 3. "Lean startups embrace failure ('fail fast')"
**Wrong**, and Ries pushes back hard:

> "I hate the idea of 'fail fast.' It's like I'm trying to run a sprint, and you're like, 'OK. Breathe fast.'" — Ries, quoted in Lean Startup Co, "4 Common Misconceptions About Lean Startup."

**The point is fast learning, not fast failure.** Failure is a byproduct; learning is the goal. A culture that celebrates failure without extracting learning is just wasteful. When the user says "we're supposed to fail fast", correct the frame: *"you're supposed to learn fast; failure is one form learning sometimes takes."*

### 4. "Established companies gain nothing from Lean"
**Wrong.** The whole point of *The Startup Way* (2017) is that the method works in Fortune 500s when adapted with executive sponsorship, protected budget, cultural commitment, and tolerance for the J-curve. GE FastWorks, Toyota (yes, they invented the parts), Intuit, and Pitney Bowes are Ries's canonical enterprise cases.

> "They think startups are all about kids eating ramen noodles and wearing a black turtleneck." — Ries on why enterprises dismiss the method.

## DO's — how to apply the method the way Ries described

### Plan the BML loop in reverse — Learn first
Start from the hypothesis you need to test. Design the smallest experiment (Measure) that produces the data. **Then** decide what to Build.

Most teams start with Build and reverse-engineer a hypothesis to justify what they already wanted to make. Push back — that's a Gantt chart with lean vocabulary.

**Source:** *The Lean Startup*, chapter 5; reinforced in the 2024 Lenny retrospective.

### Redefine "done" as validated learning
A feature isn't done when it ships; it's done when the team knows whether the hypothesis was confirmed or falsified, and has decided pivot or persevere. This matches how Perri redefines "done" in *Escaping the Build Trap* — see [[escaping-the-build-trap]].

### Cohort analysis + split tests, always
Aggregate metrics lie. Split by cohort (weekly or monthly signup groups) and by treatment (A/B) to isolate causation from noise. The four Ries-preferred devices:
1. **Split-tests (A/B).**
2. **Per-customer metrics** — trackable back to an individual customer for qualitative follow-up.
3. **Funnel / cohort analysis** — same funnel, weekly or monthly.
4. **Keyword metrics** for acquisition source quality.

**Source:** [Ries's 2009 tim.blog guest post — "Vanity Metrics vs. Actionable Metrics."](https://tim.blog/2009/05/19/vanity-metrics-vs-actionable-metrics/)

### Regular pivot-or-persevere meeting
Fixed cadence — every few weeks to few months, calibrated to startup pace. Skip it and you drift into serial mini-pivots (pivot fatigue) or into obstinate perseverance past the point of validated falsification. The regularity is what makes the decision honest.

### Small batches at every scale
Design in small batches. Ship in small batches. Review in small batches. **Batch size is the hidden variable that determines learning speed.** Most teams don't consciously choose batch size — they inherit it from Scrum cadence, quarterly planning, or release-train scheduling. Consciously reduce.

### Get out of the building (genchi genbutsu)
No dashboard replaces watching a real customer struggle with the product in their own environment. Aggregate customer research is a supplement, not a substitute.

**Practical bar:** if the last time a team member watched a real customer use the product was more than 2 weeks ago, they're operating on dashboards, not on genchi genbutsu.

### Kill features that fail their hypothesis
The Ideas tier is generative; the Learn tier is selective. Being ruthless about killing failed features is what protects team capacity for the working ones.

### Do Five Whys after every meaningful failure
Post-mortem, five layers deep, **proportional investment at every layer** — not just the technical fix but also the training, the process, the hiring. Skipping the layers = repeating the failure.

**Source:** [Ries's original 2008 Five Whys post on startuplessonslearned.com.](http://www.startuplessonslearned.com/2008/11/five-whys.html)

### Attribute the lineage
When you introduce Andon Cord, Five Whys, Genchi Genbutsu, small batches, or continuous improvement — credit Taiichi Ohno / Toyota Production System explicitly. When you introduce "get out of the building" / Customer Development — credit Steve Blank. Ries himself is meticulous about attribution and this skill should carry the same discipline. Do not present TPS or Blank inventions as Ries's inventions; they're his *translations*.

## DON'Ts — misapplications Ries has warned about

### MVP as excuse for shipping garbage
The single most-repeated misapplication Ries fights. **An MVP is not a v0.1 you're ashamed of.** It's the smallest test that produces learning. If the test doesn't require code (Dropbox video, Wizard-of-Oz behind a landing page, concierge service you provide manually), then don't write code.

The industry heard "minimum" and "product" and skipped "viable" and "validated learning." The frequent failure mode: founder has an idea → builds "the MVP" → launches it → hopes → learns nothing because it wasn't structured as a hypothesis test.

**Redirect:** when the user says "let's ship an MVP", ask three questions before letting them build:
1. *What specific hypothesis is this MVP testing?*
2. *What metric will confirm or falsify that hypothesis?*
3. *What's the smallest thing that produces that metric — and does it require code at all?*

If they can't answer 1 or 2, they're not building an MVP; they're building a first version. If the answer to 3 is "no code required", stop them from writing code.

### "Fail fast" as slogan
See Ries's quote above. The point is **learning fast**, not failing fast. A culture that celebrates failure without extracting learning is just wasteful — and it inoculates the team against actual accountability for outcomes.

**Redirect:** rephrase "fail fast" as *"learn fast; failure is one form learning sometimes takes."* When the culture pushes toward failure-worship, ask *"what specifically did we learn from this failure that changes what we do next?"* If nothing, the failure was waste, not signal.

### Applying Lean Startup where the method doesn't fit
Ries is more careful about this than his fans. Lean Startup is for **new products or services under conditions of extreme uncertainty**. Applying it to:

- A mature business unit optimizing a known-good process → different problem (Six Sigma / process optimization / operational efficiency).
- A launch at Amazon-scale commitment altitude where a broken v0.1 destroys customer trust → use Working Backwards / PR-FAQ instead. See [[working-backwards]] and the honest disagreement in `applications.md`.
- Corporate strategy at the "which markets should we be in" altitude → different altitude (Playing to Win / Rumelt / 7 Powers).

**Redirect:** when the fit is wrong, name it. Don't force Lean Startup onto problems it wasn't designed for.

### Vanity metrics dressed up as OKRs
"Grew MAUs 40%" is a vanity metric unless the growth is decomposed into cohorts + causally linked to specific experiments. The number goes up as a function of ad spend, virality of unrelated content, seasonal effects, or acquisition-channel changes; it's not a signal a team can act on.

**Redirect:** apply the substitution test. If the metric is *aggregate*, *lagging*, and moved by many uncontrolled factors, it's still vanity even framed as an OKR. Push toward cohorted, causal, per-customer metrics.

### Build-Measure-Learn as a linear waterfall
Some teams treat it as: "This quarter we Build. Next quarter we Measure. Q3 we Learn." That's **not a loop; that's a Gantt chart with lean vocabulary.** The loop is *continuous*, and each turn should be *short* (days to weeks, not quarters).

**Redirect:** ask *"how many complete BML turns have you done in the last month?"* If the answer is 0 or 1, the loop isn't running.

### Pivot fatigue / serial pivoting
Every 3 weeks a new pivot because the metric didn't move. Two failure modes:
- (a) **Hypothesis wasn't sharp enough to falsify**, so any drop in the metric feels like proof.
- (b) The team is **running experiments without a coherent underlying vision**, so pivots are random walks.

**Redirect:** the fix is the vision + the regular pivot-or-persevere cadence, not more pivots. If the hypothesis was fuzzy, sharpen it before pivoting. If the vision is fuzzy, name that as the problem — no amount of tactical pivots fixes a strategic vacuum.

### Perseverance past the falsification
The mirror of pivot fatigue. The team keeps building because they love the product, past the point where cohort data has clearly falsified the core hypothesis. Ries calls this **"achieved failure"** — perfect execution of a plan nobody wanted.

**Redirect:** when the data has falsified the hypothesis and the team is still building, ask *"what evidence would we need to see to decide to pivot?"* If the team can't name the evidence, they've decided not to pivot regardless of data. Name that.

### Applying MVP thinking at Amazon-scale commitments
Amazon rejects MVP for launches at scale — see [[working-backwards]]. Their argument: at their scale, a broken v0.1 shipped to millions is catastrophic to trust, and the cost of a bad launch dwarfs the cost of weeks on a PR/FAQ.

**This is a real disagreement; both positions are defensible.** The resolution is **cost per bet**:
- Lean Startup thrives when experiments are cheap and learning speed dominates.
- Working Backwards thrives when commitments are expensive and launch quality dominates.

A team can (and often should) use Lean Startup for the discovery phase and Working Backwards for the commitment phase of the same product. See `applications.md`.

### Cargo-cult Toyota vocabulary without the discipline
- Andon Cord as a Slack channel that nobody uses.
- Five Whys as a template that produces surface answers because nobody made the "proportional investment at every layer."
- Genchi Genbutsu as a slogan not backed by actual customer visits.
- Continuous deployment without the layered defenses (sandboxes, unit tests, CI, monitoring, Five Whys post-mortems).

**The vocabulary without the practice is worse than not adopting the vocabulary** — it inoculates the team against the real thing. If asked to introduce these devices, be honest about the underlying discipline required.

## Gotchas — things that go wrong even when you think you're doing it right

### The "actionable" metric that's actually a vanity metric in disguise
"Weekly active users" sounds actionable. It's a lagging aggregate that moves for many reasons. To be actionable it must be **cohorted, causally-linked, and per-customer or per-cohort**.

**Substitution test:** if the metric moves and you can't say which experiment caused the change, it's still vanity.

### The pivot that's actually 5 pivots stacked into one
"Same product, different customer, different channel, different pricing model, different tech stack." That's not a customer-segment pivot; that's a new company. **Real pivots are structural changes on one axis at a time.** Otherwise you can't tell which change caused the result.

**Redirect:** when the user describes "the pivot", ask them to name which of Ries's 10 pivot types this is. If the answer is "well, actually all of these", stop them — they need to sequence pivots, not stack them.

### The MVP that's actually a full product
If the team spent months on the MVP, it's not an MVP. Ries's bar: **what's the smallest thing that answers the question?** If the answer is "a landing page" or "a Zapier prototype" or "a concierge service we run manually," and the team built a full-featured app instead, they built too much.

### Innovation accounting reduced to a dashboard
The three levels of Innovation Accounting are not "add three more charts to Looker." They're a **maturity model of what you're measuring and why.** Adding metrics without the underlying discipline reproduces the vanity-metrics problem at higher volume.

**Test:** can the team articulate which level they're at (baseline / tuning the engine / pivot-or-persevere), and can they name the actionable metric that defines their current engine of growth? If not, the dashboard is decoration.

### Applying Lean Startup inside a mature business unit as if it were a startup
*The Startup Way* (2017) is explicit: enterprise applications need **executive sponsorship, protected budget, protected team, tolerance for zero-revenue years, and an explicit accountability structure separate from BAU.** Without that scaffolding, Lean Startup inside an enterprise is quickly killed by quarterly-earnings pressure. See GE FastWorks — it partially unwound after Immelt's departure.

**Redirect:** when applying inside an enterprise, first check for the scaffolding. If it's not there, the method won't stick regardless of how well you apply it. See `post-book.md` §2.

### The team that does BML in Q1, then "moves to execution" in Q2
Fatal confusion. BML is not a phase; it's the operating rhythm. "Moving to execution" is a linear-waterfall reversion. If the team is at a point where the hypothesis is validated and they're scaling the validated engine, they've moved from validated learning into growth — which is where the engine-of-growth work becomes primary — but they haven't abandoned BML; they've narrowed its scope to the growth engine.

### The founder who ran BML for years but now needs to protect the mission
This is what *Incorruptible* (2026) exists to address. **Lean Startup teaches you how to find the business; it does not teach you how to protect the mission from financial gravity once you've found the business.** Redirect to `post-book.md` §3 — the governance frame.

## Pro tips — accelerators Ries uses in his own teaching

### The "what do we need to learn?" opener
Ries opens most method-teaching sessions with this question, not with "what are you building?" It resets the frame from Build-first to Learn-first. Reach for it in the skill's responses.

### The definitional reset before deployment
When the user uses "MVP" / "pivot" / "fail fast" / "actionable metric", restate the definition first. This is a load-bearing move, not a stylistic tic. Perri does the same thing in her frame — see [[escaping-the-build-trap]].

### The TPS-lineage credit
Every time you introduce Andon Cord, Five Whys, Genchi Genbutsu, small batches, kaizen — attribute to Ohno / TPS explicitly. Ries never lets his audience forget where these come from. Neither should the skill.

### The IMVU story as origin proof
When explaining why the method exists, reach for IMVU: the wrong first product (40k lines of code thrown away), the customer development audit under Steve Blank, the 50-deploys-per-day cadence, the eventual $10M run rate. It grounds the method in a specific founder's specific mistakes.

### The self-critical retrospection move
When challenged that "Lean Startup has been misapplied", agree — Ries has said this publicly for years. Don't defend the misapplications. Name what the method actually is and what it isn't. This is not a defensive posture; it's Ries's own posture since ~2018.

### Compose, don't collapse
When Torres (continuous discovery), Cagan (empowered product teams), Perri (build trap), Blank (customer development), or JTBD (Moesta/Kalbach) come up, compose them explicitly rather than blend them. Each maps to a specific altitude or phase; the value is in naming which piece fits where. See `applications.md`.

## Language and vocabulary — say this, not that

Small phrasing shifts that carry method:

| Instead of | Use | Because |
|---|---|---|
| "Ship the MVP" | "Run the smallest test that produces validated learning" | MVP has been degraded to "small first version to ship"; the phrase-rewrite blocks the misapplication |
| "Fail fast" | "Learn fast" | Ries hates "fail fast" (see quote above) |
| "Build-Measure-Learn" (as a phase) | "Build-Measure-Learn loop" (as a rhythm) | It's a continuous cycle, not a sequence of phases |
| "Weeks of cash" | "Number of pivots remaining" | Ries's reframe of runway |
| "MAUs / total signups / cumulative downloads" | "Cohort retention / per-customer conversion / cohort funnel" | Vanity → actionable |
| "The team pivoted" (vague) | "The team ran a [zoom-in / customer-segment / value-capture / etc.] pivot" | Name the axis |
| "We need a Product Ops team" | "We need to close the specific evidence gap in [data / research / process]" | Same anti-pattern as `[[escaping-the-build-trap]]` heuristics |
| "Move fast and break things" | "Continuous deployment with layered defenses" | Continuous deployment isn't recklessness; it's the discipline that makes speed safe |
| "Customer development" | "Customer development (Steve Blank)" | Always credit Blank |
| "Andon Cord / Five Whys / Genchi Genbutsu / small batches" | "Andon Cord / Five Whys / Genchi Genbutsu / small batches (Toyota Production System / Taiichi Ohno)" | Always credit TPS |
| "Product-market fit" | "Product-market fit (Marc Andreessen coinage; the outcome Lean Startup's search phase is trying to reach)" | Not Ries's term; it's the goal the method targets |
| "Validated" (used loosely) | "Validated learning — the hypothesis was tested and either confirmed or falsified" | "Validated" alone gets used to mean "someone liked it" |

## Voice reminders when applying this section

- Reset vocabulary *before* applying the method. Definitional reset is a first-order move.
- Attribute the lineage (TPS / Ohno / Blank) explicitly. This is discipline, not decoration.
- Self-critical about the movement's misapplications. Ries is; the skill is.
- Push back on "fail fast" — verbatim if useful.
- Ask "what do we need to learn?" before "what should we build?"
- When the fit is wrong (Amazon-scale commitment, mature-business optimization, corporate strategy altitude), redirect honestly rather than force the method.

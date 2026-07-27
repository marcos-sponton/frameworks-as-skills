# Escaping the Build Trap — Material posterior al libro

> **This is the differential of this skill.** The 2018 book *Escaping the Build Trap* laid down the diagnosis, the 4-tier strategy deployment, the Problem Roadmap, and the Product Kata. Since then, Melissa Perri has published:
> - **A second book:** *Product Operations* (with Denise Tilles, 2023) — the Three Pillars framework.
> - **The Four Dimensions of a Great Product Management Organization** (blog, Jul 2024) — her post-book audit model.
> - **Weekly podcast episodes since 2020** on the *Product Thinking* podcast (271+ episodes as of June 2026), including *Dear Melissa* Q&A and guest CPO interviews.
> - **Active Substack essays** since 2023 — including the "one throat to choke" argument, the Founder Mode critique, and the Fuzzy Strategy diagnostic.
> - **Ongoing LinkedIn commentary** through 2026 on AI + PM and the State of AI in Product 2026 report.
>
> Most Claude responses about "Escaping the Build Trap" pull from the 2018 book alone. This file captures the eight years of subsequent refinements — new frameworks, updated positions, adjacent critiques, and current 2025–2026 themes. Organized so you can pull the specific piece you need.

## 2.1 Second book: *Product Operations* (with Denise Tilles, Oct 2023)

Full title: *Product Operations: How successful companies build better products at scale.* Amazon: [B0CK3HL4WF](https://www.amazon.com/Product-Operations-successful-companies-products/dp/B0CK3HL4WF).

The book operationalizes the definition Perri had used publicly since 2019:

> "Product operations is the art of removing obstacles from evidence-based decision making." — [Product Operations: The Fuel for Winning Product Strategies, 2019](https://melissaperri.com/blog/2019/7/19/product-operations-the-fuel-for-winning-product-strategies).

Cagan cites this definition explicitly as the one he uses (*Transformed*, 2024). Perri and Cagan converged on the term; Cagan credits her.

### The Three Pillars — canonical framework from the book

Detailed in `method.md`. Quick reference:

1. **Data & Insights** — instrumenting the product; aggregating usage + business data; making metrics queryable so PMs decide with evidence.
2. **Customer & Market Insights** — research ops; systematizing interviews and competitive intel.
3. **Process & Governance** — cadences, standards, tooling, prioritization frameworks; PM effort spent on judgment, not admin.

**Case studies used in the book:** Stripe, Uber, Fidelity. See `examples.md` for depth.

**Cross-reference:** [Lenny's guide with Perri on Product Ops](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-product-operations).

### Where Product Ops fails in practice
The book is not just prescriptive — it names the failure modes. Two are worth flagging in any session:

- **Product Ops as PMO in disguise.** Real Product Ops removes obstacles. Fake Product Ops adds them (templates, ceremonies, process theater).
- **Product Ops without Product Strategy above it.** If there's no Strategic Intent to serve, Product Ops fills the vacuum with process. See `heuristics.md`.

## 2.2 "Four Dimensions of a Great Product Management Organization" (Jul 2024)

Introduced in [Building a Great Product Management Organization (Jul 2024)](https://melissaperri.com/blog/2024/7/16/building-a-great-product-management-organization). This is her **post-book diagnostic model** — the audit checklist for a PM organization.

### Dimension 1 — Product Organizational Design
- Job role design — what does a PM actually do here?
- Product skill level — career ladders, hiring bar, promotion criteria.
- Structure around products — teams organized around value streams, not components.

### Dimension 2 — Product Strategy
- Strategic alignment to business — do product bets support business bets?
- Strategy creation & deployment — the 4-tier model from the 2018 book.
- Roadmapping & prioritization — Problem Roadmap; two-roadmap model.

### Dimension 3 — Product Operations
- Data & insights
- Customer & market research
- Process & governance
- (The Three Pillars from the 2023 book.)

### Dimension 4 — Product Culture
- Customer-centric mindset
- Outcome focus & incentives — team-level OKRs, not individual.
- Continuous learning
- Leadership & empowerment

**How to use it in a session:** score each dimension 1–5 with the client. Attack the weakest. Not a linear "do 1 then 2" plan. Perri is explicit: strong orgs have all four; weak orgs usually have one dimension propping up the illusion of health — usually Culture (the vocabulary) without the underlying Strategy or Ops.

## 2.3 Position on the "Product Operating Model" debate

Marty Cagan / SVPG owns the phrase **"Product Operating Model"** as a book title (*Transformed*, 2024). **Perri does not compete for that term** — she operates one level down.

Cagan explicitly credits her definition of Product Ops as the one he uses. Their frames are complementary, not overlapping:

- **Cagan** = organizational transformation. Top-level exec conversation. How does the whole company reorganize to be product-led?
- **Perri** = the operational infrastructure that makes that transformation stick + PM career + PM function health. One altitude below.

When Perri talks about a "Product Management Operating Model" in the 2023 *Product Operations* book, she means the internal operating rhythm of a PM function — career ladders, decision rights, cadences. Not the top-level org phrase.

**When responding on her behalf:** if the user is asking about Product Operating Model at the top level, credit Cagan and use this skill for the operational scaffolding underneath. Don't compete on the term.

## 2.4 Roadmap critique — evolved since 2014

Original: [Rethinking the Product Roadmap (May 2014)](https://melissaperri.com/blog/2014/05/19/rethinking-the-product-roadmap) — introduced the **Problem Roadmap**. Themes, hypotheses, solutions. No features before validation.

**Refined position (post-2019),** now split into two artifacts. See [Produx Labs — Setting the Roadmap](https://www.produxlabs.com/blog/setting-the-roadmap):

### Outcome-driven roadmap — internal document
- Audience: design + engineering + PM.
- Content: themes, outcomes, hypotheses.
- No committed features until validated.
- Starts vague (theme + outcome), gets concrete post-validation (hypothesis → solution).

### Feature-driven roadmap — external document
- Audience: sales + customers.
- Content: only things believed ready to ship, with buffer.
- Explicit "exploring, subject to change" tag for later items.
- Includes what's *not* being built and why, to manage expectations.

**Why the split matters:** the pre-2019 single roadmap conflated two audiences with two different needs. Internal audiences need honesty about uncertainty; external audiences need commitment about the near term. The split resolves the conflict without lying to either.

**Her verbatim, still-current position:**
> "The roadmap has become the symbol in many organizations of everything that is wrong with how they develop products." — [2014](https://melissaperri.com/blog/2014/05/19/rethinking-the-product-roadmap).

## 2.5 Recurring 2024–2026 themes

### Founder Mode critique (Sep 2024)

Perri's response to Brian Chesky's "Founder Mode" essay and the follow-on discourse.

> "Just because you made it from 0 to 1 doesn't mean you inherently know how to scale." — [My Thoughts on Founder Mode… and Why It's Dangerous, Sep 2024](https://melissaperri.substack.com/p/my-thoughts-on-founder-mode-and-why).

**Her structural argument:**
- 0→1 requires founder-level hands-on control. Correct.
- 1→N requires building an operating structure that runs *without* the founder in the details.
- Founder Mode as a *scaling doctrine* confuses the two. It valorizes the 0→1 pattern past the point where it's productive.
- Counter-example she uses: Mark Zuckerberg / Meta. A founder who "actively learns and adapts" and surrounds himself with experienced operators. See `examples.md`.
- Foil: Brian Chesky / Airbnb. Her earlier 2023 post [Are We Getting Rid of Product Managers?](https://melissaperri.blog/2023/7/7/are-we-getting-rid-of-product-managers) already anticipated this.

**When to invoke in a session:** any time the user is defending "the founder should own X at the team level" past the company's scale. Or when a founder-led company is losing PM talent because there's no room to make decisions.

### "One throat to choke" anti-pattern (Jun 2024)

> [Why are we making Product Managers the 'one throat to choke'?](https://melissaperri.substack.com/p/why-are-we-making-product-managers)

Perri's diagnosis: PMs get made "the 'one throat to choke'" while other functions avoid ownership. It's the mini-CEO myth in accountability form — hold the PM responsible for outcomes they can't control alone.

**Her fix:**
> "Stop assigning individual OKRs. Make them team-level."

**When to invoke in a session:** whenever an org is talking about firing/replacing PMs for missed outcomes, or when PM turnover is high. The pattern is almost never a PM-performance problem; it's an accountability-structure problem.

### "Fuzzy Strategy" diagnostic (Oct 2024)

> [How to Get Clarity When Your Company's Strategy is 'Fuzzy'](https://melissaperri.com/blog/2024/10/22/how-to-get-clarity-when-your-companys-strategy-is-fuzzy).

Method for the common case where an exec team believes it has strategy, but downstream teams can't act on it. Perri borrows **Joshua Arnold's 4 value drivers** as the discipline:

1. **Increase Revenue** — new customers, new segments, higher ARPU.
2. **Protect Revenue** — retention, defensive moves against churn.
3. **Reduce Costs** — operational efficiency inside existing business.
4. **Avoid Costs** — future risks or expenses averted.

Every strategic initiative should be traceable to one of these. If it can't be, it's not a strategic initiative — it's likely one of two patterns Perri coined:

- **Make More Money Syndrome** — a financial target ("grow 30%") stated as if it were strategy, without any mechanism.
- **Pet Projects** — solutions disguised as strategy. An exec's favorite feature idea elevated to "strategic initiative" without evidence it moves the business.

**Her load-bearing sentence:**
> "You don't need perfect strategic clarity to make good product decisions." — same essay.

The point is not to demand clarity from the exec team before the product function can move. It's to force the fuzziness into the open so the product function can build against it.

**When to invoke in a session:** any time the user says "our strategy isn't clear" as a reason for paralysis. Apply the 4 value drivers to force articulation.

### AI + PM (2025–2026)

Perri's current theme, discussed on the podcast (Ep 271, "The Gap Between AI Adoption and AI Strategy", Jun 2026) and on LinkedIn through 2026.

**Her load-bearing frame:**
- **AI as multiplier, not equalizer.** AI amplifies whatever operating model you already have. Strong PM function + AI = accelerated outcomes. Weak PM function + AI = accelerated build trap.
- **Bottleneck is upstream — discovery + decisions.** AI is useful for delivery, but delivery isn't where product orgs are stuck. They're stuck at "what to build and why". AI doesn't fix that.
- **Only ~1/3 of leaders say AI is strengthening their operating model.** From State of AI in Product 2026 survey (n=309 PM leaders, co-published with Product Circle).

**Her LinkedIn signature quote for the theme:**
> "Strategy is useless to AI until you turn it into instructions it can actually read." — LinkedIn 2026.

**Source:** State of AI in Product 2026, co-published with Product Circle. Podcast Ep 271.

**When to invoke in a session:** any time the user is asking "how do we adopt AI in our product organization?" — redirect to *"what's the operating model AI is amplifying?"* first.

### "Rethinking what Done means" (May 2026)

Podcast Ep 268 topic. The refined definition of "done" inside a Product-Ops-mature org.

**Old definition:** shipped to production.
**Perri's refined definition:** *shipped AND the hypothesis has been evaluated against the outcome*.

Under the refined definition, a feature isn't "done" when it's live — it's done when the team has data on whether it moved the metric it was meant to move, and has decided to keep it, iterate on it, or roll it back.

### "How OKRs Become Outputs Instead of Outcomes" (Apr 2026)

Podcast Ep 267. The most-referenced OKR failure mode.

**The pattern:** organizations adopt OKRs but keep them individual + top-down + tied to executive compensation. Objectives become quarterly output commitments; Key Results become milestone dates. The vocabulary is OKRs; the practice is MBO with different labels.

**Her fix:**
- OKRs at team level, not individual.
- Objectives at the *outcome* altitude (customer or business behavior change).
- Key Results as measurable movement of that outcome, not as shipped-artifact milestones.
- Individual executive comp decoupled from OKR attainment (so gaming the system doesn't produce personal gain).

## Adjacent frameworks Perri has commented on since 2018

Compatibility mapping she's discussed in podcasts and essays. See `applications.md` for a deeper table.

- **Cagan / Product Operating Model** — complementary, one altitude apart. See §2.3 above.
- **Torres / Continuous Discovery Habits** — highly compatible. Perri promotes Torres explicitly (Ep 269, May 2026: *"Continuous Discovery Habits That Actually Work"*). Torres's Opportunity Solution Tree fits inside Perri's Kata / problem-exploration loop.
- **Singer / Shape Up (Basecamp)** — rarely cited directly but consistent. Shape Up is a delivery cadence; Perri's frame is broader (career, strategy, culture, ops). She'd say Shape Up solves the delivery-side of the build trap but not the strategy-vacuum-above-teams problem.
- **JTBD (Christensen / Moesta / Kalbach)** — compatible. She uses "problem" as her primary unit, not "job", but the underlying discipline (understand demand before designing supply) is the same. Stays in "customer problems" language for accessibility.
- **Lean Startup (Ries)** — foundational influence. She keeps "build-measure-learn" and MVP concept but explicitly redefines MVP as "minimum effort to learn" and prefers "solution experimentation" to break the association of MVP with "small first version to ship."
- **OKRs (Doerr / Grove)** — uses OKRs, but with two constraints: team-level not individual, and must roll up from Strategic Intent. Warns against OKRs used to enforce output targets.
- **HEART (Google) and AARRR / Pirate Metrics (McClure)** — recommends by name for team-level metrics inside the Kata.
- **SAFe** — explicitly does *not* recommend.
- **The Product Operating Model as top-level org transformation** — Cagan's phrase, Cagan's book. She defers.

## Direct quotes worth having on hand

Quotes from post-book material that crystallize points better than the 2018 book does. Attributed with source.

> "The build trap is when organizations become stuck measuring their success by outputs rather than outcomes." — *Escaping the Build Trap*, 2018.

> "Product operations is the art of removing obstacles from evidence-based decision making." — [2019](https://melissaperri.com/blog/2019/7/19/product-operations-the-fuel-for-winning-product-strategies).

> "Just because you made it from 0 to 1 doesn't mean you inherently know how to scale." — [Sep 2024](https://melissaperri.substack.com/p/my-thoughts-on-founder-mode-and-why).

> "Stop assigning individual OKRs. Make them team-level." — [Jun 2024](https://melissaperri.substack.com/p/why-are-we-making-product-managers).

> "You don't need perfect strategic clarity to make good product decisions." — [Oct 2024](https://melissaperri.com/blog/2024/10/22/how-to-get-clarity-when-your-companys-strategy-is-fuzzy).

> "Strategy is useless to AI until you turn it into instructions it can actually read." — LinkedIn 2026.

> "It's only hard to prioritize because you don't have a product strategy." — [Oct 2019](https://melissaperri.com/blog/2019/10/31/prioritization).

> "Good prioritization is based on cold, hard facts. When you have data and you have a clear strategy, prioritization becomes easy." — [same source](https://melissaperri.com/blog/2019/10/31/prioritization).

> "Don't just turn your product owners into order-takers. Empower them to engage in discovery, customer conversations, and prioritization." — [Lenny's Newsletter with Perri](https://www.lennysnewsletter.com/p/product-owners-melissa-perri).

> "If your product owner is spending 40 hours a week writing user stories for things that are already working, you have a problem." — [same source](https://www.lennysnewsletter.com/p/product-owners-melissa-perri).

> "If you're already talking to your team daily and breaking down tasks collaboratively, great! You probably don't need a rigid Scrum framework." — [same source](https://www.lennysnewsletter.com/p/product-owners-melissa-perri).

> "Product Management has always firmly sat between business, tech, and the user/customer. … I don't think Product Management is going anywhere." — [Are We Getting Rid of Product Managers? 2023](https://melissaperri.com/blog/2023/7/7/are-we-getting-rid-of-product-managers).

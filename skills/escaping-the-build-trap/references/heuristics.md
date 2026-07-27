# Escaping the Build Trap — Heuristics, Do's, Don'ts, Gotchas

> The practical devices — the diagnostic tells and operational moves — that separate applying Perri's frame well from doing the version she spends most of her airtime critiquing. Attribution is precise: this comes from the book, this from a 2024 Substack essay, this from a 2026 podcast episode where she updated a position.

## Symptoms you're in the Build Trap

Perri's diagnostic checklist. If you can nod at more than three of these, you're in it.

- **Success is measured by features shipped, velocity, releases** — not by customer or business outcomes.
- **The backlog is always full. The team is always shipping. Customer satisfaction and business metrics are flat.**
- **PMs spend >30% of their week writing user stories for things that already work.** Perri's specific bar: *"If your product owner is spending 40 hours a week writing user stories for things that are already working, you have a problem."* — [Lenny's Newsletter with Perri](https://www.lennysnewsletter.com/p/product-owners-melissa-perri).
- **Roadmap items are locked commitments to specific solutions before problems are validated.**
- **Nobody can articulate the company strategy in one sentence** — multiple execs give different answers.
- **The team can't name the metric that would prove a feature "worked."**
- **Every stakeholder request becomes a ticket.** No push-back happens. The PM is a mailbox, not a decision-maker.
- **Sales contracts contain feature promises that then drive the roadmap.** The roadmap is a downstream artifact of the sales process, not the product strategy.
- **OKRs are individual, not team-level, and roll up to executive compensation.** The org has hijacked OKRs into an MBO-style performance-management system.
- **"Product Owner" is used as a synonym for "PM"** — a Scrum-ceremony fill-in role rather than a strategic function.

## Do's for product-led organizations

### Structure teams around value streams, not components or features
A team that owns "the checkout flow" (a component) will optimize the component. A team that owns "increase completed transactions per visitor" (a value stream) will make cross-cutting decisions. Value streams are the unit of Product Initiative ownership.

**Source:** *Escaping the Build Trap*; Product Thinking Ep 260 "Avoiding Common Mistakes in Org Design" (Jan 2026).

### Deploy strategy in 4 tiers: Vision → Strategic Intent → Product Initiatives → Options
See `method.md`. Every team-level decision should be traceable up the tiers. If the chain breaks, the strategy isn't deployed.

### Make OKRs team-level, not individual
Individual OKRs create siloed fiefdoms and re-create the "one throat to choke" pathology. Team-level OKRs force collaboration and match the reality that outcomes require multiple functions.

**Source:** [Why are we making Product Managers the 'one throat to choke'?, Jun 2024](https://melissaperri.substack.com/p/why-are-we-making-product-managers).

### Roadmap in themes/outcomes/hypotheses internally; commit to features only after validation
The Problem Roadmap. Features never appear before validation. See `method.md`.

### Publish two roadmaps: internal (outcome-driven) + external (feature-driven, with "exploring" tag)
Post-2019 refinement. Same underlying honesty; different artifacts for different audiences. External roadmap only lists things believed ready to ship, with buffer + explicit "exploring, subject to change" for later items.

**Source:** [Produx Labs — Setting the Roadmap](https://www.produxlabs.com/blog/setting-the-roadmap); `post-book.md` §2.4.

### Run the Product Kata weekly
Goal → current state → obstacle → next step → hypothesis → learning. See `method.md`. The Kata is the operational cadence that keeps discovery alive.

### Use HEART for UX metrics, AARRR for growth
Two frameworks she recommends by name for team-level metrics inside the Kata.
- **HEART** (Google) — Happiness, Engagement, Adoption, Retention, Task success.
- **AARRR / Pirate Metrics** (Dave McClure) — Acquisition, Activation, Retention, Referral, Revenue.

### Fund and staff Product Operations early
Don't wait until the PM function is drowning. Product Ops is the *fuel* — it makes evidence-based decisions possible. See the Three Pillars in `method.md`.

**Source:** [Product Operations: The Fuel for Winning Product Strategies, 2019](https://melissaperri.com/blog/2019/7/19/product-operations-the-fuel-for-winning-product-strategies).

### Empower PMs to push back on stakeholder requests
Especially when the request is a solution to an unvalidated problem. This is the difference between a PM and an order-taker.

> "Don't just turn your product owners into order-takers. Empower them to engage in discovery, customer conversations, and prioritization." — [Lenny's Newsletter with Perri](https://www.lennysnewsletter.com/p/product-owners-melissa-perri).

### Train PMs on the tactical/strategic/operational progression
Hire and promote against it. Career ladders anchored on this progression prevent the entire PM function from ossifying into Waiter roles.

### Fall in love with the problem
> "Fall in love with the problem you are solving." — *Escaping the Build Trap*.

The anti-solution-obsession move. Discovery time is time spent understanding the problem, not sketching the interface.

### Kill bad ideas fast
> "Kill the bad ideas before they take up too much time and energy from the teams." — *Escaping the Build Trap*.

The Options tier is generative; the Kata is selective. Being ruthless about killing bad options is what protects the team's time for the good ones.

## Anti-patterns (name them explicitly)

Perri names anti-patterns bluntly. When you spot one, use her name for it — the naming is part of the fix.

### Waiter PM
The order-taker. No strategic point of view. Takes requests from sales/support/execs and turns them into tickets.

> "There is no goal. There is no vision. There is no decision making involved. Waiters are reactive thinkers, not strategic thinkers." — *Escaping the Build Trap*.

**Redirect:** rewrite the PM job description to include discovery, prioritization authority, and outcome ownership. Retrain (Product Institute is her own answer). If the org structurally can't support a non-Waiter PM, the problem is one level up — the exec team hasn't decided that PMs are strategic.

### Mini-CEO PM (the myth)
> Job postings that say "PM is the mini-CEO of the product" but give the person no authority over budget, engineering, or hiring.

Perri dismantles this every chance she gets. The pattern sets PMs up to fail and produces the "one throat to choke" trap.

**Redirect:** stop using the phrase. Name what a PM *actually* owns (problem framing, discovery, prioritization within their initiative) and what they *don't* (engineering resourcing, revenue targets, cross-functional headcount). Give them decision rights matching their responsibilities.

### Former-PM PM (former project manager)
Obsessed with "when" (dates, velocity, sprints) and ignores "why" (customer problem, business outcome). Common in orgs that rebranded PMs after a waterfall-to-agile transition without retraining.

### Roadmap-as-contract
The roadmap becomes a Gantt chart of committed features with dates, delivered as a contract to sales/customers.

> "The roadmap has become the symbol in many organizations of everything that is wrong with how they develop products." — [Rethinking the Product Roadmap, 2014](https://melissaperri.com/blog/2014/05/19/rethinking-the-product-roadmap).

**Redirect:** split into two roadmaps (see Do's above). Internal outcome-driven; external feature-driven with "exploring" tag.

### Feature-factory culture
Velocity as virtue. Number of features shipped as the KPI. The build trap in its purest form.

**Redirect:** replace feature-count KPIs with outcome KPIs at the team level. Introduce the Product Kata. Make "what did we kill this quarter?" a first-class question in reviews.

### HIPPO-driven prioritization (Highest-Paid Person's Opinion)
The most senior person in the room decides which feature ships next, without data or discovery.

**Redirect:** structure decisions as "what did we learn from customers this week?" not "what does the CEO want?" Give the PM data and research to push back with.

### Peanut-buttering strategy
Too many initiatives, no resource concentration. Every team gets a thin slice; nothing gets enough resources to actually move.

**Redirect:** apply Strategic Intent — 1–3 large bets, not 15 small ones. Kill or defer the rest. This is where Perri's frame overlaps with Rumelt's *diagnose → guiding policy → coherent action* (see `applications.md`).

### Make More Money Syndrome
> A financial target ("grow revenue 30%") stated as if it were a strategy, without any mechanism.

**Source:** [How to Get Clarity When Your Company's Strategy is 'Fuzzy', 2024](https://melissaperri.com/blog/2024/10/22/how-to-get-clarity-when-your-companys-strategy-is-fuzzy).

**Redirect:** ask *how* — via which customer, via which value proposition, via which channel? Use Joshua Arnold's 4 value drivers (Increase Revenue / Protect Revenue / Reduce Costs / Avoid Costs) to force the mechanism into the open.

### Pet Projects (solutions disguised as strategy)
An exec's favorite feature idea gets elevated to "strategic initiative" without any evidence it moves the business.

**Redirect:** run the Kata on it. What outcome would it move? What's the hypothesis? What experiment would validate it? Most Pet Projects don't survive the first two questions.

### Founder Mode as scaling doctrine
The founder maintains 0→1 hands-on control past the point where the company scales past their attention.

> "Just because you made it from 0 to 1 doesn't mean you inherently know how to scale." — [My Thoughts on Founder Mode, 2024](https://melissaperri.substack.com/p/my-thoughts-on-founder-mode-and-why).

**Redirect:** distinguish 0→1 (founder should be in the details) from 1→N (founder should build the operating structure that runs without them). See her Meta/Zuckerberg counter-example in `examples.md`.

### Individual executive OKRs
> Individual OKRs create siloed fiefdoms and reward local optimization over collective outcomes.

**Source:** [Why are we making Product Managers the 'one throat to choke'?, Jun 2024](https://melissaperri.substack.com/p/why-are-we-making-product-managers).

**Redirect:** OKRs at the team level, not individual. Executive compensation tied to team-level outcomes.

### "One throat to choke" accountability
PMs made accountable for outcomes they can't drive alone — because engineering headcount, marketing spend, or sales strategy are outside their control.

**Redirect:** distribute accountability across the trio (PM + design + eng) or across the value stream. Kill individual PM OKRs. Reframe outcome ownership as team-level.

### SAFe (and other prescriptive scaled-agile frameworks)
Perri explicitly does not recommend SAFe.

**Redirect:** small-team autonomy anchored in Strategic Intent. Coordination via shared outcomes, not shared ceremonies.

### Certifications-as-training (without mentorship)
Surface credentials without the depth that comes from applied practice. Common in orgs that "invest in PM development" by buying course licenses.

**Redirect:** apprenticeship + mentorship. The Product Institute model (her own) is her answer, but the principle generalizes.

### Discovery skipped in the roadmap
No time budgeted for research, validation, or experiments. Every sprint is a delivery sprint.

**Redirect:** budget discovery time explicitly (10–20% of team capacity is her rough bar). Make discovery outcomes visible in reviews.

## Common misapplications (companies that *claim* product-led)

### Rebrand PMs as "product owners" without changing the job
Still order-takers. The Scrum ceremony fits; the strategic function doesn't exist.

### Adopt OKRs but keep them individual and top-down
They become outputs disguised as outcomes. Ep 267 topic: *"How OKRs Become Outputs Instead of Outcomes."*

### Build a Product Ops team that becomes a process police / PMO in disguise
> Real Product Ops *removes* obstacles. Fake Product Ops *adds* them.

Test: if your Product Ops team is producing more templates than PMs are producing decisions, you've built the wrong thing.

### Add "outcome" language to feature roadmaps without changing the underlying prioritization
The vocabulary is Perri's; the practice is still feature-factory. Test: do you kill features that fail to move the outcome, or do you ship them anyway?

### Hire a CPO with no authority over engineering priorities or budget
Perri: this is the "mini-CEO" pattern at the exec level. The role fails inside 18 months.

### Assume Product Ops is only for large orgs
Perri's counter: even a 50-person company benefits from *one* person owning the Three Pillars. The infrastructure matters more than the headcount.

## Gotchas (things that go wrong even when you think you're doing it right)

### The "we already have a strategy" trap
Exec team believes they have a strategy because there's a slide deck. Product function can't articulate what problems the strategy commits them to solving. The exec-level artifact and the team-level reality are disconnected.

**Redirect:** run the 4-tier deployment test. Can a random PM articulate their Product Initiative and trace it to a Strategic Intent? If not, the strategy is theater.

### The Product Ops team stood up before Product Strategy
Product Ops is the *fuel* for evidence-based decisions. If there's no strategy above it, Product Ops has nothing to serve. It defaults to process work (templates, cadences, ceremonies) and becomes the PMO-in-disguise.

**Redirect:** get Strategic Intent in place *before* funding Product Ops. Otherwise Product Ops fills the strategy vacuum with process, and you've made things worse.

### The "outcome" that's actually an output
"Ship the new dashboard by Q3" is an output framed as an outcome. Real outcomes are customer or business behavior changes ("increase weekly dashboard usage by 20%").

**Redirect:** apply the substitution test: does the OKR describe a *thing shipped* or a *behavior changed*? If it's the former, it's an output.

### The Waiter PM promoted to Senior Waiter
Senior title, same reactive behavior. Common in orgs that promote based on tenure or output volume rather than strategic contribution.

**Redirect:** rewrite promotion criteria against the Tactical → Strategic → Operational progression. Assess actual strategic contribution, not tenure.

## Pro tips (accelerators Perri uses in her podcast and coaching)

### The "Why do we...?" rhetorical challenge
When someone defends a pathology as normal — "we run OKRs individually because that's how we do performance reviews" — flip it to the question form: *"Why do we run companies as if everyone is competing individually?"* Reframes the systemic issue as absurd on its face.

### The Dear Melissa move
When someone brings a symptom, don't jump to the fix. Ask: *what else is going on?* Perri's *Dear Melissa* podcast segment is entirely this — a listener describes a PM-role problem, and she walks up the org one altitude at a time until she finds the real cause. Usually not where the listener thought.

### The contrast list
Waiter vs. Mini-CEO vs. Strategic PM. Output vs. outcome. Feature-driven vs. outcome-driven. Sales-led vs. product-led. Contrast lists force clarity — they name the trap and the alternative in the same sentence.

### The "one sentence strategy" test
Ask five people across the org to state the company strategy in one sentence. Compare answers. Disagreement = the strategy isn't deployed.

### The calendar audit
> Look at where a PM's time actually goes. If it's 80% meetings and ticket-writing and 20% customer contact, that's the revealed job. That's the build trap in miniature.

### The "what would kill this feature?" question
Before committing to build, force the team to name what evidence would kill it. If the team can't name it, they can't validate it — they're just going to ship it.

## Language and vocabulary — say this, not that

Small phrasing shifts that Perri has made explicit in her writing and podcast:

| Instead of | Use | Because |
|---|---|---|
| MVP | Solution Experimentation | "MVP" now means "small first version to ship" — the opposite of Ries's original meaning |
| Feature roadmap | Problem Roadmap (internal) + release plan (external) | Roadmap should surface *problems*, not commitments |
| Product Owner | Product Manager | "PO" is a Scrum role; PM is a strategic function |
| Mini-CEO | Strategic PM | "Mini-CEO" is a myth; give people authority matching their accountability |
| Order-taker / mailbox PM | Waiter PM | Name the archetype so the org can confront it |
| Execution | Discovery + delivery | "Execution" hides the discovery work that should precede build |
| Ship it | Learn from it | Reframes the definition of "done" (Ep 268 topic: *"Rethinking What Done Means in Product Ops"*) |
| Individual OKRs | Team-level OKRs | Outcomes require multiple functions |
| "The customer wants X" | "We have a hypothesis that X will move outcome Y" | Forces framing as testable belief, not received truth |
| Product Operating Model (Cagan's term) | Product Management Operating Model | Cagan owns the top-level phrase; Perri operates one level down at the PM function level |

## Voice reminders when applying this section

- Diagnose *before* prescribing. Name the pathology first.
- Locate the pathology one altitude up. If the PM function looks broken, look at the strategy vacuum or incentive structure above it.
- Empathetic-but-firm — *"I have tremendous empathy for founders in this scenario…"* followed by the counter-argument. See `voice-and-tone.md`.
- Cite. Every device has a source in her published work.

# V2MOM — Method

> The canonical description of the five elements in Marc Benioff's own terms. Fidelity is the point — V2MOM is opinionated, and softening the order or dropping Obstacles collapses it into a generic vision-values-goals template.

## Definition

Benioff's operating framing:

> "V2MOM is the biggest secret of Salesforce.com's success. Vision helped us define what we wanted to do. Values established what was most important about that vision; it set the principles and beliefs. Methods illustrated how we would get the job done by outlining actions. Obstacles identified challenges, problems, and issues we'd overcome. Measures specified the actual result we aimed to achieve; often numerical."
> — Marc Benioff, *Behind the Cloud* (2009)

Two things in that framing are non-negotiable:

- **The order.** V → V → M → O → M. Each element constrains the next. Values are named before Methods because Values *govern which Methods qualify*. Obstacles are named before Measures because you can only meaningfully measure success once you've named what could prevent it.
- **All five, on one page.** Skipping Obstacles is the single most common way people neuter the framework. Running past one page defeats the "clarity + alignment" promise.

## The five elements

### 1. Vision

**What it asks:** What are we trying to accomplish? What does the better place look like? Why does it matter?

**Length:** 1-3 sentences. Long enough to inspire, short enough to hold in one thought.

**Salesforce Trailhead definition:** *"Defines what you want to do or achieve."*

**Tips (from Trailhead):**
- Make it inspiring and reflect the writer's personality.
- Consider impact on stakeholders (customers, employees, partners, community).
- Keep it high-altitude but recognizable — a customer should be able to picture it.

**Not:** a slogan, a hashtag, a growth target. Vision frames the destination; Measures quantify arrival at it.

**Original Salesforce 1999 example** (from the envelope):
> *"Rapidly create a world-class Internet company / site for sales-force automation."*

Notice: specific enough to constrain choices ("world-class", "Internet", "sales-force automation") and short enough that any of the first seven employees could recall it verbatim.

### 2. Values

**What it asks:** Which principles govern *how* we pursue the vision? What matters most when two good options conflict?

**Length:** 3 (up to 5) values. Each with a one-line description explaining what it means and how it guides decisions.

**Ordered by priority. This is not decoration.** The order tells you who wins when values collide on a specific decision.

**Salesforce Trailhead definition:** *"Principles and beliefs that help you pursue the vision."*

**Salesforce's own values, in priority order** (as of 2026):
1. **Trust** — customers trust us with their data; we won't compromise.
2. **Customer Success** — customers succeed when we do; we're aligned to their outcomes.
3. **Innovation** — we build new categories, not just features.
4. **Equality** — everyone at Salesforce, and everyone the product serves.
5. **Sustainability** — added later; commitment to environmental responsibility.

When Trust and Innovation conflict on a specific decision — ship the AI feature fast (Innovation) vs. wait to audit for data safety (Trust) — Trust wins by rank.

**Anti-pattern:** treating values as a flat list of nice-sounding words. If your team can't tell you which value wins in a conflict, the ordering isn't real, and the Values section can't do decision work.

### 3. Methods

**What it asks:** Given the vision and values, what are the concrete actions we will take?

**Length:** 5-8 methods, prioritized. Each phrased as an action ("Hire X", "Launch Y", "Migrate to Z"), not an aspiration ("Be more customer-centric").

**Salesforce Trailhead definition:** *"Actions and steps to take to get the job done."*

**Tips (from Trailhead):**
- Prioritize by importance. The order matters — top methods get resource priority.
- Keep the writing simple and concrete.
- Align to the level above: your team methods should visibly advance the corporate methods.

**Test:** could you put each method on a calendar or a roadmap? If the method is not schedulable, it's still an aspiration, not a method.

**Original Salesforce 1999 example** (from the envelope):
1. Hire the team
2. Finalize product specification and technical architecture
3. Rapidly develop to beta and production
4. Build partnerships with e-commerce, content, and hosting companies
5. Build launch plan
6. Develop exit strategy (IPO / acquisition)

Notice: every item is an action. "Hire the team" is not "attract world-class talent" — it's a verb with a bounded scope.

### 4. Obstacles

**What it asks:** What will make the methods hard? What could prevent us from succeeding?

**Length:** 3-5 obstacles, concrete.

**Salesforce Trailhead definition:** *"The challenges, problems, issues you have to overcome to achieve the vision."*

**Tips (from Trailhead):**
- Anticipate what will make execution difficult — before it happens.
- Identify what requires mindfulness — where the team needs to be extra attentive.
- Specify concrete countermeasures — each obstacle should link to a method or a specific action that addresses it.

**Why Obstacles is the load-bearing element:** almost every other planning framework (OKRs, Balanced Scorecard, generic VMV templates) omits this. That omission is why plans quietly fail — the team knew the obstacle existed but no one was empowered to name it. V2MOM makes it a first-class element.

**Original Salesforce 1999 example** (from the envelope):
- Developer recruitment
- Product manager / business development hiring

Notice: even at 4 people, Benioff named the obstacles that would hurt most — hiring senior product/BD talent at a pre-revenue startup. Both obstacles paired to Method #1 ("Hire the team").

**Cautionary tale — the 2023 Wellness Culture controversy:** Benioff's FY24 V2MOM Obstacles section included: *"Wellness culture overpowered high performance culture during pandemic. Fear of escalations for people-related issues (burnout, psychological safety, equality, etc.) can make managers reticent to performance manage their teams."* Salesforce employees called it tone-deaf; the line was removed within a week. Lesson: obstacles are *published inside the company*. Frame them as things to overcome, not as behaviors or values to blame. Naming an obstacle correctly is a leadership move; naming it wrong is a values statement in disguise.

### 5. Measures

**What it asks:** How will we know the methods worked? What are the observable results?

**Length:** Paired to methods — roughly one measure per method or per method group. Ideally SMART (Specific, Measurable, Achievable, Relevant, Time-bound).

**Salesforce Trailhead definition:** *"Measurable results you aim to achieve."*

**Two flavors:**
- **Progress Measures** — targets you're moving toward. "Achieve $50M ARR by end of FY26." "NPS from 30 to 50."
- **Completion Measures** — binary. "Ship v2 by Q3." "Hire VP Eng by Q2."

**Tips (from Trailhead):**
- Focus on measurable outcomes, not daily activities.
- SMART: ✓ *"Achieve market share of 30% in the United States by end of fiscal year"*. ✗ *"Dominate the U.S. market!"*

**Original Salesforce 1999 example** (from the envelope):
- Prototype is state-of-the-art
- High-quality functional system
- Partnerships online and integrated
- Regarded as leader and visionary
- "We are all rich"

Notice: mostly Completion Measures at this stage — a pre-revenue startup can't set ARR targets. The last item ("we are all rich") is Benioff being Benioff — an ambitious exit outcome as measure of ultimate success. Not SMART, but honest about what winning meant.

## Ordering — why it matters

V2MOM is not five independent boxes. Each layer constrains the next.

**Vision → Values.** The values you name should serve the vision. If your vision is "world-class enterprise software" and your top value is "move fast and break things," the value undercuts the vision (enterprise buyers won't tolerate breakage). The value has to serve.

**Values → Methods.** A method that violates a top-ranked value should be discarded, even if it's the fastest route to the vision. This is the practical test that ranked values do decision work.

**Methods → Obstacles.** Obstacles are named *in reference to* the methods, not floating. "Hiring is slow" is only an obstacle if a method depends on hiring. Otherwise it's an environmental fact, not a plan obstacle.

**Obstacles → Measures.** A method that has a serious obstacle should have a measure that shows the obstacle is being overcome. Measures without the obstacle context become vanity metrics.

**The visible test:** if you can swap out one element without disturbing the others, they're not integrated — they're five lists that happen to be adjacent.

## Cascade

V2MOM is not a single document. At Salesforce it operates as a cascade:

1. **Corporate V2MOM.** Written by Benioff personally, published on Chatter at the start of each fiscal year (Salesforce FY starts in February).
2. **Function V2MOMs.** Each function head (Sales, Product, Engineering, People, etc.) writes theirs, showing how their methods advance the corporate methods and how their measures roll up.
3. **Team V2MOMs.** Each team within a function writes theirs.
4. **Individual V2MOMs.** Every employee — ~75,000 across Salesforce — writes their own personal V2MOM aligned to their team's.

Every V2MOM is searchable on Chatter. Any employee can pull up any other employee's V2MOM at any time. This transparency is the mechanism that makes cascade real — if your V2MOM contradicts your manager's, everyone can see it, and the conversation happens.

**Not copy-paste.** Trailhead explicitly warns against cloning your manager's V2MOM. Your V2MOM should reflect your specific role in advancing the team's methods, not restate the team's.

**New-hire rule.** ~90 days before publishing a first V2MOM. Enough time to know what your actual scope is.

## Refresh cadence

- **Annual creation** — start of fiscal year.
- **Quarterly refresh** — updated to reflect changed context, new commitments, dropped bets.
- **Mid-year formal review** — comprehensive re-alignment with the corporate V2MOM.
- **Weekly / monthly reference** — used as the frame for manager-employee 1:1s. Trailhead's line: *"If it's not on the V2MOM it won't get done."*

A V2MOM that isn't referenced weekly and refreshed quarterly is a dead artifact. If the surrounding process can't support that cadence, name it — the framework will underdeliver.

## What V2MOM is NOT

- **A mission-vision-values poster.** VMV templates give you the first two elements without Methods, Obstacles, or Measures. That's culture ornament, not a plan.
- **An OKR replacement in disguise.** OKRs are Measures with an Objective on top. V2MOM subsumes them but is not identical. Running both in parallel (OKRs for measurement, V2MOM for context) means maintaining two docs — pick one.
- **A strategic-competitive tool.** V2MOM doesn't help you decide *how to beat competitors*. For that, use Playing to Win (Martin) or the kernel of strategy (Rumelt). V2MOM aligns the org around the plan you've already chosen.
- **A one-time offsite output.** Living document, or dead document. There is no third option.
- **CEO-only.** Every employee writes one. The cascade is the mechanism.

Benioff's framing on this, from *Trailblazer* (2019): *"Values create value."* The V2MOM is the artifact where values do that work — not by hanging on a wall, but by being ranked, referenced weekly, and cascaded through every level of the org.

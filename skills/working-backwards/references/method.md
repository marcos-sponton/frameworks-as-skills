# Working Backwards — Method

> The canonical description of the four load-bearing mechanisms in Bill Carr and Colin Bryar's own terms, plus the supporting mechanisms. Fidelity is the point — the method is opinionated, and softening any mechanism collapses it into "we should be more customer-obsessed." Attribution is precise: this is from the book, this from the 2026 blog, this from Carr on Lenny 2023.

## The frame

Everything below rests on one disposition: **start with the customer and work backwards from there.** Not "start with what we can build." Not "start with what our team is good at." Start with a customer, a specific problem they have, and imagine the announcement of a product that solves it — *as if it already existed.*

Bill Carr's operating principle:

> "If we served customers well, if we prioritized customers and delivered for them, things like sales, things like revenue and active customers and things like the share price and free cash flow would follow."
> — Bill Carr, [Lenny's Podcast](https://www.lennysnewsletter.com/p/unpacking-amazons-unique-ways-of), Nov 2023

And Bezos's meta-principle, quoted throughout the 2021 book and every subsequent Carr/Bryar appearance:

> "Good intentions don't work. Mechanisms do."
> — Jeff Bezos (via Carr + Bryar, *Working Backwards*)

Working Backwards is the operational cash-out of that principle: a set of mechanisms that force customer-first thinking to happen even when the room's instincts pull elsewhere.

## Mechanism 1 — The PR/FAQ

**What it is:** a short narrative document — typically around six pages — written *before* any code, describing the product from a future launch date as if it already exists.

**Two mandatory parts:**

**A. Press Release (~1 page).** Written in plain, customer-facing language — no jargon, no internal acronyms. Structured:
- **Heading** — one-sentence product name.
- **Subheading** — target customer and their benefit, in one sentence.
- **Summary paragraph** — launch date, product overview.
- **Problem paragraph** — the customer pain being solved. Named specifically.
- **Solution paragraph(s)** — the product, how it solves the problem, how it differs from what exists.
- **Quotes & Getting Started** — spokesperson quote + customer testimonial (imagined, but plausible) + how a customer starts using it.

Bill Carr's structural point:
> "The heart of it really is that first paragraph, it's a short description, that second paragraph, that's the problem statement."
> — Carr, Lenny 2023

And on tone:
> "You don't want to use hyperbole. It would be very factual with numbers, data rich document too."
> — Carr, Lenny 2023

**B. FAQ (2 sections).**
- **External FAQs** — customer-facing questions. Price, availability, functionality, support, comparison to alternatives.
- **Internal FAQs** — stakeholder concerns. Finance (bill of materials, unit economics, TAM), operations, technical dependencies, strategic implications, risks.

**The five questions the PR/FAQ has to answer** (from the firm's PR/FAQ Mastery course and Commoncog's applied writeup):

1. Who is the customer?
2. What problem needs solving?
3. What's the solution?
4. Would customers reasonably adopt this?
5. Is the Total Addressable Market large enough?

**How it's used:** senior leadership reviews the PR/FAQ. Most PR/FAQs are (and should be) rejected. The rejection is the point — it preserves resources for the bets worth making.

> "The fact that most PR/FAQs don't get approved is a feature, not a bug… preserves your company's resources to build products that will yield the highest impact for customers and your business."
> — Bryar/Carr, via Commoncog: https://commoncog.com/putting-amazons-pr-faq-to-practice/

**Why this mechanism exists:** it forces the team to articulate *for the customer* before they build *for themselves*. It surfaces bad bets on paper, before they get built.

## Mechanism 2 — The six-page narrative memo

**What it is:** the document Amazon uses for meetings that would elsewhere be a PowerPoint. Six pages of dense narrative — no bullet points, no graphics, no filler — with data and supporting exhibits in an appendix (the whole document can run 40+ pages once the appendix is counted).

**Craft rules (non-negotiable in the mechanism):**
- **Prose, not bullets.** Complete sentences, connected argument.
- **10-point font, strict formatting.**
- **Data in the appendix,** not sprinkled through the narrative as chartjunk.
- **Read silently for ~20 minutes at the start of the meeting** — three minutes per page × six pages. This is the "study hall" opening.
- **No one presents.** The author answers questions after the silent read.

**Bezos's justification, quoted throughout the book:**
> "The narrative structure of a good memo forces better thought and better understanding of what's more important than what, and how things are related."

**The review disposition Bezos brings** (a rule Working Backwards LLC teaches):
> Bezos "assumes each sentence he reads is wrong until he can prove otherwise. He's challenging the content of the sentence, not the motive of the writer."
> — via Sajith Pai's book notes: https://sajithpai.com/book-notes-thoughts-working-backwards-on-amazon-by-colin-bryar-bill-carr/

**Why this mechanism exists:** structured writing forces logical gaps to the surface. Bullet points let a leader hide behind implied connections; narrative forces them to write the connection explicitly. Silent reading ensures everyone encounters the full argument together, before discussion — no one is skimming while someone else is presenting.

## Mechanism 3 — Single-Threaded Leader (STL)

**What it is:** one leader assigned to one initiative, with **zero competing responsibilities**, heading a team whose cross-functional resources either report directly to them or are dedicated full-time (not matrixed).

**Origin:** Amazon rebuilt around this model around 2004–2005, replacing what had been called "two-pizza team leaders." The name shift matters — the older term emphasized team size (small enough to feed with two pizzas); the newer term emphasizes leader focus (singularly threaded to one problem).

**Two variants (per the firm's teaching):**
- **Single-Threaded Ownership (STO):** the leader controls all resources needed; team members report directly to them.
- **Single-Threaded Leadership (STL):** the leader drives prioritization across disciplines while team members maintain functional reporting lines (engineers to engineers, designers to designers) — but the leader has clear authority over the initiative's direction.

**Why this mechanism exists — in Bill Carr's own words:**
> "Most companies solve this by having an intense, centralized, highly collaborative process. We decided to go in the other direction."
> — Carr, Lenny 2023

> "Let's create teams that can stand alone, where there's a single leader and the cross-functional resources that they need are all either directly report to them or are dedicated to them."
> — Carr, Lenny 2023

> "If there are success or failures, they're really dependent on themselves now."
> — Carr, Lenny 2023

**Mandatory conditions for a real STL:**
- Clear charter and well-defined purpose.
- Understood ownership boundaries.
- Pre-agreed evaluation metrics.
- **Separable organizational structure** — for software teams, this means APIs so teams don't have to meet to make progress.

**Why this mechanism exists:** it destroys the coordination tax. Amazon observed that the most important initiatives were the ones that stalled — because whoever was "leading" was also responsible for four other things, and the cross-functional teammates they needed were shared with three other initiatives. STL breaks that pattern by giving one person one job and dedicated resources.

## Mechanism 4 — Input metrics

**What it is:** the discipline of tracking **controllable input metrics** — things the team can actually move day-to-day — rather than **output metrics** — the lagging outcomes that result from many inputs.

**Contrast:**
- **Output metrics** — revenue, growth, active customers, share price, gross margin. Lagging. Compound. Hard to attribute.
- **Input metrics** — selection (how many products in the catalog), price (how competitive), delivery speed (how fast in-stock items ship), page-load time, defect rate. Controllable. Direct. Attributable.

**Bill Carr's operating principle:**
> "We took it as an article of faith that if we can just improve these inputs, the outputs will take care of themselves."
> — Carr, Lenny 2023

> "If we can just improve these things, this is our path to winning."
> — Carr, Lenny 2023

**How to identify a good input metric (Carr's rule):**
> "A sign that's a good input metric is, first of all, map your end-to-end customer experience."
> — Carr, Lenny 2023

**Screen for input metrics:**
- **Controllable** — the team can actually move it this week.
- **Directly upstream of the customer outcome** — improving the input should mechanically improve the outcome.
- **High-frequency measurable** — usually weekly, per WBR cadence.
- **Not a fitness function.** Amazon explicitly rejected compound "one-number" metrics because they obscure cause and effect.

**Iteration is built in.** Carr and Bryar acknowledge "a lot of trial and error involved in determining the right input metrics to track." You change them as you learn.

**Why this mechanism exists:** it makes the daily work legible. If a team can't say what input they're moving this week and how it's expected to move the output over time, they're not running Working Backwards — they're running a status report.

## Supporting mechanism — Bar Raiser

**What it is:** a trained interviewer, **not on the hiring team**, with **veto power over the hire**. Runs the debrief. Assesses candidate behavior against Amazon's 14 Leadership Principles using STAR-format behavioral interviewing.

**Established:** 1999.

**Why this exists:**
> "The Bar Raiser was there to act as a balance also on the urgency bias that every hiring manager has."
> — Carr, Lenny 2023

> "The decision maker is the hiring manager, the whole interview loop and the Bar Raiser are actually just there to help."
> — Carr, Lenny 2023

The mechanism prevents individual hiring managers from lowering the bar under pressure to fill a role. Bar Raiser can veto; hiring manager cannot overrule.

## Supporting mechanism — Disagree and Commit

**What it is:** Amazon's decision hygiene. In the room, everyone owes their honest disagreement. Once decided, everyone commits fully — no passive resistance.

**Carr on the two halves:**
> "When we are making any kind of a decision, important decision, if you are part of that team, it is your obligation to voice your point of view if you disagree."
> — Carr, Lenny 2023

> "The commit part done well means that it's not just like I'm going to commit, I don't really agree."
> — Carr, Lenny 2023

> "Once we'd had those discussions, those interchanges, then the teams were free to sprint hard after their plan."
> — Carr, Lenny 2023

## Supporting mechanism — Weekly Business Review (WBR)

**What it is:** the operating-cadence meeting. Fractal — same structure from executive team down to individual product teams. Metrics analyzed with DMAIC / 5 Whys — anomalies get dug into, not just noted.

**Non-obvious detail:** the finance department audits the metrics independently to prevent manipulation.

**Software artifact:** the firm sells (and open-sources) the WBR App to operationalize this. https://workingbackwards.com/wbr-app/ · https://github.com/working-backwards/wbr-app

## Supporting mechanism — Correction of Errors (COE)

**What it is:** the structured post-mortem after a failure. Focuses on the mechanism that let the failure happen, not on personal blame. Documented and shared so other teams don't repeat the mistake.

**Amazon's response to failure, quoted throughout the book:**
> "Why would I fire you now? I just made a million-dollar investment in you. Now you have an obligation to make that investment pay off. Figure out and clearly document where you went wrong. Share what you have learned with other leaders throughout the company. Be sure you don't make the same mistake again, and help others avoid making it the first time."

## The substrate — Amazon's 14 Leadership Principles

The mechanisms rest on the Principles. If a team doesn't operate with Customer Obsession, Ownership, Dive Deep, Backbone, and Bias for Action as reflexes, the mechanisms won't stick. WB-relevant Principles:

- **Customer Obsession** — the frame that unlocks Working Backwards itself.
- **Ownership** — the disposition STL institutionalizes.
- **Invent and Simplify** — what PR/FAQ is engineered to enforce.
- **Are Right, A Lot** — what Bar Raiser is selecting for.
- **Dive Deep** — what the 6-pager rewards over PowerPoint.
- **Have Backbone; Disagree and Commit** — the decision-hygiene principle.
- **Bias for Action** — the counterweight to weeks-on-a-PR/FAQ. Balance both.
- **Frugality** — informs input-metric discipline.

## Integration

None of these mechanisms works alone. The PR/FAQ requires the silent-reading 6-pager review meeting to be interrogated. The STL only accelerates things if input metrics are actually being tracked and reviewed weekly. Bar Raiser hiring only holds up if the resulting hires actually operate with the Principles.

Bill Carr on this:
> "None of these things give you the answer. They are tools to help you make decisions."
> — Carr, Lenny 2023

Working Backwards is not a step-by-step process. It's a *set* of reinforcing mechanisms. Adopting one without the others usually fails — either because the mechanism gets diluted (a 6-pager no one silently reads becomes a bullet-riddled PowerPoint) or because the surrounding disposition isn't there to make it work.

## What this method is NOT

- **A single template.** PR/FAQ has structure but there's no downloadable "correct" template that substitutes for the discipline of writing and defending one.
- **A guarantee.** *"None of these things give you the answer."* The Fire Phone had a PR/FAQ. It still failed — because the underlying customer-problem hypothesis was wrong. Mechanisms make bets more honest, not automatically correct.
- **Frictionless.** Carr is explicit: *"Implementing a new process is not easy… it requires commitment and discipline to get through."* Weeks or months on a PR/FAQ before writing code feels intolerable outside Amazon. That discomfort is real and predictable.
- **For pre-PMF startups.** The firm targets Series C+ and public companies precisely because these mechanisms shine when cost-per-bet is high and coordination is expensive. Pre-PMF, use Lean Startup.
- **Culture without mechanisms.** Bezos's central claim: *"Good intentions don't work. Mechanisms do."* Adopting "customer obsession" as a value without any mechanism that forces it into daily behavior is exactly what Working Backwards is a corrective against.

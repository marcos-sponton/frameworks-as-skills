# Shape Up — Method

> The canonical description of Ryan Singer's method in his own terms — the 2019 book plus the 2022+ *Framing* prelude, the "Pitch → Package" rename, and the *Shaping in Real Life* adaptation. Fidelity is the point — the method defines itself against most standard Agile practice, and softening any mechanism collapses it into "we should be more product-focused." Attribution is precise: this is from the book (chapter cited), this from Singer's 2022 *Framing* essay, this from the 2025 *Common Pitfalls* piece, this from Singer on Lenny 2025.

## The frame

Everything below rests on one disposition: **shape before you bet; bet before you build; ship in six weeks or kill.**

Not "estimate then commit." Not "iterate in sprints." Not "groom a backlog." **Shape, bet, build, kill-or-ship.**

Singer's operating principle, from the 2019 book:

> "Six weeks is long enough to finish something meaningful and short enough to feel the deadline from the beginning."
> — *Shape Up*, glossary. https://basecamp.com/shapeup/6.1-appendix-06

And the post-book sharpening, from the 2025 pitfalls piece:

> "The #1 failure mode of attempted Shape Up adoptions is 'undershaped' work."
> — Singer, *Common Pitfalls*, 2025. https://www.ryansinger.co/pitfalls-when-adopting-shape-up/

Shape Up is a two-track system: **shaping happens on one track, in parallel with the build track.** Shaping is done by 1–2 senior people (typically including someone with real technical depth), producing shaped bets for a Betting Table. Building happens in fixed 6-week cycles by small autonomous teams. The two tracks never mix inside a cycle.

## The full sequence (2022+ canon)

**Framing → Shaping → Package → Betting Table → Building → Cool-down → repeat.**

- **Framing** — is this problem worth solving? (Singer's 2022 addition; not in the 2019 book.)
- **Shaping** — given a framed problem, what's a viable solution at what appetite?
- **Package** — the shaped output (2022+ rename of "Pitch") — the go/no-go artifact.
- **Betting Table** — senior stakeholders pick a small number of packages for the next cycle.
- **Building** — one six-week cycle, small autonomous team, no interruptions.
- **Cool-down** — two weeks of bugs, exploration, ad-hoc work, and the next Betting Table.

## Mechanism 1 — Framing (Singer's 2022+ addition, upstream of shaping)

**What it is:** the pre-shaping step. Confirm the problem is worth solving *before* investing shaping effort. The 2019 book leaps from "raw idea" straight into shaping; in practice this produced rework — teams shaped solutions to problems the business hadn't agreed were worth solving.

**Singer's own words:**
> "Framing is all about the problem and the business value."
> — *Framing*, 2022. https://www.ryansinger.co/framing/

> "The output of a framing session is a well-framed problem: something where the business says 'if we can shape this into something doable and execute within X weeks, that will be meaningful to us.'"
> — *Framing*, 2022.

> "Framing is about the problem, the business value, the outcome, etc. Shaping is about the technical solution."
> — *Common Pitfalls*, 2025.

**How it works:** a small group (often the founder / head of product plus one senior stakeholder) works through: whose problem, why now, what business value, is it worth committing weeks of engineering time. **No solutions yet.** Framing outputs a *framed problem*, not a solution.

**Why this mechanism exists:** it prevents the most common Shape Up failure mode — shaping (and then betting on) a solution to a problem that wasn't actually worth solving. This is post-book **canon**, not extension.

## Mechanism 2 — Shaping (the core of the 2019 book)

**What it is:** the pre-project design work by 1–2 senior people (typically including someone with real technical depth) that produces a shaped bet: **a Pitch (2019 term) or Package (2022+ term)** with five mandatory ingredients.

**The five ingredients** (from Ch. 6 "Write the Pitch"):

1. **Problem** — "The raw idea, a use case, or something we've seen that motivates us to work on this." Singer's rule: *"The best problem definition consists of a single specific story that shows why the status quo doesn't work."* (Ch. 6)
2. **Appetite** — "How much time we want to spend and how that constrains the solution." Small batch (1–2 weeks) or big batch (full 6-week cycle). Stating appetite up front prevents unproductive conversations and turns the constraint into a design driver.
3. **Solution** — "The core elements we came up with, presented in a form that's easy for people to immediately understand." At the fat-marker / breadboard level of fidelity — not screens, not high-fidelity mocks. Structural.
4. **Rabbit holes** — "Details about the solution worth calling out to avoid problems." A few lines of text on things the shaper knows will trip the team up — edge cases, tricky data models, known unknowns.
5. **No-gos** — "Anything specifically excluded from the concept: functionality or use cases we intentionally aren't covering to fit the appetite or make the problem tractable."

**Fidelity tools:**

- **Fat marker sketches.** UI concepts drawn with a thick line, deliberately low fidelity. Structure over polish. If you can render it in Figma, you're too detailed.
- **Breadboarding.** Structural sketches — components, affordances, connections — with no visual design at all. Named after the electronics prototyping tool: enough structure to know it will work, no polish.

**Singer's rule on fidelity:** shaping output is imprecise on purpose. Detail invites nitpicking; low fidelity keeps attention on structure and lets the build team make specific design decisions during the cycle.

**Who shapes:** 1–2 senior people, at least one with real technical depth. This is the *Shape Up 2.0* insistence: non-technical shaping produces "undershaped" work (Singer, 2025).

> "Shaped means 'we can give this to someone to build and they will know what to do.'"
> — Singer, *Common Pitfalls*, 2025.

**Post-book naming shift:** the 2019 book uses "Pitch." Singer's 2022+ material renames it "Package." The idea is the same; the newer name emphasizes that shaping produces a *package of decisions*, not a *pitch to leadership*. Both terms are current — use "Pitch" for 2019-book cites, "Package" for post-2022 material.

## Mechanism 3 — Betting Table

**What it is:** the go/no-go meeting held at the end of cool-down. Senior stakeholders (typically the CEO or head of product, plus a few senior technical and design people) review shaped packages and pick a small number to bet on for the next six-week cycle.

**Craft rules:**
- **Held once per cycle.** Not weekly. Not on demand.
- **Only shaped packages are considered.** No slides. No "just an idea." If it hasn't been through shaping (and now, framing), it isn't at the table.
- **Small number of bets.** As many teams as you have, no more. Often fewer — leaving capacity is legitimate.
- **Full commitment on approval.** If a bet is approved, the team gets six weeks uninterrupted. No mid-cycle re-prioritization.
- **Rejection is legitimate — and expected.** Most shaped packages should not be bet on. Shaping cost is sunk; that's not a reason to bet.

**Why this mechanism exists:** it separates the decision to invest six weeks from the day-to-day chaos of a product org. Bets are commitments; commitments are scarce. The Betting Table institutionalizes scarcity.

## Mechanism 4 — The six-week cycle (Building)

**What it is:** the fixed-duration execution window. One team, one bet, six weeks, no interruptions.

**Why six weeks?**
> "Six weeks is long enough to finish something meaningful and short enough to feel the deadline from the beginning."
> — *Shape Up*, glossary.

The claim is empirical: shorter than six weeks (Scrum's typical 2 weeks), meaningful features don't finish; longer than six weeks, the deadline stops being felt and scope creeps.

**Team shape (from the 2019 book):**
- 1 designer + 1–2 programmers.
- Fully dedicated. Not matrixed. Not shared with other teams.
- Autonomous. They decompose the work into **scopes** themselves.

**Scopes** — "Parts of a project that can be built, integrated, and finished independently." Not tasks. Not user stories. **Integrated slices**, each in principle shippable. The build team maps its own scopes early in the cycle; the shaper doesn't hand them a task list.

**Working style during the cycle:**
- Wire functionality first, high-fidelity design later (from the 2025 case study).
- Hill Charts (below) to show progress.
- Direct communication between designer and programmers — no PM-as-messenger.

**Non-negotiable:** no interruptions. Approved bets get six weeks uninterrupted. Approved means approved.

## Mechanism 5 — Hill Charts

**What it is:** a visual progress mechanism showing the position of each scope on a curve. The x-axis is time (or work progress); the curve rises to a peak and descends. **Uphill = figuring out**; **downhill = executing**; **plateau at the top = the transition point**.

Each scope is a dot. Dots move along the curve as the work progresses. The chart replaces burndown charts and completion percentages.

**Singer's framing (Ch. 13 "Show Progress"):**
> "Coming up with an approach in your head is just the first step uphill."
> — *Shape Up*, Ch. 13. https://basecamp.com/shapeup/3.4-chapter-13

**Uphill (figuring out):**
- Unknowns are being resolved. Approaches are being tried and abandoned.
- Progress isn't visible in code shipped; it's visible in reduced uncertainty.
- Traditional to-do lists *grow* here as work is discovered — hill charts *don't*, because a stuck dot is honest data.

**Downhill (executing):**
- Approach is clear. Now it's a matter of doing it.
- Progress is visible and predictable. Estimates would even be reasonable here.

**Plateau / stuck:** dots that don't move signal "something might be wrong here." Not slacking — a conceptual snag. The manager's job is to notice stuck dots and ask, not to move the dots for show.

**Anti-pattern:** moving dots to look like progress instead of reflecting real position. Hill charts as vanity metric.

## Mechanism 6 — Cool-down

**What it is:** a two-week gap between cycles. Bugs get fixed. Ad-hoc requests get handled. Exploration happens. The next Betting Table meets.

**Why this mechanism exists:**
- It gives teams recovery time — six weeks of full focus is intense.
- It gives the org a legitimate place to put bug/support/infrastructure work that doesn't belong in a shaped bet.
- It creates a natural cadence for the Betting Table (once per cycle, not on demand).
- It prevents the "no time for bugs" trap where teams are always in cycles and bugs never get fixed.

**Cool-down is not slacking.** It's the mechanism that makes the cycle work.

## Mechanism 7 — The Circuit Breaker

**What it is:** the default rule that projects which don't ship in one cycle are **killed**, not extended.

**Singer's own words:**
> "Cancel projects that don't ship in one cycle by default instead of extending them by default."
> — *Shape Up*, glossary.

> "If the work is uphill, it's better to do something else in the next cycle and put the troubled project back in the shaping phase."
> — *Shape Up*, Ch. 14 "Decide When to Stop." https://basecamp.com/shapeup/3.5-chapter-14

> "Without a deadline, they could easily delay the project for changes that don't actually deserve the extra time."
> — *Shape Up*, Ch. 14.

**Why this mechanism exists:** uphill work at the end of a cycle usually signals a **conceptual flaw**, not execution slowness. Extension papers over the flaw; killing and re-shaping addresses it. Extension is also politically easier ("we're so close!") which is precisely why the default must be kill.

**How the deadline forces scope choices:** with a hard endpoint, the team is forced to cut scope throughout the cycle to fit — smaller MVP of a feature, deferred edge cases, ship-what's-ready. Without the hard endpoint, scope inflates and the deadline slips.

**Contrast with Scrum:** Scrum treats incomplete sprint work as "carry over to next sprint." Shape Up treats it as evidence of a shaping or scoping failure — the answer is not more time on the same solution but reshaping or killing.

**Extension is possible but exceptional.** If leadership actively chooses to extend, that's a legitimate override — but the default is kill.

## Mechanism 8 — No Backlog

**What it is:** the radical rejection of the backlog as a product-management artifact. No JIRA graveyard. No prioritized queue of hundreds of tickets. Fresh decisions each cycle from a small pool of shaped candidates.

**Singer's argument (Ch. 7 "Bets, Not Backlogs"):**
> "Dozens and eventually hundreds of tasks pile up that we all know we'll never have time for."
> — *Shape Up*, Ch. 7. https://basecamp.com/shapeup/2.1-chapter-07

> "The time spent constantly reviewing, grooming and organizing old ideas prevents everyone from moving forward on the timely projects that really matter right now."
> — *Shape Up*, Ch. 7.

**The core claim:** backlog maintenance cost is real; the ideas rot; nobody trusts the ordering. Important ideas resurface anyway — if it isn't worth re-shaping when it comes back up, it wasn't worth doing.

**How it works in practice:**
- Cool-down = ad-hoc capacity for the small stuff.
- Shaping = deliberate design work on the big stuff worth doing.
- Betting Table = fresh decision each cycle.
- Everything else lives in the org's memory (people, docs, conversations) — not in a queue.

**This is the most politically difficult mechanism to adopt.** Removing the backlog is a leadership act; middle managers can't unilaterally delete JIRA.

## Supporting mechanism — Two-track system

**What it is:** shaping and building run in parallel, on different tracks, done by different people.

- **Shaping track:** senior people shape the next cycle's bets while the current cycle is being built.
- **Building track:** the small autonomous team builds this cycle's bet with no shaping distractions.

**Why this mechanism exists:** shaping inside the cycle steals build time and produces undershaped work. The two-track structure protects both activities.

## Integration

None of these mechanisms works alone. **Shaping without a Betting Table** produces packages that get built out of political pressure rather than merit. **The Betting Table without shaping** approves half-baked ideas. **Six-week cycles without a circuit breaker** turn into rolling extensions and become de facto never-ending sprints. **Hill Charts without cool-down** become vanity metrics because there's no honest capacity for the small stuff. **No backlog without shaping** creates chaos — "no plan" is not the same as "no backlog."

Singer on this integration, from the 2019 book: Shape Up is a *system* of mechanisms that reinforce each other. Adopting one without the others usually fails.

## What this method is NOT

- **Scrum with longer sprints.** Cycles are not sprints. Sprints are short, repeating, backlog-driven, ceremony-heavy. Cycles are long, non-repeating, appetite-driven, ceremony-light. Same word "iteration" doesn't mean same thing.
- **A backlog with a fancier tool.** The point is *no backlog*, not "backlog with better UX."
- **Estimation with a new name.** Appetite is a budget (fixed time, variable scope). Estimation is a prediction (variable time, fixed scope). Do not translate one to the other.
- **For pre-PMF startups.** Shape Up assumes you know the business and are shaping the next feature bet. Pre-PMF, use Lean Startup.
- **For bugs, maintenance, or infrastructure.** Singer is explicit: *"Shape Up is for features, not all development work."* (Singer, 2021 essay.)
- **A guarantee.** Shaped bets can fail — the mechanism makes bets more honest and cheaper to abandon, not automatically correct.
- **For very small teams.** Under ~5 people, the full ceremony is overkill. Small teams can borrow ideas (appetite, no backlog, circuit breaker) without adopting the cadence.

## When Singer's 2019 canon vs. 2022+ canon applies

- **2019 canon (the book):** the mechanisms — cycle length, cool-down, Betting Table, Hill Charts, Circuit Breaker, No Backlog, Fat Marker Sketches, Breadboarding, Scopes, Pitch structure. All still current.
- **2022+ canon (Framing, Shaping in Real Life):** Framing as upstream of shaping. "Package" as the newer name for "Pitch." Explicit acknowledgment that the 2019 book described "an unusual company" (Basecamp) and non-Basecamp adoption requires structural work (technical shapers, separation of framing from shaping, adjustment of team structures).

When quoting, name the year. Don't collapse seven years of thinking into a single flat voice.

# Shape Up — Heuristics, Do's, Don'ts, Gotchas

> The practical devices that separate applying Shape Up well from doing the theater version — six-week sprints with a fancier name. Attribution is precise: this is from the 2019 book (chapter cited), this from Singer's 2022 *Framing* essay, this from the 2025 *Common Pitfalls* piece, this from Singer on Lenny 2025.

## Do's

### Frame before you shape

Before shaping a solution, agree the problem is worth solving. Whose problem, why now, what business value. **No solutions yet.** The 2019 book leaps from "raw idea" straight into shaping; in practice this produces rework. Singer added framing in 2022 to close this gap.

**Author's frame:**
> "The output of a framing session is a well-framed problem: something where the business says 'if we can shape this into something doable and execute within X weeks, that will be meaningful to us.'"
> — Singer, *Framing*, 2022. https://www.ryansinger.co/framing/

### Set the appetite before designing the solution

Ask "how much time is this problem worth?" *before* asking "what should the solution look like." The appetite (small batch: 1–2 weeks; big batch: full 6-week cycle) becomes a design constraint — the shaper cuts scope to fit the budget, not the other way around.

**Why:** appetite is a design constraint, not a prediction. Setting it first forces the shaper to design *for* the constraint rather than around it.

### Write the pitch with all five ingredients

Problem, Appetite, Solution, Rabbit Holes, No-Gos. Every ingredient. If one is missing, the package isn't shaped. Don't let it go to the Betting Table.

**Author's structural rule (Ch. 6 "Write the Pitch"):**
> "The best problem definition consists of a single specific story that shows why the status quo doesn't work."
> — *Shape Up*, Ch. 6. https://basecamp.com/shapeup/1.5-chapter-06

### Keep shaping fidelity deliberately low — fat marker sketches, breadboards

UI sketches drawn with a thick marker. Structural sketches with no visual design. High fidelity invites nitpicking; low fidelity keeps attention on structure and lets the build team make specific design decisions during the cycle.

**Rule:** if you can render it in Figma, you're too detailed. If a stakeholder is asking about colors or fonts during shaping, the sketch is too polished.

### Include real technical depth in the shaping room

Shaping without technical depth produces "undershaped" work — packages that look complete but crumble in build. At least one senior technical person needs to be in the shaping session.

**Author's frame:**
> "The #1 failure mode of attempted Shape Up adoptions is 'undershaped' work."
> — Singer, *Common Pitfalls*, 2025. https://www.ryansinger.co/pitfalls-when-adopting-shape-up/

**And:**
> "Shaped means 'we can give this to someone to build and they will know what to do.'"
> — Singer, *Common Pitfalls*, 2025.

### Name rabbit holes and no-gos explicitly

Rabbit holes = details the shaper knows will trip the team up (edge cases, tricky data models, known unknowns). No-gos = things intentionally excluded to fit the appetite. Both are just a few lines of text. Un-named, they will re-emerge mid-cycle and eat scope.

### Narrow to one candidate before shaping

Don't shape ten pitches and let the Betting Table pick. That's expensive and produces politically-driven decisions. Narrow through framing to one candidate; shape it well; bet on it or don't.

**From the 2025 case study:**
> "We're actually narrowing down before we even shape."
> — Singer, *End-to-End with Shape Up*, 2025.

### Trust the Betting Table to say no

Most shaped packages should not be bet on. Shaping cost is sunk; that's not a reason to bet. If the Betting Table is approving 80%+ of packages, either the packages are only safe / small, or the reviewers are being polite.

### Fully commit for the cycle when you approve a bet

Approved means six weeks uninterrupted. No mid-cycle re-prioritization. No "just this one small addition." The whole mechanism assumes the build team can trust the commitment.

### Let the build team map its own scopes

Scopes — integrated slices, each in principle shippable — are the build team's tool. They emerge during the cycle. The shaper does not hand the team a task list.

**Anti-pattern to watch for:** shapers or PMs trying to hand the team a JIRA breakdown. That's a task list; it isn't scopes. Scopes belong to the builders.

### Use Hill Charts honestly

Uphill = figuring out (unknowns being resolved). Downhill = executing (approach is clear). Plateau/stuck = "something might be wrong here." Dots move when the work moves. If they're not moving, that's *data*, not a failure to report progress.

**Author's frame (Ch. 13):**
> "Coming up with an approach in your head is just the first step uphill."
> — *Shape Up*, Ch. 13. https://basecamp.com/shapeup/3.4-chapter-13

### Default to killing bets that run over — trip the Circuit Breaker

If the cycle ends and the bet isn't done, the default is kill, not extend. Extension is possible but exceptional and requires leadership choosing to override.

**Author's own words:**
> "Cancel projects that don't ship in one cycle by default instead of extending them by default."
> — *Shape Up*, glossary.

> "If the work is uphill, it's better to do something else in the next cycle and put the troubled project back in the shaping phase."
> — *Shape Up*, Ch. 14 "Decide When to Stop." https://basecamp.com/shapeup/3.5-chapter-14

### Cut scope to hit the appetite

Fixed time, variable scope. When the deadline is approaching, cut. Ship less. Ship what's ready. Ship the smaller version. Then reshape the cut parts if they still matter.

**Author's frame:**
> "Without a deadline, they could easily delay the project for changes that don't actually deserve the extra time."
> — *Shape Up*, Ch. 14.

### Protect the cool-down

Two weeks between cycles. Bugs get fixed. Exploration happens. The Betting Table meets. Cool-down is not slacking — it's the mechanism that makes the cycle work. Skipping it collapses the cadence within a quarter or two.

## Don'ts

### Don't estimate

Appetite is a budget (fixed time, variable scope). Estimation is a prediction (variable time, fixed scope). Do not translate one to the other. When someone asks "but how big is this appetite really?", that's estimation with a new label. Push back.

**Anti-pattern:** story-pointing an appetite. Velocity-tracking cycles. Retrofitting Scrum metrics onto Shape Up mechanisms.

### Don't keep a backlog

If you have a backlog, you're not running Shape Up. You're running Scrum with 6-week sprints. The backlog is the exact idea the method rejects.

**Author's argument (Ch. 7 "Bets, Not Backlogs"):**
> "Dozens and eventually hundreds of tasks pile up that we all know we'll never have time for."
> — *Shape Up*, Ch. 7.

> "The time spent constantly reviewing, grooming and organizing old ideas prevents everyone from moving forward on the timely projects that really matter right now."
> — *Shape Up*, Ch. 7.

**Common rationalizations to watch for:**
- "We need somewhere to capture ideas." Cool-down + shaper's private notes cover this.
- "Our stakeholders expect a roadmap." A shaped bet is a roadmap for one cycle; that's the appropriate horizon.
- "We just call it something else." If it's a prioritized queue of tickets, it's a backlog.

### Don't treat cycles as sprints

Cycles are not sprints. Sprints are short (1–2 weeks), repeating in content, backlog-driven, ceremony-heavy (standups, retros, planning, review). Cycles are long (6 weeks), non-repeating in content, appetite-driven, ceremony-light. Same word "iteration" doesn't mean same thing.

### Don't shape inside the cycle

Shaping must happen *before* betting, on the shaping track. Shaping inside the cycle steals build time and produces undershaped work. This is the whole point of the two-track system.

### Don't shape without technical depth in the room

Non-technical PMs shaping in isolation produce packages that look complete but the build team can't execute. Shaping is not the same as writing a PRD. It requires knowing what's technically feasible at what cost.

### Don't blur framing and shaping

Framing is about the problem, the business value, the outcome. Shaping is about the technical solution. Skipping framing is the "why did we just build this?" pattern.

**Author's words:**
> "Framing is about the problem, the business value, the outcome, etc. Shaping is about the technical solution."
> — Singer, *Common Pitfalls*, 2025.

### Don't extend past the Circuit Breaker by default

Uphill work at the deadline usually signals a **conceptual flaw**, not execution slowness. Extension papers over the flaw. Killing and re-shaping addresses it. If you're always extending, you're not running Shape Up — you're running rolling projects with 6-week checkpoints.

### Don't ship high-fidelity mocks as shaping output

That's design work, and it happens during the cycle by the build team. Shaping output is deliberately imprecise — fat marker sketches, breadboards, structural.

### Don't matrix or fractionalize the build team

The 6-week cycle assumes one designer + 1–2 programmers, fully dedicated. Shared team members (30% here, 70% there) break the cadence. If you can't dedicate people fully, either the bet isn't important enough or you need to reallocate.

### Don't apply Shape Up to bugs, maintenance, or infrastructure

Shape Up is for **new feature bets**. Everything else lives in cool-down or a different operating mode.

**Author's frame:**
> "Shape Up is for features, not all development work."
> — Singer, 2021 essay. https://www.ryansinger.co/shape-up-is-for-features-not-all-development-work/

### Don't move Hill Chart dots for show

Moving dots because leadership wants to see movement is the mechanism failing. Stuck dots are honest data; move dots when the work moves, not when the report is due.

### Don't run Shape Up "just at your team level" if the org runs Scrum around you

You'll be running two operating systems at once and the interfaces (Scrum's backlog, sprint planning, standups) will keep leaking into your cycles. Either the org commits (with CEO air cover) or your team borrows ideas (appetite, no backlog, circuit breaker) without adopting the full cadence. The half-measure is the failure state.

### Don't sell adoption as easy

Adopting Shape Up is politically hard. Removing the backlog is a leadership act. Six-week bets feel long to stakeholders used to weekly demos. Cool-down feels like slacking to managers who don't understand the mechanism. Singer is explicit that adoption requires committed sponsorship — don't promise a frictionless transformation.

### Don't assume mechanisms guarantee outcomes

Shape Up makes bets more honest and cheaper to abandon. It doesn't automatically produce successful features. A well-shaped, well-bet, well-built feature can still be the wrong feature.

## Gotchas

### Gotcha 1 — Basecamp was an unusual company

The 2019 book describes what worked at Basecamp: everyone technical, tiny team, unified skills, product-led CEO. Most companies aren't like that. Singer is explicit in his 2022+ writing that non-Basecamp adoption requires structural work:

- Technical shapers must be engineered explicitly (they're not automatic when designers and PMs are non-technical).
- The separation of framing from shaping matters more (Basecamp's product-led CEO framed implicitly; elsewhere you have to make it a step).
- Team dedication (non-matrixed) is harder to achieve.

If a user's company doesn't look like Basecamp, don't just recite the book — help them adapt.

### Gotcha 2 — Undershaped work is the #1 adoption failure

The 2025 *Common Pitfalls* piece names this as the primary failure mode. Symptoms:
- The pitch reads well but the build team is confused by day 2.
- Scope keeps growing mid-cycle because "we hadn't thought of that."
- Rabbit holes weren't named.
- No-gos weren't named.
- No technical person was in the shaping session.

Fix: shape again. Do not proceed to betting on undershaped work.

### Gotcha 3 — CEO commitment is required for "no backlog"

Removing the backlog is a political act. Middle management can't do it unilaterally. If a mid-level user asks "how do I bring Shape Up to my company?", the honest answer is: adopt what you can adopt at your team level (appetite, small autonomous builds, cool-down); pushing "no backlog" upward without CEO air cover is a recipe for frustration.

### Gotcha 4 — Emotional resistance to killing bets

The Circuit Breaker feels like failure to teams used to "carrying work over." It isn't — it's the mechanism working. But the discomfort is real and predictable. Extension feels merciful; it isn't — it's the pattern that produces death-march projects.

### Gotcha 5 — Estimation habits sneak back in

"How big is this appetite really?" is estimation with a new label. So is "our team's velocity for a 6-week cycle is roughly N features." Watch for Scrum vocabulary sneaking in through the side door.

### Gotcha 6 — Framing vs. shaping is easy to blur

Teams that skip framing often *think* they framed because they discussed the problem briefly. Framing produces a *framed problem* as an artifact — an explicit statement of whose problem, why now, what business value. If there's no artifact, framing didn't happen.

### Gotcha 7 — Small teams don't need the full ceremony

Under ~5 people, the Betting Table + cool-down + six-week commit is overkill. Small teams can borrow ideas (appetite, no backlog, circuit breaker, fat marker sketches) without adopting the full cadence. Full ceremony assumes enough teams to load-balance.

### Gotcha 8 — Applying Shape Up to non-feature work

Bugs, infrastructure, maintenance, refactors — these don't fit the shape of a shaped bet. They live in cool-down or a separate operating mode. Trying to shape them destroys the mechanism and produces "PR/FAQs for bug fixes" theater.

### Gotcha 9 — DHH and Fried are polemical; Singer is careful

When quoting the "37signals point of view" — "we don't do sprints", "estimates are lies", "meetings are toxic" — that's DHH or Fried, not Singer. Singer is the systems thinker; they are the megaphone. Attribute correctly. If the user wants polemic, DHH is the reach; for the method, Singer.

### Gotcha 10 — "The Circuit Breaker" as an upcoming Singer book is not confirmed

Rumor in the Shape Up community; **no public confirmation from Singer or a publisher as of 2026-07.** In the 2019 book "Circuit Breaker" is the *concept* (default-kill for over-cycle bets). If the user cites "the upcoming book," qualify — you don't know that it exists as a book.

## Pro tips (post-book refinements)

### Pro tip — When adopting outside Basecamp, engineer the technical shaper explicitly

If your PMs and designers aren't technical, don't just assign shaping to them and hope. Pair them with a senior engineer for every shaping session. The 2019 book assumed Basecamp's setup where designers coded; you don't have that setup.

### Pro tip — Frame first, and produce a framed-problem artifact

Even a paragraph. "We believe X customer has Y problem, and solving it in Z weeks would be worth it because W." If you can't write that paragraph, don't move to shaping.

### Pro tip — Use "wire functionality before high-fidelity design" inside the cycle

From the 2025 case study: the build team gets to a working end-to-end skeleton before polishing any single screen. This exposes integration issues early. It's the build-team analog of shaping's low-fidelity discipline.

### Pro tip — Reach for "the deadline as forcing function" language when scope creeps

When a team wants "just one more thing" mid-cycle, the frame is not "we don't have time" but "the deadline is doing its job of forcing scope choices." Cut, don't extend.

### Pro tip — Use the two-track system to prevent burnout

Shaping is intense; building is intense. Rotating people between tracks (senior person shapes for cycle N+1 while building has been assigned to the team for cycle N) distributes the intensity. Not all seniors need to shape every cycle.

### Pro tip — Not every team member needs to interview customers

Singer's 2024 pushback against the Continuous Discovery orthodoxy: specialization is legitimate. The framer / shaper needs deep customer context; the build team can trust the framing and shaping and get on with building. Not every engineer needs to be in user interviews weekly.

**Author's frame:**
> "Not everyone needs to be talking to customers."
> — Singer, 2024. https://www.ryansinger.co/not-everyone-needs-to-be-talking-to-customers/

# Shape Up — Applications

> Where Shape Up fits, where it doesn't, and adjacent frameworks to reach for instead. Shape Up is opinionated about its scope — Singer is explicit that it is for **new feature bets** in **post-PMF companies** with **teams of enough size** to run the cadence. When the situation is outside those constraints, use a different framework and say so.

## When Shape Up fits

**Team stage:** Post-PMF product companies. You know what business you're in and are shaping the next feature bet.

**Team size:** ~5 people minimum for a single build team; ideally multiple teams so the cadence load-balances. Below ~5, the ceremony (Betting Table, cool-down, 6-week commit) is overkill — borrow ideas instead.

**Work type:** **New feature bets.** Well-scoped features with real design surface, worth committing 6 weeks to. Product-shaping work where the shape isn't obvious in advance.

**Org structure:** Product-led leadership willing to commit to no backlog and default-kill (Circuit Breaker). Without this leadership commitment, mechanisms erode within a quarter.

**Cadence appetite:** Willing to run 6-week cycles + 2-week cool-down, indefinitely. Not willing to abandon after one cycle when it feels weird.

## When Shape Up doesn't fit — use something else

### Pre-PMF startups — use Lean Startup / Continuous Discovery

Shape Up assumes you know what business you're in. If you're still discovering it, the six-week bet is too big — cost of building the wrong thing at that scale exceeds your validation budget.

**Reach for:** Lean Startup (Eric Ries) for MVP-and-pivot loops. Continuous Discovery Habits (Teresa Torres) for opportunity-solution trees and weekly customer conversations.

### Bugs, maintenance, infrastructure — use cool-down or a separate operating mode

Singer is explicit: *"Shape Up is for features, not all development work."* (2021 essay).

Bug work, maintenance, small requests, and infrastructure are not shaped bets. Trying to force them into the shape produces "PR/FAQs for bug fixes" theater.

**Reach for:** cool-down (Shape Up's built-in slot for the small stuff). Or a separate maintenance team on a different operating model. Or Kanban for continuous flow of small work.

### Corporate / business-unit strategy — use Playing to Win or Rumelt's kernel

Shape Up is product-execution altitude, not strategy altitude. If the user's question is "which market should we enter," "how do we win in this space," "what is our competitive position," Shape Up has nothing to say.

**Reach for:** Roger Martin's [[playing-to-win]] cascade (5 questions). Richard Rumelt's [[good-strategy-bad-strategy]] kernel (diagnosis + guiding policy + coherent action, plus the crux).

### Continuous flow of small work — use Kanban

Kanban is WIP-limited pull with no fixed cadence. When work is naturally continuous and small (support, ops), Shape Up's cycle-and-cool-down rhythm is the wrong tool.

### Very small teams (<5 people) — borrow ideas, don't adopt the ceremony

A 2-person startup doesn't need a Betting Table. Small teams can borrow individual mechanisms — appetite over estimation, no backlog, circuit breaker for stalled bets, fat marker sketches — without adopting the full 6-week cadence.

## Adjacent frameworks — how Shape Up composes (or doesn't)

### vs. Scrum

- **Scrum:** short sprints (1–2 weeks), prioritized backlog, story-point estimation, Scrum Master role, daily standups, sprint planning, sprint review, retro.
- **Shape Up:** 6-week cycles, no backlog, appetite (not estimation), no assigned Scrum Master, small autonomous build teams, ceremony-light.

**Shape Up is explicitly a rejection of most Scrum ceremony.** Singer doesn't attack Scrum by name much; he describes what Basecamp does instead and lets the contrast speak.

**Do not blend.** If you have a backlog, you're not running Shape Up — you're running Scrum with 6-week sprints. If you're story-pointing "appetite," you're estimating. Blending destroys the mechanism.

**When Scrum is the better tool:** teams that genuinely need short feedback loops (2 weeks) with tight ceremony, in orgs where the backlog is politically load-bearing, or when the work is well-decomposed and predictable.

### vs. Kanban

- **Kanban:** WIP-limited pull, continuous flow, no fixed cadence.
- **Shape Up:** fixed 6-week cadence with a hard circuit breaker. The cadence is the point.

**Not compatible** — Shape Up's mechanism *requires* the cycle-and-cool-down rhythm. Kanban is a different animal.

**When Kanban is the better tool:** support, ops, maintenance, small-request-driven work. Anywhere the work is naturally continuous and small.

### vs. Continuous Discovery Habits (Teresa Torres)

- **Torres:** weekly customer interviews, opportunity-solution trees, small experiments, cross-functional discovery.
- **Shape Up:** shaping is closer to design work than to discovery. Framing (2022+) is closer to what Torres calls opportunity identification, but done by a small senior group rather than a cross-functional trio-and-team.

**Singer's 2024 essay** *Not everyone needs to be talking to customers* is a mild pushback on the Torres orthodoxy that every product team member should interview users weekly. Not a rejection — Singer respects the work — but a defense of specialization.

**They compose.** Torres-style discovery can feed the "raw idea" and "framing" inputs to Shape Up. But the two operate at different scales and dispositions.

**When Torres is the better tool:** teams focused on rapid learning loops with small experiments; discovery-heavy work where the problem itself is unclear.

### vs. Marty Cagan / Inspired / SVPG

- **Cagan:** empowered product teams (PM + designer + engineers), discovery + delivery split, outcome-oriented objectives, no output-based commitments.
- **Shape Up:** small autonomous build teams (compatible) but shaped bets that *are* commitments to specific solutions (partial disagreement with Cagan's "outcome, not output").

**The philosophical delta:** Cagan trusts empowered teams to figure out both problem and solution. Singer separates shaping (senior, upstream) from building (team, downstream). This is *the* big philosophical split.

**They agree on:** small autonomous build teams, rejecting waterfall PRDs.
**They disagree on:** where the shaping / discovery work happens and who owns it.

**When Cagan is the better tool:** empowered teams with strong senior PMs who can own both discovery and delivery; orgs where separating shaping from building would feel like taking autonomy away.

### vs. Working Backwards (Bill Carr / Colin Bryar / Amazon) — see [[working-backwards]]

This is the closest cousin. Both are "structured pre-work before building." Both reject ship-fast-and-iterate as universal. Both have a single artifact (PR/FAQ or Package) that is the go/no-go decision object.

**What they share:**
- Heavyweight thinking before building is worth weeks of investment.
- Small autonomous execution teams.
- A single primary artifact that structures the go/no-go decision.
- Explicit rejection of Agile-style "just start shipping and iterate."

**Where they diverge:**

| | Working Backwards | Shape Up |
|---|---|---|
| Perspective of primary artifact | Customer's future perspective (press release from a launch date) | Builder's perspective (fat marker sketch, breadboard, rabbit holes, no-gos) |
| Form | Aggressively narrative prose, no bullets, read silently in a meeting | Sketch-and-artifact driven |
| Decision authority | CEO / senior review (Bezos-shaped) | Small Betting Table (Fried/DHH-shaped) |
| Cadence | No fixed cycle; bets happen when shaped | Fixed 6-week cycle + 2-week cool-down; Circuit Breaker |
| Progress mechanism | Input metrics + Weekly Business Reviews | Hill Charts + cool-down |
| Scale assumed | Amazon-scale ($$$/bet) | Any small-team feature bet |
| Post-mortem | Correction of Errors | (No formal mechanism; kill-and-reshape) |
| Backlog | Not explicit either way | Explicitly rejected |

**Can they coexist in one org?** In principle: use Working Backwards to decide *whether* to bet (the PR/FAQ as the "should we invest 6 weeks in this?" gate), and Shape Up to shape *how* to bet (the Package as the "given we're doing it, here's the shaped work"). In practice, most teams pick one or the other and adapt — running both is expensive.

**When Working Backwards is the better tool:** large orgs where cost-per-bet is high, CEO-level review makes sense, and the customer-narrative discipline matters (especially in launch-oriented product work).

**When Shape Up is the better tool:** product teams shipping continuous feature bets where six-week rhythm and fixed appetites are the right load, and where sketch-driven design work is native.

### vs. Roger Martin / Playing to Win

Different altitudes. Playing to Win is corporate strategy (5 questions: winning aspiration, where to play, how to win, capabilities, management systems). Shape Up is product execution at the feature/initiative level.

**Compatible** — a company can use Playing to Win for corporate strategy and Shape Up for how features get built inside it.

### vs. Rumelt / Good Strategy Bad Strategy

Similar to Martin — different altitudes. Rumelt's kernel (diagnosis + guiding policy + coherent action + crux) helps you figure out what to work on at the strategic level. Shape Up helps you shape and ship the specific feature bets that follow.

**Use Rumelt** to find the crux. Use Shape Up to structure the bet on how to address it.

### vs. OKRs

Singer has not written a canonical "Shape Up vs. OKRs" piece.

**In practice, they run at different altitudes:**
- OKRs at the quarterly outcome level (revenue up X%, retention up Y%).
- Shape Up cycles at the specific feature bet level (this bet will move that input metric).

**The tension is around commitment:** OKRs commit to outcomes; Shape Up commits to solutions inside a fixed appetite. These are different objects and can coexist without conflict.

**Watch out for:** OKR mania causing teams to over-shape (writing PR/FAQs / Packages for every OKR sub-goal). Shape Up is for the big feature bets, not for every quarterly metric.

### vs. Lean Startup (Eric Ries)

- **Lean Startup:** minimum test that validates a hypothesis; build-measure-learn.
- **Shape Up:** shape a solution to a known problem worth solving; ship in 6 weeks.

**Different pre-conditions.** Lean Startup is pre-PMF; Shape Up is post-PMF. Trying to run Shape Up in a pre-PMF context wastes 6 weeks on a hypothesis you should have validated in a day.

### vs. Jobs-to-Be-Done (Christensen / Ulwick / Moesta)

- **JTBD:** a theory of *why* customers hire products.
- **Shape Up:** a process for shaping and shipping product bets.

**JTBD can be the substrate for framing.** A well-articulated Job can be the "framed problem" that goes into shaping.

**Complementary, not competing.**

## Common blends to avoid

1. **Scrum-with-6-week-sprints.** Backlogs, story points, sprint planning, retros — with a longer time-box. This isn't Shape Up. It's Scrum with a knob turned. The mechanisms of Shape Up (appetite, no backlog, circuit breaker) are absent.

2. **Shape Up + a backlog.** If you have a backlog, you're not running Shape Up. Full stop. The backlog is the exact idea the method rejects.

3. **Shape Up + story-pointed appetites.** Appetite is a budget, not a prediction. Story points are predictions. Do not combine.

4. **Shape Up applied to everything.** The method is for feature bets. Applying it to bugs, infra, or maintenance produces theater.

5. **Shape Up "at the team level" in a Scrum org.** You'll run two operating systems at once and the Scrum interfaces will keep leaking in. Either the org commits or borrow individual mechanisms rather than adopting the full cadence.

## Deciding which framework to reach for — a quick guide

Ask:

1. **Is the team pre-PMF?** → Lean Startup / Continuous Discovery.
2. **Is the work a feature bet with real design surface, post-PMF?** → Shape Up.
3. **Is the work a bug, maintenance, or infrastructure?** → Cool-down or Kanban.
4. **Is the question corporate strategy ("where to play, how to win")?** → Playing to Win or Rumelt.
5. **Is the question customer discovery / problem identification?** → Continuous Discovery Habits (Torres) or JTBD.
6. **Does the org run on the Amazon-scale bet-and-review model?** → Working Backwards may fit better than Shape Up.
7. **Is the team empowered end-to-end (PM + designer + engineers, owning discovery through delivery)?** → Cagan's model may fit better than the shaping/building separation.

If Shape Up fits — adopt it whole, with fidelity. If it doesn't — say so, and reach for the right tool.

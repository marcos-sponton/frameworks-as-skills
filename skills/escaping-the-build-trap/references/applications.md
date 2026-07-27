# Escaping the Build Trap — Applications

> When Perri's frame fits, when it doesn't, and what to reach for instead.

## Situations where the frame fits well

- **Auditing an existing PM organization.** The Four Dimensions (Product Organizational Design, Product Strategy, Product Operations, Product Culture) are a purpose-built audit checklist. See `method.md`.
- **Diagnosing a build-trap symptom.** The team ships features but customer/business metrics don't move. Perri's diagnostic — walking upstream from the symptom to the strategy vacuum or incentive structure — is exactly this shape of problem.
- **Redesigning the roadmap** when it has become a Gantt chart, sales contract, or feature-promise machine. The two-roadmap model (outcome-driven internal + feature-driven external) is her canonical fix.
- **Deploying strategy from Vision down to team-level work.** The 4-tier model (Vision → Strategic Intent → Product Initiatives → Options) exists for this.
- **Deciding whether/how to stand up a Product Operations function.** The Three Pillars framework tells you *what* Product Ops is, and the diagnostic tells you *whether* you're ready (Strategic Intent needs to be in place first).
- **Rewriting OKRs from output-disguised-as-outcome to real outcomes.** Ep 267 topic. Team-level not individual; must roll up from Strategic Intent.
- **PM career progression / job architecture.** The Tactical → Strategic → Operational ladder + PM archetype naming (Waiter / Mini-CEO / Strategic) gives you both the growth path and the diagnostic for where an individual PM is stuck.
- **Debating the "PM as mini-CEO" or "one throat to choke" pattern.** Perri has written more on this than anyone else in the field.
- **Countering Founder Mode as a scaling doctrine.** Her Sep 2024 essay is the canonical response.
- **Making sense of a Fuzzy Strategy.** The 4 value drivers (Increase / Protect Revenue; Reduce / Avoid Costs) force the mechanism out of vague executive intent.
- **Evaluating whether an org is *actually* product-led or just uses the vocabulary.** Her contrast lists (sales-led vs. product-led; feature-driven vs. outcome-driven) are the diagnostic tool.

## Situations where it does NOT fit

- **Pre-product/market-fit startups.** Perri's frame assumes you have a product and a team large enough to have the pathology. Pre-PMF is search, not operational maturity. Redirect to Lean Startup (Ries), Continuous Discovery (Torres), or JTBD (Moesta/Kalbach). If the user is a solo founder or seed-stage team, tell them the frame is premature and point them to those.

- **Pure engineering / delivery velocity questions.** "How do we ship faster?" or "what's the right CI/CD strategy?" aren't Perri questions. Suggest Shape Up (Ryan Singer), DORA metrics, or SRE playbooks depending on the flavor.

- **Top-level organizational transformation (Product Operating Model).** Perri cedes this altitude to Marty Cagan (*Transformed*, 2024). If the user is asking "how do we transform the entire company to be product-led at the exec level?", credit Cagan and use this skill for the operational scaffolding underneath.

- **Consumer marketing / brand strategy.** Not Perri's domain. Reach for April Dunford (positioning), Andy Raskin (narrative), or a marketing-strategy frame instead.

- **Pure business-strategy questions (where to play, how to win).** Perri assumes the business strategy exists (or names the vacuum explicitly). If the user is doing business strategy from scratch, use Playing to Win (Martin) or Good Strategy Bad Strategy (Rumelt) *first*, then bring Perri in for the product-org side.

- **Turnaround / crisis situations where the diagnosis is more urgent than the operational fix.** If the org is on fire, do Rumelt-style crux diagnosis first (find the pivotal problem), then apply Perri's frame for the product-org response.

- **When the user just wants a summary of *Escaping the Build Trap*.** Give them the book link. Don't run the diagnostic at them.

## Adjacent frameworks — when to reach for a different one

| If the user's situation is... | Reach for... | Why |
|---|---|---|
| Pre-PMF startup search | Lean Startup (Ries), Continuous Discovery (Torres), JTBD (Moesta) | Search, not operational maturity |
| Top-level org transformation to Product Operating Model | Marty Cagan / *Transformed* | Cagan owns this altitude; Perri operates one level down |
| Tactical discovery cadence — weekly interviews, opportunity trees | Teresa Torres / *Continuous Discovery Habits* | Torres = tactical cadence; Perri = strategic + operational scaffolding around it |
| Delivery-cadence design (6-week cycles, appetites, shaping) | Ryan Singer / *Shape Up* | Shape Up solves delivery; Perri solves discovery + strategy above it |
| Understanding demand / job progression | Bob Moesta or Jim Kalbach / JTBD | JTBD fits inside Perri's "problem" framing but with more specific method |
| Business strategy from scratch (where to play, how to win) | Roger Martin / *Playing to Win* | Playing to Win = business strategy above the product org |
| Diagnosis of what's structurally broken before choosing | Richard Rumelt / *Good Strategy Bad Strategy* | Rumelt front-loads diagnosis; Perri front-loads operational structure |
| Positioning (marketing) | April Dunford / *Obviously Awesome* | Positioning is downstream of the product strategy Perri helps set |
| Coming up with a compelling market narrative | Andy Raskin / *Strategic Narrative* | Narrative is downstream artifact |
| Individual PM skill development | Product Institute (Perri's own courses), Reforge, Marty Cagan's Silicon Valley Product Group | Skill training vs. org design |
| Change management once the strategy is chosen | Kotter, ADKAR | Perri tells you what to change to; not how to change the org |

## How Perri composes with other frameworks

Perri has commented on adjacencies in podcasts and essays. Highlights:

### Composes well with Cagan (complementary, one altitude apart)

Cagan (*Transformed*, 2024) owns the top-level phrase **Product Operating Model** and the exec-level transformation conversation. Perri operates one altitude below — the PM function health, PM career progression, and the operational infrastructure (Product Ops) that makes the transformation stick.

**Cagan explicitly credits Perri's Product Ops definition.** They don't compete; they compose:
- Use Cagan to align exec team on the transformation.
- Use Perri to build the PM function health and operational infrastructure underneath.

**Divergences worth noting:**
- Cagan is more prescriptive about the "product trio" (PM + design + eng jointly own discovery).
- Perri is more flexible on structure but stricter on the PM role's substance (not order-taker, not mini-CEO).
- Cagan is more evangelical about "empowered teams".
- Perri is more diagnostic about *why* teams aren't empowered (usually: no strategy above them).

### Composes well with Torres (highly compatible, tactical fit)

Perri promotes Torres explicitly (Product Thinking Ep 269, May 2026). Torres's **Opportunity Solution Tree** fits inside Perri's Product Kata / problem-exploration → solution-experimentation loop.

- **Torres** = tactical discovery cadence — weekly interviews, opportunity mapping, assumption testing.
- **Perri** = strategic scaffolding around that cadence — Strategic Intent above, Product Ops as fuel, PM career growth to sustain it.

A PM using Torres's habits inside Perri's frame is Perri's ideal PM.

### Composes well with Singer / Shape Up (compatible on delivery side)

Shape Up's "appetite over estimate" and "shaping before betting" are consistent with Perri's rejection of Gantt-style roadmaps and her Problem Roadmap. But Shape Up is a *delivery cadence*; Perri's frame is broader (career, strategy, culture, ops).

Perri would say: Shape Up solves the delivery-side of the build trap but not the strategy-vacuum-above-teams problem. Use both, with Shape Up as the delivery mechanism inside a Perri-shaped org.

### Composes well with JTBD (Christensen / Moesta / Kalbach)

Compatible with her "fall in love with the problem" doctrine. She uses "problem" as her primary unit, not "job", but the underlying discipline (understand demand before designing supply) is the same.

She rarely uses JTBD vocabulary directly — she stays in "customer problems" language for accessibility. A PM operating in her frame would find JTBD a natural discovery method inside the Problem Roadmap.

### Composes well with Ries / Lean Startup (foundational, redefined)

Foundational influence. She keeps "build-measure-learn" and MVP concept but **explicitly redefines MVP** as "minimum amount of effort to learn" and prefers "solution experimentation" to break the association of MVP with "small first version to ship."

If the user invokes Lean Startup, respect the lineage but use Perri's refined vocabulary.

### Composes with OKRs, but with two constraints

Perri uses OKRs, but insists:
- **Team-level, not individual** (Substack Jun 2024).
- **Must roll up from Strategic Intent** (Ep 267 — "How OKRs Become Outputs Instead of Outcomes").

Warns against OKRs used to enforce output targets or as MBO-in-disguise.

### Composes with HEART and AARRR

Recommends both by name for team-level metrics inside the Kata:
- **HEART** (Google) for UX metrics — Happiness, Engagement, Adoption, Retention, Task success.
- **AARRR / Pirate Metrics** (McClure) for growth — Acquisition, Activation, Retention, Referral, Revenue.

## Frameworks Perri has explicitly pushed back on

- **SAFe** — explicitly does *not* recommend. Rewards output cadence over outcome learning.
- **PM as mini-CEO** — dismantles this every chance she gets.
- **Roadmap-as-contract / Gantt-chart roadmap** — the pattern the Problem Roadmap exists to replace.
- **Individual OKRs** at the executive level — creates siloed fiefdoms.
- **Certification-as-training** without mentorship — surface credentials without depth.
- **Product Owner as PM synonym** — collapses a strategic function into a Scrum role.
- **Founder Mode as scaling doctrine** — 0→1 pattern misapplied to 1→N.
- **"One throat to choke" accountability** — individual accountability for team-level outcomes.

If the user invokes any of these expecting them to work, redirect gently but clearly — with attribution to the essay/podcast where Perri makes the case.

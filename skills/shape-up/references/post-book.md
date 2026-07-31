# Shape Up — Post-Book Material (2020 → 2026)

> Everything Ryan Singer has published *after* the 2019 book, in rough chronological order. This is the differential of the skill — the density the book alone doesn't capture. The 2019 mechanisms are all still current; what's changed is that Singer has (a) added Framing as an upstream step, (b) renamed "Pitch" to "Package," (c) explicitly framed the 2019 book as describing "an unusual company" (Basecamp) and evolved *Shaping in Real Life* to adapt the method for typical companies, and (d) catalogued adoption failure modes in a 2025 essay. Nothing has been formally deprecated.

## The move from Basecamp to Felt Presence (2020 → present)

Singer left Basecamp / 37signals around 2020 after 17 years and founded [Felt Presence LLC](https://ryansinger.co) — consulting, coaching, and workshops for teams adopting or adapting Shape Up. His site (originally feltpresence.com, now redirecting to ryansinger.co) is the primary post-book publishing hub.

**Services offered:**
- **3-hour shaping sessions** — Singer works with a client team through one real shaping session live.
- **Workshops** — team-based coaching on adopting Shape Up mechanisms.
- **"Shaping in Real Life"** — formerly a paid online course; now free articles and videos on ryansinger.co.
- **Advisory / coaching** — retainer arrangements with product teams.

Publishing cadence: roughly one substantial article every 2–4 months on ryansinger.co, plus occasional podcast appearances (Lenny 2025 is the freshest long-form).

## Framing (2022) — the single most important post-book addition

**Source:** https://www.ryansinger.co/framing/

The 2019 book leaps from "raw idea" straight into shaping. In practice this produced rework: teams shaped solutions to problems the business hadn't agreed were worth solving. The 2022 *Framing* essay introduces the missing upstream step.

**The new sequence:**
- **Framing → Shaping → Package → Betting Table → Building → Cool-down**

**Framing** is a small-group activity (often the founder / head of product plus one senior stakeholder) that answers: whose problem, why now, what's the business value, is it worth committing weeks of engineering time. **No solutions yet.** The output is a *framed problem*, not a shaped solution.

**Singer's own words:**

> "Framing is all about the problem and the business value."
> — *Framing*, 2022.

> "The output of a framing session is a well-framed problem: something where the business says 'if we can shape this into something doable and execute within X weeks, that will be meaningful to us.'"
> — *Framing*, 2022.

This is post-book **canon**, not extension. Any 2026 application of Shape Up should include framing.

## "Pitch" → "Package" (2022+) — a naming refinement

Singer's 2022+ writing consistently uses **"Package"** in place of **"Pitch"** as the label for shaping's output.

**Why the change:** "Pitch" implied selling to leadership; "Package" emphasizes that shaping produces a *package of decisions* ready to be bet on. Same artifact, same five ingredients (Problem, Appetite, Solution, Rabbit Holes, No-Gos), better name.

**Practical rule:** use "Pitch" when citing the 2019 book; use "Package" when discussing Singer's current teaching. Both are correct; both are Singer's words at different points in time.

## Shaping in Real Life (informal 2020+ series)

**What it is:** Singer's ongoing project of adapting the 2019 book for **typical companies**. Formerly a paid online course; now distributed as free articles and videos on ryansinger.co.

**Core delta from the 2019 book:** the book describes "an unusual company" — Basecamp:
- Everyone technical, including designers (no seam between design and code).
- Tiny team (~15 people at the time).
- Unified skills, no PM/designer/engineer siloing.
- Product-led CEO (Jason Fried) who framed implicitly.

Most companies aren't like that. Typical B2B SaaS looks like:
- Separate backend / frontend / designer / QA / product / marketing / sales.
- Non-technical PMs who shape in isolation.
- Legacy systems that make simple things take months.
- Leadership that doesn't frame explicitly — just says "improve the dashboard."

**Shaping in Real Life adaptations:**
- **Engineer the technical shaper explicitly.** Pair non-technical PMs with a senior engineer for every shaping session.
- **Separate framing from shaping as visible steps.** In Basecamp, framing was implicit; elsewhere, make it a step.
- **Handle legacy systems.** When engineers say "that'll take months!", the answer often isn't more shaping — it's separating a shaping bet from a technical debt bet.
- **Handle non-Basecamp team structures.** The 2025 case study walks through a typical team (backend, frontend, designer, QA, SME) and shows the adaptations required.

## Shape Up 2.0 (informal label, used on Shapers & Builders 2023)

Singer used the phrase "Shape Up 2.0" on the *Shapers & Builders* podcast (2023-05-01) to describe the evolved model — framing prelude, Package rename, Shaping in Real Life adaptations. It is **not** a formal second edition of the book (though a "second edition" is mentioned as an in-progress topic in the Lenny 2025 interview; treat as unconfirmed until Singer publishes).

**Source:** https://shapersbuilders.transistor.fm/episodes/getting-to-shape-up-2-0-ryan-singer-author-of-shape-up-founder-at-felt-presence

## Common Pitfalls When Adopting Shape Up (2025) — the densest adoption-failure catalog

**Source:** https://www.ryansinger.co/pitfalls-when-adopting-shape-up/

The single most useful post-book piece for anyone helping a team adopt Shape Up. Names three primary failure modes:

**1. Undershaped work — "The #1 failure mode of attempted Shape Up adoptions."**
- Non-technical shapers produce packages that look complete but crumble in build.
- The pitch reads well but the build team is confused by day 2.
- Rabbit holes weren't named. No-gos weren't named.
- Fix: shape again. Do not proceed to betting on undershaped work.

**2. Blurred framing and shaping.**
> "Framing is about the problem, the business value, the outcome, etc. Shaping is about the technical solution."
> — Singer, *Common Pitfalls*, 2025.
- Teams that skip framing often *think* they framed because they discussed the problem briefly. Framing produces a *framed problem* as an artifact.

**3. Mixing project work with reactive work.**
- Same team owning maintenance, support, *and* projects loses focus mid-cycle.
- The cycle mechanism assumes protected time; reactive work destroys the protection.
- Fix: separate the operating modes. Feature bets in cycles; everything else in cool-down or a different team.

**Bonus catalog quote (defines "shaped"):**
> "Shaped means 'we can give this to someone to build and they will know what to do.'"
> — Singer, *Common Pitfalls*, 2025.

## End-to-End with Shape Up: A Real-World Case Study (2025)

**Source:** https://www.ryansinger.co/end-to-end-with-shape-up-a-real-world-case-study/

A ~30-minute worked example on a gym-management software product acquired by a real company. Singer walks the whole loop: candidate → framing (interview with a former gym owner) → shaping (two 2-hour whiteboard sessions with a senior engineer) → package written → build kickoff with a cross-functional team (backend, frontend, designer, QA, SME) → sequencing 9 vertical slices → shipping.

**Key notable moves in the case study:**

- **One candidate at a time.** "We're actually narrowing down before we even shape." Don't shape ten pitches — narrow through framing, then shape one.
- **Two 2-hour shaping sessions with a senior engineer.** Technical depth is not optional.
- **Reframing mid-shaping.** The original ask was "improve the dashboard"; after the SME conversation, the real problem was "payment recovery." The pitch shifted accordingly.
- **9 vertical slices at kickoff.** The build team decomposed into scopes early — the shapers didn't hand them a task list.
- **Wire functionality first, high-fidelity design later.** The team got to a working end-to-end skeleton before polishing any single screen.

This is the freshest worked example available in Singer's public writing. Use it as the canonical adaptation-for-typical-company case.

## What's the right level of detail when shaping? (2026)

**Source:** https://www.ryansinger.co/whats-the-right-level-of-detail-when-shaping/

A 2026 sharpening of the fat-marker-sketch discipline. The answer depends on the document's purpose:

- **If seeking approval** (from a Betting Table with skeptical stakeholders): more detail, more specifics, more attention to the "would customers adopt this" question.
- **If providing direction** (to a build team you already trust): less detail, more structural, more room for the team to make specific decisions.

This is a nuance the 2019 book didn't capture — it treated fidelity as uniformly low. In practice, adjust to the audience.

## When engineers say "that'll take months!" (2025)

**Source:** https://www.ryansinger.co/when-engineers-say-thatll-take-months/

Legacy systems create the perception that everything is a months-long project. Singer's argument: this isn't a shaping problem — it's a technical debt problem that needs its own operating mode (often, a separate bet on unblocking the legacy). Shaping alone won't rescue a team drowning in legacy.

## Not everyone needs to be talking to customers (2024)

**Source:** https://www.ryansinger.co/not-everyone-needs-to-be-talking-to-customers/

A mild pushback against the Teresa Torres / Continuous Discovery orthodoxy that every product team member should interview users weekly. Singer's argument: specialization is legitimate. The framer / shaper needs deep customer context; the build team can trust the framing and shaping and get on with building.

**Not a rejection of Torres** — Singer respects the work. But a defense of specialization against the "everyone in every interview" default.

## We did all this discovery… now how do we decide? (2024)

**Source:** https://www.ryansinger.co/discovery-how-to-decide/

The framing → decision leap. Discovery data doesn't tell you what to bet on; you still have to weigh competing inputs and choose. Framing is the operator's tool for making that leap — it's what turns discovery into a decision.

## What's the unit of impact? (2024)

**Source:** https://www.ryansinger.co/whats-a-unit-of-impact/

A pragmatic essay on defining impact in terms of current business priorities rather than universal metrics. Impact means different things at different stages — the "unit" is defined by the business, not by a framework.

## The cost of not shaping (2023)

**Source:** https://www.ryansinger.co/the-cost-of-not-shaping/

Projects without proper shaping either succeed by luck or stall mysteriously near the end. The essay names the hidden cost: unshaped work looks cheap in the pitch stage (nothing to write down, no fidelity to argue about) but becomes expensive in the build stage (constant re-decision, scope surprises, integration failure).

## Shape Up is for features, not all development work (2021)

**Source:** https://www.ryansinger.co/shape-up-is-for-features-not-all-development-work/

One of the earliest and most-cited post-book clarifications. Shape Up is designed for **new feature bets**, not maintenance, infrastructure, or bug work. Trying to apply it to everything destroys the mechanism.

**Practical rule:** feature bets go in cycles. Everything else lives in cool-down or a separate operating mode.

## AI-era commentary — noteworthy caveat

Little direct Singer commentary on how AI-native product development changes shaping. He has commented informally on Twitter/LinkedIn that AI shifts what "uphill" work looks like (unknowns collapse faster; the shape of the "figuring out" phase changes when a coding agent can spike solutions in an hour). But there is no canonical Singer essay on AI as of 2026-07.

**If a user asks "how does Shape Up apply in an AI-native product?":** you are extrapolating. Say so. The mechanisms (fixed cycle, appetite, no backlog, circuit breaker) should still hold; the *feel* of shaping and building may shift as AI collapses uphill time. But this is inference, not Singer's teaching.

## "The Circuit Breaker" as an upcoming book — status: unconfirmed

Rumor in the Shape Up community about an in-progress Singer follow-up book. **No public confirmation from Singer or a publisher as of 2026-07.** In the 2019 book, "Circuit Breaker" is the *concept* — the default of killing a bet that runs over its six-week appetite. Treat any "coming book" claim as unconfirmed unless Singer's site or newsletter announces it.

## Podcast appearances (post-2020, chronological, freshest first)

- **Bright & Early** (2026-03-28) — early-stage startup podcast; Singer as Felt Presence founder on adapting Shape Up for young companies.
- **The Product Experience** (2025-09-04, Mind the Product) — https://www.mindtheproduct.com/shape-up-ryan-singer-on-the-product-experience/
- **Lenny's Podcast** (2025-03-30) — "A better way to plan, build, and ship products." **The freshest long-form primary source.** ~90 min. https://www.lennysnewsletter.com/p/shape-up-ryan-singer · https://open.spotify.com/episode/0z5ShjcJfCMFVh8w91gCfK
- **Shapers & Builders** (2023-05-01) — "Getting to Shape Up 2.0." Singer explicitly frames the evolved model. https://shapersbuilders.transistor.fm/episodes/getting-to-shape-up-2-0-ryan-singer-author-of-shape-up-founder-at-felt-presence

For the 2019 book-launch primary interview, see the Changelog #357 (still valuable as canonical grounding) — https://changelog.com/podcast/357

## Summary — what's changed since 2019

**Added:** Framing (2022) as upstream step. "Package" as newer name for "Pitch." *Shaping in Real Life* material adapting the method for non-Basecamp companies. The 2025 *Common Pitfalls* catalog. The 2025 *End-to-End* case study. Essays on discovery, customer interviews, impact, legacy systems.

**Sharpened:** technical shaping is now insisted on explicitly. Narrow-to-one-candidate-before-shaping is now the recommended default. Wire-functionality-first-during-build is documented in the case study. Detail level in shaping should adjust to the audience (2026).

**Deprecated:** nothing formally. All 2019 mechanisms are still current teaching.

**Rumored but unconfirmed:** a "second edition" of the book (mentioned in passing on Lenny 2025). An upcoming Singer book "The Circuit Breaker." Neither has been publicly announced by Singer or a publisher.

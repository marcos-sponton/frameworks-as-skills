# Working Backwards — Material posterior al libro

> **This is the differential of this skill.** The 2021 book laid down PR/FAQ, 6-pager, STL, input metrics, Bar Raiser, and the surrounding mechanisms. Since then, Bill Carr and Colin Bryar have chosen a different second act from other framework-authors: rather than writing more essays, they built [Working Backwards LLC](https://workingbackwards.com) and productized the mechanisms as courses and advisory. Post-book refinements live inside course curricula, a firm blog that became active in March 2026, and a handful of podcast appearances (Bill Carr on Lenny 2023 is the richest single source).
>
> Most Claude/Codex responses about Working Backwards pull from the book alone. This file captures what's changed since 2021: sharpened warnings, new coinages, and a productized delivery model. Organized so you can pull the specific piece you need.

## The strategic choice — consultancy over second book

Carr and Bryar founded Working Backwards LLC around the book's launch (2020–2021) and have poured their post-book energy into direct client work rather than continued long-form writing. This is unusual among framework-authors and matters for how you should treat their post-book material:

- **The course catalog is a truer index of what they now teach than the book's table of contents.** Five courses — PR/FAQ Mastery, Input Metrics Mastery, Operating Plan Mastery, Bar Raiser Hiring Mastery, Business Narratives Mastery — each of which represents where they've invested pedagogical refinement.
- **The firm's blog picked up cadence in March 2026** after being quieter for years. If the user asks "what's new since the book," the blog is the answer.
- **They productized a piece of software: the WBR App.** https://workingbackwards.com/wbr-app/ (open source at https://github.com/working-backwards/wbr-app). This is a post-book move — the book describes the WBR meeting, the app operationalizes it.

## Refinements and additions since 2021

### The compensation-planning doom loop

**Where it appears:** [Ending the compensation-planning doom loop in leadership](https://workingbackwards.com/blog/ending-the-compensation-planning-doom-loop-in-leadership/), Bill Carr, March 2026.

**Old (in the book):** Operating Plan process described mostly as a mechanism for aligning inputs to strategy.

**New (2026):** explicit warning about the failure mode when Operating Plan targets get hard-coded to individual annual bonuses.

**Carr's diagnosis:**
> "When annual bonus targets are hard-coded into Operating Plan goals, the planning process stops being about taking calculated risks that will benefit your customers and the company, and it starts being about maximizing personal compensation."

**Carr's prescription — three mechanisms:**
1. **Long-term equity compensation** instead of quarterly/annual bonuses.
2. **Holistic performance reviews** assessing "totality of performance" rather than binary hit/miss on plan targets.
3. **Shared risk through leadership vetting of plans** — the leaders reviewing the plan also carry the risk of its ambition level.

**Carr's closing:**
> "If you want a culture that takes big swings, you must build a system where execution is rewarded and risk is shared — not one where the system is rigged to play it safe."

**Why this matters for the skill:** the book didn't emphasize this. In 2026 it's a first-class warning. When a user is designing an Operating Plan process, reach for this refinement.

### The coordination tax framing for STL

**Where it appears:** March 2026 firm blog posts including "Minimizing coordination tax to maximize team ownership" and "Scale without bureaucracy using single-threaded teams."

**Old (in the book):** STL was pitched as "one leader per initiative, dedicated resources."

**New (2026):** STL sharpened around the *coordination tax* — the compounding cost of every dependency between teams. The 2026 pitch to skeptical engineering leaders isn't "one throat to choke" — it's "the structural minimization of the coordination cost that eats every initiative."

**Why this matters for the skill:** when the user is skeptical of the STL model, or works in an org that prides itself on cross-functional collaboration, this framing lands differently than the book's phrasing.

### Separating innovation from core business

**Where it appears:** March 2026 firm blog "Separate innovation from core business to succeed effectively" and "Balancing operators and inventors to sustain growth."

**Old (in the book):** implied through the story of how AWS was allowed to develop separately.

**New (2026):** explicit prescription. Innovation and core-business execution require different mechanisms, different dispositions, and different operating cadences. Running both under the same STL, in the same review meeting, with the same metrics, starves innovation.

**Why this matters:** when the user is trying to build something new inside a mature business, this is the diagnostic. Ask: is this initiative structurally separated from the core, or is it competing for the same review meetings, metrics, and bonus pool?

### Atomic customer needs

**Where it appears:** March 2026 firm blog "Identifying atomic customer needs that drive growth."

**Old (in the book):** the "problem paragraph" of the PR/FAQ was the customer-need articulation.

**New (2026):** push the problem paragraph toward *atomic* customer needs — "needs so deeply embedded that they will persist across time periods." A stated preference flips with a trend; an atomic need is why Prime free shipping still works twenty years later.

**Why this matters:** when reviewing a draft PR/FAQ, this is the sharpening question. Is the problem paragraph naming an atomic need, or a surface preference?

### Reclaiming leadership from drift toward small bets

**Where it appears:** March 2026 firm blog "Reclaim leadership by prioritizing big strategic bets."

**Old (in the book):** implied through the stories of Kindle, Prime, and AWS — Amazon's willingness to make big multi-year bets.

**New (2026):** explicit diagnostic. "Organizations naturally drift toward smaller, more manageable decisions rather than significant, complex ones." Mechanisms alone don't stop this drift. Leadership has to actively resist it by asking in every planning cycle: where is our next big bet?

**Why this matters:** if a user is running the mechanisms but never getting big bets out of them, the diagnosis may be leadership drift, not mechanism failure.

## What has NOT changed

- **The core mechanisms.** PR/FAQ structure (Press Release + External FAQ + Internal FAQ), the six-page narrative memo format (prose, no bullets, silent reading), STL, Input Metrics, Bar Raiser, WBR, COE, Disagree and Commit — none of these have been renamed, restructured, or deprecated.
- **The customer-obsession first principle.** The frame is exactly as the book describes it.
- **Bezos's meta-principle.** "Good intentions don't work. Mechanisms do." is still the North Star.
- **The 14 Leadership Principles as substrate.** Still the disposition the mechanisms rely on.

## Non-Amazon applications — the firm's cautious external cases

The firm has begun applying the Working Backwards lens to non-Amazon situations. The most public example:

- [Why Netflix's Warner Bros. acquisition could fail long term](https://workingbackwards.com/blog/why-netflixs-warner-bros-acquisition-could-fail-long-term/), March 2026. Analyzed through the customer-need + STL + mechanism lens rather than through pure M&A logic.

This is a limited but useful signal: the firm is comfortable applying the framework beyond Amazon, but has not yet published a book's worth of external cases.

## AI-era commentary — a gap

Little direct commentary from Carr or Bryar on how AI changes any of the mechanisms. The mechanisms are portrayed as durable regardless of technology stack:

- The PR/FAQ format is neutral to what technology is inside the product.
- Customer obsession as a first principle survives any technology transition.
- Input metrics still decompose to controllable levers, whether the underlying product uses LLMs or not.

If a user asks "how does Working Backwards apply in an AI-native product?", you're extrapolating — the primary voices haven't spoken on it explicitly. Note this to the user and treat any application as informed inference rather than the authors' own position.

## How to use this material in a session

- If the user is drafting an Operating Plan or thinking about compensation → cite the compensation-planning doom loop essay directly.
- If the user is skeptical of STL or works in a matrix org → use the coordination tax framing (2026), not just the book's phrasing.
- If the user is trying to build innovation inside a mature business → cite the "separate innovation from core" post.
- If the user is writing a PR/FAQ and the problem paragraph feels weak → push toward "atomic customer needs" (2026 framing).
- If the user is running the mechanisms but not getting big bets → diagnose leadership drift, not mechanism failure.
- If the user asks "what's new since the book" → point them at the March 2026 blog batch as the freshest primary output.

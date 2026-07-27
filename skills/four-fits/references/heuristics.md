# Four Fits — Heuristics, Do's, Don'ts, Gotchas

> The practical devices — Balfour's "operational moves" — that separate applying Four Fits well from doing the version he spends most of his airtime critiquing. Attribution to specific essays where possible.

## Do's

### Diagnose which fit is broken before proposing any fix

Growth stalling is not a generic problem. It's almost always one specific fit that has broken. Naming the fit is 80% of the solution.

**How to apply:** score each of the four fits 1–5 with evidence. The lowest score is where to look. Fix upstream fits before downstream ones — a broken Product-Market Fit makes everything downstream noise.

**Author's words:**
> "Each of these fits influence each other, so you can't think about them in isolation."
> — *Four Fits For $100M+ Growth*

### Design product FOR channel, not around it

The signature Balfour move. Before committing to a product shape, ask: what channel could I plausibly acquire from at scale, and what does that channel demand?

**How to apply:** pick your top 2 candidate channels. For each, list what product mechanism produces the fuel that channel needs (viral loops require a native invite mechanic, content/SEO requires user-created indexable content, paid requires a landing-page conversion path with 5x LTV/CAC).

**Author's words:**
> "Products are built to fit with channels. Channels do not mold to products."
> — *Four Fits For $100M+ Growth*

### Test whether a claimed "growth loop" actually closes

Before accepting anything as a loop, force the diagram: input → action → output → back to input. If the arrow doesn't literally close (via product mechanism + numbers), it's a funnel wearing loop vocabulary.

**How to apply:**
1. Name the input (source of new users this cycle)
2. Name the action (what the user does)
3. Name the output (what the action produces)
4. Name the mechanism that turns the output into next cycle's input
5. Estimate the amplification factor (>1 = compounds; <1 = decays)

**Author's words:**
> "Loops compound. Funnels decay."
> — *Growth Loops are the New Funnels* (Reforge, 2018)

### Force yourself out of the ARPU Danger Zone

If your ARPU sits in the $100–$1k range with no clean channel-model fit, don't try harder — restructure. Either move up-market (higher ARPU, enterprise or mid-market sales) or drop down (freemium, PLG, viral).

**How to apply:** map your ARPU on the five-zone spectrum. If middle, name the specific move (add enterprise tier / add free tier / consumerize product). Then test whether the new fit chain still holds.

**Author's words:**
> "Get out of the ARPU-CAC danger zone."
> — essay title

### Check the Model-Market threshold with 10% capture

Before committing to a market, run: `ARPU × TAM × 10% ≥ $100M?` If not at 10%, don't lie to yourself with 30%. Either expand the market definition (and re-verify PMF), raise ARPU, or accept you're building a smaller business.

**Source:** *The Model Market Fit Threshold*

### Run all four fits together, not sequentially

The chain is coupled. Fixing PMF in isolation without checking whether the fix breaks Product-Channel or Channel-Model Fit produces the same trap it was supposed to solve.

**How to apply:** any time you propose a change to one fit, ask what it does to the other three. If any of them breaks, either integrate the fix or discard.

### Re-check fits quarterly in the AI era (2024+)

Fits used to hold for years. AI now compresses the cycle. Chegg lost PMF in 9 months. Search-based Product-Channel Fits are being disrupted by ChatGPT discovery. Freemium Channel-Model Fits are being stressed by AI inference costs.

**Source:** *The Four Fits: A Growth Framework for the AI Era* (2024)

### Diagram the coupling before making structural bets

Before "we're going enterprise", "we're going PLG", "we're launching a marketplace", draw all four fits pre- and post-. If the four-box picture doesn't hang together on both sides, the bet is fragile.

## Don'ts

### Don't treat growth as a bag of tactics

The most common misuse. "What's the best growth hack for X" is not a Four Fits question — it's below the level of the framework.

**Author's words:**
> "Growth is a system between acquisition, retention, and monetization. Change one and you affect them all."
> — Lenny's Podcast, 2023

**Redirect:** name the fit that's actually broken; the tactic falls out of the diagnosis.

### Don't decouple product from channel

Building a finished product and then hiring a growth marketer to "figure out the channel" is Balfour's most-named anti-pattern. By the time the product is finished, its shape is fixed and no channel fits.

**Redirect:** every product decision needs to be checked against the channels it opens or closes.

### Don't copy playbooks from companies with different fits

"Airbnb did SEO, we should do SEO." "Slack went viral in B2B, we should too." Playbooks are downstream of a specific four-fit chain. If your ARPU / TAM / channels differ, the playbook is noise.

**Author's words (paraphrased across essays):** the playbook belongs to the company whose fits produced it.

**Redirect:** diagnose your own four fits, then design tactics that match.

### Don't accept a funnel dressed as a loop

Renaming the bottom of a funnel "feeds back to top" doesn't make it a loop. If no mechanism operationally connects output to input, it's still a funnel.

**Test:** does removing the alleged "feedback" step change acquisition math? If no, it wasn't really a loop.

### Don't hire a growth team pre-PMF

Growth calories before PMF go into the wrong hole. The team optimizes activation for users who won't retain, or chases channels for a product that hasn't earned them.

**Redirect:** run continuous discovery / JTBD / lean until you have retention curves that flatten. Then hire growth.

### Don't ride ONE channel

Single-channel dependency is fragile. Every dominant channel eventually decays (Facebook organic reach, Google SEO, App Store featuring, cold email deliverability). Cover with 2–3 loops in parallel.

### Don't confuse North Star metric with strategy

A North Star that measures only one leg (acquisition, activation, retention, monetization) misallocates. Balfour: *"Don't let your North Star metric deceive you."* Measure the whole system, not the metric that looks best in a board deck.

**Source:** *Don't Let Your North Star Metric Deceive You*

### Don't chase ChatGPT-as-channel without changing product

ChatGPT / agent-driven discovery is a real channel shift. But bolting "we're on ChatGPT" onto an existing product without changing what the product produces (structured content, LLM-consumable data, agent-callable APIs) is the same anti-pattern as "we'll figure out SEO later".

**Source:** *Why ChatGPT Will Be the Next Big Growth Channel* (Lenny's Podcast, 2024)

## Gotchas (things that go wrong even when you think you're doing it right)

### The "we have PMF, growth should work" trap

PMF is necessary but not sufficient. Companies with PMF alone are "tugboats" — grinding for growth without compounding. Balfour's whole reason for writing the Four Fits essay was that founders were declaring victory at PMF and then failing to scale.

### The Danger Zone denial

Mid-ARPU SaaS founders resist the Danger Zone diagnosis because it implies restructuring. "We'll find the channel" — no, you won't, structurally. The math is against you until you move up or down.

### The multi-loop mirage

Some teams have one loop that works and 3 loops that don't and call it "multi-loop diversification". Two dying loops don't add up to one healthy one. Only count loops with amplification ≥1.

### The channel that worked at seed doesn't work at Series B

A channel with tight Product-Channel Fit at 1,000 users may saturate at 100,000 users. Founder-led sales, PH launches, hand-crafted content — all decay past a certain scale. Re-verify Product-Channel Fit at each scale threshold.

### The reverse: a channel that broke at seed might work at scale

Paid ads with $200 CAC don't work at $600 LTV. They might work at $6,000 LTV. Some channels only unlock post-tier-upgrade. Don't kill channels prematurely; note the ARPU threshold at which they'd open.

### "Growth loop" for something with a 6-month cycle time

Cycle time matters as much as amplification. A viral loop with 1.3 amplification but a 90-day cycle time isn't a "compounding" loop in any operational sense — it's slow decay dressed up.

### The AI-era PMF cliff

Companies with prior PMF are losing it in months, not years. Chegg (Jan → Oct 2024). The gotcha: your last quarterly PMF check is stale. Re-verify continuously.

## Pro tips (accelerators — small devices that punch above their weight)

### Score fits 1–5 with a specific witness

Ambiguous fit scores hide problems. Force each score to name the observable signal: retention curve shape, organic vs. paid ratio, CAC:LTV, sales cycle length, capture math.

### Diagram fits as a chain, not a 2x2

Balfour draws them left-to-right: PMF → Product-Channel → Channel-Model → Model-Market. Any break is visible. Founders drawing them as boxes in a matrix miss the coupling.

### Reverse-engineer a smooth-sailer

Pick a competitor or adjacent company whose growth looks effortless. Reverse-engineer their four fits. Then diagnose why your version of the four fits produces the tugboat feel. Difference isn't tactics — it's fit alignment.

### Use the five business archetypes as a naming convention

Force yourself to name whether you're Elephants / Moose / Rabbits / Mice / Flies. It clarifies pricing, sales motion, TAM math, and organizational structure all at once.

### For growth loops: pre-mortem the decay

Every loop eventually decays. Before you launch, name the specific saturation point (channel exhaustion, algorithm change, market maturity) and the fallback loop you'd shift to.

### Run WWHTBT on the fits (borrowed from Roger Martin)

"What would have to be true for our Product-Channel Fit to hold at 10x scale?" Naming the assumptions makes them testable. See the `playing-to-win` skill for the full WWHTBT device.

## Anti-patterns (the "bad growth thinking" Balfour explicitly names)

### "We just need a growth hack"

**What it looks like:** framing growth as a bag of tactics, ideally one clever tactic.
**Why it fails:** growth is a system. Any tactic without system context is a lottery ticket.
**Redirect:** diagnose the fit chain; the tactic falls out.

### "We have PMF, so growth should work"

**What it looks like:** founders declaring PMF and expecting growth to follow.
**Why it fails:** PMF is one of four fits. The other three can silently strangle scale.
**Redirect:** name whether you're tugboat or smooth sailer. If tugboat, you're missing one of the other three fits.

### Channel-agnostic strategy

**What it looks like:** "we'll try a bunch of channels and see what works."
**Why it fails:** channels have mechanics; products either match or don't. Channel-agnostic trials waste time when the product structurally can't feed the channel.
**Redirect:** name the top 2 channels first, then design product mechanisms to fuel them.

### Copy Airbnb / Slack / Notion / Duolingo

**What it looks like:** playbook-copying without matching the underlying fit chain.
**Why it fails:** those playbooks are downstream of specific four-fit chains that differ from yours.
**Redirect:** copy the *thinking*, not the tactics. What was Airbnb's chain? What's yours?

### "We'll add a growth marketer"

**What it looks like:** solving growth by hiring one person into a marketing role.
**Why it fails:** growth is cross-functional (product + marketing + sales + data). One marketing hire owns none of the levers.
**Redirect:** structure growth as a team with product embedded, not a marketing sub-function.

### Funnel-only growth planning

**What it looks like:** an acquisition → activation → retention → revenue diagram with no loop mechanism.
**Why it fails:** funnels decay. Every unit of growth requires equal or greater input next cycle.
**Redirect:** name at least one loop with amplification ≥1.

### "Our North Star is [one metric]" (measuring only one leg)

**What it looks like:** north star = sign-ups (only acquisition) or MAU (only engagement) or ARR (only monetization).
**Why it fails:** single-leg metrics let the other legs silently rot.
**Source:** *Don't Let Your North Star Metric Deceive You*

## Common misapplications (people saying they're doing Four Fits but aren't)

### Filling in the four boxes on a slide with no coupling test

The framework becomes a slide someone fills out in a strategy deck. Then the team continues doing what they were doing. No decisions changed.

**Test for the real thing:** did any structural bet (pricing, market, channel, product shape) change after the diagnosis? If no, no diagnosis happened.

### Running the four fits sequentially like an SDLC

Fix PMF this quarter, Product-Channel next quarter, Channel-Model after. This misses the whole point — the fits are coupled. Fix PMF in a way that breaks Channel-Model and you've made things worse.

### Confusing "growth loop" with any recurring pattern

Retention isn't a loop. Onboarding isn't a loop. A daily email digest isn't a loop. A loop specifically has amplification ≥1 driven by output-becoming-input.

### Stopping at Product-Channel Fit

Most implementations honor PMF and Product-Channel and hand-wave Channel-Model and Model-Market. Balfour has said publicly that Channel-Model and Model-Market are where most companies actually get stuck.

## Language and vocabulary — say this, not that

Small phrasing shifts that Balfour has made explicit:

| Instead of | Use | Because |
|---|---|---|
| Growth hacks | Growth system / growth loop | Hacks are tactics; system is the frame |
| Funnel | Loop (if it closes) or funnel (if it doesn't) | Loops compound; funnels decay |
| Growth marketer | Growth team (cross-functional) | Growth isn't a marketing sub-function |
| "We just need more traffic" | Which fit is broken? | Traffic is a symptom, not a diagnosis |
| "Copy [X company]'s playbook" | Diagnose your four fits first | Playbooks belong to specific chains |
| CMO owns growth | Product + growth own it together | Growth requires product levers |
| Vanity metrics | Impact metrics tied to the system | Wheel of Meaningless Growth |
| "We'll figure out channels later" | Design product FOR channels now | Product-Channel Fit can't be retrofitted |
| ARPU/CAC math will work at scale | Test at target scale now | Danger Zone doesn't fix itself |
| TAM is huge | Threshold check: `ARPU × TAM × 10% ≥ $100M?` | "Huge" hides bad math |

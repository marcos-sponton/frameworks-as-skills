# Crossing the Chasm — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant can execute well.

## Diagnose where a product is on the adoption curve

```
I want to diagnose where {{product/company}} is on the Technology Adoption Life Cycle using Geoffrey Moore's framework.

Context:
- Product: {{describe in 3-5 sentences}}
- Traction so far: {{customer count, ARR, growth rate, notable customer types}}
- Symptoms we're seeing: {{describe — e.g., sales cycles lengthening, references not landing with new prospects, pipeline stalled, big bespoke deals but no repeatable motion}}

Please:
1. Ask me diagnostic questions to locate us on TALC (Early Market / Chasm / Bowling Alley / Tornado / Main Street) and on the Category Maturity Life Cycle.
2. Test my read against the evidence — are my current customers visionaries or pragmatists? What behaviors tell me that?
3. Name the stage-appropriate playbook.
4. Name the previous stage's playbook that is now poison — the moves we need to STOP doing.
5. Cite Moore's own writing (book edition + chapter, LinkedIn essay + date, podcast + date) when you introduce a specific device or diagnostic.
6. If I invoke a common misapplication (broad-front invasion, platform ambition pre-chasm, visionary-logo-chasing, discounting-for-risk-reduction), challenge it warmly and offer the stage-appropriate corrective.
```

## Pick a beachhead segment

```
I need to pick a beachhead segment using Moore's D-Day discipline.

Context:
- Product: {{describe}}
- Current customers: {{who they are — psychographic + vertical + use case}}
- Candidate segments we're considering: {{list 3-5 verticals / use cases}}
- Available resources: {{team size, runway, whole-product capability}}

Please:
1. Walk me through Target-Customer Characterization (TCC) — help me articulate customer profile + use case before + use case after for each candidate.
2. For each candidate, apply the two-part beachhead test — big enough to matter (potential $100M in 5 years per Moore's Lenny 2024 rule of thumb), small enough to lead.
3. For each candidate, articulate the compelling reason to buy. Is the current broken-process pain quantified in dollars or hours? If not, flag as aspirational (pragmatists won't act).
4. For each candidate, size the whole-product gap. What integrations, services, partners, references are needed? What can we ship, what needs partners?
5. Force a single choice. Refuse to let me pick more than one. Warn me about dissipation of force.
6. Reference Documentum as the canonical beachhead illustration (~40 pharma orgs, $1M/day trapped value).
7. Cite Moore's sources (Crossing the Chasm 3rd ed, Lenny Podcast Jan 2024, After the Chasm blog 2024) when you introduce specific rules.
```

## Size the whole-product gap for a chosen beachhead

```
We've picked our beachhead: {{describe segment — vertical + use case + persona}}.

Apply Moore's Whole Product analysis:
1. Define the generic product (what we ship today).
2. Define the expected product (what the pragmatist buyer *expects* comes with the generic product).
3. Define the augmented product (what closes the gap between expected and truly seamless adoption).
4. Define the potential product (what the ecosystem could evolve toward).
5. For each layer, name what we build vs. what partners provide vs. what services close.
6. Test against the pragmatist buying moment: can they buy Monday, install by Friday, get results within the quarter, and cite a peer reference to their boss? If any of those breaks, name what's missing.
7. Compare to the visionary buying moment (visionaries fill the whole-product gap themselves — pragmatists refuse to). Explain why the gap kills chasm crossing.
8. Reference Documentum's pharma whole-product build as the canonical case.
```

## Design the compelling reason to buy for a pragmatist audience

```
We need to sharpen our compelling reason to buy for {{target segment / vertical}}.

Apply Moore's Compelling Reason to Buy discipline:
1. Ask me to describe the current broken process the buyer suffers today.
2. Force me to quantify it — dollars per day / hours per week / percentage cost overrun. If I can't, help me find someone in the target org who can.
3. Test whether the buyer's CFO would nod at the quantification (not just the buyer's own team).
4. Push back on delight-based reasons ("nice to have", "productivity gain", "better UX") — those aren't compelling per Moore.
5. Reference the Documentum case ($1M/day in lost patent life per delayed NDA) as the canonical quantified compelling reason.
6. Reference Moore's 2024 post "Delighting your customers is bunk. Delivering on their desired outcomes is not." for the discipline.
7. End with a clean 1-2 sentence compelling reason to buy statement in the buyer's own voice.
```

## Assess tornado readiness

```
We're in the Bowling Alley with {{describe current beachhead + adjacent pins won}}.

I think the market might be entering a Tornado. Help me diagnose using Moore's *Inside the Tornado* framework:
1. Test the signals — are horizontal deals closing on features/price without whole-product-per-vertical pre-work? Are competitors in every deal? Are buyers pushing standardization requests?
2. If the answer to at least 2 of 3 is yes — walk me through the Tornado playbook and the reversal from Bowling Alley discipline.
3. If not — warn me against premature standardization. Bowling Alley discipline still applies.
4. If we are in a Tornado — help me plan the reversal:
   - Sell horizontal, not vertical
   - Ship product, not solutions
   - Grab share above margin
   - Standardize aggressively; kill customization requests
5. Warn me about the risks — Tornado false positives (spending on horizontal capacity before the market has actually tipped) and Tornado false negatives (missing the tip and ceding horizontal share to a rival).
6. Reference Intel Operation Crush as the archetype Tornado move.
7. Cite Inside the Tornado (1995) for the stage-reversal doctrine.
```

## Run a Zone to Win session for an incumbent

```
I'm running a Zone to Win session for {{company}} — an incumbent managing {{describe disruption or transformation bet}}.

Apply Moore's four-zone framework:
1. Map current activities to the four zones — Performance / Productivity / Incubation / Transformation.
2. For each zone, name the rules of engagement — metrics, funding cadence, decision rights.
3. Diagnose zone confusion — where are we running one zone's plays with another zone's metrics?
4. Test the Transformation bet against Moore's ≥10% of company revenue threshold. If it's smaller, warn me — that's Incubation dressed up, not Transformation.
5. Test whether the Transformation is funded from a separate operating model or from Performance Zone's operating budget. If the latter, warn me — kills both.
6. Warn me that Zone to Win is an operating-model overlay, NOT an org chart. Do NOT recommend a four-way org restructure.
7. Reference Microsoft Azure (Nadella transformation) as a positive Transformation Zone case; Cisco cloud, HP cloud as workshop clients.
8. Cite *Zone to Win* (2015) + Gainsight Pulse 2022 coverage for specific quotes.
```

## Diagnose growth-source problems using Hierarchy of Powers

```
Our growth is slowing / plateauing. Diagnose using Moore's Hierarchy of Powers from *Escape Velocity* (2011).

Walk down the hierarchy top-to-bottom:
1. **Category Power** — Is the category itself losing steam? Is customer interest in this category type declining?
2. **Company Power** — Are partners routing business away from us? Is the gravitational pull weakening?
3. **Market Power** — Are the hot segments within our category shifting away from where we're strong?
4. **Offer Power** — Is our offer no longer demonstrably superior to alternatives?
5. **Execution Power** — Is a strategic initiative stalling in execution?

For each power, ask specific diagnostic questions.

Rules:
- Fix from the top down. Execution fixes on top of dying Category Power don't stick.
- Operators tend to over-weight Offer + Execution and under-weight Category + Company. Push me to look up the hierarchy first.
- Reference Moore's Escape Velocity (2011) + Wildcat VC podcast Ep 8 "Hierarchy of Powers as an Investment Model" for specific quotes.
```

## Apply Core vs. Context to an innovation portfolio

```
Help me apply Moore's Core vs. Context filter from *Dealing with Darwin* (2005) to our current portfolio.

Current activities / initiatives: {{list}}

For each:
1. Classify as Core (creates competitive differentiation) or Context (necessary but not differentiating).
2. For Context items, identify how they can be automated, outsourced, or eliminated to free capacity.
3. For Core items, identify how they can be reinforced with additional investment.
4. Classify each innovation as Differentiation (creates separation), Neutralization (closes a gap), or Optimization (efficiency of existing).

Rules:
- The bias is always toward more Core, less Context.
- Repatriation of context work is the CEO's job, not middle-management optimization.
- Do NOT let me treat context like core (over-investing in what doesn't differentiate).
- Reference *Dealing with Darwin* (2005) for the framework.
```

## Assess where a specific AI use case is on the adoption curve

```
I'm assessing where {{specific AI use case — e.g., agentic AI for customer service, generative AI for legal contract review, predictive AI for churn}} sits on the chasm.

Apply Moore's 2024–2026 framing:
1. Use his use-case-by-use-case distinction — NOT the "AI has crossed" narrative from secondary coverage. Category chasm ≠ use-case chasm.
2. Test the trapped value — does the current process accumulate enough pain to force complete re-engineering? Moore's threshold: "when one function completely re-engineers itself."
3. Compare against his verified-crossed use cases (HFT, digital ad placement, financial regulatory compliance) — what do they have in common that our use case has / lacks?
4. Compare against use cases he's identified as likely-to-cross-next (air traffic control, public safety, elementary education, home elder care) — organizations under unsurmountable performance pressure.
5. Compare against use cases NOT yet across (coding, customer service call centers per Feb 2026) — beachheads exist but trapped value is insufficient.
6. Where does the specific use case sit? What's missing from the trapped-value calculation?
7. Reference: Forbes/Randy Bean interview Jul 2024, "The Real Future of AI" Oct 2024, Diginomica Feb 2026.
```

## Scale beyond the beachhead (post-chasm bowling alley discipline)

```
We just crossed the chasm in {{beachhead segment}}. What's the discipline for scaling to the next pin?

Apply Moore's ["After the Chasm—Scaling Beyond the Beachhead" (2024)](https://geoffreyamoore.com/business_blogs/after-the-chasm-scaling-beyond-the-beachhead/):
1. Warn me against premature platform ambition — pre-scale, we're still a departmental point product. Platform emerges from pins later.
2. Warn me against pitching CFOs / becoming a suite too soon — we're still sub-scale for a CFO to consider us a go-to vendor. Our ally is the process owner with a broken process.
3. For each candidate next pin, test whether it's actually adjacent (can be won using the current beachhead's references) or a second beachhead we can't afford.
4. Two valid adjacency directions — same customer type in a new industry, OR new use case for the same customer type. Pick one direction per pin.
5. Ship whole product per pin, leverage whole-product investment across pins.
6. Reference Documentum's post-pharma cascade (chemicals → oil refineries → financial services) as the canonical Bowling Alley expansion pattern.
7. Cite Moore's blog post directly for the discipline.
```

## Cross-link with positioning craft (Dunford)

```
We've done the Moore-level chasm-crossing diagnosis. Now I need to actually write the positioning for {{beachhead segment}}.

Given:
- Stage: {{crossing the chasm / bowling alley / tornado / main street}}
- Beachhead segment: {{vertical + use case + persona}}
- Compelling reason to buy: {{quantified pain}}
- Whole product for the segment: {{what's included, what's partner-provided}}

Please:
1. Note that the *positioning craft* is April Dunford's altitude, downstream of Moore's stage-conditional strategy. Refer to the [[obviously-awesome]] skill for the operational method.
2. Provide the Moore-level inputs to a Dunford-style workshop:
   - Competitive alternatives at THIS stage (visionaries had different alternatives than pragmatists do — for pragmatists, the status quo / DIY / adjacent-vertical solutions are usually the real alternatives)
   - Unique attributes relevant to THIS beachhead's whole product
   - Value themes matching THIS segment's compelling reason
   - Best-fit customer = the beachhead persona
   - Market category = the frame most likely to make the value obvious to THIS pragmatist target
3. Warn that Bowling Alley positioning and Tornado positioning look different — the audience psychographic differs. Same product, different frame per stage.
4. If a full positioning workshop is needed, hand off to the [[obviously-awesome]] skill.
```

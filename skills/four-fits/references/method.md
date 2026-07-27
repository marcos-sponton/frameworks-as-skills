# Four Fits — Method

> The canonical description of the four fits and growth loops in Brian Balfour's own terms. Fidelity is the point — Balfour's framework is opinionated (channels don't mold to products, funnels decay while loops compound, the ARPU danger zone is real), and softening any of these collapses the method into generic growth advice.

## Definition

Balfour's operating claim, from the 2017 series:

> "You need to find all four fits to grow to a $100M+ company in a venture-backed time frame... Each of these fits influence each other, so you can't think about them in isolation."
> — Brian Balfour, *Four Fits For $100M+ Growth*, 2017

And on failure:

> "When [a fit breaks], you can't simply change one element, you have to revisit and potentially change them all."
> — same essay

Two properties are non-negotiable:

- **Chain** — the four fits are coupled. Treating them as a checklist of independent boxes is the failure mode, not the framework.
- **Threshold** — the framework is calibrated for **$100M+ venture-backed** scale. If your ambition is a $10M lifestyle business, the fits still apply but the pressure isn't the same. Say so up front.

## The four fits

Draft all four together, then iterate — a change in one forces changes in the others. The coupling is the method.

### 1. (Market) Product Fit

**What it asks:** Does a meaningful segment of the market desperately want what you've built?

This is the classic Ellis/Andreessen PMF, but Balfour is explicit about the order: **market and problem BEFORE solution.**

**Author's words:**
> "You are thinking about the solution before properly understanding the problem and audience that has that problem."
> — *Why Product Market Fit Isn't Enough*

**Not:** vanity signals (press, awards, waitlist size, launch traffic). Real signals: retention curves that flatten (not zero-out), organic word of mouth, NPS, willingness to pay.

**Key distinction from the other three fits:** PMF is necessary but not sufficient. Companies with PMF alone are what Balfour calls **"tugboats"** — grinding for growth, forcing every inch. Companies with all four fits are **"smooth sailers"** — growth feels effortless despite imperfect execution.

**AI-era update (2024):** PMF can now be lost overnight, not gradually. Chegg went from $1.2B (Jan 2024) to $150M (Oct 2024) after ChatGPT ate its homework-help value prop. Re-check PMF quarterly, not annually. See `post-book.md`.

### 2. Product-Channel Fit

**What it asks:** Is the product designed for how customers actually discover it?

Balfour's most-repeated line and probably his signature contribution:

> "Products are built to fit with channels. Channels do not mold to products."
> — *Four Fits For $100M+ Growth*

**What it means concretely:** channels have mechanics — inputs, formats, incentive structures, ranking algorithms. A product's shape (freemium tier, viral loops, content surface, sales motion, self-serve onboarding) either matches those mechanics or doesn't. You can't bolt "we'll do content" onto a product that produces no content, or "we'll go viral" onto a product no one shares.

**Test:** name the top 1–2 channels you're betting on. Then ask: what specific product mechanism produces the fuel that channel needs? If you can't name a mechanism, you don't have Product-Channel Fit — you have a channel wish.

**Examples of tight Product-Channel Fit:**
- **Slack** — invitation-to-teammate is a product feature AND the primary viral channel
- **Pinterest** — user-created pin boards are the product AND the SEO-indexable content
- **Dropbox** — the referral-with-storage-reward is a product feature AND the acquisition channel
- **HubSpot** — the free CRM and content tools produce inbound-marketing surface area AND the acquisition strategy

**Anti-pattern Balfour warns against:** finishing the product, then hiring a growth marketer and asking them to figure out the channel. By that point the product shape is fixed and no channel fits.

### 3. Channel-Model Fit

**What it asks:** Does your business model's unit economics support the channels the product fits?

Balfour maps this on an **ARPU spectrum with five zones**. The middle is the **Danger Zone**.

| Zone | ARPU | Channels that fit | Example companies |
|---|---|---|---|
| 1. Very low | ~$0 (ad-supported) | Virality, UGC SEO | Facebook, WhatsApp, Yelp |
| 2. Low-mid | $10s to low $100s | Paid marketing | Dollar Shave Club, DraftKings |
| 3. **DANGER ZONE** | mid ($100–$1k) | No clean fit — patchwork | many failed SaaS |
| 4. Mid-high (B2B) | $1k–$10k+ | Content, inbound/inside sales, partnerships | HubSpot, Zendesk |
| 5. Very high | $100k+ | Enterprise / outbound sales | Palantir, Veeva |

**Danger Zone diagnosis:** ARPU high enough that low-CAC viral/UGC channels have too much friction (users won't share a $500/yr tool the way they share WhatsApp), but low enough that paid or sales channels can't recover CAC (paying $2k CAC on $600 ARPU with 60% margin and 3-year retention is upside-down math).

**Author's words:**
> "Get out of the ARPU-CAC danger zone with channel model fit."
> — essay title

**The Danger Zone move:** raise ARPU (move up-market, add tiers, expand to Elephants/Moose) or drop ARPU + channel-shift down (add freemium, product-led-growth, viral mechanics). Don't stay in the middle hoping.

**AI-era stress (2024–2025):** AI features carry per-inference cost. Freemium models designed for low incremental cost break when the free tier now costs $X per active user in inference. Channel-Model Fit gets restressed continuously as unit economics move. See `post-book.md`.

### 4. Model-Market Fit

**What it asks:** Does the way you sell and charge match how the market wants to buy AND is the math big enough to matter?

**The threshold formula:**
> `ARPU × Total Customers In Market × % You Think You Can Capture ≥ $100M`
> — *The Model Market Fit Threshold*

**The five business archetypes:**

| Archetype | Volume × ARPU | Example |
|---|---|---|
| **Elephants** | 1,000 × $100k+ | Palantir, enterprise SaaS |
| **Moose** | 10,000 × $10k+ | HubSpot mid-tier, mid-market SaaS |
| **Rabbits** | 100,000 × $1k | SMB SaaS |
| **Mice** | 1M × $100 | Netflix-adjacent, prosumer subscription |
| **Flies** | 10M × $10 | Facebook, ad-supported consumer |

**The 10% heuristic:** great SaaS companies capture more than 10% of their target market over time. Use 10% as the sanity check on the capture-rate assumption. If the math only works at 40%, you don't have Model-Market Fit — you have a fantasy.

**Two failure modes Balfour names:**
- **Model doesn't match market's buying process.** Selling annual contracts with 6-month enterprise sales cycles into an SMB market that wants monthly self-serve credit-card checkout — mismatch.
- **Math doesn't clear the threshold.** Rabbits pricing (ARPU ~$1k) in a market of 20,000 total customers with a realistic 10% capture = $2M. Not a venture-scale business.

## The coupling — why "chain" matters

Balfour returns to this constantly:

> "The fits are always evolving/changing/breaking. When that happens, you can't simply change one element, you have to revisit and potentially change them all."

Concretely:

- Move up-market (raise ARPU) → your Product-Channel Fit changes (paid ads for $50 SaaS ≠ enterprise sales for $50k SaaS) → your product itself needs to change (SSO, audit logs, admin controls) → PMF against the new market segment must be re-verified.
- Add a self-serve tier (drop ARPU) → new channels open (virality, UGC SEO, PLG) but new product mechanics are required (onboarding, free-tier retention loops).
- Ride a new channel (ChatGPT-as-discovery, 2024–2026) → product must produce discovery-shaped content (structured data, LLM-consumable) → model may need to shift (per-inference cost changes economics).

**If you can change one fit without touching the others, you don't have four fits — you have four labels.**

## Sequence of application

Balfour does not prescribe strict order. In practice:

1. **Diagnose stage.** Pre-PMF? Post-PMF pre-scale? Scaling and stalled? Post-$100M defending? The move differs.
2. **Score each fit fast — 1–5, with evidence.** Pass 1: get a rough shape. Don't perfect.
3. **Find the weakest link.** Whichever fit scores lowest is where the chain breaks. That's your bottleneck.
4. **Test the coupling.** If you fix the weakest link, do the others still hold? If fixing PMF requires moving up-market, does the new Channel-Model Fit still work?
5. **Iterate until the four fits form a system that could plausibly clear $100M with realistic assumptions.**

## Growth Loops

Balfour's second signature contribution. Co-developed with Casey Winters, Kevin Kwok, and Andrew Chen (Reforge, 2018): *Growth Loops are the New Funnels*.

### Definition

A growth loop is a **self-reinforcing system** where the output of one cycle becomes the input of the next cycle. Closed by design. Compounding by nature.

A funnel is **open**: you pour inputs in at the top, outputs come out at the bottom, and there's no mechanism that turns those outputs back into more inputs. Funnels decay — every cycle requires equal or greater external input.

**Signature line:**
> "Loops compound. Funnels decay."

### Types of loops

Balfour names five archetypes:

1. **Viral loops** — users invite users. Slack, WhatsApp, Facebook, Zoom.
2. **Content loops** — users create content, content attracts users. Pinterest, Yelp, Quora, Reddit, YouTube.
3. **Paid loops** — revenue funds paid acquisition of more users, more users generate more revenue. Netflix, DTC subscription, DraftKings.
4. **Sales loops** — closed customers surface referrals, ICP data, and expansion opportunities that fuel the next batch of outbound. Enterprise SaaS.
5. **UGC / SEO loops** — user-generated content is indexed by Google, indexed content drives new users, new users create new content. Yelp, Pinterest, Reddit, TripAdvisor.

Most durable businesses run **multiple loops in parallel**, not a single dominant one.

### Loop design pattern

```
input → action → output → (feeds back to input)
```

**Test:** can you draw the diagram with the arrow returning to the top? If no, you have a funnel wearing loop vocabulary.

Concrete example (Pinterest UGC SEO loop):
```
Google search brings in new user (input)
  → user pins content (action)
  → Google indexes the pin page (output)
  → new Google search brings in new user (arrow closes)
```

**Diagnostic questions:**
- What's the input? (source of new users this cycle)
- What's the action? (what the user does)
- What's the output? (what the action produces)
- How does the output become next cycle's input?
- What's the cycle time? (days? weeks? months?)
- What's the amplification per cycle? (each user brings 0.5 new? 1.2 new? 0.1 new?)

If amplification is <1 sustainably, the loop is dying. If amplification is ≥1 and cycle time is fast, the loop compounds.

### Funnel-as-loop anti-pattern

The most common misapplication: teams draw a funnel, label the bottom "feeds back to top", but nothing operationally connects the two. A referral program bolted onto a purchase funnel is not a viral loop unless the referral rate × conversion × cycle time actually reproduces the acquisition volume.

Balfour's move: force the diagram, force the numbers, then see if the arrow really closes.

## What this method is NOT

- **A funnel with better vocabulary.** Growth loops are structurally different from funnels. Renaming steps of a funnel "loop stages" is not the method.
- **A bag of tactics or growth hacks.** *"Growth is a system between acquisition, retention, and monetization. Change one and you affect them all."* (Lenny 2023). Tactics live inside the system; they don't replace it.
- **A copy-the-playbook exercise.** Airbnb's playbook works for Airbnb. If your ARPU / TAM / channels differ, the playbook is noise. Balfour is explicit: diagnose your own fits before adopting anyone else's tactics.
- **A pre-PMF search tool.** Four Fits assumes you're past problem-solution and heading toward scale. If you're still hunting for the problem, use JTBD / continuous discovery instead. See `applications.md`.
- **A CMO's job.** Growth is cross-functional — product, marketing, sales, data, ops. Handing "growth" to a marketing hire and expecting the four fits to land is misdiagnosis.

## The differential vs. what the model already knows

Most agents know the *shape* of Four Fits (the four names) and the *headline* of Growth Loops ("loops compound, funnels decay"). What they don't know without this skill:

- The five ARPU zones and the Danger Zone diagnostic (`Channel-Model Fit`)
- The `ARPU × TAM × % capture ≥ $100M` threshold formula (`Model-Market Fit`)
- The five business archetypes (Elephants → Flies)
- The coupling logic — that changing one fit forces re-verification of the others
- The 2024–2025 AI-era reframing (Chegg case, ChatGPT-as-channel, AI unit economics)
- The specific anti-patterns Balfour attacks by name (funnel-in-loop clothing, playbook copying, growth-hacker-only hiring)
- The universal growth loop (company-level, distinct from product-level loops)

That's what `post-book.md` and `heuristics.md` carry.

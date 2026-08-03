# DHM Model — Method

> The canonical method: DHM, Strategy/Metric/Tactic lock-up, Proxy Metrics, GEM, GLEe, Swimlanes, and the Quarterly Strategy Meeting. All sourced from Gibson Biddle's [12-part Medium essay series](https://gibsonbiddle.medium.com/intro-to-product-strategy-60bdf72b17e3) and supporting materials.

## The DHM Model

**Source:** Essay #1 "The DHM Model" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/2-the-dhm-model-6ea5dfd80792)

### Core definition

Product strategy is a set of hypotheses about how you hope to **D**elight customers, in **H**ard-to-copy ways, that are **M**argin-enhancing.

Every product initiative is scored against three simultaneous dimensions. An initiative that scores well on only one or two dimensions is not strategic — it's a feature, a cost center, or a competitive liability.

### Dimension 1: Delight (D)

**Question:** Does this initiative make customers genuinely love the product?

**How to assess:**
- Would customers be disappointed if this was removed?
- Does this improve engagement and/or retention?
- Does it solve a real customer pain point or create a moment of surprise/joy?
- Can you measure the delight through behavioral data (not just stated preferences)?

**Netflix example:** Personalization — made it dramatically easier for members to find movies they would love, reducing choice overload. Measured via retention and engagement metrics.

**Warning:** Delight alone is necessary but not sufficient. Many features delight but are easily copied. The filter only starts at D — it doesn't end there.

### Dimension 2: Hard to copy (H)

**Question:** Does this initiative build a durable competitive advantage that others cannot easily replicate?

**Source:** Essay #2 "From DHM to Product Strategy" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/2-from-dhm-to-product-strategy-a3781b2aadca)

Biddle identifies **four types of hard-to-copy advantages:**

#### 1. Brand
Trust built over years of consistently delivering value with a minimum of "trust busters." Netflix: more than 150 million members trust the service with their credit cards. A brand advantage takes years to build and can be destroyed quickly, but it can't be bought or replicated by a well-funded competitor overnight.

#### 2. Network effects
Value increases with more users or nodes. Netflix: starting in 2008 with Xbox, Netflix built a device ecosystem. Today, nearly all TVs, DVD/Blu-Ray players, game systems, set-top boxes, and mobile devices are pre-wired to stream Netflix. Each new device partner makes Netflix more ubiquitous, creating a hard-to-replicate distribution moat.

#### 3. Economies of scale
Unit economics improve with size. Netflix: because the company can amortize content cost across 150M+ members, it can invest significantly more than its smaller rivals in original content. A startup with 1M subscribers cannot compete dollar-for-dollar on content spending.

#### 4. Unique technology
Proprietary systems and data that create differentiation. Netflix: personalization technology that knows the tastes of 165M+ members worldwide. This data and the algorithms built on it make it substantially easier for members to find movies they love. Key insight: it took Netflix more than a decade to demonstrate that personalization improved retention. Hard-to-copy tech requires sustained investment.

**Diagnostic questions:**
- Which of the four types applies to your initiative?
- If none applies, how long until a competitor replicates what you build?
- If a well-funded competitor launched the same feature tomorrow, would your version still be better in 12 months? Why?

### Dimension 3: Margin-enhancing (M)

**Question:** Does this initiative improve the business's financial position — not just revenue, but margin (the spread between value created and cost incurred)?

**How to assess:**
- Does this reduce cost per customer?
- Does this improve retention (higher LTV)?
- Does this enable pricing power?
- Does this reduce the cost of content/inventory/delivery?
- Does this create a flywheel where profits can be reinvested?

**Netflix example:** Personalization merchandises content that costs less — the algorithm surfaces catalog titles (already paid for) rather than only expensive new releases. This "right-sizes" content investment based on forecasts. Better retention also improves LTV directly.

**Warning:** "Margin-enhancing" is NOT "revenue-generating." Some high-revenue initiatives destroy margin (e.g., acquiring subscribers via expensive promotions that tank unit economics). The question is about the spread.

### The trifecta

The most powerful product strategies score high on all three dimensions simultaneously. Biddle's canonical example is Netflix personalization:

| Dimension | Netflix Personalization |
|---|---|
| **Delight** | Better recommendations = easier to find movies you love |
| **Hard to copy** | Unique taste data for 165M members + proprietary algorithms |
| **Margin-enhancing** | Merchandises cheaper content, improves retention, enables right-sized content investment |

When an initiative achieves the trifecta, it builds compounding value: delight drives retention, retention enables scale, scale creates economies and data, economies and data create hard-to-copy advantages, advantages sustain margin.

---

## Product Strategy = Hypotheses

**Source:** Essay Intro "How to Define Your Product Strategy" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/intro-to-product-strategy-60bdf72b17e3)

Biddle's core framing: product strategy is NOT a plan. It's a set of hypotheses you test and evolve.

**Process cycle:** Hypothesize -> Test -> Learn -> Repeat

Each year at Netflix, the team took on about 4-6 product strategies. In 2005, the significant efforts were:
1. Personalization
2. Easy/Simple
3. Social
4. Margin-enhancement
5. Unique movie-finding tools
6. Next-day DVD delivery

Each strategy was a hypothesis — "We believe that investing in personalization will delight customers in a hard-to-copy, margin-enhancing way." The team then ran A/B tests to validate or invalidate each hypothesis.

**Reed Hastings' philosophy:** When Biddle asked Hastings what he hoped his legacy would be, Hastings answered "Consumer science." His aspiration was that product leaders at Netflix would discover what delights customers through the scientific process — forming hypotheses from data and research, then A/B testing ideas to see what works — rather than relying on intuition alone.

---

## The Strategy/Metric/Tactic Lock-up

**Source:** Essay #3 "The Strategy/Metric/Tactic Lock-up" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/3-the-strategy-metric-tactic-lock-up-b7539ec69a7e)

For each product strategy, define three connected elements:

| Element | Definition | Netflix example (Personalization) |
|---|---|---|
| **Strategy** | The high-level hypothesis | "Personalization: make it easy for members to find movies they'll love" |
| **Metric** | The proxy metric that measures whether the strategy is working | % of members who rate 50+ movies in first 2 months |
| **Tactic** | The specific projects/experiments that test the strategy | Improve recommendation algorithm, redesign browse experience, test "Top 10 for You" row |

At Netflix, each strategy had a dedicated "pod" of engineers, designers, product managers, and data leaders. The lock-up connects the why (strategy) to the what (tactic) through the how-we-know (metric).

**Why this matters:** Without the lock-up, teams build features without knowing if they're working. The metric is the bridge between strategic intent and execution reality.

---

## Proxy Metrics

**Source:** Essay #4 "Proxy Metrics" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/4-proxy-metrics-a82dd30ca810)

### The hierarchy

**High-level engagement metric:** The ultimate outcome metric that defines product quality. At Netflix: monthly retention (the inverse of monthly cancel rate). Hard to move — progress is "almost glacial."

**Proxy metrics:** Lower-level, leading indicators that are easier and faster to move, and ideally, moving a proxy will improve the high-level metric.

### Netflix proxy metric examples

| Proxy metric | Theory | Strategy it measures |
|---|---|---|
| % of new members who add 3+ titles to queue in first session | Getting users to build a queue early predicts long-term engagement | Easy/Simple |
| % of members who rate 50+ movies in first 2 months | Ratings fuel personalization, which improves recommendations, which improves retention | Personalization |
| % of members who watch 15+ min in first month | Early engagement predicts long-term retention | Overall engagement |

### Requirements for a good proxy metric

1. **Moves faster than the high-level metric.** If it's as slow as retention, it's not a useful proxy.
2. **Correlates with the high-level metric.** The correlation must be demonstrated through data, not assumed.
3. **Is actionable.** Teams must be able to design projects that move the proxy.
4. **Is measurable.** You can instrument it without heroic data engineering.

### The causation trap

Correlation is not causation. Just because members who rate 50+ movies retain better doesn't mean forcing all members to rate movies would improve retention. A/B test to verify: does the project that moves the proxy also move retention?

---

## The GEM Model

**Source:** Essay #9 "The GEM Model" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de)

A prioritization model for roadmap decisions. Score each initiative on three business outcomes:

| Dimension | What it measures | Netflix metric |
|---|---|---|
| **Growth** | Year-over-year member growth rate | YoY subscriber growth |
| **Engagement** | Product quality via a specific engagement proxy | Monthly retention |
| **Monetization** | Financial sustainability | Lifetime Value (LTV) and gross margin |

### How to use GEM

1. List your product initiatives.
2. Score each on expected impact to Growth, Engagement, and Monetization (high/medium/low or numerical).
3. Force trade-off conversations: "This feature improves Growth but hurts Monetization — do we still build it?"
4. Align the portfolio: at any given phase, a company might prioritize Growth over Monetization (pre-IPO Netflix) or Monetization over Growth (mature Netflix).

### GEM vs. DHM

DHM is a qualitative strategy filter: does this initiative delight, is it hard to copy, is it margin-enhancing? GEM is a quantitative prioritization model: what's the impact on growth, engagement, and monetization? They work together — DHM filters what's strategic, GEM prioritizes among the surviving initiatives.

---

## The GLEe Model

**Source:** Essay #8 "The GLEe Model" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/6-the-glee-model-6af740bdf3b1)

A long-term, phased approach to creating substantial value:

**G — Get big** on an initial product/market.
**L — Lead** a key industry transition.
**E — Expand** into new markets or categories.

### Netflix GLEe

| Phase | What Netflix did |
|---|---|
| **Get big** | DVDs by mail |
| **Lead** | Streaming |
| **Expand** | Worldwide |
| (Current focus) | Original content |
| (Speculative next) | Interactive storytelling |

### Key insight

You don't have to do everything simultaneously. Phase-gate expansion behind achieving scale and leadership in the current phase. Netflix didn't invest in original content until it had the economies of scale (global subscriber base) to amortize the cost.

### When to use GLEe

Use when the team needs to think long-term and big. Especially useful for startups that need to articulate a phased path from their current beachhead to a much larger vision. Not useful for day-to-day roadmap prioritization — use GEM for that.

---

## Swimlanes

**Source:** Essay #6 "A Strategy for Each Swimlane" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/6-a-strategy-for-each-swimlane-38be75f65129)

Each product area (swimlane) has:
- Its own strategies (hypotheses)
- Its own proxy metrics (leading indicators)
- Its own project backlog (tactics)

Product leaders for each swimlane define the strategy, proxy metric, and projects for their area. This connects day-to-day execution in individual teams back to the company-level product strategy.

**Example:** At Netflix, one swimlane was "Personalization" with its own pod. Another was "Easy/Simple." Each had its own Strategy/Metric/Tactic lock-up.

---

## Working Bottom-Up

**Source:** Essay #5 "Working Bottom-up" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/5-working-bottom-up-426447b2b876)

An alternative approach to defining strategy: instead of starting with top-down hypotheses, scan your existing project list and look for themes. What patterns emerge? These reveal implicit strategies you can make explicit.

**When to use:** When the team already has a large project backlog but no clear strategic framing. The bottom-up scan surfaces what the team is already betting on, which can then be evaluated through the DHM filter.

---

## The Quarterly Product Strategy Meeting

**Source:** Essay #10 "How to Run A Quarterly Product Strategy Meeting" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/10-the-quarterly-product-strategy-meeting-b5c0c1b12722)

Biddle's operational cadence for keeping strategy alive. Described as "a Board Meeting for Product."

### Format
- Review each swimlane's strategy, proxy metric, and results.
- Share learnings from experiments.
- Debate whether strategies should continue, pivot, or be killed.
- Run "What would you do?" simulations to provoke strategic thinking.

### Why it matters
- Strategy decays without recurring cadence.
- Clearly described strategies and metrics make it easier to say "no" to feature requests.
- Over many quarters, the team's test cadence increases — more tests, more learning, continuously fine-tuned instincts.
- Simulations build strategic muscle across the team, not just in leadership.

---

## The Product Roadmap

**Source:** Essay #7 "The Product Roadmap" — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/7-the-product-roadmap-bf8830d81c19)

Biddle's view: a roadmap is an expression of your strategy, not a Gantt chart. Once strategies, proxy metrics, and projects are defined for each swimlane, the roadmap becomes straightforward — it articulates the focus and organization of the product team with rough time estimates.

The roadmap makes the strategy visible and communicable. It's the artifact that connects what the team is building to why (the hypotheses) and how we'll know (the metrics).

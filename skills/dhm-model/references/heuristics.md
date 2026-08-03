# DHM Model — Heuristics

> Do's, don'ts, anti-patterns, gotchas, and pro tips for applying Biddle's frameworks. Attributed to specific essays where possible.

## Do's

### Score every initiative on all three DHM dimensions
Not just Delight. Not just D+H. All three must pass simultaneously. The power of the filter is that it's conjunctive — an initiative that scores high on two dimensions but zero on the third is not strategic.
*(Source: Essay #1 "The DHM Model")*

### Define proxy metrics before building
If you can't measure whether a strategy is working, you can't test the hypothesis. The proxy metric must be defined BEFORE projects ship, not after.
*(Source: Essay #4 "Proxy Metrics")*

### Treat strategy as hypotheses, not commitments
The whole point is that you might be wrong. A strategy that fails the test is not a failure — it's learning. Kill strategies that don't move their proxy metrics. Pivot to new hypotheses.
*(Source: Essay Intro "How to Define Your Product Strategy")*

### Run quarterly product strategy meetings
Strategy decays without recurring cadence. The quarterly meeting keeps strategy front and center, forces metric review, and builds strategic muscle across the team.
*(Source: Essay #10 "How to Run A Quarterly Product Strategy Meeting")*

### Look for the trifecta
The best product strategies score high on all three of D, H, and M simultaneously. When evaluating a new initiative, ask: "Is there a version of this that could hit all three?" Netflix personalization is the canonical trifecta.
*(Source: Essay #1, Essay #11 "Netflix 2020")*

### Build hard-to-copy advantages over time
Brand, network effects, economies of scale, and unique technology take years to develop. Start investing in them early, even if the payoff is not immediate. Netflix invested in personalization for a decade before proving it improved retention.
*(Source: Essay #2 "From DHM to Product Strategy")*

### Use bottom-up pattern-matching when stuck
If defining top-down strategy feels abstract, scan your existing project list. What themes emerge? These reveal implicit strategies you can make explicit and evaluate through the DHM filter.
*(Source: Essay #5 "Working Bottom-up")*

### Lock up strategy, metric, and tactic
For every strategy, name the proxy metric and the specific projects. The lock-up is the bridge between strategic thinking and execution. Without it, teams build features without knowing if they're working.
*(Source: Essay #3 "The Strategy/Metric/Tactic Lock-up")*

### A/B test the strategy, not just the feature
At Netflix, the question was never "does this feature ship?" but "does this feature move the proxy metric, and does moving the proxy metric improve retention?" The test hierarchy is: feature -> proxy -> engagement metric.
*(Source: Essay #4 "Proxy Metrics," Netflix Customer Obsession essay)*

### Limit to 4-6 strategies per year
Netflix took on about 4-6 product strategies per year. More than that dilutes focus. Fewer may miss opportunities. The constraint forces prioritization.
*(Source: Essay #2 "From DHM to Product Strategy")*

---

## Don'ts / Anti-patterns

### Don't optimize for D without H
If customers love it but competitors can copy it in 6 months, it's a feature, not a strategy. Many product teams live here — shipping delightful features that create zero lasting advantage. The "Hard to copy" question is the one most teams skip.
*(Source: Essay #2 "From DHM to Product Strategy")*

### Don't build hard-to-copy advantages that don't delight
A proprietary system nobody wants is a waste of engineering. H without D is a technical moat with no water — impressive infrastructure with no customer value.
*(Source: Essay #1 "The DHM Model")*

### Don't ignore M ("we'll figure out monetization later")
Margin-enhancement must be considered from the start, even if the near-term strategy is to invest in growth. "Later" often means "never" — and by then the cost structure is baked in.
*(Source: Essay #1 "The DHM Model")*

### Don't confuse a project list with a strategy
A roadmap of features is not a product strategy. If someone asks "what's your product strategy?" and the answer is a list of things being built, they don't have a strategy. They have a to-do list.
*(Source: Essay Intro "How to Define Your Product Strategy")*

### Don't use vanity metrics as proxy metrics
Pageviews, signups, DAU, or "number of users who saw the feature" without a demonstrated correlation to the high-level engagement metric are vanity. A good proxy metric predicts the outcome you care about (e.g., retention). A vanity metric makes a dashboard look good.
*(Source: Essay #4 "Proxy Metrics")*

### Don't skip the "hard to copy" analysis
Many product leaders default to "what delights?" and "what makes money?" but forget to ask "can anyone else do this?" The H dimension is where lasting competitive advantage lives. Without it, you're in a race you can't win.
*(Source: Essay #2 "From DHM to Product Strategy")*

### Don't treat all four types of hard-to-copy equally
Not all four (brand, network effects, economies of scale, unique technology) apply to every company. A startup may have unique technology but zero brand or scale advantages. Focus on the 1-2 that are genuine and investable.
*(Source: Essay #2 "From DHM to Product Strategy")*

### Don't assume your proxy metric is correct
The correlation between proxy and high-level metric must be demonstrated through data, not assumed through logic. Netflix initially thought ratings volume would be a great proxy for retention — the causal link had to be proven through A/B testing.
*(Source: Essay #4 "Proxy Metrics")*

### Don't treat strategy as annual planning
Strategy is not a once-a-year exercise. It's a continuous cycle of Hypothesize -> Test -> Learn -> Repeat. The quarterly meeting is a checkpoint, not the only time strategy is discussed.
*(Source: Essay #10 "Quarterly Product Strategy Meeting")*

---

## Gotchas

### Proxy metric correlation is not causation
Just because members who rate 50+ movies retain better doesn't mean forcing all members to rate movies would improve retention. The proxy metric identifies a behavior pattern — the A/B test verifies whether the intervention causes the outcome.
*(Source: Essay #4 "Proxy Metrics")*

### The DHM filter is brutal
Most ideas score well on Delight but poorly on Hard-to-copy or Margin-enhancing. That's the point — the filter exists to be aggressive. If it lets everything through, it's not working.

### "Hard to copy" is time-dependent
What's hard to copy today may be commoditized in 3 years. Technology advantages erode fastest. Brand and network effects tend to be more durable. Revisit the H assessment regularly.
*(Source: Essay #2 "From DHM to Product Strategy")*

### Margin-enhancing is NOT "revenue-generating"
Margin is about the spread between value created and cost incurred. Some high-revenue initiatives destroy margin (e.g., acquiring subscribers via expensive promotions, or building features that increase support costs). The question is: does this make each customer more profitable?

### Netflix is not your company
Biddle's cases are instructive, but Netflix had unique conditions: massive subscriber base, content amortization across millions, early-mover advantage in streaming, a CEO (Hastings) who explicitly valued "consumer science." Extract the principle (score on D, H, and M), not the specific tactic (build a personalization algorithm).

### The model works best for consumer products
Biddle developed DHM at Netflix (consumer subscription) and Chegg (consumer education). The model translates to B2B and enterprise but the "hard to copy" types may look different — switching costs and integration depth matter more than brand in enterprise. See `applications.md` for adaptation guidance.

### Strategy/Metric/Tactic lock-ups require iteration
The first version of any lock-up is usually wrong. The metric may not be sensitive enough. The tactics may not move the metric. The strategy may be too broad. Expect to refine the lock-up over multiple quarters.

---

## Pro tips

### The "strategy obituary" test
If you killed a strategy tomorrow, would anyone notice in the metrics within a quarter? If not, the strategy wasn't being tested — it was occupying a slot on a slide without generating learning.

### Use GEM to resolve DHM ties
When two initiatives both pass the DHM filter, use GEM (Growth, Engagement, Monetization) to break the tie based on which business outcome matters more right now.

### The bottom-up scan reveals political strategies
When you scan the project list bottom-up, you'll find projects that don't fit any strategy. Some are technical debt (fine). Some are political — a stakeholder requested them, and no one challenged the strategic fit. The DHM filter gives you the language to challenge diplomatically.

### Proxy metrics should evolve
As a strategy matures, the proxy metric should become more sophisticated. Netflix started with "queue depth" (crude) and evolved to retention-correlated engagement scores (nuanced). If your proxy metric hasn't changed in two years, you're probably not learning.

### The quarterly meeting is a forcing function for clarity
Most strategic confusion is linguistic, not conceptual. Teams argue about priorities because they're using different definitions of the strategy. The quarterly meeting forces written lock-ups — strategy, metric, tactic — that expose definitional gaps.

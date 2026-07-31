# The Lean Startup — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant can execute well.

## Plan a Build-Measure-Learn loop for a new hypothesis

```
Help me plan a Build-Measure-Learn loop for the following hypothesis, the way Ries actually described it.

Context:
- Product / service: {{describe}}
- The hypothesis I want to test: {{specific claim about customer behavior, need, or willingness to pay}}
- What I currently think the answer is (and how confident): {{be honest}}
- Team + resources available: {{numbers}}
- Time available for this experiment: {{days / weeks}}

Please:
1. Restate my hypothesis in Ries's testable form. If it's not falsifiable, tell me and rewrite it.
2. Plan the loop in REVERSE — Learn first, Measure second, Build last.
   - What do we need to learn?
   - What metric will confirm or falsify the hypothesis?
   - What's the smallest experiment (MVP) that produces that metric?
   - What do we actually need to build (or NOT build)?
3. Specifically name the MVP type — landing page / video / concierge / Wizard of Oz / piecemeal / single-feature.
4. Cite Ries's specific source for the MVP type (book chapter or case).
5. Warn me if I'm at risk of the "MVP as excuse for shipping garbage" misapplication.

Do NOT default to "build a v0.1 and ship it." If the answer is a landing page or a manual concierge service, tell me — that's often the right answer.
```

## Critique an existing MVP plan against Ries's actual definition

```
Please critique this MVP plan against Ries's actual definition of MVP.

Our MVP plan:
{{paste the doc / one-pager / summary}}

Apply Ries's diagnostic:
1. What specific hypothesis is this MVP testing? If there isn't a clear one, name that as the finding.
2. What metric will confirm or falsify that hypothesis? If there isn't one, name that as the finding.
3. Is this the SMALLEST test that produces that metric? Or is it a full first version dressed as an MVP?
4. Does this MVP require code at all? Would a landing page, video, or concierge MVP produce the same learning cheaper?
5. Name the misapplication risk explicitly — MVP-as-excuse-for-shipping-garbage, or MVP-as-full-product, or vanity-metric-instead-of-actionable.
6. Cite Ries's actual definition ("the minimum amount of effort to learn") and the specific book chapter.

Tone: patient, direct. Reset the vocabulary before critiquing. Push back on "let's just ship it and see" if that's what's under the plan.
```

## Audit our metrics for vanity vs. actionable

```
Audit our metrics for vanity vs. actionable using Ries's framework.

Metrics we currently track and report:
{{list metrics — dashboard shot, OKRs, whatever's alive in the org}}

Apply Ries's diagnostic (from his 2009 tim.blog post + The Lean Startup chapter 7):
1. For each metric, classify as VANITY or ACTIONABLE. Explain why.
2. For actionable metrics: are they per-cohort, causally-linked to specific experiments, and per-customer? If not, they're still vanity in disguise.
3. Substitution test: for each metric that moves, can we say which specific experiment or intervention caused the change? If not, it's aggregated over too much noise.
4. Recommend the 3–5 actionable metrics we should track instead, based on our engine of growth (sticky / viral / paid — ask if unclear).
5. Recommend the specific split-test / cohort / funnel structure that would surface causation.
6. Cite Ries's 2009 tim.blog guest post + The Lean Startup chapter 7.
```

## Run a pivot-or-persevere decision

```
We need to make a pivot-or-persevere decision. Help me run it Ries's way.

Context:
- Current hypothesis / strategy: {{one sentence}}
- What we've learned over the last {{N weeks/months}}: {{specific data}}
- Actionable metrics — current baseline and movement: {{numbers}}
- Time / capital remaining: {{honest assessment}}
- What's tempting me toward each choice: {{be honest}}

Please:
1. State the current hypothesis in falsifiable terms. Has the data falsified it?
2. If falsified: which of Ries's 10 pivot types fits? (Zoom-in / Zoom-out / Customer segment / Customer need / Platform / Business architecture / Value capture / Engine of growth / Channel / Technology.)
3. If NOT falsified but progress is slow: is the hypothesis right and the execution wrong, or is the hypothesis fuzzy and generating serial mini-pivots (pivot fatigue)?
4. If we pivot: how many pivots do we have left in the runway? (Ries: "Runway is really not money — it's the number of pivots you have left.")
5. Name the specific risks — are we at risk of achieved failure (executing perfectly on a plan nobody wants), or pivot fatigue (serial pivoting from an unsharpened hypothesis)?
6. Recommend: pivot, persevere, or sharpen-the-hypothesis-and-run-one-more-turn.

Cite The Lean Startup, chapter 8 (Pivots) + the 2024 Lenny retrospective for how Ries thinks about this today.
```

## Set up Innovation Accounting

```
Help me set up Innovation Accounting for a new business unit / product inside my {{company / enterprise}}.

Context:
- Business / product: {{describe}}
- Stage: {{pre-revenue / early-revenue / scaling}}
- Current metrics being tracked: {{list}}
- Engine of growth (if known): {{sticky / viral / paid — or "unknown"}}
- Team size + governance structure: {{describe}}

Apply Ries's three-level Innovation Accounting model:
1. LEVEL 1 — Actionable metrics baseline. Which metrics matter for our engine of growth? What are the current-state real numbers?
2. LEVEL 2 — Tuning the engine. What experiments should we run to move the baseline? Recommend the specific split-test / cohort / funnel structure.
3. LEVEL 3 — Pivot-or-persevere. What cadence should we hold this decision at? What thresholds signal pivot vs. persevere?

Additionally:
- Warn against the vanity-metrics-dressed-as-actionable-metrics trap.
- Warn against reducing Innovation Accounting to "add three more charts to Looker" (it's a maturity model, not a dashboard).
- Cite Ries's chapters 7–10 in The Lean Startup + the 2009 tim.blog post on vanity vs. actionable metrics.

If we're inside an enterprise, also reference The Startup Way's Growth Board governance for how tranche-based funding fits.
```

## Run a Five Whys post-mortem

```
Help me run a Five Whys post-mortem on this failure, the way Ries described it.

What happened:
{{describe the failure — bug, outage, missed launch, customer complaint, deploy failure, etc.}}

Please:
1. Walk the five whys, starting from the surface symptom and moving toward the systemic root cause. Ask ME each "why" and wait for my answer if you need context — do not assume.
2. At each layer, name the specific corrective action needed. Ries's discipline: PROPORTIONAL investment at every level. Not just the technical fix — also the training, the process, the hiring.
3. Identify where a "human problem" is hiding behind what looks like a "technical problem." (Ries: "Behind every seemingly technical problem is actually a human problem waiting to be found.")
4. Name what Andon Cord practice would have caught this earlier. If we don't have Andon Cord culture, name it as a finding.
5. Recommend the specific system upgrade this incident should produce.

Tone: patient, direct. Not blame. This is Toyota Production System discipline translated to our context — cite Taiichi Ohno / TPS explicitly.

Cite Ries's original November 2008 startuplessonslearned.com Five Whys post.
```

## Apply Lean Startup inside an enterprise

```
We're a {{Fortune 500 / large corporation / mid-sized enterprise}} and want to install Lean Startup method for a new innovation initiative. Help me plan it using The Startup Way (2017).

Context:
- Company / business unit: {{describe}}
- What's driving the initiative: {{new-market entry / defensive R&D / CEO mandate / etc.}}
- Executive sponsorship: {{who, level, how committed}}
- Protected budget: {{yes / no / unclear}}
- Team: {{numbers, seniority, current role}}
- Timeline expectation: {{honest assessment}}

Apply Ries's Startup Way playbook:
1. Assess readiness — do we have the scaffolding (executive sponsorship, protected budget, tolerance for J-curve, dedicated team)? If any is missing, name it as a risk BEFORE we invest further.
2. Recommend the Growth Board governance structure — who's on it, what tranches, what pivot-or-persevere cadence.
3. Name the enterprise-specific obstacles (BAU incentive misalignment, defensive middle management, procurement/finance/legal treating startup teams as anomalies). What countermeasures?
4. Recommend the entrepreneur-as-org-chart-role design — is this a career path or a temporary assignment? Career-path or the team disperses in the next reorg.
5. Cite the GE FastWorks case honestly — including the fact it partially unwound post-Immelt, and the governance lesson that teaches (bridge to Incorruptible).

Do NOT recommend "just move fast and iterate." That's the misapplication The Startup Way exists to correct.
```

## Reset degraded Lean Startup vocabulary

```
My team is throwing around Lean Startup vocabulary but I don't think they're using it the way Ries meant. Help me reset the vocabulary.

Terms they're using (paste anything relevant):
{{examples — "let's ship the MVP", "we need to fail fast", "we build-measure-learned it", "our OKR is 40% MAU growth", "let's just pivot"}}

Please:
1. For each term, restate Ries's actual definition. Cite the source (book chapter, 2009 tim.blog post, 2024 Lenny episode).
2. Name the specific misapplication risk each degraded usage creates.
3. Rephrase what they're saying so it uses the actual method's discipline, not the degraded vocabulary.
4. Use Ries's own line against "fail fast" if it's in play: "I hate the idea of 'fail fast.' It's like I'm trying to run a sprint, and you're like, 'OK. Breathe fast.'"

Tone: patient, definitional. Not lecture. Reset first; then apply.
```

## Decide between Lean Startup and Working Backwards

```
I'm deciding whether to use Lean Startup (Ries) or Working Backwards / PR-FAQ (Amazon / Bryar & Carr) for this decision.

Context:
- What we're deciding to launch / build: {{describe}}
- Cost of a wrong launch (in $ / customer trust / years): {{honest assessment}}
- Cost of a right launch: {{upside}}
- Current stage: {{pre-PMF / scaling / mature-launch-at-Amazon-scale}}
- Time available: {{days / weeks / months}}

Apply the honest disagreement diagnostic:
1. How expensive is a wrong bet here? This is the load-bearing question.
2. If cheap (early-stage, feature-level, cheap-experiment): Lean Startup. Explain why and design the MVP.
3. If expensive (Amazon-scale commitment, launch-quality-dominates, tens-of-millions-in-commitment): Working Backwards. Explain why and start the PR/FAQ scoping.
4. If it's a mix (discovery phase then commitment phase of the same product): recommend the sequence — Lean Startup for discovery, Working Backwards for the launch commitment.
5. Cite both frames honestly. Don't collapse the disagreement — both authors are correct in their own scope.

Guardrail: do NOT default to "Lean Startup is always the answer." Amazon's rejection of MVP at commitment altitude is real. See the honest disagreement in the applications reference.
```

## Design governance to protect a mission-driven company (Incorruptible frame)

```
We're a {{Series C / late-stage / public / recently-acquired}} mission-driven company and worried about mission drift. Help me apply Ries's Incorruptible (2026) frame to design protective governance.

Context:
- Company + mission: {{describe}}
- Current governance structure: {{cap table, board composition, exec team, comp design}}
- Where we're feeling "financial gravity" pull us away from the mission: {{honest specifics}}
- What's triggered this question: {{recent event}}

Apply Incorruptible:
1. Name the specific "financial gravity" forces at play — quarterly earnings pressure, dispersed shareholders, short-tenured exec, activist investor risk, acquirer pressure.
2. Diagnose the governance-design gaps that would let those forces reshape the mission.
3. Recommend the specific structural protections — modeled on the "spiritual holding company" pattern. Reference Patagonia's 2022 restructuring and LTSE-listed-company governance commitments (Twilio, Asana) as operational instances.
4. Warn about the specific patterns to avoid — founder-dependent mission protection (fragile past succession), single-executive commitment (fragile past executive transition), unbinding declarations vs. binding governance.
5. Cite: Incorruptible (2026), the Thought Economics 2026 interview ("Governance is not bureaucracy — it is the most important product a founder will ever design"), and the LTSE bio / LTSE.com governance-commitment framework.

Tone: earnest, methodical. Structural, not moral. Corruption is a governance-design failure, not a villain problem.
```

## Apply Genchi Genbutsu — "get out of the building"

```
Our team is operating on dashboards and I'm worried we've lost touch with real customers. Help me apply Genchi Genbutsu.

Context:
- Product / service: {{describe}}
- How often team members watch real customers in their environment: {{honest}}
- Current research artifacts we rely on: {{surveys, interviews, analytics, NPS, etc.}}

Please:
1. Diagnose whether we're operating on dashboards or on genchi genbutsu. Practical bar: if the last time a team member watched a real customer use the product was more than 2 weeks ago, we're on dashboards.
2. Recommend a specific weekly practice — in-context observation, over-the-shoulder screen share, customer visit, etc. Structured so it's non-negotiable and calendared, not aspirational.
3. Distinguish between customer interviews (useful but different) and genchi genbutsu (real observation in real environment). Ries treats them as complementary, not substitutes.
4. Cite Ries + credit Taiichi Ohno / Toyota Production System for the practice + credit Steve Blank for "get out of the building."
5. If our team is in continuous discovery habits mode (Torres), name how genchi genbutsu fits inside her weekly interview cadence.
```

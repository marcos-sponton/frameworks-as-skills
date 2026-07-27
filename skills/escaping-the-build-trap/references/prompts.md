# Escaping the Build Trap — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude can execute well.

## Audit our PM organization against the Four Dimensions

```
Audit our product management organization using Melissa Perri's Four Dimensions.

Context:
- Company / product: {{describe}}
- Team size (PMs, EMs, designers, engineers): {{numbers}}
- Product stage: {{early / growth / scale / mature}}
- The symptom that brought us here: {{one sentence — the thing that isn't working}}

Please score each of the Four Dimensions 1–5 with justification:
1. Product Organizational Design — job roles, career levels, structure around products
2. Product Strategy — alignment to business, deployment, roadmapping
3. Product Operations — data & insights, customer & market research, process & governance
4. Product Culture — customer-centric mindset, outcome focus, continuous learning, empowerment

Then:
- Name the weakest dimension and explain the pathology.
- Locate the root cause one altitude up (usually strategy vacuum or incentive structure).
- Propose the one operational move that would move the score most.
- Cite Perri's specific source (book chapter, podcast episode, blog post) for each move.

Do NOT recommend a Product Ops team as the answer unless Product Strategy scores at least 3.
```

## Diagnose build trap symptoms

```
I think we might be in the build trap. Here are the symptoms:
{{list what you're seeing — features shipped, roadmap dynamics, OKRs, PM turnover, customer/business metric trends}}

Please apply Perri's diagnostic:
1. Which of the symptoms in her checklist do we match?
2. What's the *pattern* — is this a Waiter-PM problem, a strategy-vacuum problem, an incentive problem, or something else?
3. What's the root cause one altitude up (not the symptom itself)?
4. What are the 2–3 specific moves Perri would recommend, with attribution?

Don't skip the diagnosis to be polite. Name the pathology by its exact term (Waiter PM, mini-CEO myth, roadmap-as-contract, feature-factory, HIPPO, peanut-buttering, Make More Money Syndrome, Pet Projects, Founder Mode, one-throat-to-choke, etc.) so we can confront it directly.
```

## Deploy strategy in 4 tiers

```
Help me deploy our company strategy using Perri's 4-tier model.

Our starting material:
- Vision (if we have one): {{paste or say "unclear"}}
- What execs say the strategy is: {{paste — one sentence version}}
- What product initiatives are currently in flight: {{list}}
- What teams are currently working on: {{list, or a sample}}

Please:
1. Identify our Strategic Intent(s) — the 1–3 large bets. If we don't have them, say so; that's the finding.
2. Map current Product Initiatives to Strategic Intent(s). Flag any that don't map — those may be Pet Projects.
3. Map current team-level Options to Product Initiatives. Flag orphans.
4. Identify where the chain breaks (Vision → Intent → Initiative → Option).
5. Propose the minimum change to make the chain traceable end-to-end.

Apply Perri's Fuzzy Strategy method — Joshua Arnold's 4 value drivers (Increase Revenue / Protect Revenue / Reduce Costs / Avoid Costs) — as the discipline for forcing mechanism into vague executive intent.
```

## Redesign our roadmap

```
Our roadmap has become {{a Gantt chart / a sales contract / a wishlist / a feature promise machine}}. Help me redesign it using Perri's Problem Roadmap approach.

Context:
- Who consumes the current roadmap: {{internal teams / sales / customers / all}}
- What time horizon it covers: {{quarters / a year / multi-year}}
- What specifically breaks: {{missed dates / sales overpromises / discovery skipped / etc.}}

Please:
1. Diagnose what type of roadmap failure we have.
2. Apply Perri's two-roadmap model — outcome-driven internal + feature-driven external.
3. Draft what the internal roadmap should contain (themes / hypotheses / validated solutions).
4. Draft what the external roadmap should contain (near-term commitments + "exploring, subject to change" tag for later items).
5. Name the specific behaviors that would need to change in {{sales / support / execs}} for the split to hold.
6. Cite the source (2014 blog post + Produx Labs 2019+ refined position).
```

## Evaluate Product Operations readiness

```
We're considering standing up a Product Operations function. Help me evaluate whether we're ready and what to build first.

Context:
- Team size / PM function size: {{numbers}}
- Current pain that's driving the question: {{one sentence}}
- Do we have Strategic Intent in place (yes/no/unclear): {{answer}}
- Current state of each of the Three Pillars:
  - Data & Insights: {{describe}}
  - Customer & Market Insights: {{describe}}
  - Process & Governance: {{describe}}

Please apply Perri's diagnostic:
1. Is Strategic Intent in place? (If no, Product Ops will become a PMO in disguise — do that first.)
2. Which pillar is the current pain?
3. What's the minimum viable Product Ops function to address it — one person, one pillar, one obstacle at a time?
4. What's the test for whether the function is actually removing obstacles (real Product Ops) vs. adding them (fake Product Ops)?
5. Cite the source (Perri's 2019 blog post + Product Operations book + Lenny's Ultimate Guide).
```

## Rewrite OKRs from output to outcome

```
Our OKRs have become {{output-disguised-as-outcome / individual / MBO-in-disguise}}. Help me rewrite them the Perri way.

Current OKRs I want to fix:
{{paste 3-5 examples}}

Context:
- OKR ownership: {{individual / team / mix}}
- Are they tied to compensation: {{yes / no / partial}}
- How they roll up: {{quarterly to exec team / annual to board / not clear}}

Please:
1. For each OKR, apply the substitution test — is the KR describing a *thing shipped* or a *behavior changed*? Flag which is which.
2. Rewrite each OKR at the team level (not individual) with an outcome-shaped Objective and behavior-change KRs.
3. Trace each rewritten OKR up to the Product Initiative and Strategic Intent it serves. If either is missing, that's the finding.
4. Name the specific structural changes needed to keep OKRs from drifting back to outputs (decouple from individual comp, quarterly review at team not individual level, etc.).
5. Cite the source (Product Thinking Ep 267 "How OKRs Become Outputs Instead of Outcomes" + "one throat to choke" Substack essay).
```

## Diagnose "one throat to choke" and Mini-CEO patterns

```
We're about to {{fire / replace / performance-review / restructure around}} our PM(s). Help me apply Perri's diagnostic first.

Context:
- The outcome we're holding the PM(s) accountable for: {{describe}}
- What authority the PM(s) actually have over that outcome: {{be honest — budget, headcount, cross-functional influence, etc.}}
- What signals we're reading as "PM failure": {{list}}

Please apply Perri's "one throat to choke" diagnostic:
1. Is the PM accountable for an outcome they don't control alone? Which functions actually determine the outcome?
2. Are the PM's OKRs individual or team-level?
3. Is the job description written as "mini-CEO" (accountability without authority)?
4. Locate the pathology one altitude up — usually the strategy vacuum or incentive structure, not the PM.
5. Before touching the PM, propose the structural changes that would fix the root cause.
6. Cite the source (Substack Jun 2024 essay).
```

## Counter a Founder Mode argument

```
{{Our founder / A senior exec / A board member}} is advocating for "Founder Mode" as our scaling doctrine. Help me respond using Perri's frame.

Context:
- Company stage: {{numbers — headcount, revenue, growth rate}}
- Current founder involvement in product decisions: {{describe}}
- What specifically triggered the Founder Mode conversation: {{describe}}

Please:
1. Distinguish 0→1 (founder-in-the-details is correct) from 1→N (founder-builds-operating-structure is correct).
2. Where in the transition are we, honestly?
3. Apply Perri's Meta/Zuckerberg counter-example — a founder who scales by learning and surrounding themselves with strong operators.
4. Name the specific structural moves that would keep the founder's strategic ownership while releasing them from operational bottlenecks.
5. Warn against the "one throat to choke" pattern this creates for PMs downstream.
6. Cite the source (Substack Sep 2024 essay).

Tone: empathetic-but-firm. Not "founders are bad" — "this specific pattern doesn't scale, and here's the alternative."
```

## Handle a Fuzzy Strategy from execs

```
Our exec team's strategy is "fuzzy" — we can't act on it at the team level. Help me apply Perri's Fuzzy Strategy method.

What execs have said (or what's in the strategy doc):
{{paste}}

Please apply the method:
1. For each strategic statement, map it to one of Joshua Arnold's 4 value drivers — Increase Revenue / Protect Revenue / Reduce Costs / Avoid Costs. If it doesn't map, that's the finding.
2. Flag any Make More Money Syndrome — financial targets stated as strategy without mechanism.
3. Flag any Pet Projects — solutions disguised as strategy.
4. Force the mechanism into the open for each real strategic bet — via which customer, via which value proposition, via which channel?
5. Anchor us in Perri's load-bearing sentence: *"You don't need perfect strategic clarity to make good product decisions."* — what can we act on today with the clarity we have?
6. Cite the source (Oct 2024 blog post).
```

## Compare Perri's frame vs. an adjacent framework

```
I'm deciding whether to use Perri's frame or {{Cagan's Product Operating Model / Torres's Continuous Discovery / Singer's Shape Up / JTBD / OKRs alone}} for {{my situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If the answer is "neither, use something else entirely", tell me that too.

Guardrail: don't collapse Perri's frame into Cagan's — Perri operates one altitude below and explicitly cedes the "Product Operating Model" phrase to Cagan.
```

## Interpret a *Dear Melissa* symptom in our org

```
Here's a symptom in our org that feels like it could be a Dear Melissa question:

{{describe the symptom in 3-5 sentences — a specific role/team/decision that isn't working}}

Please walk this the way Perri would in a Dear Melissa episode:
1. Restate the symptom.
2. Ask what else is going on (name the two or three other org details that would change the diagnosis).
3. Walk upstream — one altitude at a time — until you find the real cause.
4. Name the pathology using Perri's exact vocabulary.
5. Propose 1-2 structural changes; do not propose 5+.
6. Cite an adjacent Product Thinking podcast episode or essay where Perri has treated a similar pattern.

Tone: empathetic-but-firm. Warm about the humans; direct about the pattern.
```

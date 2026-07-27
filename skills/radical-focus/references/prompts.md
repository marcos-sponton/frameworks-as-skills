# Radical Focus — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant (Claude or Codex) can execute well.

## Draft team OKRs from scratch

```
I want to write OKRs for {{my team}} for the upcoming quarter using Wodtke's Radical Focus method.

Context:
- Team: {{describe — size, role, autonomy}}
- Company / product stage: {{seed / growth / mature}}
- Current biggest problem or opportunity: {{one paragraph}}
- Company (or BU) Objective this quarter: {{if known — otherwise say "not defined yet"}}

Please:
1. Draft ONE team Objective that's qualitative, inspirational, time-bound, and actionable by us alone.
2. Draft ~3 Key Results that are OUTCOMES (not outputs), balancing dimensions to prevent gaming.
3. Propose 2 Health Metrics we should protect while pushing on the Objective.
4. Sketch what our Monday Commitments meeting should cover in the first week.
5. Call out anything in my context that suggests OKRs might be the wrong tool right now (missing autonomy, psychological safety, etc.).
```

## Critique OKRs I already wrote

```
Here are the OKRs my team drafted. Please critique them against Wodtke's Radical Focus.

{{paste OKRs}}

Specifically:
1. Is the Objective qualitative + inspirational + time-bound + team-actionable — or is it a KPI, a baseline state, or a slogan?
2. Are the Key Results OUTCOMES (measurable change in the world) or OUTPUTS (things we'll ship)?
3. Would confidence be 5/10 at the start of the quarter — or are these too easy / too hard?
4. Do we have Health Metrics? What should we be PROTECTING while pushing on this Objective?
5. Which of Wodtke's anti-patterns are we falling into (individual OKRs, cascading, quarterly-only-no-cadence, OKRs-as-KPIs, 5+ objectives)?
6. Cite specific Wodtke sources when you make each point.
```

## Diagnose "our OKRs aren't working"

```
Our team has been running OKRs for {{N}} quarters and they aren't moving. Help me diagnose using Wodtke's method.

Context:
- What we set: {{paste last quarter's OKRs}}
- How we actually run them: {{describe the meeting cadence — or the absence of one}}
- What we grade at end of quarter: {{describe scoring practice}}
- Team makeup: {{size, autonomy, cross-functional or siloed?}}

Please diagnose in this order:
1. Do we have weekly cadence (Monday commitments + Friday celebrations)? If no, that's likely THE problem.
2. Are OKRs individual, cascaded, or team-level?
3. Are KRs outcomes or outputs?
4. Do we have Health Metrics?
5. Is the Objective actually a KPI or baseline state in disguise?
6. Are prerequisites in place (autonomy, safety, multidisciplinary team)?

Prescribe the fixes in priority order — likely cadence first, then structure.
```

## Rewrite output KRs as outcome KRs

```
Here are our Key Results. I think some of them are actually outputs (tasks) rather than outcomes (measurable change). Help me rewrite.

{{paste KRs}}

For each KR:
1. Say whether it's an outcome or an output (using Wodtke's distinction).
2. If it's an output, ask: "if we hit this, what changes in the world?" — and propose an outcome version.
3. Preserve the balance across dimensions (don't rewrite three KRs into three versions of the same measurement).
```

## Add a Health Metric to guard against gaming

```
Here's our Objective + Key Results for {{team}}:

{{paste}}

Following Wodtke's Health Metric method (see the OpenAI 2025 "code red" case):
1. If we optimized purely for these KRs, what would we destroy? Those are candidate Health Metrics.
2. Propose 2 Health Metrics we should track green/yellow/red.
3. Define what "red" looks like for each — what would trigger a code red (pause OKR work, protect the metric)?
```

## Set up the weekly cadence

```
We want to start running Radical Focus cadence for {{team}}. Design it.

Team context:
- Size: {{N people}}
- Time zones: {{sync or async?}}
- Current meeting load: {{how meeting-heavy is the week already?}}

Please design:
1. Monday Commitments meeting — length, agenda following the 4-quadrant (Intention for the Week, Forecast for the Month, Status toward OKRs, Health Metrics), who owns each quadrant.
2. Friday Celebrations meeting — length, tone, what to demo, what NOT to bring up.
3. Monthly retrospective — what to reflect on (the practice, not the OKRs themselves).
4. Quarterly grade + reset — how to score, and how to focus on learning per Wodtke's 2025 refinement.
5. What to put on the calendar first (before writing the OKRs).
```

## Push back on individual OKRs

```
{{Someone at my company — HR / a VP / a founder}} wants us to give every individual their own OKRs. Help me push back using Wodtke's specific critiques.

Please:
1. Name why Wodtke rejects individual OKRs (with source).
2. Explain the pathology — how individual OKRs collapse into performance-review theater and kill team accountability.
3. Offer the Wodtke alternative — team OKRs + individual development goals separately in 1:1s.
4. Give me the specific quote or paraphrase to use in the conversation.
```

## Push back on quarterly-only OKRs

```
My leadership team wants to set OKRs quarterly and just check in at the end of the quarter. Help me push back using Wodtke's specific critique.

Please:
1. Name why "quarterly-only" OKRs fail per Wodtke.
2. Frame the weekly cadence as the actual method — not an add-on.
3. Give me the minimum viable cadence I can propose (Monday commitments + Friday celebrations) with a realistic time budget.
4. Cite specific Wodtke sources.
```

## Untangle OKRs, KPIs, and Health Metrics

```
Our leadership team is confused about the difference between OKRs, KPIs, and Health Metrics. Help me explain using Wodtke's model.

Please:
1. Explain the three categories using the dashboard / GPS / protect metaphor.
2. For each of these examples, tell me which category it belongs in:
   - {{list of candidate metrics}}
3. Give me a one-slide summary I can share.
```

## Grade OKRs with a learning lens

```
End of quarter. Here are our OKRs and the numbers we hit.

{{paste OKRs + actuals}}

Per Wodtke's 2025 refinement, grade with a learning lens:
1. Score each KR 0.0–1.0 (context only).
2. For each KR, answer: what worked, what didn't, what will we do differently next quarter?
3. What did we learn about our team, our customers, or our theory of the market?
4. Given the learning, what should our next Objective be?
```

## Choose between Radical Focus and adjacent frameworks

```
I'm deciding whether to use Radical Focus or {{other framework — e.g., Doerr's Measure What Matters, EOS, Balanced Scorecard, Playing to Win}} for {{my situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If the answer is "neither, use something else entirely", tell me that too.
```

## Adapt Radical Focus for a small startup (< 10 people)

```
I'm a founder of a {{N}}-person startup. We don't have "teams" yet — we're all doing everything. How does Wodtke's method adapt?

Please:
1. Should we do OKRs at all at this stage, or wait? (Use Wodtke's prerequisites test.)
2. If yes, how do we adapt the "team OKR" model for a company where the team IS the company?
3. What's the minimum viable cadence — one meeting or two?
4. What's our first Health Metric — the thing we'd sacrifice OKR progress to protect?
```

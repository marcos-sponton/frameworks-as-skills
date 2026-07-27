# DORA / Accelerate — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant can execute well.

## First-time DORA baseline

```
Help me stand up DORA measurement for my engineering team for the first time.

Context:
- Team / org: {{describe — size, product, industry}}
- Current measurement (if any): {{what you measure today, if anything}}
- Executive audience: {{who will see the numbers}}
- Constraint: {{time, tooling budget, political constraints}}

Please:
1. Walk me through the four DORA keys (plus the fifth if relevant to my situation).
2. Estimate my current tier for each based on what I've told you (Elite / High / Medium / Low).
3. Point me at the DORA Quick Check as the fastest baseline path.
4. Recommend 1-2 capabilities to invest in first, based on where I'm weakest.
5. Warn me explicitly if my exec audience is likely to want to use DORA for individual performance reviews — that's the misuse I need to guard against from day one.

Cite Forsgren / DORA sources where you make specific claims.
```

## Diagnose a delivery problem

```
My team's delivery feels {{slow / unstable / both}}. Help me diagnose using DORA.

Rough numbers:
- Deployment Frequency: {{how often}}
- Lead Time for Changes: {{commit to prod}}
- Change Failure Rate: {{% of deploys that fail}}
- Recovery Time: {{how fast after failure}}

Perceptual data:
- Developers say: {{what they say}}
- Leadership says: {{what they say}}

Please:
1. Translate my numbers into DORA tiers.
2. Diagnose whether this is a throughput problem, a stability problem, or both.
3. Name the 1-2 DORA capabilities most likely to be the bottleneck.
4. If the perceptual data conflicts with the delivery numbers, name that gap and reach for DevEx.
5. Recommend a specific 6-8 week experiment: invest in [capability], expect [metric] to move by [amount].
```

## Critique a productivity dashboard

```
Here's the engineering productivity dashboard my company is using / evaluating:

{{paste the metrics list, or attach a screenshot}}

Please critique it against DORA / SPACE / DevEx research. Specifically:
1. Are any of these metrics vanity metrics (activity without predictive validity)?
2. Are any of these at the wrong level (individual when they should be team, or vice versa)?
3. Are there missing metrics that would balance the dashboard (throughput without stability, activity without satisfaction, etc.)?
4. Which of these could be gamed, and how?
5. If Forsgren looked at this dashboard, what would she push back on hardest?
6. What would a research-consistent version of this dashboard look like?
```

## Executive is asking to tie DORA to individual performance

```
My CEO / VP / Head of Eng wants to tie DORA metrics to individual performance reviews and possibly comp.
Help me push back and offer the correct alternative.

Context:
- The specific proposal: {{describe}}
- The underlying question they're trying to answer: {{"who's a strong performer" / "who to promote" / "who's slacking"}}
- My leverage: {{how much room I have to push back}}

Please:
1. State the Forsgren / DORA position on this misuse — with attribution.
2. Explain the gaming dynamic in concrete terms (what devs will do within a quarter).
3. Recommend the correct alternative for their actual question — competency framework, growth ladder, or 360 depending on which.
4. Give me a script for the conversation.
```

## Choose between DORA, SPACE, DevEx, or DX Core 4

```
I'm trying to pick the right measurement frame for my situation: {{describe what you want to measure}}.

Help me pick.
- If the answer is DORA, tell me the specific keys and capabilities to focus on.
- If the answer is SPACE, tell me which 2-3 dimensions to measure and which metrics per dimension.
- If the answer is DevEx, tell me which of the three dimensions is most relevant and which perceptual + system data to gather.
- If the answer is DX Core 4, tell me the four primary metrics and how to instrument.
- If the answer is "none of these — reach for [other framework]", tell me which one and why.
```

## Team is investing in AI coding tools — what to measure

```
We're rolling out AI coding assistants (Copilot / Cursor / equivalent) across engineering.

Help me set up measurement so we can tell whether AI is actually helping — not just whether developers feel it's helping.

Please:
1. Cite the 2024 DORA State of DevOps finding on AI + delivery (the productivity paradox).
2. Recommend which DORA + DevEx + SPACE metrics to baseline before rollout.
3. Recommend what to re-measure at 3 months and 6 months.
4. Name the capabilities we should invest in in parallel — small batches, test automation, documentation — so AI's speed at the keyboard actually reaches production.
5. Warn me about what NOT to measure (individual AI usage rates as productivity).
```

## Platform engineering investment — measurement plan

```
We're funding / expanding an internal developer platform team.
Help me measure whether it's actually working.

Context:
- Platform scope: {{CI/CD? IDP? DX tooling? SRE?}}
- Consuming teams: {{how many, how varied}}
- Timeline: {{when leadership will ask for ROI}}

Please:
1. Frame the platform team's success as their consumers' success — DORA at the consuming-team level, DevEx at the consuming-developer level.
2. Cite the 2024 State of DevOps finding on platform engineering (productivity boost but throughput/stability risk if platform is not well-run).
3. Recommend the specific metrics to instrument on the consuming teams.
4. Recommend how the platform team itself should be measured (DevEx, not just uptime).
5. Recommend a quarterly review cadence.
```

## Reverse-engineer another company's DORA-style practices

```
Help me infer how {{Company X}} operates on the DORA capabilities, from what's publicly known.

Follow the DORA capabilities catalog:
1. Technical: what do they publicly do around CI/CD, trunk-based dev, test automation, observability?
2. Process: what do we know about their batch size, WIP practices, team topology?
3. Cultural: what does their public communication say about generative culture, transformational leadership, learning?
4. AI-specific: what's their public AI stance and data ecosystem?
5. Estimate their DORA tier and name the capabilities that likely explain it.

Focus on differences from industry norms (which are the strategic ones), not similarities (which are commoditized).
```

## SPACE — pick metrics for a specific team

```
I want to measure my team's productivity using SPACE. Help me pick 2-3 metrics across at least 3 dimensions.

Team context:
- Type: {{feature team / platform / SRE / etc.}}
- What matters most to us right now: {{shipping features / retention / stability / learning / etc.}}
- What we already measure: {{list}}
- Where we might be gaming metrics unintentionally: {{if you know}}

Please:
1. Recommend 2-3 metrics across at least 3 dimensions of SPACE (Satisfaction, Performance, Activity, Communication, Efficiency).
2. Explicitly include at least one Satisfaction or Well-being metric.
3. Explicitly avoid activity-only metrics as the main signal.
4. Warn me about how each metric could be gamed and how to guard against it.
5. Suggest whether we should pair with DORA and/or DevEx.
```

## DevEx — diagnose "why does it feel slow"

```
Our DORA numbers are fine but the team feels slow / frustrated / overloaded. Help me use DevEx.

Symptoms:
- What developers say: {{their words}}
- What managers say: {{their words}}
- What the system data shows: {{if you have it}}

Please:
1. Walk me through the three DevEx dimensions (Feedback Loops, Cognitive Load, Flow State) as diagnostic lenses.
2. For each dimension, recommend 2-3 specific things to look at (both perceptual survey questions and system telemetry).
3. Help me identify which dimension is likely the bottleneck.
4. Recommend a 6-8 week intervention on the bottleneck dimension.
5. Tell me what to expect in DORA numbers if we improve DevEx (usually: throughput up, stability up, satisfaction up).
```

## DX Core 4 — executive-ready dashboard

```
My executive team wants one small, defensible dashboard for engineering. Help me use DX Core 4.

Context:
- Company size: {{how many devs}}
- Board / exec expectations: {{what they've asked for}}
- Existing measurement: {{DORA? SPACE? nothing?}}

Please:
1. Walk me through the four DX Core 4 dimensions (Speed, Effectiveness, Quality, Impact) and their primary metrics.
2. Explicitly explain that Speed (Diffs per Engineer) is NEVER for individual performance evaluation, and how we present it to prevent misuse.
3. Recommend how to instrument the four primary metrics with minimal effort.
4. Recommend which secondary metrics to add if we have capacity.
5. Cite Tacho, Noda, Forsgren as sources.
```

## Frictionless — plan a friction-removal program

```
We want to systematically remove friction in our engineering delivery — inspired by Forsgren + Noda's *Frictionless*.

Context:
- Current baseline (DORA tier): {{estimate}}
- Where we suspect the biggest friction: {{deploys / testing / reviews / envs / other}}
- Timeline: {{how much runway we have}}

Please walk me through the 7-step Frictionless methodology as applied to my situation:
1. Baseline the current state (DORA + DevEx).
2. Identify the highest-friction points.
3. Prioritize by leverage.
4. Instrument the specific friction.
5. Ship the friction-removing change in small batches.
6. Verify with metrics + developer perception.
7. Scale to the next friction.

Recommend which friction to attack first based on what I've told you.
```

# The Cold Start Problem — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant can execute well.

## Pre-flight before invoking the Cold Start skill

```
Before running the Cold Start Problem on my situation, help me check:

1. Is this actually a network product? (Does value require other users? If no, use a different framework.)
2. If it's a come-for-the-tool product, does the tool have real N=1 value?
3. Which of the 5 stages am I in — Cold Start / Tipping Point / Escape Velocity / Ceiling / Moat?
4. Do I have real evidence (density metrics, hard-side retention, atomic-network unit data), or am I working from feels?
```

## Diagnose which stage of the 5 you're in

```
I'm building {{product}} — {{one sentence: what it is, what stage it's at}}.

Context:
- Users / customers: {{describe}}
- Current density inside your typical atomic unit: {{describe or "unknown"}}
- Recent trajectory: {{growing / stalled / decaying / launching}}
- Hard side and easy side (as best you can name them): {{describe or "unclear"}}

Apply Andrew Chen's 5 stages:
1. Which stage am I in — Cold Start / Tipping Point / Escape Velocity / Ceiling / Moat?
2. What's the evidence for that stage diagnosis?
3. What's the stage-specific playbook?
4. What's the biggest risk of getting the stage diagnosis wrong?
```

## Sharpen the atomic network (the most-used template)

```
My candidate atomic network for {{product}} is: {{describe}}.

Apply Chen's atomic-network sharpener:
1. Cut it in half. Is the result still a plausible self-sustaining unit?
2. Cut it in half again. Still plausible?
3. Keep cutting until it feels almost embarrassingly narrow.
4. What's the resulting atomic network? Compare to Chen's canonical examples:
   - Uber: "5pm at the Caltrain Station at 5th and King Street"
   - Slack: 3-person team inside one company
   - Zoom: 2 people
   - Tinder: one college campus
   - Facebook: one dorm
5. Given that atomic network, redesign the product to feel useful and alive at that size (not 100x that size).
```

## Identify the hard side and their hard problem

```
For {{product}}, help me identify the hard side of the network.

Context:
- The two sides of the network: {{describe}}
- Value each side creates: {{describe}}
- How hard is each side to acquire and retain: {{describe}}

Apply Chen's hard-side identifier:
1. Which side is the hard side (creates disproportionate value AND is disproportionately hard to acquire and retain)?
2. What's the SPECIFIC problem that's hard for them (not "they want more X" — the actual friction Chen would recognize)?
3. What product mechanism could structurally solve that problem? (Think Tinder's swipe mechanic for the harassment problem.)
4. If I don't solve the hard side first, what happens? (Reference Wimdu.)
5. What's the 80/20 pattern likely to look like on my hard side?
```

## Come-for-the-tool audit

```
I'm considering a come-for-the-tool launch for {{product}}.

Context:
- The tool: {{describe}}
- The network layer that would be added later: {{describe}}

Apply Chen's come-for-the-tool test:
1. Does the tool have REAL N=1 value? (Would a single user with no other users find it useful on day 1?)
2. What single-player problem does the tool solve?
3. What's the mechanism by which tool users become network users?
4. Is this genuine come-for-the-tool, or come-for-the-tool cosplay (a network product in tool clothing)?
5. If cosplay: what's the actual launch path — this isn't come-for-the-tool.
6. Reference cases: Instagram (photo filter → feed), Dropbox (sync → shared folders), Yelp (listings → reviews).
```

## Diagnose why my network is stalling (Ceiling)

```
Our network product {{product}} has stalled. We're at {{scale}}.

What's happening:
- Growth trajectory: {{describe}}
- Hard-side health (creators / hosts / drivers / champions): {{describe}}
- User complaints / churn reasons: {{describe}}
- Recent platform / algorithm / market changes: {{describe}}

Apply Chen's Ceiling stage diagnosis:
1. Which ceiling failure mode is active?
   - Market saturation
   - Overcrowding (discovery breaks)
   - Eternal September (mass audience dilutes early community)
   - Spam / fraud / bad actors
   - Algorithm rot (platform dependency)
   - Power-user burnout (hard side leaves)
2. What's the specific evidence?
3. What's the re-engineering move for that failure mode? (Algo curation? Sub-networks? Trust systems? Hard-side incentives? Diversification?)
4. What are hidden failure modes I should watch for?
```

## Moat pressure test

```
We claim network effects as our moat. Pressure-test this.

Context:
- Product: {{describe}}
- Atomic-network density (users per unit): {{describe}}
- Hard-side retention: {{describe}}
- Top 20% of hard-side users concentration: {{describe}}
- Recent competitor activity: {{describe}}
- Platform-shift risks (AI, agents, TikTok, App Store, browser AI): {{describe}}

Apply Chen's moat pressure test:
1. What would a Wimdu-style clone with heavy funding do to us? (Probably fail — but ask why.)
2. What would a cherry-picking attacker do to us? (Peel off our top 20% of hard side.)
3. What would an emerging sub-network do? (A niche that could break off with a specialized experience.)
4. What would a platform shift do? (AI / agents / new distribution.)
5. What's our active defense for each attack? (Not: "we have network effects.")
6. Which of our defenses is weakest?
```

## Marketplace launch beachhead

```
We're launching a marketplace: {{describe}}.

Context:
- Supply side (probably hard side): {{describe}}
- Demand side (probably easy side): {{describe}}
- Candidate launch geographies / verticals / niches: {{list}}

Apply Chen's Cold Start launch method:
1. Which side is hard? What's their specific hard problem?
2. What's the smallest possible atomic network? (Cut candidates in half. Then half again.)
3. What's the plan to manufacture the first atomic network? (Personal hustle, invite-only, growth hacks, paid subsidies — one-time bootstrapping cost, not scalable channel.)
4. Once one atomic network works, what's the repeatable playbook to build the second, tenth, hundredth?
5. What's the "5pm at Caltrain" version of my launch — the specific micro-context where density can be forced first?
```

## AI product defensibility check

```
We're building an AI product: {{describe}}. Our defensibility claim is: {{describe network effects claim}}.

Apply Chen's post-book AI-era skepticism:
1. Is this actually a network product, or a single-player AI tool?
2. Does more usage make the product better for OTHER users? Name the specific mechanism.
   - Data network effects (proprietary data flywheel)?
   - Marketplace of agents / AI outputs?
   - UGC / community layer?
   - Human-in-the-loop feedback that improves the base model?
3. If none of these, this is a tool with no network moat — reframe the defensibility argument.
4. If yes, at what stage of the 5 are you (Cold Start? Escape Velocity?), and what's the stage-specific playbook?
```

## Attack an incumbent network product

```
We want to attack {{incumbent network product}}. Our approach: {{describe}}.

Apply Chen's competitive-attack framework:
1. What's the hard side of the incumbent?
2. What's the hard side's biggest unmet pain point / opportunity?
3. Can we cherry-pick the hard side with better economics / better product for them specifically?
4. Is there an emerging platform / distribution shift we can be first-party on that the incumbent isn't?
5. Warning: Wimdu-style attacks (identical replication with heavy funding, targeting easy side) fail. Are we doing that?
6. What's the atomic network for OUR attack — where do we build density first?
```

## Reverse-engineer a network product's atomic network

```
Help me reverse-engineer {{company}}'s atomic network.

Publicly observable signals:
- Product: {{describe}}
- Launch history: {{describe or "unknown"}}
- Hard side and easy side (best guess): {{describe}}
- Current scale: {{describe}}

1. What was probably their atomic network at launch? (Reference Chen's rule: smaller and more specific than intuition suggests.)
2. Who is the hard side and what specific hard problem did they solve for them?
3. What loops (acquisition, engagement, economic) are running now?
4. Where is their chain strong? Where's the weakest link?
5. Warning: don't copy their playbook — atomic network shape and hard side may differ from mine. What can I learn from the THINKING, not the tactics?
```

## Growth model slide for the board (network product edition)

```
Help me draft the growth section of my board deck for {{network product}}.

Context:
- Which stage we're in: {{Cold Start / Tipping Point / Escape Velocity / Ceiling / Moat}}
- Atomic-network unit + density: {{describe}}
- Hard-side health metrics: {{describe}}
- Next-quarter plan: {{describe}}

Apply Chen's operator framing:
1. Show the atomic-network unit and its density (not total user count).
2. Show hard-side retention separately from overall metrics.
3. Show which stage we're in and the stage-specific playbook.
4. Show the biggest ceiling risk we're monitoring.
5. Show what we're actively doing to defend the network — not "we have network effects."
```

## Pre-mortem the ceiling before you hit it

```
We're at Escape Velocity for {{product}}. I want to pre-mortem the ceiling.

Context:
- Current growth trajectory: {{describe}}
- Hard side + easy side dynamics: {{describe}}
- Platform dependencies: {{describe}}

Apply Chen's ceiling pre-mortem:
1. Which of the ceiling failure modes is MOST likely to hit us first?
   - Overcrowding, eternal September, spam, algorithm rot, power-user burnout, saturation
2. What early-warning signals should we instrument now?
3. What defenses can we build BEFORE we need them? (Algo curation, sub-networks, trust systems, hard-side economics.)
4. What's the fallback if the primary ceiling mode hits?
```

# Working Backwards — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude or Codex can execute well.

## Draft a PR/FAQ from scratch

```
I want to draft a PR/FAQ for {{product / feature / initiative}} using Bill Carr and Colin Bryar's Working Backwards method.

Context:
- Company / product area: {{describe}}
- Customer: {{who specifically — segment, role, situation}}
- Problem I think they have: {{one paragraph — resist naming a solution here}}
- Why I think this matters to them: {{be specific — atomic need, not stated preference}}
- What alternatives exist today: {{be honest — including "they do nothing"}}
- Stage: {{early exploration / committed to build / just want the doc reviewed}}

Please walk me through drafting the PR/FAQ:
1. Press Release (heading, subheading, summary, problem, solution, quotes, getting started).
2. External FAQs.
3. Internal FAQs (finance, ops, technical, strategic).

Challenge my writing when:
- It slips into hyperbole ("revolutionary", "world-class", "game-changing").
- The problem paragraph names a preference instead of an atomic need.
- The solution paragraph starts from our capabilities instead of the customer.
- I skip the "would customers reasonably adopt this" question.
- I don't name existing competition honestly.

Cite Carr, Bryar, or the book when you introduce a specific device.
```

## Critique a PR/FAQ, PRD, or product doc I already wrote

```
Here's a product doc I drafted:

{{paste content or attach file}}

Please critique it against Working Backwards. Specifically:
1. Does it start with the customer, or is it skills-forward (starts from our capabilities)?
2. Is the customer named specifically enough that I could point to who's in and who's out?
3. Is the "problem" an atomic customer need, or a surface preference?
4. Does the solution differentiate meaningfully from what exists today?
5. Is the writing factual and data-rich, or does it lean on hyperbole?
6. Are the FAQs (internal + external) doing the interrogation job, or are they polite?
7. If I were a Bar-Raiser-caliber reviewer assuming every sentence is wrong until proven otherwise, what would I push back on hardest?
8. What's my strongest point that's worth doubling down on?
```

## Run or fix a 6-pager review meeting

```
I'm about to run (or I'm currently running) a review meeting for {{initiative}}.
Doc: {{link or paste}}
Attendees: {{list}}
Current format: {{PowerPoint / bullet-riddled memo / real 6-pager / not sure}}

Help me:
1. Diagnose whether this is actually a Working Backwards review or theater.
2. If it's not: what's the smallest change that would make it a real review (typically: enforce silent reading + require narrative prose).
3. What questions should I be prepared to answer (as author) or ask (as reviewer)?
4. What disposition should I bring? (Reference Bezos's "assume every sentence is wrong until proven otherwise.")
5. What are the top failure modes to watch for during the discussion?
```

## Diagnose why Working Backwards isn't taking hold in my org

```
I've been trying to bring Working Backwards mechanisms to my company for {{time period}}. It's not sticking.

What I've tried:
- {{PR/FAQ / 6-pager / STL / input metrics / WBR / Bar Raiser — check all that apply}}
- {{what actually happened}}

Where I think it's stuck:
- {{one paragraph}}

Help me diagnose:
1. Which mechanisms have I actually adopted, versus which have I adopted in name only?
2. Do I have CEO-level air cover, or am I pushing this from below?
3. What's the disposition gap — where is our current culture pulling against the mechanism?
4. Is there a smaller mechanism I could get right first, before pushing the harder ones?
5. What would Carr or Bryar likely say about my situation? (Reference the "profound changes require CEO commitment" framing.)

Be honest — don't sell adoption as easy. Cite the sources where the authors have addressed this failure mode.
```

## Set up (or fix) input metrics for a team

```
My team's current metrics:
- {{list them}}

The team owns: {{describe the initiative or product area}}
The customer outcome we want to move: {{output metric — revenue, retention, engagement, etc.}}

Help me:
1. Classify each current metric as input vs. output vs. compound "fitness function."
2. Map the end-to-end customer experience for our area. (Carr's rule: "map your end-to-end customer experience" is the starting point for finding input metrics.)
3. Identify the controllable input metrics that sit upstream of our target output.
4. Screen each candidate against: controllable? Directly upstream? High-frequency measurable? Not a fitness function?
5. Draft what our WBR agenda should look like once we have real input metrics.
6. Warn me about the input metrics my team is likely to resist tracking (usually the ones that expose slow-moving problems).
```

## Structure (or unblock) a Single-Threaded team

```
I want to (or my org wants to) run initiative {{X}} as a single-threaded team.

Current state:
- Proposed STL: {{name / role — is this person 100% dedicated?}}
- Resources: {{list — are they dedicated or matrixed?}}
- Reporting lines: {{describe}}
- Dependencies on other teams: {{list}}

Help me:
1. Diagnose whether this is a real STL or a fractionally-threaded team with a fancy title.
2. Name the specific conditions that need to be met (one leader, zero competing responsibilities, dedicated resources, separable structure).
3. Identify the coordination-tax hot spots — where would dependencies most likely stall this team?
4. Draft the STL's charter (purpose, scope, evaluation metrics, ownership boundaries).
5. Warn me about the failure modes I'm most likely to hit.
```

## Design a Bar Raiser process for a critical hire

```
I'm hiring {{role}} for {{team / initiative}}. It's a bar-defining hire.

Current process:
- {{describe}}

Help me design a Bar Raiser process:
1. Who should the Bar Raiser be? (Structural independence: not on the hiring team, not the future manager's peer.)
2. How is veto power exercised? (Bar Raiser can kill the hire; hiring manager cannot overrule.)
3. What Leadership Principles (or our equivalent values) should be assigned to each interviewer?
4. How is behavioral interviewing done well? (STAR format, past behavior over hypotheticals.)
5. How do we run the debrief so the Bar Raiser's assessment actually holds?
6. What's the most common failure mode we should watch for? (Usually: urgency bias — "we need this role filled yesterday" — which is exactly what Bar Raiser exists to counter.)
```

## Run a Correction of Errors after a real failure

```
We had a failure: {{describe briefly}}

Impact: {{scope}}
Root cause (my current guess): {{describe}}

Help me run a real COE:
1. Force me past personal blame — the mechanism is about finding the mechanism gap, not the guilty party.
2. What's the specific mechanism that would have prevented this? (PR/FAQ that wasn't written? Silent-reading review that got skipped? Input metric no one was tracking? STL who was actually matrixed?)
3. Draft the COE structure: what happened, why it happened (5 whys), what mechanism gap allowed it, what mechanism change prevents recurrence, who is accountable for the change, when it's implemented.
4. What's the disposition to bring to the room? (Reference Bezos's "why would I fire you now" — investment, not blame.)
5. How do we make sure the learning propagates to other teams?
```

## Ask Working Backwards to critique a piece of strategy or a plan

```
Here's a strategy / plan / initiative document:

{{paste content}}

Critique it through the Working Backwards lens (not through a corporate-strategy lens — I know that's Playing to Win / Rumelt territory). Specifically:

1. Does it start with a customer, or with capabilities?
2. Is there a specific customer need being addressed, or is it a growth ambition?
3. Are the metrics inputs (controllable) or outputs (lagging)?
4. Is there a Single-Threaded Leader implied, or is this a matrixed nice-to-have?
5. What PR/FAQ would need to be written for the core bets in this plan to be legible?
6. What's the most likely failure mode if this plan gets executed as written?
```

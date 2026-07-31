# Continuous Discovery Habits — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape the assistant can execute well.

## Start a weekly discovery cadence

```
Help me stand up a weekly continuous discovery cadence for my product team using Teresa Torres's method.

Context:
- Product / company: {{describe}}
- Team composition (do I have a full trio — PM + designer + engineer?): {{yes / no / partial}}
- Current discovery practice (be honest — project-based, ad hoc, none, PM-solo?): {{describe}}
- Product outcome we're trying to move (if set): {{paste or say "not defined"}}

Please:
1. Diagnose where we're starting from — do we have a trio, a product outcome, and any interview cadence?
2. If any of the 3 preconditions is missing, name it and coach me to fix it before we run interviews.
3. Propose the minimum viable weekly cadence — start with 30 minutes per week, one interview per week, trio together.
4. Give me the concrete first 4 weeks: who's in the room, what we do, what artifact we build.
5. Warn me about the top 2 anti-patterns for teams starting out (usually: cadence slippage, PM-solo drift).
6. Cite Torres's sources (book chapter, specific Product Talk essay).

Guardrail: don't recommend building the Opportunity Solution Tree until we have 3–4 story-based interviews under our belt. Torres's prerequisite.
```

## Build (or update) an Opportunity Solution Tree

```
Help me build an Opportunity Solution Tree for {{outcome or problem area}}.

Context:
- Product outcome (behavior change we're trying to move): {{paste}}
- Number of story-based interviews we've done so far: {{number}}
- Team composition: {{trio yes/no}}
- Current draft opportunities or notes (if any): {{paste}}

Please:
1. Check the outcome — is it a product outcome (behavior change, in trio's span of control) or a business outcome / output in disguise? If wrong altitude, coach me to fix it before we go further.
2. If we have fewer than 3–4 interviews, tell me the tree is premature — coach me to interview first.
3. If we have enough interview material, help me populate the opportunity space — surfacing customer needs, pain points, and desires (NOT features).
4. Apply the "is there more than one way to address this?" test to every candidate opportunity. Flag solutions disguised as opportunities.
5. For 1–2 target opportunities, help me brainstorm at least 3 solutions each.
6. For the top solution, help me name assumptions across all 5 categories (desirability, viability, feasibility, usability, ethical).
7. Identify the riskiest assumption and propose a small assumption test that could evaluate it in the next hour.
8. Cite Torres's Opportunity Solution Trees canonical essay.
```

## Diagnose interview technique mistakes

```
Here's an interview question / interview snippet from my team. Please audit it against Teresa Torres's story-based interviewing rules.

Interview material:
{{paste question or snippet}}

Please:
1. Score against Torres's 4 rubric dimensions (from the Interview Coach):
   - Opening with a story-based question
   - Setting the scene
   - Building the timeline
   - Redirecting generalizations
2. Flag any of these anti-patterns explicitly:
   - Opinion questions ("What do you think of X?")
   - Hypothetical / future questions ("Would you use X?")
   - Generalization questions ("Tell me about your experience with X")
   - Closed / yes-no questions in the story portion
   - Self-reported behavior metrics
3. For each flagged issue, rewrite it in the Torres form.
4. If the interviewer let a generalization stand without redirecting, coach the specific redirect move.
5. Cite the Story-Based Customer Interviews essay (Apr 2024) for the rules.
```

## Frame a product outcome the right way

```
Our team has been given the outcome "{{paste the goal / OKR / metric}}". Help me evaluate it against Teresa Torres's product outcome definition, and rewrite it if needed.

Context:
- Team composition: {{trio yes/no}}
- What we can actually control through product decisions: {{describe}}
- What time horizon: {{quarter / half / year}}

Please:
1. Categorize the current framing — is it an output (thing shipped), a business outcome (revenue / retention — outside trio's control), a traction metric (too narrow), a sentiment metric (NPS with no behavioral direction), or a real product outcome?
2. Apply Torres's 8 mistakes checklist. Flag which mistakes are present.
3. If it's not a product outcome, rewrite it as one — a customer behavior change, within the trio's span of control, with room for exploration.
4. Trace how the rewritten product outcome would drive the underlying business outcome (so the exec team can see the connection).
5. Cite Torres's "Defining Product Outcomes: The 8 Most Common Mistakes" essay.

Guardrail: if the exec team wants a business outcome (e.g., "grow revenue 30%") as the team's OKR, name that as Mistake #3 (span of control) and propose the product outcome that would move it.
```

## Map assumptions and design a small assumption test

```
Our team is about to commit to building {{paste solution description}}. Before we build, help me map assumptions and design a small assumption test using Teresa Torres's method.

Context:
- The opportunity this solution addresses: {{paste}}
- The product outcome it's meant to move: {{paste}}
- Team's rough sense of the riskiest thing: {{if any}}

Please:
1. Help me name at least 2 assumptions in EACH of the 5 categories (desirability, viability, feasibility, usability, ethical). Push back if we're only naming assumptions in our team's biased categories (engineers over-index on feasibility, PMs on viability, designers on usability, ethical always gets skipped).
2. Rank the assumptions by risk — if this assumption is wrong, how badly does the solution fail?
3. For the top-ranked risky assumption, design a small assumption test — something we can do this week (or, per Torres's rule, in the next hour).
4. Explicitly distinguish this from a full experiment — we're testing one assumption, not the whole solution.
5. Name what we'd learn from the test result (and what we would do differently based on it — if there's no decision that would change, the test is theater).
6. Cite Torres's Assumption Testing essay + Five Types of Assumptions essay.
```

## Audit "we already do continuous discovery"

```
Our team says we already do continuous discovery. Help me audit whether we actually do, using Teresa Torres's definition.

What we currently do:
{{describe interview cadence, who runs interviews, what artifact tracks discovery, how often it updates}}

Please apply Torres's 4 diagnostic questions:
1. Is the interview happening THIS week (and next, and the week after)?
2. Is the FULL trio (PM + designer + engineer) in it?
3. Was it a STORY-BASED interview (grounded in a specific past instance) or a "chat with the user"?
4. Did it UPDATE the Opportunity Solution Tree (or equivalent living artifact)?

If any answer is no, name the gap.
If multiple answers are no, we don't do continuous discovery — we do something else (project-based, PM-solo, ad hoc, or theater). Name which pattern.

Then:
- Propose the smallest first change to close the biggest gap.
- Warn about the 2 most common adoption slips (usually cadence slippage after week 4, and PM-solo drift).
- Cite Torres's canonical definition of continuous discovery.

Tone: warm about the humans, strict about the rules. This is a diagnostic, not a judgment.
```

## Reframe "opportunities" that are features in disguise

```
Here's our current opportunity list. Please audit it against Teresa Torres's opportunity-vs-solution test.

Current "opportunities":
{{paste list}}

For each item, apply Torres's test: "Is there more than one way to address this?"

- If YES → it's a real opportunity. Keep it as-is.
- If NO → it's a solution disguised as an opportunity. Rewrite it:
  - Move the current item to Layer 3 (solutions) of the OST.
  - Put the underlying customer need / pain point / desire in Layer 2 (opportunities).
  - Force the team to name at least 2 other candidate solutions for that opportunity.

Example the assistant should follow:
- ❌ "Customers can fast-forward through commercials" (solution)
- ✅ "Customers don't like commercials" (opportunity) — with solutions: fast-forward, skip button, ad-free tier, shorter ads

Then: for each real opportunity, note whether we have interview evidence supporting it (which interview, what quote) or whether it's team speculation. If speculation, flag it — Torres's rule: opportunities come from customer interviews, not team brainstorming.

Cite the Opportunity Solution Trees canonical essay.
```

## Position Torres's method vs an adjacent framework

```
I'm trying to decide whether to use Teresa Torres's Continuous Discovery Habits or {{Cagan's Product Operating Model / Perri's Escaping the Build Trap / Lean Startup / JTBD / OKRs alone}} for {{my situation}}.

Help me pick. If the answer is "use both, in this composition", tell me the composition. If the answer is "neither, use something else entirely", tell me that too.

Guardrail: don't collapse Torres's method into any of the others. Torres explicitly composes with Cagan (one altitude below), with Perri (adjacent scaffolding), with JTBD (compatible substance, methodology-agnostic language), and with Lean Startup (foundational, MVP redefined). She refuses to be turned into a rigid recipe or paired with any one framework as doctrine.
```

## Coach the trio dynamic (kill the PM-solo pattern)

```
On our team, the PM does all the customer interviews and reports back to the rest of the team. Our "designer" and "engineer" see only summaries. Help me fix this using Teresa Torres's product trio approach.

Context:
- Why it currently works this way: {{describe — usually scheduling, seniority, or "the engineer is too busy"}}
- What the team resists most about changing it: {{honest read}}

Please:
1. Name why PM-solo discovery breaks Torres's method (loses trio's shared context; engineer never hears the customer; designer's assumptions never get exposed live).
2. Propose the minimum first change — get the designer into ONE interview this week. Not all interviews. Not a formal reorg. One.
3. Rotate the interview lead across weeks so all three build the muscle.
4. Warn about the "spectator trio" pattern — trio in the room but only PM asks questions.
5. Cite Torres on trio-based discovery — Product Talk essays + book chapter.

Tone: acknowledge the practical constraints (engineers are busy, designers have 3 projects) while holding the line that the trio is non-optional.
```

## Handle "should we use AI to replace discovery?"

```
Someone at our company is arguing we can use AI to synthesize customer needs instead of running weekly interviews. Help me respond using Teresa Torres's frame.

Context:
- Who's making the argument (exec / eng / other): {{describe}}
- The specific proposal (AI on support tickets, AI-generated personas, LLM interview simulation, etc.): {{describe}}

Please:
1. Distinguish what AI CAN accelerate in the discovery loop (evals, prototyping, prompt design, coaching, transcript synthesis) from what AI CANNOT replace (actual customer contact, watching a real person struggle with your product, hearing an unexpected story).
2. Apply Torres's load-bearing frame: AI accelerates the trio; AI does not replace the customer conversation.
3. Reference the Interview Coach case — Torres eats her own dog food on AI + product, but the AI COACHES the practice, it doesn't replace it.
4. Name what specifically would go wrong if we replaced weekly interviews with AI-generated personas (the assumption never gets tested against a real customer; the opportunity space stops being grounded in evidence; the tree becomes internal projection, not discovery).
5. Propose the compromise — use AI to accelerate specific parts of the loop; keep the weekly customer conversation as non-negotiable.
6. Cite Torres's Interview Coach evals essay + her 2025-2026 LinkedIn commentary.
```

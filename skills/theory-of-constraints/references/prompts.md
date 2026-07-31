# Theory of Constraints — Invocation Prompts

> Templates for the most common ways a user brings a TOC-shaped problem. Each has the shape of a task the assistant can execute end-to-end, in Jonah's or Goldratt's voice.

## Diagnose a bottleneck

**User frame:** "I think we have a bottleneck. Help me figure out where it is."

**Assistant flow:**
1. Ask: what is the Goal of this system? (Refuse to move on until named in one sentence.)
2. Ask: what does the system produce, and how is Throughput measured today?
3. Ask: where does WIP pile up? Where do people wait? What decisions have queues?
4. Propose a constraint candidate. Test it: if this were relieved, would system-level Throughput go up? If not, keep looking.
5. Classify the constraint: physical capacity / market / policy / supplier.
6. Route to the right layer: physical → Layer B (DBR or CCPM); policy/conflict → Layer C.
7. Warn about inertia and the elevation trap before proposing tactics.

## Run a Current Reality Tree

**User frame:** "We have all these problems and I don't know where to start."

**Assistant flow:**
1. Elicit the list of Undesirable Effects — the concrete "these things are wrong" complaints. Aim for 5–10.
2. For each UDE, ask "why does this happen?" — write the cause as a node connected by an arrow.
3. Continue backward until you hit nodes that don't have obvious causes (or where causes are outside the system boundary).
4. Look for **convergence** — nodes that cause multiple UDEs. These are candidates for root causes.
5. Test each root-cause candidate: if this were fixed, how many of the UDEs would disappear?
6. Name the small number (1–3) of root causes.
7. Route the highest-leverage root cause into an Evaporating Cloud (if it's a conflict) or an FRT (if it's a change proposal).

## Draw an Evaporating Cloud

**User frame:** "We've been arguing about X for months. Help me resolve it."

**Assistant flow:**
1. Ask: what is the common objective both sides agree on? (Box **A**.)
2. Ask: what is the need each side is trying to satisfy? (Boxes **B** and **C**.)
3. Ask: what action or condition does each side want? (Boxes **D** and **D'**.)
4. Read the Cloud back: "In order to achieve A, we must satisfy B; in order to satisfy B, we must have D. In order to achieve A, we must also satisfy C; in order to satisfy C, we must have D' — which conflicts with D."
5. Surface assumptions on each arrow: why does B require D specifically? Why does C require D' specifically? Why do D and D' actually conflict?
6. Invalidate the weakest assumption. Propose an **injection** — a new action that satisfies both B and C without the D/D' conflict.
7. Test the injection with a Future Reality Tree — trace forward, flag Negative Branches, prune before implementing.

## Plan a project with CCPM

**User frame:** "We have a hard deadline and my project keeps slipping. Help me plan it differently."

**Assistant flow:**
1. Get the task list with dependencies and per-task estimates.
2. Cut each estimate to ~50% probability (the "median" without padding).
3. Identify the **Critical Chain** — the longest sequence of **resource-constrained** dependent tasks. Not just the longest dependency chain.
4. Aggregate the removed safety into a **Project Buffer** at the end of the Critical Chain.
5. Place **Feeding Buffers** where non-critical paths merge into the Chain.
6. Place **Resource Buffers** as early-warning signals for critical resources.
7. Kill multitasking — sequence per-resource, one task at a time.
8. Set up buffer-consumption tracking: Chain progress vs. Buffer consumption. Chain 50%/Buffer 80% = red.
9. Warn about Student Syndrome (don't defer start) and Parkinson's Law (report early finishes forward).

## Translate DORA into TOC

**User frame:** user is running a software delivery team and wants to understand the DORA/TOC connection.

**Assistant flow:**
1. Name the mapping: DORA measures ARE TOC measures for software.
   - Deployment Frequency + Lead Time = Throughput.
   - Change Failure Rate + Recovery Time = Stability of the flow.
2. Reframe the DORA capabilities as TOC levers:
   - Trunk-Based Development, Small Batches → Exploit-and-Subordinate at the delivery pipeline constraint.
   - Test Automation, CI → protect the constraint from defective work.
   - Loose Coupling, Documentation → subordinate non-constraint teams so they can move without blocking the constraint team.
3. If the user is in a Phoenix-Project shaped situation (all changes routed through one senior engineer, everyone at 100% utilization, deploys stuck), diagnose it as a classic TOC bottleneck — cite Brent / NCX-10.
4. Cross-link **[[dora-accelerate]]** for the specific measurement stack.

## Push back on "everyone at 100% utilization"

**User frame:** a manager wants to push utilization to 100% across the team.

**Assistant flow:**
1. Ask: which resource on this team is the constraint of the overall delivery pipeline?
2. Explain: if the constraint is at 100% and the non-constraints are also at 100%, they are producing WIP the constraint cannot consume. This surfaces as pileups or defective work reaching the constraint.
3. Cite: **activation ≠ utilization** (Goldratt). Activation feels productive; utilization requires the activity to move the system toward the Goal.
4. Propose: instrument the constraint's utilization, not the non-constraints'. Non-constraints should have idle time. That idle time is a feature.
5. Redirect: if the goal is "we need more Throughput," run the Five Focusing Steps starting with Identify — because "more utilization everywhere" is the wrong lever.

## Diagnose why a Six Sigma / Lean / Agile initiative stalled

**User frame:** "We ran Six Sigma / Lean / Agile and the top-line numbers didn't move. Why?"

**Assistant flow:**
1. Ask: did the initiative target the constraint, or was it applied everywhere?
2. Almost always the answer is "everywhere" or "the loudest problem." Explain: work at non-constraints does not move Throughput. The bottom line only moves when the constraint moves.
3. Propose: run the Five Focusing Steps to identify the actual constraint. Then compose the initiative's tools at the constraint (Six Sigma variation reduction at the constraint; Lean waste removal at the constraint; Agile ceremonies aligned to the constraint's needs).
4. Cite: local optima do not sum to a global optimum (Goldratt).

## Convert cost-accounting thinking into Throughput thinking

**User frame:** the user is defending a cost-accounting decision (killing a "low-margin" product, cutting a "high-cost" resource) and the assistant needs to introduce Throughput Accounting.

**Assistant flow:**
1. Restate the decision in cost-accounting terms: "you're proposing to X because the cost accounting says Y."
2. Test in Throughput terms:
   - Does the "low-margin" product consume constraint time? If not, it produces T at ~zero incremental OE — keep it.
   - Does the "high-cost" resource sit at the constraint? If yes, its "cost" is the wrong metric; its T-per-constraint-hour is the metric that matters.
3. Cite: "There is no such thing as product profit or product cost. Prices are determined by customers' perception of value." (Goldratt.)
4. Warn about running both accounting systems in parallel: they answer opposite questions. For this decision, use Throughput Accounting.

## Full session — TOC diagnosis of a stalled improvement effort

**User frame:** the user has been running improvement initiatives for a year and results haven't moved. They want a full TOC pass.

**Assistant flow:**
1. **Layer A:** name the Goal. Audit the current metrics against T/I/OE. Retire the ones that measure cost-accounting artifacts.
2. **Layer B — Identify:** where's the constraint? Physical, market, policy, supplier?
3. **Layer B — Exploit:** is the constraint at 100% *useful* utilization? What's stealing constraint time (setup, defects, meetings, idle waits)?
4. **Layer B — Subordinate:** are non-constraints running at their own local optima? Are their incentives shaped around that?
5. **Layer B — Elevate:** what would it cost to add capacity at the constraint? (Compute *after* Exploit and Subordinate reveal the gap.)
6. **Layer C** (if the constraint is a policy or a conflict): run the Thinking Processes — CRT for the UDE list, Cloud for the stuck conflict, FRT for the proposed injection.
7. **Inertia audit:** what rules were built around old constraints and still run?
8. **Report:** name the constraint, the exploit-subordinate-elevate sequence, the policy audit, and the expected T movement. Warn about the next constraint.

## Fast on-ramp — user is TOC-curious but hasn't read anything

**User frame:** "I've heard about *The Goal* — give me the TL;DR."

**Assistant flow (short — do NOT run the full skill):**
1. Point at *The Goal* (2004 revised edition) — https://northriverpress.com/
2. Four canonical concepts in one paragraph:
   - The Goal of a for-profit business is to make money.
   - Measure it as Throughput (money in from sales), Inventory (money invested in things to sell), Operating Expense (money spent turning I into T). Increase T, decrease I, decrease OE — together.
   - Every system has one constraint at a time. Global Throughput = constraint Throughput.
   - Five Focusing Steps: Identify → Exploit → Subordinate → Elevate → Repeat (without letting inertia keep the old rules).
3. Note: three layers, not one. Read the book for Layer C (Thinking Processes) and DBR/CCPM.
4. If the user is in software: also mention *The Phoenix Project* as the IT translation.

## When NOT to run the skill

- User's real question is product discovery, PMF search, or "what should we build" → point at JTBD, Continuous Discovery, Pattern Breakers.
- User's real question is strategy at company / market level → point at Playing to Win, 7 Powers, Rumelt.
- User has a 3-person team and a to-do list → don't apply TOC; suggest a simple prioritization method.
- User wants a full *Goal* summary → give the short on-ramp above and stop.

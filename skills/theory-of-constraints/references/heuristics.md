# Theory of Constraints — Heuristics, Do's, Don'ts, Gotchas

> The practical devices — Goldratt's "how to actually apply this" — with attribution. What he pushed back on in *The Goal*, what Efrat carries forward, what Kim/Ching/Tendon add for knowledge work.

## Do's

### Name the Goal before naming a metric

Every metric proposed must be tested against "does this move us toward the Goal?" If you can't answer, the metric is measuring the wrong thing. This is the Jonah opening move; imitate it.

**Author's words:**
> "Productivity is meaningless unless you know what your goal is."
> — Goldratt

### Instrument the constraint, not the line

Drum-Buffer-Rope needs three instrumented points (Drum, buffer origin, Rope release). Kanban systems instrument every workstation. Fewer instrumented points = clearer signal, less noise. Applied to project work: instrument the Critical Chain's buffer consumption, not every task's percentage-complete.

### Buffer time, not inventory

Buffers protect the constraint from upstream variability. Inventory piled in front of the constraint is not a buffer — it's a symptom of upstream failing to subordinate. Time buffers absorb variability without adding I.

### Exploit before you elevate

Steps 2 and 3 (Exploit + Subordinate) are free. Step 4 (Elevate) costs money. Managers reflexively jump to Step 4 because it looks like action. Most systems have 20–50% latent capacity in Steps 2–3 that gets ignored. Always run Exploit + Subordinate first — the free capacity often removes the need to spend.

### Cut the padded estimate and pool the safety (CCPM)

Take each task estimate, cut it roughly in half, pool the aggregated safety into a Project Buffer. Individual overruns are absorbed by the shared buffer. The project completes faster than the sum of the safe estimates because statistical variation cancels across the pool.

### Attack multitasking before adding capacity

The single-highest-leverage move in most CCPM implementations. A resource doing three things "in parallel" finishes all three later than doing them sequentially. Sequence the work.

**Author's words:**
> "Focusing on everything is synonymous with not focusing on anything."
> — Goldratt

### When the constraint moves, question every rule

After elevating, the org still runs the old rules. This is where TOC implementations die — the visible constraint moves but the *policy constraint* (the rule shaped around the old bottleneck) becomes the new limit. Every elevation triggers a "what rule are we still running that assumes the old constraint?" audit.

### Use the Cloud on stuck disagreements

Compromise loses; dissolution wins. Every stuck two-sided conflict rests on an assumption. Find it. Invalidate it. Both sides now agree without either giving up their need.

**Author's words (Goldratt's axioms of *The Choice*):**
> "One, people are good. Two, every conflict can be removed. Three, every situation, no matter how complex it initially looks, is exceedingly simple."
> — Goldratt, *The Choice*

### Start every diagnosis with "what is the Goal of this system?"

If the user can't state the Goal in one sentence, everything downstream is guessing. Refuse to move on until the Goal is on the table. This is the Jonah move; imitate it verbatim.

### Cite the source

TOC is 40+ years old and often bastardized. When you invoke a piece of the framework, name where it came from — *The Goal* Ch. 8, *Critical Chain*, Satellite Program module, TOCICO 2023 paper, Kim's Three Ways, Ching's FOCCCUS Formula. The citation grounds the invocation.

## Don'ts

### Don't try to keep every resource busy

"A worker sitting idle" is only a problem if that worker is the constraint. Non-constraint workers *should* have idle time. Otherwise they produce WIP in front of the constraint (increasing I) or push defective work into the constraint (destroying T).

**Author's words:**
> "'Utilizing' a resource means making use of the resource in a way that moves the system toward the goal."
> — Goldratt, *The Goal*

Activation ≠ utilization. Activation feels productive; utilization actually is.

### Don't measure productivity as units produced

Units in the warehouse are Inventory, not Throughput. Throughput requires the *sale*. This is the mistake that made UniCo look profitable while going bankrupt in *The Goal*.

### Don't push work into the plant early

The Rope releases material only when the Drum needs it. Pushing early creates WIP that hides the actual constraint and delays true signals. In software: don't start work items before the downstream capacity is ready to consume them — the started-not-done pile becomes invisible I.

### Don't skip the Thinking Processes for a policy constraint

If the bottleneck is a rule, buying a machine won't fix it. If the bottleneck is a conflict, adding staff won't fix it. Match the tool to the type of constraint. Reaching for DBR on a policy constraint is the classic misdiagnosis.

### Don't run cost accounting alongside Throughput Accounting for the same decision

The two answer opposite questions. Product-cost thinking will always resist obvious Throughput moves (accepting an "unprofitable" order that fills constraint time and generates real margin; discontinuing a "profitable" product that steals constraint time from higher-T alternatives). Pick one, and for TOC decisions, it must be Throughput Accounting.

### Don't confuse activation with utilization

A resource can be activated (running, doing something) without being utilized (moving the system toward the Goal). The distinction is doctrinal — Goldratt returns to it in every book. When a manager reports "we're at 98% utilization" on a non-constraint, that's activation; the utilization is 0%.

### Don't treat "the market" as the constraint too fast

When capacity is idle, managers reflexively say "we need more sales." Sometimes true; often the internal constraint is a policy that keeps sales *unable* to be closed (long lead times, inflexible offers, credit terms, minimum order sizes). Test both.

### Don't sell DBR to a software team as-is

Software delivery is closer to a project pipeline than a manufacturing line. Reach for CCPM + TOC-adapted flow (Kim's Three Ways, Ching's Bottleneck Rules, Tendon's TameFlow) rather than force-fit DBR. Cross-link to **[[dora-accelerate]]** — DORA's four keys are Throughput measures for software.

### Don't reduce TOC to "find the bottleneck"

Three layers (Goal + measurements / Five Focusing Steps / Thinking Processes). Any output that only touches Layer B has lost the point. Any output that only touches Step 1 of Layer B has lost 95% of the point.

## Gotchas — the classic misreads

### "TOC = find the bottleneck" (the most common gutting)

TOC is Goal + Measurements + Five Focusing Steps + DBR/CCPM + Thinking Processes. The one-line summary loses 90% of the method. Users who "know TOC" from a blog post usually have the one-liner and none of the layers. Rebuild the layers before diagnosing anything.

### Confusing constraint with problem

Every organization has 100 problems; it has (approximately) one constraint. The constraint is the one whose relief moves the system forward. The rest are noise until the constraint is handled. Users who list five "equally important bottlenecks" haven't identified the constraint yet.

### The elevated constraint that no one notices moved

Elevated + old-rules-still-running = the classic stall. Symptom: the improvement initiative worked, but the numbers didn't move. Diagnosis: the constraint moved to a new resource, and the old policies (still shaped around the old constraint) are now the limit.

### Assuming the constraint is inside the plant

It might be a customer, a supplier, a regulator, or a policy of your own making. Look outside the walls. In services and knowledge work, the constraint is often a decision-maker's calendar or a hand-off between departments.

### Statistical fluctuations misunderstood

A "balanced line" (every station rated for equal capacity) doesn't stabilize; it stalls. Because normal statistical variation stacks with dependent events. Goldratt's dice-game chapter (Ch. 14 of *The Goal*) is the entire proof. Any manager arguing for perfect line balance hasn't understood the dice game — send them there.

### Efficiency reporting as management theatre

Reporting 98% utilization of non-constraint resources feels like management doing its job. It is producing inventory the constraint can't process, hiding the real problem, and adding OE. Efficiency-everywhere is a bug, not a feature.

### The "five bottlenecks" list

Users often present a list of "five things that are slowing us down." That's a list of Undesirable Effects (UDEs), not five constraints. Run a Current Reality Tree — the five UDEs will usually collapse to 1–3 root causes.

### CCPM applied without killing multitasking

Cutting estimates and adding buffers without also killing multitasking produces a slower project than CPM did. The buffer gets consumed by context-switch losses. Multitasking removal is not optional; it is the load-bearing move.

### Elevating capacity without redesigning incentives

The plant now has a bigger constraint. But the incentive system still rewards local efficiency, individual output, department-level metrics. The elevated capacity gets absorbed by non-constraints running faster; the constraint remains constrained by the old policy. Redesigning incentives is part of subordination — not a separate HR project.

### Treating throughput and inventory as opposites

The intuition is "reducing inventory means reducing throughput." False. Reducing WIP means faster cycle time, faster feedback, less rework, more T. Correctly-run TOC reduces I *and* increases T simultaneously. This is Goldratt's echo of what Lean says about pull systems, from a different angle.

### Skipping Layer A because "we already have KPIs"

The existing KPIs are almost always cost-accounting KPIs. That is exactly the problem TOC is designed to fix. Do not diagnose constraints while the measurement system is still driving behavior away from the Goal. Fix the measurements first, or run TOC alongside them and watch the two answer contradictory questions.

### "The Thinking Processes are too abstract"

Managers under time pressure resist the trees ("we don't have time to diagram this"). The counter: the alternative is another six months of the same recurring problem. The 4-hour Cloud session that dissolves a two-year interdepartmental conflict is not overhead; it's the highest-leverage 4 hours the org can spend. Efrat's *The Choice* makes this argument explicitly.

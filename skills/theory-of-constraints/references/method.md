# Theory of Constraints — Method

> The canonical description of Goldratt's method in three interlocking layers. Fidelity is the point — reducing TOC to "find the bottleneck" loses 90% of the framework. Every claim here is traceable to *The Goal*, a later Goldratt novel, the Satellite Program, or a named post-Goldratt steward.

## Core insight (the finding of *The Goal*)

> "The performance of a system is determined by its bottleneck, not by the efficiency of its individual components."

Every system with dependent steps and statistical variation has a single limiting factor at any moment in time — its constraint. Global throughput equals the throughput of that constraint. Optimizing anywhere else destroys global performance. Any framing of "we need every resource at 100% utilization" or "we need to balance the line" is wrong at the level of the arithmetic.

This is not an opinion; it is the geometry of the system. Goldratt's dice-game chapter in *The Goal* is the proof: even a perfectly "balanced" line of five stations, each averaging four units/hour, produces less than four units/hour because normal statistical fluctuations stack across dependent events.

---

## Layer A — The Goal and Throughput Accounting

Before any metric, any tactic, any recommendation, name **the Goal**.

### The Goal

In *The Goal*, Jonah refuses to discuss anything until Alex Rogo can state it. Alex circles through "efficiency," "productivity," "shipping product," "quality" — all rejected. The Goal, for a for-profit business, is:

> "To make money by increasing net profit, while simultaneously increasing return on investment, and simultaneously increasing cash flow."
> — Goldratt, *The Goal*

For a non-profit or a system with a different mandate, name that Goal explicitly. Every downstream decision is tested against it.

### The three measurements

Traditional cost accounting measures product cost, direct labor, overhead absorption. Goldratt argued these systematically drive decisions *away* from the Goal. **Throughput Accounting** replaces them with three measurements:

- **Throughput (T)** — "the rate at which the system generates money through sales." Not units produced. Not deployments shipped. Not features written. *Sales.* A finished good sitting in the warehouse has zero throughput.
- **Inventory (I)** — "all the money the system has invested in purchasing things it intends to sell." Raw materials, WIP, finished goods, equipment, facilities. Everything the system bought.
- **Operating Expense (OE)** — "all the money the system spends turning Inventory into Throughput." Labor, overhead, utilities.

### The imperative

**Increase T. Decrease I. Decrease OE.** In that priority order — Throughput is unbounded; Inventory and OE have floors.

The measurements interact:
- **Net Profit = T − OE**
- **Return on Investment = (T − OE) / I**
- **Productivity = T / OE**
- **Turns = T / I**

### Why this replaces cost accounting

Cost accounting allocates OE across products via absorption. This creates artifacts:
- A product looks "unprofitable" because its allocated overhead exceeds its margin, and gets discontinued — even though its true contribution to T is positive and it fills constraint time that would otherwise be idle.
- A product looks "profitable" but consumes constraint time other products need — its opportunity cost in lost T is invisible to cost accounting.
- A "productivity improvement" at a non-constraint gets rewarded even though it produces WIP the constraint can't process, increasing I with zero T movement.

**Do not run cost accounting and Throughput Accounting in parallel on the same decision.** They answer opposite questions. Pick one for the decision, and for TOC decisions, it must be Throughput Accounting.

### Signature quote

> "Tell me how you measure me and I will tell you how I will behave."
> — Goldratt

The measurement is the leverage. Change the measurement, the behavior changes downstream. This is why Throughput Accounting is a *replacement*, not a supplement.

---

## Layer B — The Five Focusing Steps (POOGI)

**POOGI = Process Of Ongoing Improvement.** The operating loop.

From the canonical wording:

**1. Identify the system's constraint(s).**
The constraint is where demand meets or exceeds capacity. It's the resource whose throughput determines the system's throughput. Not the loudest problem. Not the resource with the most complaints. The actual bottleneck.

Types of constraint:
- **Internal capacity** — a machine, a person, a team, a decision-making step.
- **Market** — demand is less than capacity; the system could produce more if there were buyers.
- **Policy** — a rule the org invented (batch sizes, approval steps, resource allocations) that limits flow even though physical capacity exists.
- **Supplier / external** — a vendor, regulator, or upstream dependency limits input.

Signs of an internal constraint: WIP piled up in front of it; downstream resources idle waiting; overtime concentrated on it; expediting to make it work faster.

**2. Decide how to exploit the system's constraint.**
Before spending a dollar, squeeze every drop out of the current constraint.
- The constraint never idle — no lunch break, no meetings, no setup during peak.
- No defective input reaching the constraint — quality-inspect *before* the bottleneck.
- No wasted constraint time on things a non-constraint could do.
- Prioritize work that produces the highest T-per-constraint-minute.

This step is free. It's also usually 20–50% latent capacity.

**3. Subordinate everything else to the above decision.**
Every non-constraint operates at the pace of the constraint, not at its own local optimum.
- Non-constraints have idle time. This is correct. Do not let managers report it as a problem.
- Non-constraint resources produce exactly what the constraint can consume — no more.
- Rewards, targets, and reporting for non-constraints must be redesigned around subordination, not around local efficiency.

This is the counterintuitive core: **running a non-constraint at 100% is a bug.** It produces WIP the constraint can't process (increasing I) or defective work that reaches the constraint (destroying T).

**4. Elevate the system's constraint.**
Only now do you spend money. Add capacity: hire, buy equipment, invest, outsource. Elevation is the expensive step; it must come *after* exploitation and subordination or you're buying capacity you already had.

**5. Warning! If in the previous steps a constraint has been broken, go back to step 1 — but do not allow inertia to cause a system's constraint.**

The moment you elevate one constraint, another becomes the constraint. Two failure modes:
- **Missing the move** — the new constraint is unseen; the system stalls without anyone noticing.
- **Inertia** — the org's rules, incentives, and processes are still shaped around the *old* constraint. The visible constraint moved; the policy constraint remains.

Every elevation triggers a rule audit: what practices did we invent to accommodate the old bottleneck? Are any of them the new limit?

---

## Layer B applied to production — Drum-Buffer-Rope (DBR)

TOC's manufacturing scheduling method. Three roles.

- **Drum** — the pace of the constraint. Nothing in the plant runs faster than this. The Drum is the master schedule.
- **Buffer** — a *time* buffer (not an inventory pile) in front of the constraint. Buffers are managed by color:
  - **Red** — buffer nearly consumed; constraint at risk of starvation. Act now.
  - **Yellow** — watch.
  - **Green** — safe.
- **Rope** — the mechanism that releases raw material into the plant only *when the Drum needs it*, buffer time in advance. Not before. The Rope pulls; material doesn't push.

### Instrumentation

DBR instruments only three points:
1. The Drum (the constraint).
2. The origin of the buffer (input to the constraint).
3. The Rope release (material entry into the plant).

Compare to Lean's kanban (every station) and MRP's push (every workstation on a schedule). Fewer instrumented points = clearer signal, less noise.

### Simplified DBR (S-DBR)

A less-complex variant developed post-Goldratt. Used when the plant has one clear internal constraint and the market is a soft constraint. Reduces buffer management and consolidates the Rope. Widely used in job-shop and small-plant contexts.

### When DBR fits, when it doesn't

- **Fits:** manufacturing, physical assembly lines, warehouse operations, physical distribution.
- **Doesn't fit as-is:** knowledge work, software delivery, project-based work (see CCPM below), service organizations (better addressed by TOC-adapted flow / TameFlow).

---

## Layer B applied to projects — Critical Chain Project Management (CCPM)

TOC's project methodology, introduced in *Critical Chain* (1997). Key differences from Critical Path Method (CPM):

### Cutting estimates, pooling safety

CPM estimates each task with padding baked in (managers add safety to protect their task's on-time delivery). Under Parkinson's Law, that padding gets consumed; the task finishes at the estimate regardless.

CCPM's move:
1. Estimate each task at aggressive (~50% probability) duration — the "median" estimate without padding.
2. Aggregate the removed safety into shared **buffers**.

The aggregated buffer is smaller than the sum of individual safeties because statistical variation cancels: some tasks overrun, others under-run, and the pooled buffer absorbs the net.

### The Critical Chain

The **Critical Chain** is the longest sequence of **resource-constrained** dependent tasks. Not the longest sequence of dependencies (that's the Critical Path). Resource contention is a first-class concern; two tasks that need the same resource cannot be scheduled in parallel even if their dependencies allow it.

### The three buffer types

- **Project Buffer** — a single time buffer at the end of the Critical Chain, protecting the project completion date.
- **Feeding Buffers** — placed where non-critical paths merge into the Critical Chain, protecting the Chain from feeder delays.
- **Resource Buffers** — early-warning signals that a resource needs to be ready when the Critical Chain calls for it.

### Buffer management

The project's health is read as **buffer consumption vs. progress on the chain**. A dashboard shows:
- Chain progress (% complete).
- Project Buffer consumption (% used).

If Chain 50% done and Buffer 80% consumed → alarm (red). If Chain 80% done and Buffer 40% consumed → healthy (green).

### What CCPM diagnoses that CPM misses

- **Student Syndrome** — team members don't start until the deadline is close. Safety in the estimate is consumed before real work begins. Once behind, no recovery.
- **Parkinson's Law** — work expands to fill the time available. Even early finishes are held (nobody wants to look like they under-estimated).
- **Multitasking** — the single largest productivity killer in CCPM's analysis. A resource split across three parallel tasks finishes all three later than doing them sequentially. Sequence the work.

### Efrat's extension — *Goldratt's Rules of Flow* (2023)

Applies CCPM logic to **multi-project environments** — engineering, digital transformation, product organizations running many parallel initiatives. Central claim: the constraint in multi-project settings is usually a shared resource type (senior architects, integration engineers, decision-makers). Sequencing the initiative flow against the constrained resource type dramatically increases throughput.

---

## Layer C — The Thinking Processes (for policy / belief / conflict constraints)

Five logical tools for when the constraint isn't a machine. When you can't just add capacity to fix it, because the constraint is a rule, a belief, a conflict, or a habit.

Two logic types:
- **Sufficient Cause (SC)** — "If X, then Y." Used in the trees (CRT, FRT, PRT partially, TRT).
- **Necessary Condition (NC)** — "In order to X, we must have Y." Used in the Evaporating Cloud.

The five tools answer three sequential questions:

### What to change?

**Current Reality Tree (CRT)**
- Purpose: identify the root cause(s) beneath a list of Undesirable Effects (UDEs).
- Input: a list of UDEs — the concrete "these things are wrong" complaints from the system.
- Method: work backward from each UDE via cause-and-effect. Cluster. Look for the small number (usually 1–3) of root causes that generate most of the UDEs.
- Output: the root cause(s). This is what to change.
- Common failure: treating a symptom as a root cause. If your "root" is another effect, keep going backward.

### What to change to?

**Evaporating Cloud (EC / Conflict Cloud)**
- Purpose: dissolve a stuck conflict rather than compromise.
- Structure: a five-box diagram.
  - **A** — the common objective both sides agree on.
  - **B** — the need one side is trying to satisfy.
  - **C** — the need the other side is trying to satisfy.
  - **D** — the action or condition one side wants.
  - **D'** — the opposing action or condition the other side wants.
  - Reading: "In order to achieve A, we must satisfy B; in order to satisfy B, we must have D. In order to achieve A, we must also satisfy C; in order to satisfy C, we must have D' (which conflicts with D)."
- Method: surface the assumptions on each arrow (why does B require D? why does C require D'? why do D and D' conflict?). Invalidate the assumption; the conflict evaporates — both sides get their need without either giving up.
- Output: an **injection** — a new action or condition that satisfies both B and C without the D/D' conflict.

**Future Reality Tree (FRT)**
- Purpose: trace the injection forward to show the desired future state, and to flag Negative Branches (bad side effects) so they can be pruned.
- Method: from the injection, use Sufficient Cause logic to build the tree of consequences. Where an unintended negative effect appears (a **Negative Branch**), define a supplementary injection to prune it before implementation.
- Output: a validated future state with negative branches pruned.

### How to cause the change?

**Prerequisite Tree (PRT)**
- Purpose: map the obstacles between now and the desired future state; define intermediate objectives that would overcome each obstacle.
- Method: list obstacles. For each obstacle, define an intermediate objective (IO) whose achievement removes the obstacle. Sequence IOs by dependency.
- Output: an ordered set of IOs — the milestones that make the future state reachable.

**Transition Tree (TRT)**
- Purpose: the ordered action plan connecting where you are to each intermediate objective.
- Structure: at each step, name the specific **need**, the **action** that satisfies it, and the expected **result**.
- Output: the executable plan.

### When to reach for the Thinking Processes vs. DBR/CCPM

- **Physical/capacity constraint** → Layer B (DBR or CCPM). Buying a machine, adding staff, sequencing work.
- **Policy / belief / conflict constraint** → Layer C. The constraint is a rule, an assumption, or a stuck disagreement. No amount of physical capacity fixes it.

The most common misdiagnosis is reaching for Layer B on a Layer C constraint. Symptoms: elevation cycles that don't move the numbers, the same problems recurring after every improvement initiative, cross-department blame loops. If Layer B has been run twice and nothing moved, the constraint is probably in Layer C.

---

## Sequence of application

1. **Name the Goal.** Explicit. One sentence.
2. **Establish the three measurements.** Test the current metrics against T/I/OE. Retire metrics that don't move the Goal.
3. **Identify the constraint.** Physical or policy? Internal or external?
4. **Match the layer.** Physical → DBR (production) or CCPM (projects). Policy/conflict → Thinking Processes (CRT → EC → FRT → PRT → TRT).
5. **Run the Five Focusing Steps.** Exploit before elevating. Subordinate everything else, including the incentives.
6. **Watch for inertia after elevation.** Rule audit. The old constraint's rules will still be running.
7. **Iterate.** POOGI is ongoing. The next quarter's constraint is different from this quarter's.

---

## What this method is NOT

- **Not "find the bottleneck."** That's one step of one layer. Three layers, all necessary.
- **Not compatible with cost-accounting-driven decisions.** Throughput Accounting replaces; it does not supplement.
- **Not for individual performance evaluation.** Local optimization of individuals destroys global throughput. Same warning as DORA on this point — different domain, same arithmetic.
- **Not a substitute for product discovery.** TOC optimizes the delivery of value; it does not tell you which value to deliver.
- **Not for tiny teams.** TOC needs dependent steps + statistical variation. A 2-person team's work is a to-do list, not a system.
- **Not "TOC vs. Lean" as either/or.** Many practitioners combine them (Marris Consulting: "TOC to prioritize which Lean improvement to sequence first").

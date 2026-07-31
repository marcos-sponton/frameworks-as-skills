# Theory of Constraints — Applications and Adjacent Frameworks

> When TOC fits, when it doesn't, and which framework to reach for in each case. Especially important because TOC has a strong pull — "find the bottleneck" sounds universally applicable, but the method needs specific preconditions to produce signal.

## When TOC fits

### Preconditions

TOC needs three things to work:
1. **Dependent steps** — the output flows through a sequence where each step depends on prior steps.
2. **Statistical variation** — the steps don't produce identically every cycle; there's real variance.
3. **A definable Goal** — the system has a clear objective throughput can be measured against.

Systems that satisfy all three: production lines, project pipelines, service organizations with defined workflows, healthcare patient flow, distribution/replenishment systems, software delivery pipelines.

### Best fits by domain

- **Manufacturing** (canonical fit — *The Goal*).
- **Physical distribution and warehousing.**
- **Retail replenishment** — *Isn't It Obvious?* + Ptak's DDMRP.
- **Project management with hard deadlines** — CCPM, especially when multitasking is destroying delivery.
- **Multi-project portfolios** — Efrat's *Goldratt's Rules of Flow*.
- **Software delivery** — through Kim's translation (*The Phoenix Project*, DORA); DBR does not fit as-is.
- **Healthcare patient flow** — well-documented sector.
- **ERP / enterprise software implementations** — *Necessary But Not Sufficient*.

## When TOC does NOT fit

### Product discovery / PMF search

TOC optimizes the delivery of value; it does not tell you which value to deliver. If the user is doing customer discovery, JTBD interviews, PMF search, feature prioritization based on demand signal — reach for:
- **Continuous Discovery Habits** (Teresa Torres)
- **JTBD** (Bob Moesta — see [[bob-moesta]])
- **Pattern Breakers** (Mike Maples — see [[pattern-breakers]])
- **Escaping the Build Trap** (Melissa Perri — see [[escaping-the-build-trap]])

TOC applied to the wrong question produces beautifully-run delivery of the wrong thing.

### High-altitude strategy

TOC operates below strategy. If the user is asking "where should we play" or "how do we win" or "what's our diagnosis at company level":
- **Playing to Win** (Roger Martin — see [[playing-to-win]])
- **7 Powers** (Hamilton Helmer — see [[7-powers]])
- **Good Strategy / Bad Strategy** (Rumelt — see [[good-strategy-bad-strategy]])
- **Strategic Narrative** (Andy Raskin — see [[strategic-narrative]])

Note the useful mapping: Rumelt's "crux" is Goldratt's constraint at strategy altitude. Use Rumelt for the strategic diagnosis, then TOC for the operational execution once the strategy is set.

### Tiny teams

TOC needs a system with dependent steps and statistical variation. A 2–5 person team's work is a to-do list, not a system. Prioritization at that scale is a to-do problem, not a TOC problem. Reach for:
- Any lightweight prioritization method (ICE, RICE, or just talking through it).
- **V2MOM** (see [[v2mom]]) for alignment.
- **Radical Focus** (John Doerr / Christina Wodtke — see [[radical-focus]]) for OKR discipline.

### External-only, structural constraints

If the bottleneck is regulatory, monopolistic supplier, or a structural market condition with no internal degrees of freedom — TOC can diagnose it but cannot move it. Name the constraint honestly, then reach for:
- Political / legal remediation (outside the framework).
- **Counter-positioning** (7 Powers) to build a business the incumbent's structure prevents them from copying.

## Adjacent frameworks — composition and comparison

### vs. Lean / Toyota Production System

**Common ground:**
- Both attack local optima.
- Both focus on flow through the system.
- Both agree "activity ≠ productivity."
- Both derive from careful observation of production systems.

**Divergences:**
- **How you attack:** Lean attacks *waste* everywhere in the system, continuously, incrementally. TOC attacks *the constraint*, treating waste elsewhere as second-order. Lean is horizontal; TOC is vertical.
- **Pull vs. drum:** Lean pulls with kanban at every station. TOC releases with a rope from a central drum. Lean instruments every workstation; TOC instruments the constraint and its buffers.
- **Balance vs. deliberate imbalance:** Lean pursues line balance. TOC argues balance is impossible (statistical fluctuations + dependent events) and pursues *deliberate imbalance* around the drum with buffers absorbing variability.
- **Speed to result:** TOC advocates argue TOC produces bottom-line results faster because effort concentrates on the one place that moves the number. Lean advocates argue Lean produces more durable results because it changes the whole system's habits.

**Composability:** Marris Consulting explicitly promotes "TOC to prioritize which Lean improvement to sequence first." A common pattern: use TOC's Five Focusing Steps to identify the constraint; use Lean tools (5S, Value Stream Mapping, Kaizen) as the *how* of Exploit and Subordinate at that constraint.

### vs. Six Sigma

Six Sigma reduces variation as its primary objective. TOC accepts variation as inherent and buffers against it. Not opposed; different primary objectives. **Six Sigma at the constraint is high-leverage; Six Sigma at a non-constraint is Sigma-project money spent producing no T improvement.** The composition rule: pick the constraint (TOC), then apply Six Sigma there.

### vs. DORA / Accelerate — see [[dora-accelerate]]

**DORA measures are TOC measures for software delivery.** Deployment Frequency + Lead Time = Throughput (in software terms). Change Failure Rate + Recovery Time = stability of the flow. The four DORA keys are the software-delivery restatement of Goldratt's *T*.

Forsgren's insight that "speed and stability are not a tradeoff" is Goldratt's insight that "increasing T, decreasing I, decreasing OE" go together — from the same set of capabilities. Both push back against the "we're slowing down to be safer" misdiagnosis, using the same underlying arithmetic.

The 30+ DORA capabilities are, in TOC vocabulary, the levers you use in Steps 2–4 (exploit / subordinate / elevate) once you've identified the delivery-pipeline constraint. Small Batches, Trunk-Based Development, Test Automation, Continuous Delivery — all are Exploit-and-Subordinate moves for a software constraint.

***The Phoenix Project* is the explicit bridge** — Kim/Behr/Spafford deliberately wrote it as *The Goal* for IT. The Three Ways are the DevOps restatement of POOGI:
- First Way — Flow → Five Focusing Steps.
- Second Way — Feedback → buffer management as diagnostic signal.
- Third Way — Continuous Experimentation → POOGI as team culture.

**When to reach for TOC over DORA:** when the software system also touches physical production, cross-functional handoffs, or when the constraint is a policy/organizational conflict rather than a delivery-pipeline capability. When to reach for DORA over TOC: when the user is specifically instrumenting delivery performance and needs the tier language and capability catalog.

### vs. Kanban (David J. Anderson)

Kanban's WIP limits are TOC's subordination (Step 3) applied to knowledge work: cap the WIP so the constraint is protected from being flooded. Anderson has written explicitly about the TOC lineage; Kanban is TOC-compatible. Combining: use Kanban's board and WIP limits as the operational implementation of TOC's subordination on a knowledge-work team.

### vs. Lean Startup (Eric Ries)

Ries's Build-Measure-Learn is a Thinking-Processes-shaped loop for product discovery:
- Identify what to change → validated learning (CRT).
- Decide what to change to → pivot (as injection tested via FRT/PRT).
- Cause the change → MVP + measurement (TRT).

Ries acknowledges Lean and TOC influence directly. The frameworks compose: Lean Startup runs the discovery loop; TOC optimizes delivery of the validated learning.

### vs. Systems Thinking (Peter Senge)

Both are systemic; TOC is more prescriptive. Senge gives archetypes (limits to growth, shifting the burden, tragedy of the commons); Goldratt gives a specific operating method (Five Focusing Steps + Thinking Processes). Complementary:
- **Senge** for framing why systems misbehave and building the systemic mental model.
- **Goldratt** for the operating manual to fix the specific system in front of you.

### vs. Playing to Win (Roger Martin) — see [[playing-to-win]]

Playing to Win answers "what strategy?" — winning aspiration, where to play, how to win, capabilities, management systems. TOC answers "given a strategy, why is execution stuck and where's the one lever?"

Composition: PtW to set the strategy; TOC to diagnose the constraint that's preventing the strategy from being executed at the intended throughput.

### vs. Rumelt's Kernel of Strategy — see [[good-strategy-bad-strategy]]

Rumelt's "the crux" is TOC's constraint at strategy altitude — the single pivotal challenge on which the whole strategy turns. Different domain (strategy vs. operations), same underlying claim about leverage: one thing matters far more than others, and pretending it doesn't is what makes strategy bad.

Composition: Rumelt to diagnose the strategic crux; TOC to run the ongoing operational improvement inside the strategy that responds to the crux.

### vs. OKRs / V2MOM / Rockefeller Habits — see [[radical-focus]], [[v2mom]]

These frameworks answer "what do we do?" (goals, aspirations, cascades). TOC answers "why does the system produce what it currently produces, and where's the one lever?" TOC precedes goal-setting — set OKRs *after* you know the constraint, or the goals will be pulled toward non-constraints and produce local optimization.

### vs. Team Topologies (Skelton & Pais)

Team Topologies designs how teams should be organized for fast flow — stream-aligned teams, platform teams, enabling teams, complicated-subsystem teams. TOC diagnoses whether the current team topology has a constraint (usually a platform-team dependency or a cross-team handoff). Composition: use Team Topologies to *design* team structure; use TOC to *diagnose* where the current structure has become the constraint.

### vs. Continuous Discovery Habits (Teresa Torres) / JTBD (Bob Moesta) — see [[bob-moesta]]

Discovery frameworks answer "what should we build?" TOC answers "given what we're building, why is our delivery of it constrained?" Complements — TOC does not do discovery, discovery does not do delivery.

## The composition patterns worth remembering

- **Rumelt (crux) → Playing to Win (cascade) → TOC (operational execution)** — for a full strategy-to-execution stack.
- **TOC (constraint identification) → Lean (waste reduction at the constraint) → Six Sigma (variation reduction at the constraint)** — for continuous improvement in production.
- **JTBD / Continuous Discovery (what to build) → DORA / TOC (how to deliver it fast and stably)** — for product organizations.
- ***The Phoenix Project* + DORA + Team Topologies** — for a DevOps / platform-engineering organization; TOC is the underlying substrate that all three assume.

## The most common misapplication

**"We need TOC because we have too many things going on."**

Not necessarily. TOC helps if the too-many-things share a single constraint (a resource, a decision-maker, a hand-off). If the too-many-things are independent (different customers, different products, different teams with no shared resources), you don't have a TOC problem — you have a prioritization / portfolio problem. Reach for Radical Focus (three top-line OKRs), a portfolio-review process, or explicit strategic choice about what to stop doing.

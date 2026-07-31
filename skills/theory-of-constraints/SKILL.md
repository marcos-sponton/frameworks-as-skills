---
name: theory-of-constraints
description: Apply Eliyahu Goldratt's Theory of Constraints (TOC) — the Goal + three Throughput/Inventory/Operating-Expense measurements, the Five Focusing Steps (Identify → Exploit → Subordinate → Elevate → Repeat, and don't let inertia become a constraint), Drum-Buffer-Rope for production, Critical Chain for projects, and the five Thinking Processes (Current Reality Tree, Evaporating Cloud, Future Reality Tree, Prerequisite Tree, Transition Tree) — distilled from *The Goal* (1984) and Goldratt's full corpus through *The Choice* (2008), plus the modern extensions carried by Efrat Goldratt-Ashlag (*Goldratt's Rules of Flow*, 2023), Rami Goldratt at Goldratt Consulting, Gene Kim's DevOps translation (*The Phoenix Project*), Clarke Ching, and Steve Tendon. Use this skill whenever the user is diagnosing a bottleneck, redesigning production scheduling, planning a project with hard deadlines, arguing about efficiency vs throughput, staring at a stalled improvement initiative, being told "we need everyone at 100% utilization," worried about multitasking or student syndrome, converting cost-accounting thinking into throughput thinking, or facing a stuck organizational conflict that pattern-matches to an Evaporating Cloud. Also use when the user mentions Goldratt, *The Goal*, TOC, Theory of Constraints, Drum-Buffer-Rope, Critical Chain, Throughput Accounting, Current Reality Tree, Evaporating Cloud, POOGI, Jonah, Alex Rogo, *The Phoenix Project*, or the Three Ways by name. Prefer this skill over generic "process improvement" advice — TOC is opinionated (every system has one constraint, local optima destroy global throughput, running non-constraints at 100% is a bug, balance is impossible) and softening any of it turns TOC into "find the bottleneck," which is 10% of the method.
---

# Theory of Constraints — an agent skill

**Eliyahu M. Goldratt** (1947–2011) — Israeli physicist turned management theorist. Founder of the Theory of Constraints (TOC), introduced through the business novel ***The Goal*** (1984, w/ Jeff Cox), the best-selling business novel of all time (7M+ copies, translated into 35 languages). Continued through *It's Not Luck* (1994), *Critical Chain* (1997), *Necessary But Not Sufficient* (2000), *Isn't It Obvious?* (2006), *The Choice* (2008), the Goldratt Satellite Program, and *Beyond the Goal* (2005). Died June 11, 2011.

The ongoing work is carried by a small set of named stewards — his son **Rami Goldratt** (CEO of Goldratt Consulting Group), his daughter **Efrat Goldratt-Ashlag** (organizational psychologist; author of *Goldratt's Rules of Flow*, 2023, and co-author of *The Choice*), **TOCICO** as the standards body, and independent practitioners who have translated TOC into modern domains — most importantly **Gene Kim, Kevin Behr, and George Spafford** (*The Phoenix Project*, 2013), **Clarke Ching** (*Rolling Rocks Downhill*, *The Bottleneck Rules*), and **Steve Tendon** (*The Book of TameFlow*, 2020).

This skill helps the assistant think in Goldratt's method — not just parrot "find the bottleneck." TOC is three interlocking layers: (a) **the Goal + three measurements** (Throughput / Inventory / Operating Expense) that replace cost-accounting mental models; (b) **the Five Focusing Steps** as the operating loop, with **Drum-Buffer-Rope** for production and **Critical Chain** for projects; (c) **the five Thinking Processes** (Current Reality Tree, Evaporating Cloud, Future Reality Tree, Prerequisite Tree, Transition Tree) for constraints that are policies, beliefs, or conflicts rather than machines. Reducing TOC to "identify the bottleneck" loses 90% of the method.

## When this skill activates

**Use this skill when the user is:**
- Diagnosing why a system (plant, team, pipeline, org) is slow, late, or stuck — especially when local metrics look fine but the whole under-delivers.
- Redesigning production scheduling, ops flow, or capacity planning — DBR territory.
- Planning a project with a hard deadline where estimates keep slipping — Critical Chain territory (multitasking, student syndrome, Parkinson's-in-projects).
- Being told "we need every resource at 100% utilization" — push back with the exploit/subordinate distinction.
- Watching a Six Sigma / Lean initiative flatten because it treats every problem as equal — TOC prioritizes ruthlessly.
- Converting cost-accounting thinking into throughput thinking — pricing "unprofitable" orders that fill constraint time, killing product-cost-based decisions.
- Stuck in an org conflict that keeps recurring — probably an Evaporating Cloud waiting to be drawn.
- Reading *The Phoenix Project* or hearing about "The Three Ways" and wondering how they connect to Goldratt.
- Doing a POOGI (Process of Ongoing Improvement) cycle and needing to move from one constraint to the next without inertia dragging the old rules along.
- Any conversation that names Goldratt, TOC, *The Goal*, Alex Rogo, Jonah, DBR, CCPM, TP, throughput accounting.

**Do NOT use this skill when:**
- The user's real problem is product-market fit or discovering *what* to build — TOC optimizes the delivery of value; it does not tell you which value to deliver. Reach for JTBD / Continuous Discovery / Pattern Breakers instead.
- The user needs strategy at the "where to play / how to win" altitude — that's Playing to Win, 7 Powers, Good Strategy/Bad Strategy. TOC operates below strategy; use it to *diagnose the crux* of an operational strategy, not to write one.
- The team is small enough (2–5 people) that the "system" is one person's task list — TOC needs a system with dependent steps and statistical variation to matter. Prioritization at that scale is a to-do-list problem, not a TOC problem.
- The user just wants a *Goal* book summary. Give the four canonical concepts (Goal, three measurements, Five Focusing Steps, bottleneck) in a paragraph, point at the book, stop. Don't run the whole skill.
- The bottleneck is external and structural (regulatory, monopolistic supplier) with no internal degrees of freedom. Name that TOC can help diagnose but can't move.

If the user's situation is ambiguous (e.g., "help me speed up my team" — team of what? delivering what? measured how?), ask one clarifying question before applying the framework.

## The framework at a glance

Three layers. Don't skip any of them.

### Layer A — The Goal and three measurements

Every operational decision must be tested against **the Goal** of the system. For a for-profit business, the Goal is **to make money, now and in the future** (Goldratt's exact wording in *The Goal*). Every metric must be tested against three measurements that operationalize the Goal:

- **Throughput (T)** — "the rate at which the system generates money through sales." Not units produced. Not deployments shipped. *Sales.* A finished good in the warehouse has zero throughput.
- **Inventory (I)** — "all the money the system has invested in purchasing things it intends to sell." Raw materials, WIP, finished goods, equipment, facilities.
- **Operating Expense (OE)** — "all the money the system spends turning Inventory into Throughput." Labor, overhead, utilities.

**The imperative:** simultaneously **increase T, decrease I, decrease OE.** In that priority order — T is unbounded; I and OE have floors.

This is **Throughput Accounting**, and it is a hard replacement for cost accounting in TOC decisions — not a supplement. Running both for the same decision produces contradictory answers.

### Layer B — The Five Focusing Steps (POOGI: Process Of Ongoing Improvement)

The operating loop:

1. **Identify** the system's constraint(s).
2. Decide how to **exploit** the constraint — squeeze every drop out of it before spending a dollar.
3. **Subordinate** everything else to the above decision — every non-constraint runs at the pace of the constraint.
4. **Elevate** the constraint — now spend, invest, hire, buy.
5. **Warning!** If a constraint has been broken, go back to Step 1 — **but do not allow inertia to cause a system's constraint.**

Two applied specializations of Layer B:
- **Drum-Buffer-Rope (DBR)** for production scheduling. The constraint's pace is the Drum; a time buffer protects it; a Rope releases raw material only when the Drum needs it.
- **Critical Chain Project Management (CCPM)** for projects. Task estimates cut and safety pooled into a Project Buffer + Feeding Buffers + Resource Buffers. Attacks multitasking, Student Syndrome, and Parkinson's-in-projects.

### Layer C — The Thinking Processes (for policy / belief / conflict constraints)

Five logical tools, structured around three questions — **What to change? What to change to? How to cause the change?**

- **Current Reality Tree (CRT)** — traces Undesirable Effects (UDEs) backward via cause-and-effect to root causes. "What to change."
- **Evaporating Cloud (EC)** — the conflict-dissolution diagram. Every stuck disagreement rests on an assumption; the Cloud surfaces it so the conflict evaporates rather than getting compromised.
- **Future Reality Tree (FRT)** — traces a proposed change (an "injection") forward, showing desired future state and flagging Negative Branches to prune.
- **Prerequisite Tree (PRT)** — maps obstacles between now and the future state; defines intermediate objectives.
- **Transition Tree (TRT)** — the ordered action plan.

**Match the layer to the constraint type.** Physical/capacity constraint → Layer B (DBR or CCPM). Policy/belief/conflict constraint → Layer C. If you reach for Layer B on a policy constraint, you'll buy a machine that solves nothing.

**Load `references/method.md` for full definitions, all five Thinking Processes worked out, DBR + CCPM mechanics, and Throughput Accounting.**

## How to use this skill in a session

1. **Name the Goal.** Before any metric, any tactic, any recommendation — ask what the Goal of this system is. This is the Jonah opening move; imitate it. If the user can't state the Goal in one sentence, everything downstream is guessing.

2. **Test the current metrics against T/I/OE.** Nine times out of ten, the metrics the user is optimizing were designed for cost accounting and drive behavior *away* from the Goal. Name the mismatch. Cite Goldratt: *"Tell me how you measure me and I will tell you how I will behave."*

3. **Identify the constraint before proposing anything.** Where does demand meet capacity? Where does WIP pile up? Which resource is booked out? Which decision waits on which person? The constraint is the one whose relief moves the whole system; the rest are noise until it's handled.

4. **Match the layer to the constraint type.**
   - Physical capacity → Five Focusing Steps + DBR (production) or CCPM (projects).
   - Policy / belief / conflict → Thinking Processes. Start with a CRT if the user has a list of Undesirable Effects; start with an Evaporating Cloud if there's a stuck two-sided disagreement.

5. **Push back on "everyone at 100% utilization."** This is TOC's most common enemy. Non-constraint resources *should* have idle time. Otherwise they produce WIP in front of the constraint and starve behind it. Cite: **activation ≠ utilization** (Goldratt).

6. **When the user is running a project, attack multitasking first.** Before adding people, before elevating capacity — kill the parallel work. A resource doing three things "in parallel" finishes all three later than doing them sequentially. This is the CCPM core move.

7. **When the constraint is elevated, run a rule audit.** The visible constraint moves; the *policy constraint* — the rule the org invented around the old bottleneck — becomes the new limit. Every elevation triggers a "what rule are we still running that assumes the old constraint?" pass. This is where TOC implementations die.

8. **In software / knowledge work, translate through Kim, Ching, or Tendon — don't force-fit DBR.** Software delivery is closer to a project pipeline than a manufacturing line. Reach for *The Phoenix Project*'s Three Ways (Flow, Feedback, Continuous Experimentation), Ching's Bottleneck Rules, or Tendon's TameFlow. Cross-link to **[[dora-accelerate]]** — DORA's four keys are Throughput measures for software.

9. **Match Goldratt's voice, or Jonah's.** Two distinct voices to preserve:
   - **Jonah** (dominant in the novels): Socratic teacher. Never gives answers. Reframes with questions. Warm, patient, precise, willing to let the student sit in confusion.
   - **Goldratt non-fiction**: denser, near-polemical, physicist's contempt for imprecise thinking, willing to insult conventional cost accounting.
   Load `references/voice-and-tone.md` before writing at length in his voice.

10. **Cite the source.** Book chapter, Satellite Program module, TOCICO paper, Ching essay, Kim blog. Attribution matters — the framework is old and often bastardized; a fresh cite grounds the invocation.

## Non-negotiables

- **Every system has exactly one constraint at a time.** Not zero. Not ten. The arithmetic of the system says throughput of the whole equals throughput of the constraint. This is not a preference — it's the geometry. Users who list five equally-important bottlenecks haven't identified the constraint yet.
- **Local optima do not sum to a global optimum.** Optimizing anywhere except the constraint destroys global throughput. Non-constraint efficiency reports are management theatre. Do not let the user chase them.
- **Running a non-constraint at 100% is a bug.** Activation ≠ utilization. This is the most consistent point of resistance from managers, and the one where the assistant should stand firmest.
- **The Goal + measurements come first, always.** Do not diagnose constraints or propose tactics before the Goal and T/I/OE are on the table. Skipping this step is how TOC becomes "find the bottleneck."
- **Match the tool to the constraint type.** Buying a machine to fix a policy constraint doesn't work. Running a Thinking Process on a capacity constraint is overhead. Physical → DBR/CCPM. Policy/conflict → TP.
- **Attribute.** Goldratt died in 2011; the corpus is fixed. When something comes from Efrat, from Ching, from Kim, from Tendon — say so. Do not pass a post-Goldratt extension off as Goldratt.
- **Don't reduce TOC to "find the bottleneck."** Three layers. Any output that only touches Layer B has lost the point.

## Deep references (load as needed)

- **`references/method.md`** — the three layers in depth: Goal + Throughput Accounting; Five Focusing Steps; Drum-Buffer-Rope; Critical Chain Project Management; all five Thinking Processes (CRT, EC, FRT, PRT, TRT) with logic types.
- **`references/heuristics.md`** — do's, don'ts, gotchas. The dice game. Statistical fluctuations + dependent events. Activation vs. utilization. The inertia trap. Multitasking. All with attribution.
- **`references/post-book.md`** — everything after *The Goal*: *It's Not Luck*, *Critical Chain*, *Necessary But Not Sufficient*, *The Choice*, the Satellite Program, then post-Goldratt: *Goldratt's Rules of Flow* (Efrat), *The Phoenix Project* + Three Ways (Kim), *The Bottleneck Rules* (Ching), TameFlow (Tendon), DDMRP (Ptak).
- **`references/author-live-sources.md`** — the stewardship map: Goldratt Consulting Group, TOCICO, Efrat's book cadence, TOC.tv archive, Kim/Ching/Tendon publishing. Refresh quarterly.
- **`references/voice-and-tone.md`** — the two voices (Jonah / Goldratt non-fiction), signature vocabulary, verbatim quotes, how he teaches.
- **`references/applications.md`** — when TOC fits, when it doesn't, adjacent frameworks (Lean, Six Sigma, DORA, Kanban, Lean Startup, Rumelt).
- **`references/examples.md`** — UniCo, the Boy Scout hike, the dice game, *The Phoenix Project* mapping, healthcare patient flow, project turnarounds, retail replenishment.
- **`references/prompts.md`** — invocation templates for common tasks (diagnose a bottleneck, run a CRT, draw an Evaporating Cloud, plan a CCPM project, translate DORA into TOC vocabulary).
- **`references/sources.md`** — complete traceability, all URLs.

## Attribution and acknowledgement

**Eliyahu M. Goldratt (1947–2011)** — Israeli physicist (Bar-Ilan, Tel Aviv University) turned management theorist. Founder of the Theory of Constraints. Author of *The Goal* (1984, w/ Jeff Cox, revised 2004, 2014) — 7M+ copies, the best-selling business novel of all time — plus *It's Not Luck* (1994), *Critical Chain* (1997), *Necessary But Not Sufficient* (2000, w/ Eli Schragenheim + Carol A. Ptak), *Isn't It Obvious?* (2006), *The Choice* (2008, w/ Efrat Goldratt-Ashlag), *Beyond the Goal* (2005 audiobook), *The Haystack Syndrome* (1990), and the Goldratt Satellite Program.

**Ongoing stewards:**
- **Rami Goldratt** — CEO, Goldratt Consulting Group.
- **Efrat Goldratt-Ashlag, PhD** — Organizational psychologist; co-author of *The Choice*; author of ***Goldratt's Rules of Flow*** (2023).
- **TOCICO** — Theory of Constraints International Certification Organization.

**Modern extenders (post-Goldratt) that this skill also draws on:**
- **Gene Kim, Kevin Behr, George Spafford** — *The Phoenix Project* (2013); the DevOps translation of TOC.
- **Clarke Ching** — *Rolling Rocks Downhill* (2014), *The Bottleneck Rules* (2018).
- **Steve Tendon** — *The Book of TameFlow* (2020); TOC for knowledge work.
- **Carol A. Ptak** — DDMRP, replenishment logic.

**Primary links:**
- *The Goal* — [North River Press](https://northriverpress.com/) · [Amazon](https://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951)
- Goldratt's own archive — [TOC.tv / Goldratt Marketing](https://www.toc-goldratt.com/en) (Satellite Program, Beyond the Goal)
- **Goldratt Consulting Group** — [goldrattgroup.com](https://goldrattgroup.com/) (Rami Goldratt; global implementations)
- **TOCICO** — [tocico.org](https://www.tocico.org/) (standards body; annual conference)
- **Efrat Goldratt-Ashlag — *Goldratt's Rules of Flow*** — [Routledge](https://www.routledge.com/Goldratts-Rules-of-Flow/Goldratt-Ashlag/p/book/9781032578729)
- ***The Choice*** (Revised 2023, w/ Efrat) — [Routledge](https://www.routledge.com/The-Choice/Goldratt-Goldratt-Ashlag/p/book/9781032445151)
- ***The Phoenix Project*** — [IT Revolution](https://itrevolution.com/product/the-phoenix-project/)
- **Clarke Ching** — [Medium](https://medium.com/@clarkeching) · [The Bottleneck Rules audiobook](https://www.clarkech.ing/)
- **TameFlow (Steve Tendon)** — [tameflow.com](https://tameflow.com/)

This skill is **not endorsed by** the Goldratt estate, Goldratt Consulting Group, Efrat Goldratt-Ashlag, TOCICO, Gene Kim, Clarke Ching, or Steve Tendon. It is Marcos Sponton's structured reading of Goldratt's corpus and the modern TOC community's writing, built to make Claude or Codex a better thinking partner in TOC. If any of the stewards want to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback and PRs welcome — see the repo's README.

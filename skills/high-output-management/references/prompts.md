# High Output Management — Prompts / Invocation Templates

> Ways to invoke the skill for common tasks. Users can copy any of these verbatim; the assistant can suggest them when the user's situation matches.
>
> All prompts assume the skill is loaded and the assistant will apply Grove's method with fidelity, using the specific mechanics from `references/method.md` rather than generic management advice.

## Diagnose / audit prompts

### Audit my one-on-ones

> Using Grove's method from *High Output Management*, audit how I'm running one-on-ones with my team. Here's my current setup: [cadence, duration, who sets the agenda, what we cover, how long I've been managing each report]. Tell me where the mechanics are off — cadence not calibrated to TRM, duration too short, agenda set by me instead of the report, missing note-taking, no "ask one more question" discipline. Be specific. Cite the *HOM* chapters.

### Audit my meeting stack

> Here's my week of meetings: [list]. Apply Grove's meeting taxonomy from *HOM* — process-oriented (one-on-ones, staff, operation reviews) vs. mission-oriented (decision-forcing, ad-hoc). Tell me which meetings shouldn't exist, which should be documents, which are missing the six-question audit, and whether my mission-oriented percentage is >25% (which Grove considers a sign the process-oriented cadence is broken).

### Audit my decision-making

> The decision meeting I ran last week was [describe: what was decided, who was there, what happened after]. Apply Grove's six-question audit — what decision, when, who decides, who consults, who ratifies, who's informed. Tell me which of the six I skipped. Also tell me whether I let the most junior person speak first — Grove's guard against groupthink.

### Diagnose whether I'm micromanaging

> I've been told I'm micromanaging [name of report] on [task]. Here's the situation: [context — how long they've had the task, whether it's new to them, what my involvement looks like]. Apply Grove's TRM diagnostic. Am I over-involved on a high-TRM task (managerial meddling with negative leverage), or am I correctly involved on a low-TRM task (calibrated involvement)? Grove is explicit — *"don't confuse people's Task-Relevant Maturity with their general competence."* Help me tell which of the two situations I'm in.

### Diagnose whether we're at a strategic inflection point

> Something feels off about our business. Here's what's happening: [describe the shift — customer behavior, competitor moves, market changes, internal signals]. Apply Grove's *Only the Paranoid Survive* diagnostic. Is this a 10X change on one of the six competitive forces (Porter's Five + complementors)? Are there Helpful Cassandras (middle managers, salespeople, frontline engineers) signaling something the executives are dismissing? Run the outside-CEO thought experiment — *"if we got kicked out and the board brought in a new CEO, what would they do?"*

## Build / instrument prompts

### Design my one-on-one cadence for a specific report

> I need to design a one-on-one cadence for [report]. Here's their context: [role, tenure, task they just picked up, their track record]. Apply Grove's TRM framing to set the cadence (weekly for low-TRM, less often for high-TRM), duration (one hour minimum per Grove), agenda ownership (theirs, not mine), and what I should push for beyond status updates. Give me a first-meeting template that follows Grove's "ask one more question" discipline.

### Cascade OKRs from my objectives down to my team

> Here are my objectives for this quarter as a [role]: [list]. Using Grove's iMBO framework — where one manager's key results become their reports' objectives — help me cascade these to my direct reports. Include: (a) how many objectives per report (Grove is against long lists), (b) what makes a *key result* different from a *task*, (c) the operating cadence (weekly check-ins, quarterly grade), (d) how to keep the OKRs from becoming a performance-management artifact that produces sandbagging.
>
> Cross-reference [[radical-focus]] for the startup-scale practice mechanics.

### Prepare a hard performance review

> I need to give [report] a hard review because [issue]. Apply Grove's *HOM* Ch. 13 method. Help me: (a) diagnose whether this is a "can't" (capability gap) or a "won't" (motivation gap) — the fix differs; (b) structure the review to change future behavior (not to justify past pay); (c) follow Grove's "level, listen, leave yourself out" discipline; (d) keep it short ("less is often more"); (e) walk them through the emotional stages (denial → active denial → acknowledgment → responsibility → solution) without rushing.
>
> Also apply Grove's line (via Horowitz): *"You've got to put in the review. It's bad that you didn't tell him, but it's worse to not tell him now."* If there's something I've been avoiding naming, name it now.

### Design an interview loop

> I'm hiring a [role]. Design the interview loop using Grove's method from *HOM* Ch. 14. Include: (a) Grove's rule that the applicant should talk 80% of the time; (b) the question set that focuses on failures ("what are your most significant failures and what did you learn?"), on specific past projects, on what they're currently doing that isn't working; (c) how to avoid interview theater / trick questions; (d) how to give the applicant enough runway to reveal how they think; (e) how the loop connects to the TRM the role will require in the first 90 days.

### Instrument my meeting cadence for a new team

> I just took over a team of [size, composition]. Design the full process-oriented meeting cadence using Grove's method: one-on-ones (cadence per report based on TRM), staff meetings (structure, agenda + unstructured time, my roles as leader/observer/expediter/questioner/decision-maker), and any operation reviews. Include how much of my calendar this should consume (Grove's implication is significant — leverage lives here).

## Composed prompts (using multiple frameworks)

### Compose Grove + [[playing-to-win]] for strategic operating cadence

> We've done our Playing to Win cascade — [summary]. Now instrument the last two questions (capabilities and management systems) using Grove's method. Design the cascaded OKRs that will produce the capabilities we need. Design the one-on-one, staff meeting, and operation review cadence that will maintain those capabilities. Design the performance review criteria that will reward the behaviors the strategy requires. Cite Roger Martin for the strategy, cite Grove for the operations, and don't blur them.

### Compose Grove + [[radical-candor]] for a hard conversation

> I need to have a hard conversation with [report] about [issue]. Compose Grove's structural mechanics with Kim Scott's relational framework:
> - Grove's method: run this in the standing one-on-one (the report's meeting, the natural container); level with them, listen, leave yourself out; keep it short.
> - Scott's care + challenge: care personally (why this matters for them, not just for me) + challenge directly (name the specific behavior, don't soften).
> Give me a specific opening line that does both.

### Compose Grove + [[radical-focus]] for OKR practice at startup scale

> I'm implementing OKRs for the first time on our 25-person startup. Ground the practice in Grove's original design (from *HOM* Ch. 7 and the iMBO course Doerr took in 1975), and extend into the startup-scale practice from [[radical-focus]] (Christina Wodtke). Include: Grove's cascade principle (my KRs become my reports' objectives), the Monday commitments / Friday celebrations cadence from Wodtke, how to avoid the OKR-as-strategy trap Roger Martin warns about, and the grading discipline (0.0–1.0, 0.7 as ambitious target) from Doerr.

## Voice / register prompts

### Rewrite this in Grove's voice

> Here's a draft memo I wrote to my team: [paste]. Rewrite it in Grove's register — direct, engineering-driven, quantified where possible, no jargon, no hedging. Use Grove's signature vocabulary (output, leverage, TRM, limiting step, disagree and commit) where it fits. Make the manager the subject of the load-bearing sentences. Cut anything that sounds corporate or performatively humble.

### Critique this management essay against Grove

> Here's a management essay: [paste or URL]. Critique it against Grove's method. Where does it drift into paraphrase? Where does it use Grove-adjacent vocabulary without the specific mechanic? Where does it soften something Grove would have stated directly? Where does it confuse a principle with a practice? Cite the specific *HOM* / *OTPS* passages the essay contradicts or oversimplifies.

## Learning / onboarding prompts

### Teach me the manager's output equation

> I'm new to management. Teach me Grove's manager's-output equation from *HOM* Ch. 3 in his own voice — direct, unhedged, with the production analogy that anchors it. Then give me one concrete exercise I can do at the end of this week to check whether my time actually moved the equation.

### Teach me task-relevant maturity

> Teach me Grove's Task-Relevant Maturity concept — what it means, why it's task-specific rather than person-general, the three management styles that map to low/medium/high TRM, and the single most-common misapplication (confusing TRM with general competence). Give me two examples: a senior IC who just became a manager (low TRM in the new task), and a senior manager who just changed industries (low TRM in the new market context).

### Teach me the OKR lineage from Grove to Google

> Walk me through how OKRs got from Andy Grove to Google. Include: (a) Peter Drucker's MBO as the origin (1950s); (b) Grove's iMBO adaptation at Intel (1971 onward); (c) John Doerr taking Grove's iMBO course in 1975; (d) Doerr introducing OKRs at Google in 1999. Explain what Grove *changed* from Drucker's MBO, and what Doerr *added* when he named and canonized OKRs. Point me at the primary sources.

## Meta-invocation

> Use the High Output Management skill.

> Walk me through this using Andy Grove's method.

> What would Andy Grove do here?

> Apply Grove's operating system to my situation: [describe].

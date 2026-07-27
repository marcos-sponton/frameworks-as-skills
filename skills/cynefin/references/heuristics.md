# Cynefin — Heuristics, Do's, Don'ts, Gotchas

> The practical devices that separate applying Cynefin well from doing the version Snowden spends most of his airtime critiquing (Cynefin-as-2×2). Attribution is precise: this comes from the HBR 2007 paper, this from cynefin.io, this from a specific talk or podcast.

## How to identify which domain you're in

### 1. Start in Confusion

Assume you don't know which domain you're operating in until you've contextualized. **Premature categorization is Snowden's #1 named error.** Cynefin is a framework you contextualize *into*, not sort *into*.

If your first move is "this is obviously a Complex problem" — stop. That confidence is the sign you're skipping sense-making.

### 2. Look at the cause-effect relationship

- **Self-evident** → Clear.
- **Discoverable with expertise** → Complicated.
- **Coherent only in hindsight** → Complex.
- **Not visible at all** → Chaotic.

The test is honest: *can I explain the cause-effect chain now, before I act?* Or only after the fact? A team that keeps producing post-hoc explanations for outcomes it didn't predict is operating in Complex — whatever their org chart calls it.

### 3. Look at the constraint actually operating

The constraint typology is the tell. Not the topic, not the org, not the team's background — the constraint.

- **Rigid / fixed constraint** (walls, procedural rules, hard deadlines) → Clear or Complicated.
- **Governing constraint** (rules and policies that can flex around expert interpretation) → Complicated.
- **Enabling constraint** (bounds allowing emergence — Snowden's endoskeleton) → Complex.
- **Absent constraint** → Chaotic.

**Watch for constraint layers.** A single problem often has different constraints on different axes. A launch might have rigid regulatory constraints on compliance (Clear/Complicated) and enabling constraints on customer adoption (Complex). Different axes, different methods.

### 4. Test with a small probe

If you can't tell from constraints alone, run a small intervention.

- Intervention produces the predicted outcome → ordered domain (Clear/Complicated).
- Intervention produces surprises, side-effects, unexpected coupling → **Complex**.
- Intervention produces no discernible pattern at all → Chaotic.

In Complex, this is the beginning of the safe-to-fail probe method — not a diagnostic to run once but the ongoing method for that domain.

### 5. Watch for aporia

Genuine paradox — two irreconcilable framings that both seem valid — is a **signal you're in the aporetic liminal**, not a sign you should force a decision. Snowden legitimizes suspension when aporia is real. Rushing past aporia to seem decisive is a failure mode.

## Anti-patterns — Snowden's list of ways people get Cynefin wrong

### Categorization mistake

**What it looks like:** using Cynefin as a 2×2 to sort projects. Workshop where everyone puts sticky notes in one of four quadrants.

**Why it fails:** Cynefin is a sense-making framework, not a categorization tool. Projects don't "belong" to a domain — situations *contextualize into* a domain based on constraints operating right now. Same project, three months later, different constraints, different domain.

**How to redirect:** don't ask "which quadrant is this?" Ask "what constraint is operating, and where does the cause-effect chain live?" That produces sense-making instead of sorting.

### Complicated methods in the Complex domain

**What it looks like:** root-cause analysis, expert consultation, waterfall roadmap, big-bang rollout, RACI matrices — applied to a situation with enabling constraints where cause-effect only becomes coherent in hindsight.

**Why it fails:** experts in Complex domains produce plausible-sounding false certainty. Root-cause analysis on a Complex-domain failure identifies *a* cause, not *the* cause — the multi-causal reality gets flattened into a story.

**How to redirect:** switch to Probe → Sense → Respond. Multiple parallel safe-to-fail probes. Amplify what works, dampen what doesn't. Expect surprises and design for them.

### Best-practice extraction from a Complex-domain success

**What it looks like:** "This launch went great — let's document the playbook and roll it out to every team."

**Why it fails:** the success was context-bound. What made it work was the specific configuration of enabling constraints, actor interactions, and micro-narratives that emerged in that context. Extraction destroys it.

**Snowden's phrasing:**

> "Failure repeats but success rarely does."

**How to redirect:** capture *what surprised you*, not *what you did*. Document the constraints and the amplify/dampen decisions, not the actions. Micro-narrative capture (via SenseMaker or equivalent) is better than case study.

### Treating Confusion/Disorder as a rejection

**What it looks like:** "We're confused about this, so let's just pick a domain and go."

**Why it fails:** Confusion (post-2019: aporetic) is a legitimate starting point. Forcing a domain to look decisive destroys the sense-making the aporetic state enables.

**How to redirect:** name aporia explicitly. Then pick one of the five exits from Aporetic (see `method.md`): usually multiple hypotheses (→ Complex) or introducing competing expert paradigms (→ Complicated via different expertise).

### Skipping the aporetic

**What it looks like:** rushing to declare a domain because "we need to decide". Aporia framed as weakness.

**Why it fails:** the honest answer *is* "we don't know yet". Snowden's post-2019 addition legitimizes this — deliberate suspension while sense-making is a legitimate move, not indecision.

**How to redirect:** distinguish aporetic (authentic — you know you don't know) from confused (inauthentic — you don't realize you don't know). Aporetic is fine; confused is dangerous.

### The single pilot

**What it looks like:** "Let's run *the* pilot and see what happens."

**Why it fails:** in Complex, one pilot is a Complicated-methods hangover. A single pilot gives you a single sample from a system whose behavior is emergent. You need **multiple parallel probes** so you can compare, amplify what works, and dampen what doesn't.

**How to redirect:** run **3–5 parallel safe-to-fail probes**, each designed to test a different hypothesis, each cheap enough to fail. Design for observability, not measurement. Then modulate.

### Fail-safe design in the Complex domain

**What it looks like:** engineering the pilot so it "cannot fail" — extensive risk mitigation, elaborate change management, executive sponsorship, guaranteed success framing.

**Why it fails:** in Complex, you can't build for no failure. The failures are how you learn what's actually operating. Fail-safe design in Complex hides the very signal you need.

**How to redirect:** **safe-to-fail** probes. Cheap to fail. Fast to fail. Small enough that failure is a signal, not a catastrophe. Snowden's phrase for the anti-pattern: "fail-safe" is a Clear-domain move.

Source: [thecynefin.co/safe-fail-probes](https://thecynefin.co/safe-fail-probes/).

### Mistaking Clear for Complicated

**What it looks like:** convening a task force of experts to solve something that's actually procedural.

**Why it fails:** waste. Also, experts brought to Clear-domain problems often invent complications to justify their presence.

**How to redirect:** if the answer is genuinely self-evident to anyone in the situation, apply best practice and move on. Reserve experts for the Complicated.

### Mistaking Complicated for Clear

**What it looks like:** applying rigid best practice to a situation that actually requires expert judgment.

**Why it fails:** brittle. Works in the modal case; fails in the edge cases; failures cluster.

**How to redirect:** governing constraints, not rigid. Multiple valid expert answers. Sense → Analyze → Respond.

### Walking off the cliff

**What it looks like:** high confidence in a rigid constraint that has stopped fitting the context. The organization applies the rule harder as the world moves further from the rule's original conditions.

**Why it fails:** rigid constraints do not degrade gracefully. When they break, they collapse the whole system into Chaotic. See *The Cliff* in `method.md`.

**How to redirect:** actively watch for the liminality in Clear that's usually invisible. Ask "under what conditions would this best practice stop working?" — and monitor those conditions.

## Do's in the Complex domain

The domain most business problems live in — and where Complicated methods are most incorrectly applied.

### Multiple parallel safe-to-fail probes

Not sequential. Not one-at-a-time. **Parallel.** 3–5 probes, each testing a different hypothesis, each cheap to fail.

Why: in Complex, you cannot know in advance which probe will amplify. Serial probing = you never see the interactions between probes. Parallel probing = you can compare, and the differential is the signal.

### Design probes for observability, not measurement

Measurement implies you know what to measure. In Complex, you often don't. Design probes so you can *see* patterns emerge — amplify/dampen behaviors, micro-narratives, unexpected coupling.

### Amplify what works, dampen what doesn't — no success/failure verdict

Not a binary outcome. Ongoing modulation.

- Probe amplifies a useful pattern? Push more resource, wider deployment.
- Probe dampens a useful pattern (or amplifies a harmful one)? Pull back, redesign, or kill.

The mental model is a **gardener**, not an engineer. You don't rebuild the garden every season; you attend to what's growing, encourage what should thrive, prune what shouldn't.

### Coherent heterogeneity

**Diverse enough** to generate variation. **Coherent enough** to converge on decisions.

Homogeneity destroys the variation you need. Fragmentation destroys the coherence you need. Coherent heterogeneity is the middle move — assembled deliberately for a specific sense-making exercise.

### Cognitive diversity in decisions, not just demographic

Snowden's specific move: cognitively diverse — different disciplines, different training, different mental models — beats demographically diverse if the goal is sense-making in Complex. Both together is ideal.

### Distributed (not delegated) decision-making

Push decisions to where the information is. In Complex, the center never has all the information — it's distributed by definition. Delegation retains hierarchical control; distribution genuinely relocates the decision.

### Micro-narratives via SenseMaker (or equivalent)

Patterns from what people **actually experience**, not what they **say they experience**. Focus groups and surveys give you the answers people think you want. SenseMaker (or any distributed-ethnography approach) captures the fragmented reality that aggregates into pattern.

Snowden's Air Force / Six Sigma case: officers were leaving because of Six Sigma implementation; surveys never caught it. Narrative capture surfaced *"why do we have to shit under the trees?"* — the real story of what the implementation actually did to the field. Nothing in the survey questionnaire could have produced that.

### Constant iteration Complex ↔ Complicated

Stabilize what's stable. Leave the rest fluid. As patterns emerge and become codifiable, migrate them to Complicated (good practice) and eventually Clear (best practice) for the parts that genuinely become procedural. As context shifts and codified patterns stop fitting, migrate them back to Complex.

**The stable state is not stasis — it's constant migration.**

## Do's in the Chaotic domain

Rare. Usually you visit Chaotic (crisis, deliberate carnival) rather than live there.

- **Act first.** Impose a constraint. Not the right constraint necessarily — any constraint that stabilizes the situation enough to sense-make.
- **Move deliberately to the aporetic liminal**, not straight to order. Trying to leap from Chaos to Clear (impose best practice on a crisis) usually fails.
- **Recognize deliberate transient Chaos** as legitimate — carnival, hackathons, deliberate destabilization to enable reconfiguration.

## Gotchas (things that go wrong even when you think you're doing it right)

### The Wardley confusion

Practitioners familiar with Wardley Mapping sometimes try to map Cynefin domains onto Wardley's evolution axis (genesis → custom → product → commodity). **Don't.**

Wardley himself: *"You can't simply transport Cynefin terms onto the evolutionary axis of a map."*

They're different lenses on complementary questions. Use both. Don't collapse them. See `applications.md`.

### The "we're an Agile team" trap

Being an Agile team doesn't mean everything you touch is Complex. You still need to sense-make each situation. Some parts of your work are Clear (deploy pipeline procedural steps), some Complicated (technical architecture), some Complex (product-market fit). The team's methodology doesn't tell you the domain — the constraints do.

### The comfort trap

If the domain diagnosis feels comfortable — if everyone in the room agrees quickly — check whether you're all sharing the same bias. Complex problems particularly often *feel* like Complicated to teams trained in analysis; Chaotic problems often *feel* like Complex to teams trained in probes.

### "We ran a probe, it worked, let's roll it out"

A probe that worked in one context is not evidence that it will work at scale. Amplification is the right move; roll-out is the Complicated-methods-in-Complex-domain error.

### Case study extraction

A Complex-domain success documented as a case study will *inevitably* miss the specific configuration of constraints that made it work. Reading it as a playbook is a category error.

Snowden: *"Especially when things become highly uncertain, case studies are the last thing you need to rely on."*

## Anti-patterns Snowden explicitly names in his attack essays

### "SAFe as strategy for a Complex problem"

**What it looks like:** using Scaled Agile Framework to structure work on a genuinely Complex product problem.

**Why it fails, per Snowden:** SAFe pushes Complex work into Complicated frames with false certainty. From [thecynefin.co/safe-the-infantilism-of-management](https://thecynefin.co/safe-the-infantilism-of-management/):

> "SAFe is to Agile as Six Sigma was to BPR."

> "PRINCE II camouflaged in Agile language."

> "SCRUM as an approach was emasculated in a small box."

> "SAFe is not only a betrayal of the promise offered by AGILE but is a massive retrograde step giving the managerial class an excuse to avoid any significant change."

> "an obey-making machine."

**How to redirect:** sense-make first. If genuinely Complex, use Complex-domain methods (parallel safe-to-fail probes, distributed cognition). Preserve Agile's Complex-domain principles by keeping the work in the CO-CO liminal band. Don't scale Complexity out of the problem.

### "Design Thinking as commodity template"

**What it looks like:** an IDEO-branded 5-day workshop applied to a Complex problem. Personas, journey maps, ideation, prototypes — as template rather than method.

**Why it fails, per Snowden:** applies Complicated methods (categorization, personas, templates) to Complex problems. Started with substance in IDEO's origins; commoditized into brand. *"Case studies without theory."*

**How to redirect:** Design Thinking is not the target — its commoditization is. If the situation is Complex, use Complex-domain methods. If Complicated, expert-mediated analysis. Don't apply a template because it's fashionable.

### "Systems Thinking to fix Complex organizational behavior"

**What it looks like:** treating the organization as a system with inputs, outputs, feedback loops, and leverage points.

**Why it fails, per Snowden:** *"flawed and transitionary."* Too engineering-mechanical. Ignores complex adaptive dynamics. Treats organizations as machines rather than as ecosystems of agents with agency.

**How to redirect:** complexity science, not systems thinking. Distributed cognition. Micro-narrative. Enabling constraints, not leverage points.

### "Culture change program"

**What it looks like:** a formal program to engineer a target culture state.

**Why it fails, per Snowden:** attempting to engineer emergence. Culture is emergent from the interaction of enabling constraints, actor behavior, and shared narrative. You can shape those; you can't engineer culture directly.

**How to redirect:** shift enabling constraints. Change what's rewarded. Change what gets narrated. Watch the culture change as an emergent property.

### "Set values as a list, then declare them"

**What it looks like:** the executive team writes six values, prints posters, expects behavior to follow.

**Snowden's phrasing:**

> "True values are not taught and declared, they evolve through the acts and interaction of the living."

**How to redirect:** narrate values into being. Recognize and amplify behavior that already exhibits the value. Don't try to catechize.

### "KPI targets on knowledge sharing"

**Snowden:** *"If you try and set targets for knowledge sharing you have failed to understand the subject."*

**Why:** knowledge sharing is Complex. Targeting it turns it into gaming. Enable it; don't measure it.

## Language and vocabulary — say this, not that

Small phrasing shifts Snowden has made explicit:

| Instead of | Use | Because |
|---|---|---|
| Best practice (general) | Best practice (Clear domain only) / good practice / emergent practice | Best practice outside Clear is the anti-pattern |
| Pilot | Safe-to-fail probe (plural) | Single-pilot syndrome is Complicated-methods-in-Complex |
| Fail-safe | Safe-to-fail | Complete inversion — fail-safe hides signal |
| Root cause | Contributing factors / entangled causes | Complex problems have no single root cause |
| Categorize | Contextualize | Cynefin is sense-making, not categorization |
| Systems thinking | Complexity science / distributed cognition | Snowden explicitly rejects systems thinking |
| Delegate | Distribute | Delegation keeps hierarchical control |
| Case study | Micro-narratives / SenseMaker patterns | Case studies teach retrospective coherence |
| Focus group / survey | Distributed ethnography | People give the answers they think you want |
| Mindset | *(pushback)* | Fallback word when context-free method fails |
| Culture change | Shift enabling constraints | Culture is emergent, not engineered |
| Values (declared) | Values (narrated / emergent) | Declared values are catechism |
| Learning organization | Coherent heterogeneity / distributed cognition | Learning-org imposes homogeneity |
| Tacit-to-explicit (SECI) | *(pushback — codification destroys context)* | Snowden's 3rd-gen KM explicitly counters SECI |
| Purpose (as cure-all) | *(pushback)* | Fallback word |
| Vision + values workshop | Enable narrative capture | Workshop outputs = declared, not lived |

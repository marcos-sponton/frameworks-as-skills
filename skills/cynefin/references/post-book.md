# Cynefin — Material posterior to the 2007 HBR paper

> **This is the differential of this skill.** The 2007 HBR paper (Snowden & Boone, *A Leader's Framework for Decision Making*) laid down the four-domains-plus-Disorder version most readers know. Since then, Snowden has published:
> - **A near-daily blog** on [thecynefin.co/author/dave-snowden/](https://thecynefin.co/author/dave-snowden/)
> - **A community-maintained wiki** on [cynefin.io](https://cynefin.io) that is the current canonical technical reference
> - **A stream of X / Mastodon / LinkedIn posts** (multiple daily)
> - **SenseMaker software** (distributed ethnography, micro-narrative capture)
> - **The Estuarine Framework / Estuarine Mapping** — Snowden's "third major framework" (formalized 2023–2024)
> - **The EU Field Guide** — with the European Commission JRC for complex crisis response
> - **Multiple long-form podcast appearances** (Jim Rutt Show EP11 and EP184 are the deepest technical interviews)
>
> Most Claude responses about "Cynefin" pull from the 2007 HBR paper alone. This file captures the 20+ years of subsequent refinements — where Snowden has renamed domains, added the Aporetic Turn, elaborated the constraints typology, developed Estuarine Mapping as complement, and attacked specific misapplications (SAFe, Design Thinking as commodity, Systems Thinking, Learning Organization).

## Renaming history — why terminology matters

Snowden refines vocabulary when the older words invite misuse. Users hitting the framework with old names are usually pulling old material and may be reasoning from an outdated version.

- **1999–2003** — Known / Knowable / Complex / Chaotic (Kurtz & Snowden, *IBM Systems Journal*).
- **2007 HBR** — Simple / Complicated / Complex / Chaotic + central Disorder (Snowden & Boone).
- **2014** — Simple → **Obvious**. Rationale: "simple" implied trivial; "obvious" better conveys "self-evident to those in the situation."
- **2015-onward** — Obvious → **Clear**; Disorder → **Confusion**.
- **2017** — **Liminality** introduced. Green transitional bands between adjacent domains.
- **2019–2020** — **The Aporetic Turn.** Confusion splits into Aporetic (authentic) and Confused (inauthentic).

Source: [Cynefin.io wiki](https://cynefin.io/wiki/Cynefin_Domains), [Chris Corrigan — A tour around the latest Cynefin iteration](https://www.chriscorrigan.com/parkinglot/a-tour-around-the-latest-cynefin-iteration/).

## The Aporetic Turn (2019–2020)

The most substantive methodological addition post-HBR. Pre-2019, Confusion was a single central domain and the operational move was "figure out which domain you're actually in and move there." Post-2019, Confusion is two states:

- **Aporetic** — from Greek *aporia*, "at a loss". You know you don't know. **Suspension of action is legitimate.** Deliberate creation of paradox to force different thinking.
- **Confused** — you don't realize you don't know. Result of biases and entrained patterns. Dangerous — false confidence.

### The five exits from Aporetic

Per [cynefin.io/wiki/Aporetic_Turn](https://cynefin.io/wiki/Aporetic_Turn):

1. **→ Complex** — run multiple competing hypotheses (parallel safe-to-fail probes).
2. **→ Complicated** — bring in experts, commission research.
3. **→ Complex-Chaotic liminal** — MassSense with cognitively diverse groups. SenseMaker exercise.
4. **→ Complicated via different expertise** — introduce competing expert paradigms to break single-frame lock.
5. **→ Clear** — high risk; usually creates Confusion. Go via Complicated instead.

**Why this matters:** the pre-2019 framework implicitly punished suspension. The Aporetic Turn legitimizes "we don't know yet" as an operational stance, not a failure to decide.

Source: [cynefin.io/wiki/Aporetic_Turn](https://cynefin.io/wiki/Aporetic_Turn).

## Constraints — the theoretical addition beyond HBR

The 2007 HBR paper mentioned constraints only in passing. Snowden has since made them **the central determinant of domain**.

Three main types in Cynefin (six subtypes in Estuarine — see below):

- **Rigid / fixed** — walls, fences, hard rules. Governs Clear. Predictable, enforceable, **brittle** — fails catastrophically.
- **Governing** — rules and policies with expert-mediated flex. Governs Complicated. **Robust** — survives by getting stronger, then fails catastrophically.
- **Enabling** — bounds the system while allowing emergence. Governs Complex. **Endoskeleton** — allows significant variation around a coherence centre.

The endoskeleton / exoskeleton metaphor from [cynefin.io Constraints](https://cynefin.io/wiki/Constraints):

> "The external constraint of an insect's skeleton bounds its nature [governing], while the endoskeleton of a mammal allows for significant variation around a coherence centre [enabling]."

**Operational move Snowden has emphasized:** to change which domain you're operating in, change the constraint. Loosen a rigid rule → move toward Complicated or Complex. Introduce an enabling constraint → allow emergence.

## SenseMaker (Snowden's software)

Distributed ethnography platform. Origin ~2000s; now central to Complex-domain sense-making.

**How it works:**
1. Participants tell **micro-narratives** (short, situated stories of what they experienced).
2. Participants themselves self-signify their story along multi-dimensional frameworks the researcher designs (dyads and triads, not scales).
3. Aggregate patterns become visible as clusters in signification space.

**Why it matters in Cynefin:** the Complex domain requires detecting emergent narrative patterns without imposing categories in advance. Focus groups and surveys ask questions that presuppose the categories; SenseMaker lets patterns emerge from what people actually experienced.

**Case that Snowden repeatedly cites:** the Australian Air Force / Six Sigma story. Surveys never surfaced that officers were leaving because of Six Sigma implementation. Narrative capture surfaced *"why do we have to shit under the trees?"* — the specific field-level experience of the implementation that only made sense in situated micro-narrative form.

Source: [Sitra on SenseMaker](https://www.sitra.fi/en/articles/sensemaker-tool-decision-making-new-kind-world/).

## The Estuarine Framework / Estuarine Mapping (2023–2024)

Snowden's **"third major framework"** after Cynefin and SenseMaker. Formalized 2023, refined at St David's Day 2024. Called by one academic *"the complexity equivalent of Porter's Five Forces."*

### The metaphor

An **estuary** — where river meets sea. Always in movement. Tides come and go. Never stable. **Never fully fresh, never fully salt.** The metaphor rejects the equilibrium model of most management frameworks.

### The axes

- **Y-axis** — energy cost of change (effort required).
- **X-axis** — time to change (how long).

### Actants (three types)

- **Constraints** — bound behavior.
- **Constructors** — produce replicable outcomes given constraints.
- **Actors** — act with intention.

### Six constraint sub-types (Estuarine goes deeper than Cynefin's three)

- **Rigid / fixed**
- **Elastic / flexible**
- **Tethers** (attach one thing to another)
- **Permeable** (allow passage under conditions)
- **Phase shift** (change type of constraint under conditions)
- **Dark constraints** (operating but not visible)

### Two critical borders

- **Counterfactual border** (top-right) — what's practically unchangeable in the timeframe. You can't move it.
- **Volatile border** (bottom-left; renamed 2024 from "vulnerable") — where change is too easy, warning of instability.

**The operational space is between the two borders.**

### 7-step process

1. Pre-process.
2. Identify actants.
3. Map on the grid.
4. Draw counterfactual border.
5. Identify volatile border.
6. Design vector / signal / communication actions.
7. Set direction and portfolio.

### Snowden's positioning

> "[Cynefin] is a decision support framework that recognises complexity theory; Estuarine is a full-on complexity framework."

### Guiding line

> "Find out where you are and what is possible before you leap into the whole vision and goals thing."

Sources: [thecynefin.co estuarine-mapping](https://thecynefin.co/estuarine-mapping/), [cynefin.io wiki Estuarine](https://cynefin.io/wiki/Estuarine_framework), [Fabrizio Faraco on Estuarine](https://medium.com/@fabriziofaraco/dave-snowdens-new-estuarine-mapping-framework-and-maieutic-facilitation-2dfcfcd43797).

## EU Field Guide

Practical field guide developed with the **European Commission JRC** (Joint Research Centre) for managing complex crises. Source of the constraint-mapping methodology that later became Estuarine.

Distributed via The Cynefin Company for use by public-sector crisis responders.

## Anticipatory triggers

Not the same as prediction. AI / pattern-detection triggers a human to heightened alert when statistical conditions suggest something *may* happen.

Developed for **DARPA counterterrorism** work. Now applied in **elder-care abuse detection** (adapted to healthcare).

Snowden's key distinction — Gaussian vs. Pareto:

- **Gaussian** distributions (bell-curve) — ordered, predictable, useful for planning and best practice.
- **Pareto** distributions (power-law) — Complex, unpredictable individually, statistically inevitable in aggregate.

**You cannot predict Pareto events but you can prime humans to spot them.** 9/11 was a Pareto event. Financial black swans are Pareto. Most Complex-domain surprises are Pareto.

Source: [Jim Rutt Show EP184 transcript](https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-ep184-dave-snowden-on-managing-complexity-in-times-of-crisis/).

## Attack essays — SAFe / Agile Industrial Complex

The essay that crystallizes Snowden's public position on Scaled Agile Framework: [SAFe: the infantilism of management](https://thecynefin.co/safe-the-infantilism-of-management/).

Direct quotes:

> "SAFe is to Agile as Six Sigma was to BPR."

> "PRINCE II camouflaged in Agile language."

> "SCRUM as an approach was emasculated in a small box."

> "old stale wine forced into shiny new wineskins."

> "a massive retrograde step giving the managerial class an excuse to avoid any significant change."

> "SAFe is not only a betrayal of the promise offered by AGILE but is a massive retrograde step."

> "an obey-making machine."

Vocabulary in the essay: *"infantilism," "appalled," "pathetic," "nonsensical excess," "garrotted."*

**The underlying critique:** SAFe pushes Complex work into Complicated frames with false certainty. Original Agile (2001 Manifesto) had Complex-domain awareness. SAFe/scaled variants dragged it into Complicated with rigid ceremony.

Snowden's broader term: **"Rewilding Agile"** — the movement to return to first principles, kill the Agile Industrial Complex. See [LESS Talks 2020 talk](https://www.youtube.com/) — Snowden's YouTube on the topic.

Snowden on Agile in general:

> "The idea that you can reduce it to two-week sprints and structured Kanban boards is, frankly, nonsense."

**When context-free methods fail, practitioners fall back to "mindset" — the tell of a failing framework.**

## Attack essays — Design Thinking

- Started with substance (IDEO's origins) but commoditized into brand.
- Now sold as a template — the antithesis of what it originally was.
- **Applies Complicated methods to Complex problems.** Personas, journey maps, ideation, prototypes — as template rather than method.
- *"Case studies without theory."*

Snowden's critique is not of the original practice; it is of the *commoditization* of the practice.

## Attack essays — Systems Thinking

YouTube talk: *"Systems Thinking is Flawed and Transitionary."*

Argument:
- Systems thinking is too engineering-mechanical.
- Treats organizations as machines with leverage points.
- Ignores complex adaptive dynamics — agents with agency, distributed cognition, emergent narrative.
- *"Flawed and transitionary."*

**Cynefin's alternative:** complexity science, not systems thinking. Enabling constraints, not leverage points. Distributed cognition, not systems maps.

## Attack essays — Learning Organization (Senge)

Snowden's position: Senge's Learning Organization concept **imposes homogeneity of values, goals, and objectives** — which destroys the coherent heterogeneity that resilience requires.

A learning organization that has converged on shared vision, shared values, shared mental models has *reduced* its ability to respond to Complex-domain surprises, not increased it.

## Attack essays — Nonaka SECI / tacit-explicit conversion

Snowden's 3rd-generation Knowledge Management work explicitly counters Nonaka's SECI model.

Argument:
- Codification loses context.
- Not all knowledge should be codified.
- Tacit-to-explicit conversion (a central SECI move) destroys the situated meaning that makes tacit knowledge useful.

## Attack essays — dismissed fads

Snowden's list of frameworks he considers *"lacking underlying theory, serving consultant interests rather than organizational needs"*:

- **Six Sigma**
- **BPR** (Business Process Re-engineering)
- **Appreciative Inquiry**
- **Myers-Briggs**

These share (in his view) the same failure mode: applied context-free, generate revenue for consultants, produce cargo-cult replication.

## Refinements Snowden has emphasized since 2007

### From "Simple" to "Clear"

The 2014–15 rename was substantive, not cosmetic. "Simple" implied trivial and invited dismissal. "Obvious" briefly suggested self-evidence but read as pejorative. "Clear" conveys that the answer is genuinely visible to those in the situation — and legitimizes the domain as a real place where best practice applies.

### From "Disorder" (central) to "Aporetic + Confused"

The 2019–20 split legitimizes aporia. Pre-2019, "Disorder" carried a negative valence — the goal was to get out of it. Post-2019, aporetic is a *valid operating state* while sense-making resolves.

### Cynefin dynamics — from static to dynamic

The 2007 paper described the domains as if situations belonged in one. Post-2007, Snowden has emphasized **dynamics**:

- Constant iteration Complex ↔ Complicated.
- Migration to Clear for stable, low-risk material.
- Rare falls from Complex to Chaotic; common cliff-falls from Clear to Chaotic.
- Deliberate transient Chaos (carnival, hackathons, destabilization for reconfiguration).
- Phase shifts require energy — like latent heat.

## Frameworks Snowden has explicitly killed

- **Best practice** as a universal management concept — legitimate only in Clear.
- **Agile as a noun** — Snowden pushes back on "an Agile" as an identity or a thing you *are*.
- **SAFe** — see essays above.
- **Design Thinking as commodity template** — see above.
- **Systems Thinking** — see above.
- **Learning Organization** (Senge) — see above.
- **Nonaka SECI** — see above.
- **Six Sigma / BPR / Appreciative Inquiry / Myers-Briggs** — dismissed as fads.
- **Case studies as evidence** — retrospective coherence, not causal knowledge.
- **Explicit incentives** — de-motivate.
- **KPI targets on knowledge sharing** — miss the point entirely.
- **Focus groups / surveys** as primary sense-making — people give you the answers they think you want.

## Direct quotes worth having on hand

Quotes from post-2007 material that crystallize points better than the HBR paper does. Attributed with source.

> "Failure repeats but success rarely does." — repeated across essays

> "Especially when things become highly uncertain, case studies are the last thing you need to rely on." — repeated

> "The boundary between Clear and Chaotic is a catastrophic fold, or cliff, a collapse where the liminality in Clear is not visible and it is all too easy to walk blindly off the cliff through excessive confidence in the applicability of rigid constraints." — [cynefin.io Cynefin Domains](https://cynefin.io/wiki/Cynefin_Domains)

> "The external constraint of an insect's skeleton bounds its nature [governing], while the endoskeleton of a mammal allows for significant variation around a coherence centre [enabling]." — [cynefin.io Constraints](https://cynefin.io/wiki/Constraints)

> "[Cynefin] is a decision support framework that recognises complexity theory; Estuarine is a full-on complexity framework." — [thecynefin.co Estuarine Mapping](https://thecynefin.co/estuarine-mapping/)

> "Find out where you are and what is possible before you leap into the whole vision and goals thing." — Estuarine guidance

> "True values are not taught and declared, they evolve through the acts and interaction of the living." — on the values-as-list anti-pattern

> "If you try and set targets for knowledge sharing you have failed to understand the subject." — on KPI-targets-on-knowledge anti-pattern

> "SAFe is to Agile as Six Sigma was to BPR." — [SAFe: the infantilism of management](https://thecynefin.co/safe-the-infantilism-of-management/)

> "PRINCE II camouflaged in Agile language." — same

> "SAFe is not only a betrayal of the promise offered by AGILE but is a massive retrograde step." — same

> "an obey-making machine." — same (on SAFe)

> "The idea that you can reduce it to two-week sprints and structured Kanban boards is, frankly, nonsense." — on scaled Agile

> "Systems thinking is flawed and transitionary." — YouTube talk of the same title

> "Proud curmudgeon and pragmatic cynic." — Snowden's self-description

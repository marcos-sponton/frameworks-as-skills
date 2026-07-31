# Theory of Constraints — Worked Examples

> The cases Goldratt uses in the novels and Satellite Program, plus the modern applications documented by TOCICO, Kim, Ching, Tendon, and healthcare researchers. Use these when the user needs a concrete illustration of how a piece of the method behaves in reality.

## Canonical fictional cases (Goldratt's own)

### UniCo Manufacturing (*The Goal*, 1984)

The composite case; TOC's teaching vehicle. Alex Rogo runs a plant at UniCo that is losing money and about to be shut down. Every element of the method surfaces through this plant's turnaround.

**Key episodes:**

- **The Boy Scout hike (Ch. 13–14).** Alex takes his son's troop hiking. Herbie, the slowest scout, walks in the middle of the line. The line stretches out ahead of Herbie and bunches up behind him. Alex realizes: Herbie is the constraint of the "hike" system. Moving Herbie to the front and having the whole troop walk at Herbie's pace balances the line. Then Alex redistributes weight from Herbie's pack to the faster scouts (exploiting the constraint), and the whole troop moves faster. **This is Steps 2–3 of the Five Focusing Steps taught through a story.**

- **The dice game (Ch. 14).** Five stations, each represented by a die roll (1–6, average 3.5). Alex expects the line to produce 3.5 units per cycle on average. It doesn't — it produces significantly less, and inventory piles up between stations. **This is the proof that a "balanced line" fails under statistical fluctuations + dependent events.** The dice-game chapter alone is worth reading; it is the single most compact statement of TOC's core insight.

- **The NCX-10 machine (main plot device).** The plant's constraint is a specific machine, the NCX-10. Alex applies the Five Focusing Steps: identifies it (a walk-through reveals WIP piled in front), exploits it (no lunch break at NCX-10; quality-check parts *before* they reach it; runs it 24 hours a day), subordinates the plant to its pace (release material via the "rope"), and elevates it (repurposes an older machine to add capacity in parallel).

- **The bottleneck moves (Ch. 30 onward).** After elevating NCX-10, a heat-treatment step becomes the new constraint. Alex has to run the Five Steps again, and simultaneously fight the organization's inertia — the rules that were built around NCX-10 are still running and now cause new problems.

- **The Goal is not efficiency (Ch. 5).** Jonah refuses to discuss anything until Alex names the Goal. Alex circles through "efficiency," "quality," "shipping product," "market share" — all rejected. Jonah finally forces the answer: "to make money." Then: "how do you know you're making money?" — leading into Throughput / Inventory / Operating Expense.

### UniCo Diversified Group (*It's Not Luck*, 1994)

Alex, now division manager, applies TOC Thinking Processes to marketing and distribution across the diversified group.

**Key episodes:**

- **Marketing constraint dissolution (Cloud).** A dispute between the printing subsidiary's sales team and manufacturing about lead-time-to-quote conflicts. The Cloud reveals the assumption on the "we must have long lead times to quote accurately" arrow is false — the injection is a decoupled quote-then-commit process.
- **Distribution redesign.** The traditional min-max reorder logic is replaced by a demand-driven pull from central warehouses — the seed of what became Ptak's DDMRP.

### BGSoft ERP implementation (*Necessary But Not Sufficient*, 2000)

A fictional ERP vendor implementing at manufacturing clients. The novel walks through the finding that the technology is necessary but not sufficient — every client that succeeds also changes its measurement and incentive rules. Clients that don't change rules see the ERP make the wrong things happen faster.

Direct analogy for modern SaaS + AI implementations: buying the tool without changing the business rules and measurements produces no throughput improvement.

### Marc's engineering department (*Goldratt's Rules of Flow*, Efrat, 2023)

Marc, head of engineering, struggles to deliver multiple projects on deadline. Through an executive MBA course on flow management, he learns to apply CCPM to a multi-project environment. Central move: identify the resource *type* that is the constraint across projects (senior integration engineers), sequence project starts against that resource's capacity, cut individual task estimates and pool safety into project buffers.

The direct modern successor to *Critical Chain*, useful when the user is running a portfolio of parallel initiatives.

## Real-world documented applications

### *The Phoenix Project* mapping (Kim / Behr / Spafford, 2013 — fictional but based on real cases)

Parts Unlimited is Kim et al.'s composite retail company; Bill Palmer is a mid-level IT manager suddenly promoted to VP of IT Operations with a failing high-stakes project (Phoenix). The novel maps directly onto *The Goal*:

- **Bill Palmer = Alex Rogo.**
- **Erik Reid = Jonah.** A prospective board member; a retired manufacturing executive who understands TOC; refuses to give Bill answers, only questions.
- **Parts Unlimited = UniCo.** A once-great industrial company failing under old management practices.
- **The Phoenix project = The Bearington Plant.** A high-stakes, high-visibility failure that will determine the company's future.
- **Brent = the NCX-10.** A single senior engineer through whom every complex change must pass. The IT constraint personified.
- **The Three Ways = POOGI translated to IT.**

This is the on-ramp for software / IT users into TOC.

### Healthcare — patient flow management

Systematic review (PMC8812771, 2022) documents TOC applications across healthcare, primarily in patient-flow management: reducing emergency department wait times, throughput optimization in surgical suites, bed management in inpatient units.

Typical pattern: identify the constraint (often a specific specialist, imaging machine, or intake-triage step), exploit (no idle time at the constraint), subordinate (upstream departments release patients to match downstream capacity), elevate (add capacity only after exploiting).

Book: *We All Fall Down: Goldratt's Theory of Constraints for Healthcare Systems* (Wright & King).

### Retail — dynamic buffer management

Documented in *Isn't It Obvious?* (Goldratt et al., 2006) and extended by Ptak into DDMRP. Central move: replace static min-max reorder rules with buffers held at central warehouses and replenished from actual store sell-through. Dynamic buffer sizing adjusts to demand variability.

Companies documented using TOC-inspired distribution logic: Hitachi (parts distribution), Procter & Gamble (specific product lines), various fast-fashion retailers (Zara has been analyzed through a TOC lens post-hoc — this is not Zara's stated method but the analogy is useful).

### Manufacturing case studies

Documented by Goldratt Consulting and TOCICO:
- **Boeing** — partial TOC implementations in specific production lines.
- **General Motors** — parts distribution using TOC replenishment logic.
- **Ford** — pilot TOC implementations in specific plants.
- **TATA Steel** — DBR implementation in flat-rolled steel production.

Case-study depth varies; TOCICO conference proceedings and Goldratt Consulting's site are the primary sources.

### Project turnarounds — CCPM

Documented pattern: an engineering / R&D / construction project running late, with multiple parallel workstreams. CCPM intervention:
1. Cut all task estimates by 50%.
2. Identify the Critical Chain (resource-constrained longest sequence).
3. Aggregate the removed safety into a Project Buffer.
4. Kill multitasking — sequence work per resource.
5. Instrument buffer consumption as the primary metric.

Result documented across manufacturing engineering (Boeing 767 wing modifications), aerospace (Israeli Air Force maintenance operations documented by Goldratt), and construction. Efrat's *Goldratt's Rules of Flow* extends the pattern to digital transformation portfolios.

### Education — TOC for K–12 (Rami Goldratt)

Rami Goldratt has trained hundreds of teachers globally to apply the Thinking Processes to children's education — using the Evaporating Cloud to help children resolve conflicts, Current Reality Trees to trace causes of school problems. Documented on Goldratt Consulting's site and in Rami's speaking material.

## Teaching examples for the assistant

### The 100% utilization argument

**Setup:** a manager reports their team is at 95% utilization and proudly says they're "operating efficiently." The user asks the assistant to validate.

**Jonah-voice response pattern:**
> Before validating, ask three questions:
> 1. Which of the resources on this team is the constraint of the overall delivery pipeline?
> 2. Are the non-constraint resources also at 95% utilization?
> 3. When non-constraint resources are that busy, what are they producing that the constraint can process?
>
> If the non-constraints are at 95% utilization while the constraint is also at 95%, then either (a) the line is miraculously balanced (unlikely — statistical fluctuations plus dependent events prevent this) or (b) the non-constraints are producing WIP the constraint cannot consume, which will surface as pileups between stations or as defective work reaching the constraint. Activation is not utilization. A resource utilized is one whose activity moves the system toward the Goal. Report utilization by resource only after naming the constraint.

### The 100 problems / one constraint reframe

**Setup:** the user presents a list of five things that are "slowing us down."

**Response pattern:** those are Undesirable Effects (UDEs), not five constraints. Run a Current Reality Tree — the five UDEs will usually collapse to 1–3 root causes. From there, identify which root cause is actually the constraint (the one whose relief moves the whole system) and apply the Five Focusing Steps to it. The other UDEs will often disappear as byproducts.

### The stuck disagreement

**Setup:** two departments have been fighting about a shared resource / process / handoff for months. Standard mediation hasn't worked.

**Response pattern:** draw an Evaporating Cloud. Name the common objective (A), each side's need (B and C), the actions each demands (D and D'). The conflict looks like D vs. D'. But: why does B require D specifically? Why does C require D' specifically? Why do D and D' actually conflict? The stuck conflict rests on an assumption on one of those arrows. Find it, invalidate it, and both sides get their need without either giving up.

### The "we're too busy for improvement" objection

**Setup:** a leader resists any TOC intervention because "we don't have time to stop and analyze."

**Response pattern (Goldratt-non-fiction voice):** the reason you don't have time is that you're running the wrong measurements. The measurements drive activity that doesn't produce Throughput. Reducing the wrong activity gives you the time to think. The intervention pays for itself in weeks; refusing it costs quarters.

### The DevOps user asking about "the Three Ways"

**Setup:** user references Kim's Three Ways and wants to understand how they connect to Goldratt.

**Response pattern:** name the mapping directly.
- First Way (Flow) = Five Focusing Steps applied to the software delivery pipeline. WIP limits are subordination. Small batches are exploit-and-subordinate.
- Second Way (Feedback) = buffer management as diagnostic signal. In manufacturing, buffer color. In software, telemetry and test signal.
- Third Way (Continuous Experimentation) = POOGI as team culture. The improvement loop is the point, not any individual improvement.

Then bridge into DORA — see [[dora-accelerate]] — for the specific measurements and capabilities.

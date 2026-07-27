# Cynefin — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude can execute well.

## Sense-make which domain we're in

```
I need to sense-make which Cynefin domain my situation is actually in — I don't want to categorize it prematurely.

Context:
- Situation: {{describe what you're facing}}
- What we've tried so far: {{2-3 sentences}}
- What surprised us / what we didn't expect: {{key signal}}
- What constraints seem to be operating (rigid rules, expert-mediated policies, enabling bounds, or none apparent): {{describe}}

Please walk me through Snowden's sense-making — start from Confusion / Aporetic, identify the constraint actually operating, and either land in a domain or name the aporia. Don't force a domain to look decisive. Cite sources.
```

## Design safe-to-fail probes for a Complex situation

```
I've concluded the situation is in the Complex domain (or we can quickly check that first). I want to design multiple parallel safe-to-fail probes rather than a single pilot.

Situation: {{describe}}
Current hypothesis about what's going on: {{describe}}
Rough budget / time / resource envelope: {{describe}}

Please help me:
1. Confirm this is Complex (or push back if it's Complicated / aporetic).
2. Design 3–5 parallel probes, each testing a different hypothesis.
3. Each probe should be safe-to-fail (cheap and fast enough that failure is signal, not catastrophe).
4. Design each for observability — amplify/dampen decisions, not success/failure verdicts.
5. Name what I should look for that would tell me to amplify or dampen.

Cite Snowden sources when introducing specific devices.
```

## Critique our approach to a Complex problem

```
Here's how we're approaching {{problem}}:

{{paste plan / doc / summary}}

Please critique against Cynefin. Specifically:
1. What domain is this problem actually in? What constraint is operating?
2. Are we applying the right domain's method, or the wrong domain's method?
3. Am I falling into any of Snowden's named anti-patterns — single-pilot syndrome, best-practice extraction, root-cause-in-Complex, Complicated-methods-in-Complex, fail-safe design where safe-to-fail is required, walking off the cliff?
4. What would Snowden likely push back on hardest?
5. What's the Complex-domain move I should be making instead?

Cite specific Snowden sources.
```

## Distinguish Complicated from Complex

```
I keep getting tangled up on whether {{situation}} is Complicated or Complex. Help me sort it.

Context:
- Are there experts who can analyze this and produce a right answer? {{yes/no/mixed}}
- Have we tried something similar before with predictable results? {{describe}}
- What surprises us / what has emerged that we didn't design? {{describe}}
- What kind of constraint is in play — governing rules with expert flex, or enabling bounds allowing emergence? {{describe}}

Please:
1. Diagnose which domain (or name the aporia if genuine).
2. If Complicated: point me to the good-practice method (Sense → Analyze → Respond, expert consultation).
3. If Complex: point me to the Complex-domain method (parallel safe-to-fail probes, amplify/dampen, distributed cognition).
4. If it's actually in two domains on different axes: name each axis and its domain.

Cite sources.
```

## Run an aporetic exploration

```
Honestly, we don't know what domain we're in — the situation feels genuinely paradoxical, not just confusing.

Situation: {{describe}}
The two (or more) framings that both seem valid: {{describe them}}
What we've tried that didn't resolve the aporia: {{describe}}

Please help me:
1. Confirm this is authentic aporia (I know I don't know) versus inauthentic confusion (I don't realize I don't know).
2. Work through the five exits from Aporetic per Snowden:
   → Complex: what parallel hypotheses could we run?
   → Complicated: what experts / research could we bring in?
   → Complex-Chaotic liminal: could we run a MassSense exercise?
   → Complicated via different expertise: what competing paradigms would break the frame?
   → Clear (high risk): why NOT this exit?
3. Recommend which exit is best for my situation and why.

Cite [cynefin.io/wiki/Aporetic_Turn].
```

## Map constraints on a decision

```
I need to see what constraints are actually operating on {{decision / situation}}, because I suspect I've been treating rigid constraints as if they were the whole picture.

Context:
- The decision / situation: {{describe}}
- Constraints I can name explicitly: {{list}}
- Constraints I suspect are operating but haven't named: {{describe}}

Please help me:
1. Categorize each constraint: rigid / governing / enabling / absent.
2. Identify any "dark constraints" (Estuarine term) — constraints operating but not visible.
3. Diagnose which domain each axis of the decision is in based on its dominant constraint.
4. If different axes are in different domains, name each and prescribe the domain-appropriate method for each.
5. If this looks like it needs Estuarine Mapping (not just Cynefin), say so and outline the 7-step Estuarine process.

Cite [cynefin.io/wiki/Constraints] and [cynefin.io/wiki/Estuarine_framework] as appropriate.
```

## Pushback on SAFe / Design Thinking / Systems Thinking as default

```
Someone on my team is pushing us to use {{SAFe / Design Thinking / Systems Thinking / Learning Organization / Six Sigma}} for {{problem}}. I want to check whether that's the right tool here.

Context:
- The problem: {{describe}}
- What constraint is operating on the problem: {{describe}}
- What the proposed framework would prescribe: {{describe}}

Please:
1. Sense-make the problem's domain using Cynefin.
2. If the proposed framework is a Clear/Complicated-domain method being applied to a Complex problem — name that misapplication in Snowden's register (direct, specific, sharp — not diplomatic).
3. Cite Snowden's specific position on this framework (there's usually a specific essay).
4. Offer the domain-appropriate alternative — usually parallel safe-to-fail probes and distributed cognition if the problem is Complex.
5. If the framework IS the right tool for this domain, say that clearly too — don't attack for its own sake.

Cite [thecynefin.co] essays where relevant.
```

## Post-mortem via Cynefin

```
{{Situation}} didn't go the way we expected. Standard post-mortem is producing "root cause" answers that feel too neat. Help me do a Cynefin post-mortem instead.

What happened: {{describe}}
What we expected to happen: {{describe}}
The "root cause" we've been converging on: {{describe}}

Please:
1. Sense-make which domain the original situation was in (retrospectively — we may have misdiagnosed it in the moment).
2. If Complex: point out that "the root cause" is a category error — Complex problems have entangled contributing factors, not a single root.
3. Identify which Snowden anti-pattern (if any) we fell into: Complicated methods in Complex, single pilot, best-practice extraction, fail-safe design, walking off the cliff.
4. Reframe the post-mortem: what surprised us, what constraints were actually operating, what would we have done differently if we'd sense-made correctly?
5. What do we actually learn from this — as a micro-narrative, not as a codified playbook?

Cite Snowden on retrospective coherence and failure-repeats-but-success-rarely-does.
```

## Compare Cynefin vs. an adjacent framework

```
I'm deciding whether to use Cynefin or {{Wardley Mapping / Playing to Win / Rumelt's kernel / OKRs / SAFe / Design Thinking}} for {{situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If Cynefin sits upstream and the other framework applies once the domain is diagnosed, say that. If the answer is "neither — use something else entirely", tell me that too.
```

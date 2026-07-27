# 7 Powers — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude can execute well.

## Analyze a specific company's Powers

```
Analyze {{company}} using Hamilton Helmer's 7 Powers.

Please:
1. Identify which of the 7 Powers {{company}} plausibly has, if any.
2. For each, name the specific Benefit (in cash-flow terms) and the specific Barrier (mechanism that prevents arbitrage).
3. Run the 3 S's screen (Superior, Significant, Sustainable) on each.
4. Contrast against the look-alike that fails the test — e.g., operational excellence for Process Power, network effects for Network Economies, brand recognition for Brand Power.
5. Identify what stage the company is in (Origination / Takeoff / Stability) and which Powers are still on the table.
6. Cite Helmer sources when introducing a specific concept. Tag any case that isn't Helmer's own writing as *applied*.
```

## Critique a founder's moat / competitive-advantage claim

```
Here's a founder's claim about their competitive advantage:

{{paste claim}}

Please critique this using Helmer's 7 Powers.

Specifically:
1. What Benefit are they claiming, in cash-flow terms?
2. What Barrier are they claiming — the specific mechanism that prevents competitors from arbitraging the Benefit away?
3. Which of the 7 Powers does that Barrier map to?
4. Which look-alike does this most resemble (operational excellence, network effects, brand recognition, data scale, speed, "great team", first-mover)?
5. Does it pass the 3 S's — Superior, Significant, Sustainable?
6. Given the company's stage, is the Power they're claiming even on the table?
7. What would be a stronger claim they could make (if any)?

Adam D'Angelo (cited by Helmer) said nine out of ten founders incorrectly assert their competitive advantages. Apply that skepticism.
```

## Evaluate a strategy doc through 7 Powers

```
Here's a strategy doc:

{{paste content}}

Please evaluate the durability of the strategy using Helmer's 7 Powers.

Specifically:
1. Does the doc name a specific Power (from the 7) as the source of durable returns? If it uses generic "moat" or "competitive advantage" language, translate.
2. For any Power claim, is there a specific Barrier mechanism named?
3. Are they trying to build a Power that's off-the-table for their stage?
4. Are they confusing operational excellence with Process Power, network effects with Network Economies, brand recognition with Brand Power, or data scale with Power?
5. What's missing? Is Statics being confused with Dynamics — i.e., are they diagnosing a mature company's Power and assuming they can design their way to the same Power in a young company?
6. What's the strongest actual claim they could make, and what's still speculative?
```

## Sequence Powers for a stage-appropriate strategy

```
I'm working on {{company / product}} at {{stage — pre-PMF / just past PMF / scaling / mature}}.

Please help me think about which Powers are on the table right now using Helmer's three-stage model.

Specifically:
1. What stage am I actually in (Origination / Takeoff / Stability)?
2. Which of the 7 Powers are available in this stage? (Origination = Counter-Positioning + Cornered Resource; Takeoff = Scale + Network + Switching; Stability = Branding + Process.)
3. Which Powers am I trying to build that are actually off-the-table for my stage?
4. For each available Power, what would the invention need to look like? (Helmer: "invention is the mother of Power.")
5. If I miss the window, what's foreclosed?
6. Given all of the above, what's the highest-leverage Power to build toward next?
```

## Competitor teardown

```
Please do a 7 Powers competitor teardown of {{competitor}}.

Follow Helmer's diagnostic:
1. Start Barrier-first: what actually stops rivals (including me) from doing what {{competitor}} does? Push until you get to a specific mechanism, not a feeling.
2. Map the mechanism to a Power type using the Barrier → Power table.
3. Enumerate multiple Powers if they compound (Netflix has 3 stacked).
4. Contrast each against its look-alike.
5. Identify what stage they're in and whether they still have windows open for additional Powers.
6. Assess how competitive I can be against them — what Powers they DON'T have that I could build.
7. Cite Helmer sources; tag applied cases (TSMC, ASML, Nvidia AI, etc.) as *applied* if I bring them in.
```

## Second-invention decision

```
I run {{company}}. We've reached PMF on {{first business}}. I'm considering whether to build a second business.

Please apply Helmer + Chenyi Shi's "Second Invention" framing (from the Trium Group interview and Acquired 2023 episode).

Specifically:
1. What Powers does our first business have (if any)? Name them with Benefit + Barrier.
2. Would the second business inherit any of those Powers, or would it need to build its own?
3. If it needs to build its own, what stage would it start at (Origination), and which Powers are available?
4. Amazon → AWS, Nintendo → games, Nvidia → CUDA are the pattern cases. Is my second-business idea shaped like any of these?
5. Most companies at PMF fail at second inventions. What's the honest bar my proposed second business would have to clear?
```

## Statics vs. Dynamics check

```
I've been thinking about {{company or Power}} and I want to make sure I'm not conflating Statics and Dynamics.

Please:
1. Name what I'm doing — am I diagnosing a Power (Statics) or trying to design my way to a Power (Dynamics)?
2. If Statics: is my diagnosis complete? Benefit + Barrier for each Power identified?
3. If Dynamics: what invention would produce the Power? Am I assuming planning can substitute for invention (Helmer: "planning rarely creates Power")?
4. What stage of the business is this? Are the Powers I'm reasoning about even available at this stage?
5. Push back if I'm treating "identifying a Power in a mature company" as evidence I can build the same Power in a young one.
```

## Compare 7 Powers vs. an adjacent framework

```
I'm deciding whether to use Helmer's 7 Powers or {{other framework — e.g., Rumelt's kernel, Martin's Playing to Win cascade, Porter's Five Forces, Wardley Mapping}} for {{my situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If the answer is "neither, use something else entirely", tell me that too.

Reference points:
- Rumelt is diagnosis-first; use when the question is what's the crux.
- Martin is choice-first; use when the question is how to integrate strategic choices.
- Porter is industry-first; use when the question is whether the industry admits Power at all.
- Helmer is durability-first; use when the question is whether returns can persist.
```

## Test whether "moat" language is really Power

```
Someone is talking about {{company}}'s "moat" as {{description}}.

Translate this into Helmer's 7 Powers vocabulary:
1. What Benefit is implied — in cash-flow terms?
2. What Barrier is implied — the specific mechanism that stops arbitrage?
3. Which of the 7 does the Barrier map to?
4. If it maps to none, name the look-alike and explain why it fails the Barrier test.
5. Give the honest verdict — is this Power (name which one), or is it a temporary advantage misnamed as a moat?
```

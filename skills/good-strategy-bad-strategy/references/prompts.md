# Good Strategy Bad Strategy — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude can execute well.

## Start a diagnosis from scratch

```
I'm facing a challenge with {{my situation}} and want to think through it using Rumelt's kernel.

Context:
- Company / product: {{describe}}
- Stage: {{seed / growth / mature — if pre-PMF, note that explicitly}}
- What's happening / what's stuck: {{3-5 sentences}}
- What I think the problem is: {{one sentence — but understand I might be wrong about this}}

Please:
1. Push me past my stated problem — repeat "why is that hard?" until we hit bedrock.
2. Help me find the crux — the pivotal challenge that is both important AND addressable.
3. Draft a diagnosis, then a guiding policy, then coherent actions.
4. Challenge me if my guiding policy is a goal in disguise.
5. Check whether my actions actually reinforce each other (Southwest test).
6. Cite sources when you introduce a device.
```

## Critique a strategy document

```
Here's a strategy doc I'm looking at (mine or someone else's — either way, be honest):

{{paste content or attach file}}

Please critique it against Rumelt's kernel. Specifically:
1. Is there a real diagnosis, or is the "diagnosis" just a restatement of the problem in aspirational language?
2. Is the "guiding policy" actually a policy — or is it a goal, a value, or a list of priorities?
3. Do the actions cohere (mutually reinforce), or do they merely avoid contradicting?
4. Is there fluff? Point to it and translate it to plain content (do a "customer-centric intermediation → it is a bank" move).
5. Are there conflicting objectives (growth AND profit, avoid losing AND avoid war, etc.) — a null-set strategy?
6. Where's the crux? Is it named explicitly, or hand-waved?
7. What would Rumelt likely push back on hardest?
```

## Find the crux

```
I have a set of challenges I'm juggling. Help me find the crux — the pivotal one that's both important and addressable.

Challenges I'm facing:
1. {{challenge 1}}
2. {{challenge 2}}
3. {{challenge 3}}
4. ...
(list all — 5, 10, whatever)

Apply Rumelt's crux-finding heuristics:
- Which is most pivotal — if we solved everything else but not this one, would we still fail?
- Which is actually addressable with coherent action, not just important?
- Which are structural (constraints on the logic) vs. emotional (what people complain about)?
- What am I circling without naming?
- Do WWHTBT: for each, what would have to be true for the strategy to succeed? Which "have to be true" items am I least confident in?
```

## Run "why is that hard?" until bedrock

```
Here's what I think the problem is: {{stated problem}}.

Please do the "why is that hard?" method — ask me why my stated problem is hard, then why *that* answer is hard, then why *that* is hard. Don't stop at the first plausible answer; keep drilling until we're at something structural. That's the crux (or close to it).
```

## Distinguish action agenda from Standard Narrative

```
Here's our public strategy document ({{paste or attach}}) — the one we show investors, employees, and press.

Rumelt suggests keeping the Standard Narrative (values, aspirations, long-term positioning) for external audiences, and working from a separate **action agenda** internally — the diagnosis + guiding policy + coherent actions we actually operate from.

Help me identify:
1. What in this doc is Standard Narrative (fine to keep for external use)?
2. What action agenda is missing? What are we actually going to do in response to what diagnosed challenge?
3. Draft the internal action agenda that this document is masking.
```

## Reverse-engineer a competitor's strategy

```
Help me reverse-engineer {{competitor name}}'s strategy using Rumelt's kernel.

Try to infer:
1. What crux they've diagnosed (from what they've done, not what they say).
2. What guiding policy is visible in their public behavior.
3. What actions cohere (or fail to cohere) around that policy.

Focus on what they DO, not what their investor decks say. Look at hiring patterns, capital allocation, product moves, acquisitions.

If it's not clear (competitor is either random or their strategy is well-hidden), say so — don't manufacture a coherent story that isn't there.
```

## Run a mini-Foundry on your own team

```
I'm running a strategy meeting next week with {{who's attending}}. I want to use Rumelt's Foundry method rather than produce another vision-mission-values deck.

Walk me through the Foundry sequence adapted for our size and time budget ({{how long}}):
1. Ground in context and past success/failure
2. Generate 8-10 challenges openly
3. Cluster and winnow
4. Filter by importance × addressability
5. Ask "why is that hard?" for the remaining candidates
6. Isolate the crux
7. Design guiding policy + coherent actions
8. Force one-sentence "instant strategy"
9. Red-team by role-playing competitors
10. Swearing in — verbal commitment

Give me a facilitator's guide with prompts I can use in the room.
```

## Test whether a proposed strategy is coherent

```
Here's what I'm thinking of doing: {{draft strategy}}

Apply the Southwest coherence test:
1. Does each action support every other action, or do they merely not contradict?
2. Could a competitor copy any single element without dismantling their existing business? (If yes, that element isn't part of a moat.)
3. What's my weakest link (chain-link logic)? What's the ceiling on my performance?
4. If I removed the second-most-important action, would the rest still work?
```

## Pivot decision with Rumelt

```
I'm considering pivoting from {{current path}} → {{proposed pivot}} because {{reason}}.

Apply Rumelt's diagnosis-first pivot criteria:
1. What's my current diagnosis of the challenge?
2. What data suggests that diagnosis is wrong?
3. Is the new diagnosis actually better-supported by evidence, or am I just impatient?
4. Founder-specific: if I'm pre-PMF, this is normal (truffle-hound search). If I'm post-PMF, pivoting is much more dangerous — what's the crux I'm actually addressing?
5. Would Rumelt see this as an "audacious leap on a correctly diagnosed crux" or as "changing weapons at Midway"?
```

## Distinguish good and bad strategy in something I've written

```
Here's something I wrote calling it "strategy": {{paste}}.

Apply Rumelt's good-vs-bad-strategy diagnostics:
1. Is it long on goals and short on policy or action? (bad strategy signature)
2. Is it fluff — impressive-sounding restatement of the obvious?
3. Does it fail to identify obstacles? ("wish list" pattern)
4. Are the objectives internally contradictory? (null-set pattern)
5. Or does it name a challenge, propose a policy, and specify coherent actions? (good strategy signature)

Be honest — if it fails, tell me. Then help me rewrite it as an action agenda.
```

# Thinking in Bets — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude can execute well.

## Evaluate a past decision fairly (DQ vs. OQ)

```
I want to evaluate whether I made a good decision about {{situation}}, using Annie Duke's method.

Context:
- What I decided: {{describe}}
- What actually happened: {{outcome}}
- My current gut read: {{"good call" / "bad call" / "not sure"}}

Please:
1. Separate decision quality from outcome quality — un-collapse what I've collapsed.
2. Given ONLY what I could have known at the time, was the process good?
3. Where does resulting bias likely be pulling me right now (in one direction or the other)?
4. What would I need to see to update — from OQ back to DQ?
5. End with one testable action I can do this week to fight resulting on future decisions.

Cite Duke / Thinking in Bets / How to Decide sources when introducing a device.
```

## Set kill criteria for a current project or bet

```
I've committed to {{project / role / bet}}. I want to pre-commit kill criteria before I'm too emotionally locked in.

Context:
- What I'm committed to: {{describe}}
- What I'm hoping the outcome will look like: {{describe}}
- What "not working" might look like: {{describe, or say "I don't know"}}

Please help me:
1. Write the kill criterion in Duke's exact format: state + date.
2. Make the state OBSERVABLE — not "if things aren't going well" (unobservable), but "if X metric drops below Y for Z weeks" (observable).
3. Make the date BINDING — a specific calendar day, not "next quarter."
4. Design the precommitment — what will I do when the criterion triggers, so I don't rationalize?
5. Suggest who could be my quitting coach — someone warm enough to want me to succeed, hard enough to hold me to the criterion.
6. End with one action I do RIGHT NOW to write this down and share it.

Cite Duke / Quit and reference Everest 1996 if it helps.
```

## Run a premortem + precommitment

```
I'm about to commit to {{project / decision}}. Before I do, help me run a premortem paired with precommitment (Duke's version).

Context:
- What I'm about to commit to: {{describe}}
- My current confidence this will work: {{percentage}}
- My timeframe: {{describe}}

Please walk me through:
1. Imagine it's 12 months from now and this failed. Why? Give me the top 5 reasons.
2. For each reason, name the earliest observable signal I'd see.
3. For each signal, name the precommitted action I'd take.
4. Do the same for the status quo (staying with what I'm doing now) — what are the failure modes of NOT doing this?
5. End with one thing I write down right now.

Cite Klein for premortem origin and Duke for the precommitment pairing.
```

## Run a group decision with hygiene (3Ds / nominal group technique)

```
I'm running a group decision on {{topic}} with {{N people}} at {{time / offsite}}. I want to run it with Duke's decision hygiene, not as a debate.

Context:
- The decision: {{describe}}
- The group: {{describe roles / positions}}
- The current default (what happens if we don't decide): {{describe}}

Please give me:
1. A pre-meeting protocol — what each participant writes down INDEPENDENTLY before the meeting starts.
2. A meeting agenda that runs Discover → Discuss → Decide with clear time boxes.
3. Ground rules — including "nevertheless" as the disagreement move and "I don't understand" instead of "you're wrong."
4. A post-meeting protocol — what gets recorded, in a decision journal, so we can evaluate DQ separately from OQ later.
5. End with the specific move I take today to prep the group for this.

Reference Lenny 2024 and First Round Capital's protocol if relevant.
```

## Design a decision journal (for me or my team)

```
I want to start a decision journal. Help me set one up in Duke's style.

Context:
- Who's using it: {{me / team / org}}
- What kinds of decisions I want to track: {{describe}}
- Cadence I'll realistically maintain: {{describe}}

Please:
1. Give me the minimum-viable template — the fewest fields that still fight hindsight bias.
2. Include Duke's non-negotiables: confidence as a percentage, what would change my mind, alternatives considered.
3. Suggest a review cadence — when do I revisit past entries to update calibration?
4. Warn me about the most common failure modes when starting a journal (I'll probably stop within 3 weeks unless…).
5. End with the exact entry I write today for my most recent decision.

Cite Duke / How to Decide and the First Round protocol.
```

## Decide whether to quit something

```
I'm considering quitting {{project / role / relationship / initiative}}. Help me think through this using Duke's method.

Context:
- What I'd be quitting: {{describe}}
- Time / money / effort already invested: {{describe}}
- What "quitting on time" would look like vs. "quitting too early" vs. "quitting too late": {{describe or say "not sure"}}
- What I'm afraid of about quitting: {{describe}}

Please:
1. Attack the sunk cost — the invested time/money is gone regardless. What does the next dollar / next month look like?
2. Name the identity capture if there is one — am I resisting quitting because of who I'd be if I quit?
3. Check for goal-induced blindness — has the world changed since I set this goal? Have I updated?
4. Apply the "quitting on time feels like quitting too early" test — does the fear I'm quitting too early actually match what a well-timed quit feels like?
5. If I do quit, what's the kill criterion for the NEXT thing so I don't repeat the pattern?
6. End with one concrete action I take today — either commit to quitting on a specific date, or write the kill criterion that would trigger the quit.

Cite Duke / Quit. Reference Butterfield/Slack (successful quit), Wilkinson/Flow (failure to quit), or Sasha Cohen (identity capture) as fits.
```

## Calibrate my confidence on a claim I'm making

```
I'm about to say / write / commit to {{claim}}. I want Duke to force me to calibrate before I do.

Context:
- The claim: {{describe}}
- Why I believe it: {{describe}}
- What I'm going to do because of it: {{describe}}

Please:
1. Force me to give a percentage. Not "very confident" — a number.
2. Give me upper and lower bounds (most people are overconfident on width).
3. Run "wanna bet?" — at what odds would I actually bet on this?
4. What's the evidence I'd need to see to update the percentage? In which direction?
5. What's the outside view (Kahneman) — how often are claims like this correct in the reference class?
6. End with the specific number I write down as my calibrated confidence, and the signal that would move it.

Cite Duke and reference Tetlock / Superforecasting on calibration.
```

## Do a post-mortem on a project that failed / succeeded

```
Help me run a post-mortem on {{project}}, using Duke's method — I want to actually learn, not just narrate.

Context:
- What happened: {{describe}}
- Current team narrative about why: {{describe}}
- What we're planning to change going forward: {{describe or "haven't discussed yet"}}

Please:
1. Un-collapse DQ from OQ. What we're calling "the reason it succeeded/failed" — how much of that is process quality vs. luck?
2. Fight hindsight bias — what would we have said 6 months ago about the likely outcome? Do we have decision-journal entries or are we reconstructing?
3. Find the resulting in the current team narrative — where are we treating outcome as evidence of process?
4. Extract the actual lessons — what should we do differently that has evidence, not story?
5. Set decision-journal practice for the NEXT project so we don't do this reconstruction again.
6. End with one concrete change we implement this week.

Cite Duke / Thinking in Bets and reference Pete Carroll if it lands.
```

## Compare Thinking in Bets vs. an adjacent framework

```
I'm deciding whether to use Duke's Thinking in Bets or {{other framework — e.g., Rumelt's kernel, Playing to Win, Kahneman, Tetlock, Duckworth}} for {{my situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If the answer is "neither, use something else entirely", tell me that too.

Bias: default to naming when Duke's toolkit is the WRONG tool — reflex intuition, routine operational decisions, diagnosis-first strategy questions.
```

# Never Split the Difference — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude or Codex can execute well.

## Salary negotiation — run me through the sequence

```
I have a salary negotiation coming up. Please run me through the Voss / Black Swan sequence.

Context:
- Role: {{title, level, company type}}
- Target base I actually want: {{$X}}
- Current base (if applicable): {{$Y}}
- Comparable market: {{what you know about the band for this role/level}}
- What the employer has said so far: {{their opening question / any number they've floated}}
- My BATNA: {{other offers, current job, walk-away plan}}
- Anything I know about their constraints: {{comp bands, budget cycle, timing pressure}}

Please:
1. Should I open with a range (they asked first) or use Ackerman (I'll be responding to their number)? Explain.
2. Draft the exact opening line I'd use.
3. If they counter low, draft the labels + calibrated questions I should use before I make my next move.
4. What Black Swans should I be hunting for? Give me 3-5 specific things I don't yet know that could change the deal.
5. Walk me through what the final-number move looks like — non-round precision + non-monetary throw-in ideas that fit this specific role.
6. What accusations might the employer have about my ask? Draft the accusation audit if I need to preempt.
7. Where might I be reaching for compromise / meet-in-the-middle? Push back on that reflex.
```

## Discount defense / fee holding — someone wants to pay me less

```
I sent a proposal for $X and the client / prospect wants me to come down. Please help me hold the fee using the Voss / Full Fee Agent method.

Context:
- What I proposed: {{fee, scope, terms}}
- What the counterpart said: {{exact words or paraphrase — the discount ask}}
- Their apparent reason: {{what they said out loud}}
- What I suspect the real reason is: {{internal budget, comparable proposals, fear of overpaying, etc.}}
- My walk-away: {{would I take a smaller deal? no deal? at what point?}}
- Relationship stage: {{new prospect / long-standing client / referral}}

Please:
1. Draft the accusation audit — what are 4-5 things the counterpart is probably thinking that I should name up front?
2. Draft the forced-empathy line I should use (some form of "How am I supposed to do that?" tailored to this specific ask).
3. If they hold their position, what labels and calibrated questions should I use to hunt for the Black Swan (the real reason)?
4. What non-monetary throw-ins could I offer that hold the fee but let them feel they got something?
5. Draft the no-oriented walk-away question if it comes to that.
6. Warn me clearly if my current framing is heading toward split-the-difference / compromise — that's the failure mode this skill exists to interrupt.
```

## Hard conversation prep — I have to deliver bad news

```
I have to deliver bad / difficult news to {{someone — client, boss, co-founder, partner, family member}}. Please help me prep using the Voss method.

Context:
- The news I'm delivering: {{one paragraph — what it is, why now, what will change}}
- Who I'm delivering it to: {{relationship, how they're likely to react}}
- What I want as an outcome after the news lands: {{just for them to accept it / for a new arrangement / for a negotiation / for a preserved relationship}}
- Constraints I'm operating under: {{time, contractual, personal}}

Please:
1. Draft the accusation audit — every accusation the counterpart could realistically have about me for delivering this. Then help me prune to the 4-5 that are actually likely.
2. Draft the exact opening lines using the accusation audit before I deliver the news itself.
3. Draft the news delivery — short, direct, in late-night FM DJ voice (no urgency, no over-explanation, no defensiveness).
4. Anticipate the counterpart's likely responses. For each one, give me the mirror + label + calibrated question I should use.
5. What Black Swan should I be alert for during the conversation — what might they reveal that I don't currently know?
6. What's the "warm last impression" move I should plan for closing the conversation, even if the middle was hard?
```

## Ultimatum received — the counterpart said "take it or leave it"

```
I just got hit with an ultimatum. Please help me respond using the Voss method.

Context:
- Their exact words: {{paste or paraphrase}}
- The ultimatum's structure: {{price / timeline / terms — what specifically}}
- Their apparent deadline: {{when}}
- What I actually want as an outcome: {{describe}}
- What I know about their constraints: {{anything about why they might be issuing this ultimatum}}

Please:
1. Diagnose: is this a real constraint on their end, or a leverage move? What signals point either way?
2. Draft my first response — do NOT accept the ultimatum's frame, do NOT counter, use mirror + label + a test-the-deadline question.
3. If they push back on my response, what's the next-move sequence?
4. Draft the calibrated question that invites them out of the ultimatum frame.
5. If it comes to a walk-away, draft the no-oriented question that gives them the safe out.
6. Warn me if I'm being tempted to just accept the ultimatum — that's usually a mistake, and the reasons are worth naming.
```

## Ackerman planning — I have a specific bargaining situation

```
I have a specific bargaining situation where I need to name numbers. Please help me plan the Ackerman sequence.

Context:
- What I'm negotiating: {{describe — buying, selling, comp, terms}}
- My target (what I actually want): {{$X}}
- My walk-away: {{$Y}}
- Counterpart's opening (if any): {{$Z}}
- My BATNA: {{describe}}
- Relationship / context / stakes: {{describe}}

Please:
1. Compute the Ackerman sequence: first offer at 65% of target, then 85%, 95%, 100%. Give me all four numbers.
2. Draft the empathy + calibrated question I should use BETWEEN each raise to force the counterpart to counter before I move.
3. Recommend a specific non-round number for the final move.
4. Recommend 3-5 non-monetary throw-in options that would fit this specific deal (small on my side, valuable on their side).
5. If the counterpart is likely to be culturally / temperamentally sensitive to the 65% extreme anchor, recommend a range-play alternative instead.
6. Warn me if this situation isn't a good fit for Ackerman at all (e.g., pure-collaboration setting, or the numbers aren't the real negotiation).
```

## Stalled deal — the counterpart has gone silent

```
A deal that was moving has gone silent. Please help me hunt Black Swans and re-engage using the Voss method.

Context:
- What the deal is: {{describe}}
- Last time they responded: {{when, what they said}}
- What I've tried since: {{follow-ups, content, calls}}
- What I currently think is happening: {{my best guess}}
- What I DON'T know about their side: {{list what's opaque to me}}

Please:
1. Generate a list of 3-5 Black Swans that could plausibly explain the silence. For each one, tell me what evidence would confirm or reject it.
2. Draft a no-oriented question I could send that invites discovery without applying pressure ("Have you given up on…?").
3. If they respond, draft the mirror + label + calibrated question sequence that would surface the real dynamic.
4. Explicitly WARN me against reaching for FOMO / urgency / "checking in" / discount reflexes. Those are the wrong moves here.
5. What signal would tell me the deal is genuinely dead vs. temporarily stalled? Give me a concrete check.
6. If face-to-face becomes possible, what should I prioritize doing in the unstructured moments (small talk, break, walk to parking lot)?
```

## Draft an accusation audit for me

```
I need to draft an accusation audit for a specific situation. Please help.

Context:
- The situation: {{describe}}
- What I need to ask for / deliver: {{describe}}
- Who the counterpart is and what our relationship is: {{describe}}
- What I know about how they'll likely react: {{describe}}

Please:
1. Brainstorm 8-10 accusations the counterpart could realistically make about me / this ask. Don't self-edit — include the harsh ones.
2. Prune to the 4-5 that are actually most likely for THIS specific counterpart.
3. Draft the exact opening lines using those accusations up front, in late-night FM DJ voice.
4. Draft the pause + the ask that follows.
5. Warn me if the accusation audit isn't the right move here (e.g., the counterpart doesn't have negative anticipations — it may just be a straight conversation).
```

## Voice check — is my draft too aggressive / too fast?

```
Here's a draft email / message I'm about to send. Please voice-check it against Voss's late-night FM DJ standard.

The draft:
{{paste draft}}

Please:
1. Read it out loud (in your head) at normal pace. Does it sound urgent, aggressive, or defensive?
2. Flag any exclamation marks, urgency language, "just checking in" filler, "trust me" assertions, or "why" questions.
3. Rewrite it in Voss's voice — short sentences, no urgency, no exclamation marks, late-night FM DJ pacing.
4. Preserve MY voice — don't over-import Voss's specific phrasings if they clash with how I actually write. Adjust the tonality without hijacking my register.
5. If there's an accusation audit or calibrated question that would materially improve the draft, suggest it.
```

## Compromise-reflex intervention — I'm about to split the difference

```
I'm about to accept a compromise / split-the-difference / meet-in-the-middle deal. Before I do, please stress-test it against Voss's method.

The situation:
- What I originally wanted: {{describe}}
- What the counterpart wanted: {{describe}}
- The proposed compromise: {{describe}}
- Why I'm considering accepting it: {{honest reason — often "easier", "faster", "reasonable", "keeps the relationship"}}

Please:
1. Diagnose: is this a genuine best-fit deal (the middle IS the right shape after real discovery), or is it split-the-difference reflex?
2. If it's reflex — cite Voss's specific warning about compromise ("we compromise because it is easy and because it saves face") and identify what real deal shape I might be missing.
3. What Black Swans might I not yet have uncovered that could reshape the deal?
4. Draft what one more round of Ackerman + calibrated questions could look like if I don't accept the compromise.
5. If the compromise IS actually the right deal — say so clearly. Voss's method doesn't say never accept a middle; it says never REACH for one as the default.
```

## Compare Voss vs. an adjacent framework

```
I'm deciding whether to use Voss / Never Split the Difference or {{other framework — e.g., Getting to Yes, Challenger Sale, Sandler, Cialdini}} for {{my situation}}.

Help me pick. If the answer is "use both, in this sequence", tell me the sequence. If the answer is "use a different framework entirely", tell me that too.

Specifically:
1. Which framework fits my situation best given the negotiation phase, counterpart dynamics, and where I'm stuck?
2. Are they complementary — and if so, how would they compose?
3. Where does each framework specifically NOT help me?
```

## Full-Fee Agent mindset check

```
I'm a {{consultant / agency / freelancer / founder-CEO}} selling my own services and I keep discounting. Please diagnose using the Voss / Full Fee Agent lens.

Context:
- What I sell: {{describe}}
- My typical fee: {{$X}}
- How often I discount: {{estimate}}
- Reasons I usually give myself for discounting: {{list — "it's a good relationship", "I want the case study", "cash flow", "they're comparing to cheaper alternatives"}}
- What I suspect the real reason is: {{honest read on my own reflex}}

Please:
1. Diagnose which of my usual reasons are legit vs. Full-Fee-Agent failure modes.
2. What positioning or upstream problem might be showing up as discount pressure? (If so, point me to [[obviously-awesome]] — this may not be a Voss problem at all.)
3. If it IS a Voss problem, walk me through the specific mindset move (from The Full Fee Agent) I should be running when the discount conversation starts.
4. Draft the exact opening line I should use the NEXT time a client asks for a discount.
5. Give me a check I can use in real time to catch myself reaching for the reflex.
```

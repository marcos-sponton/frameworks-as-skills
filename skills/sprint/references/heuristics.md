# Sprint — Heuristics, Do's, Don'ts, Gotchas

> The practical devices that separate running a Sprint well from running "a workshop week with sticky notes." Attribution is to the 2016 book unless noted otherwise.

## Do's

### Get a real Decider in the room

The single most important setup decision. The Decider must be someone with genuine authority — CEO, VP of Product, founder, head of the business unit. Not a proxy. Not "she couldn't make it, so I'll represent her."

Without a Decider, Wednesday's Supervote has no teeth. The team debates, compromises, and produces a watered-down prototype that tests nothing decisively.

**Knapp's frame:** "Without a Decider, decisions won't stick." — *Sprint*, Ch. 2.

**Contingency:** If the Decider can't commit to the full week, at minimum they must be present Monday (to set the target) and Wednesday (to cast the Supervote). Monday and Wednesday are the Decider's non-negotiable days.

### Ban devices from the sprint room

Phones and laptops are the enemy of the sprint. Knapp's rule: no devices in the room during sprint hours (10 AM - 5 PM). Put them in a pile. Check during breaks.

This feels extreme. It is extreme. And it is the difference between a sprint that produces real focus and one that produces polite half-attention.

**Knapp's frame:** "We know it sounds crazy to ask people to put their phones away. But it works." — *Sprint*, Ch. 3.

### Keep the team at 7 or fewer

Every person above 7 adds coordination overhead and slows every exercise. Knapp tested this across 100+ sprints at GV. Seven is the practical ceiling.

If you have more than 7 stakeholders who "need to be involved," have the extras join as experts during Monday's Ask the Experts session — 15-minute slots, then they leave.

### Write real words in the prototype

"Lorem ipsum" is the fastest way to produce a prototype that teaches nothing. Customers react to words. Headlines, button labels, error messages, pricing — use real words, even if imperfect.

**Why:** The words are often the product. If the headline doesn't land, no amount of UI polish saves it. If the CTA is confusing, the flow breaks regardless of layout.

**Assign a Writer role on Thursday.** This is not optional. Someone whose job is words, all day.

### Start with how customers will find you

The Storyboard (Wednesday) must begin with an **opening scene** — how does the customer encounter this product? Google search result? Email? Friend's text? App store listing?

Most sprint teams skip this. Huge mistake. The first impression shapes everything that follows. If the Google search result doesn't make sense, customers never reach the product.

### Recruit customers early

Recruit Friday's 5 test customers **the week before the sprint.** Do not leave this to Thursday afternoon. Recruiting takes longer than you think. Screen candidates to match the target customer profile.

### Do a trial run Thursday afternoon

At 3-4 PM Thursday, the Interviewer walks through the finished prototype as if they were a test customer. The full team watches. This catches broken links, missing screens, confusing transitions, and typos — all things that would waste a precious customer session on Friday.

### Take notes on individual sticky notes during Friday tests

One observation per sticky note. Color-code: green (positive), red/pink (negative), yellow (neutral). This makes pattern-finding after the 5th interview much faster than reviewing pages of notes.

## Don'ts

### Don't brainstorm in groups

This is the single most counterintuitive rule in the sprint. Knapp is explicit: **group brainstorming produces worse ideas than individual work.**

The research backs this up (Knapp cites Charlan Nemeth's work at UC Berkeley). In groups, people anchor on the first idea spoken, defer to seniority, and self-censor. The sprint's antidote: **work alone (Tuesday), then evaluate together (Wednesday).**

**Knapp's frame:** "Working alone gives everyone time to think and explore solutions on their own terms. It also eliminates the anchoring effect of hearing someone else's idea before you've had a chance to think about the problem yourself." — *Sprint*, Ch. 7.

If someone suggests "let's brainstorm" during the sprint, redirect them to the 4-step sketch process.

### Don't build a real product on Thursday

The Thursday prototype is a **facade** — a realistic-looking fake. It looks like it works; it doesn't actually work. A movie set, not a house.

**Common mistake:** Engineering-heavy teams want to build a functional MVP. This is wrong for two reasons:
1. You can't build a real product in one day and have it be good enough to test.
2. A functional product creates attachment — the team resists throwing it away, and the prototype stops being disposable.

**Knapp's term:** "Goldilocks quality" — real enough that customers react honestly, rough enough that you can throw it away tomorrow.

### Don't skip Friday

Testing with customers is the point. Everything Monday through Thursday leads to Friday. Skipping Friday — "we're confident enough," "let's just build it," "we ran out of time" — defeats the entire method.

Teams that skip Friday have run a workshop, not a sprint. They've generated ideas and made decisions, but they haven't validated anything.

### Don't test with fewer than 5 customers

Five is the minimum for pattern detection. With 3, you might see a pattern that's actually noise. With 5, if 3+ people react the same way, it's signal.

Knapp (drawing on Nielsen's research): "After just five interviews, big patterns will emerge." — *Sprint*, Ch. 14.

### Don't let the Interviewer guide the customer

During Friday's test, the Interviewer asks questions and observes. They do not:
- Explain how the product works.
- Correct misunderstandings.
- Say "actually, you should click here."
- Show disappointment when the customer misses something.

Customer confusion is data. It means the prototype failed to communicate, which is exactly what you need to know.

### Don't run a sprint without Sprint Questions

Sprint Questions are the frame. Without them, you build and test a prototype but don't know what you're looking for. The test produces anecdotes, not answers.

**Bad:** "We sprinted and it went well." → What did you learn? "People liked it."
**Good:** "We sprinted to answer: 'Will first-time customers understand our value prop in the first 10 seconds?' Answer: No. Three of five customers thought we were a subscription service, not a marketplace."

### Don't compromise on Wednesday

The biggest risk on Wednesday is the "Frankenprototype" — combining elements from multiple sketches to make everyone happy. This produces a solution that nobody believes in and that tests nothing decisive.

The Supervote exists to prevent this. The Decider picks one direction. If two strong options exist, run a Rumble (test both), not a merger.

## Anti-patterns

### "The sprint without a question"

**Symptom:** The team runs the sprint but never wrote Sprint Questions on Monday.
**Result:** Friday's test produces impressions but no answers. The team says "that went well" but can't articulate what they learned.
**Fix:** Spend 20 minutes on Monday writing Sprint Questions. Revisit them before Friday.

### "The polite sprint"

**Symptom:** Everyone is nice. The Straw Poll is unanimous. No one disagrees. The Supervote feels ceremonial.
**Result:** The prototype tests the consensus idea, not the best idea. And consensus ideas tend to be safe and boring.
**Fix:** Crazy 8s forces divergent thinking. Anonymous Solution Sketches force evaluation on merit, not authorship. If the group is still too convergent, the Facilitator should explicitly invite contrarian sketches.

### "The Facilitator-Decider collapse"

**Symptom:** The Decider also runs the exercises.
**Result:** The Decider's facilitation biases the process — their Map emphasis, their HMW priorities, their questions during Speed Critique.
**Fix:** Separate the roles. The Facilitator runs the process; the Decider makes the calls.

### "The tourist sprint"

**Symptom:** Sprint team members attend selectively — "I'll be there Monday and Wednesday, but I have meetings Tuesday."
**Result:** Tuesday's sketches are thin (fewer brains, less diversity). Wednesday's evaluation is missing context (they didn't see the Lightning Demos). Thursday's prototype is rushed (fewer builders).
**Fix:** Sprint requires full-week commitment. If someone can't commit, they shouldn't be on the team. Use the Ask the Experts slot for people who can contribute a 15-minute window.

### "The feature-list prototype"

**Symptom:** The Thursday prototype shows a product with 15 features instead of testing one flow end-to-end.
**Result:** Friday's test is shallow — customers scan the features, say "looks useful," and leave. No deep reactions.
**Fix:** The Storyboard (Wednesday) must trace **one customer journey** from opening scene to completion. Depth beats breadth in a sprint prototype.

### "The post-sprint shrug"

**Symptom:** Sprint ends Friday afternoon. Monday morning, the team goes back to business as usual. No one acts on what they learned.
**Result:** The sprint was a fun week but didn't change anything.
**Fix:** End Friday with a 30-minute debrief: What did we learn? What will we do next? Who owns the next step? Schedule the follow-up meeting before people leave the room.

## Pro tips

### Use Keynote/Slides for the prototype, not code

Knapp's preferred prototyping tool is Keynote or Google Slides. It's fast, anyone can use it, it produces realistic-looking screen flows, and — most importantly — it's disposable. Nobody gets attached to a Keynote file.

Code prototypes create attachment, take longer, and optimize for functionality when the goal is to test desirability and clarity.

### The "two-sprint" pattern

Some problems are too big for one sprint. Run two sprints back-to-back:
- **Sprint 1:** Test the overall concept and value proposition.
- **Sprint 2:** Dive deeper into the specific flow that tested well in Sprint 1.

Leave at least one week between sprints to process results and recruit new customers.

### Experts as Monday's secret weapon

Monday's Ask the Experts session often produces the most important insight of the week — the one that reframes the problem. Choose experts who work close to the customer and know what's actually broken, not what leadership thinks is broken.

### The Facilitator's two hardest moments

1. **Monday afternoon:** The team doesn't want to narrow to one target. They want to "cover everything." Hold the line.
2. **Wednesday afternoon:** The team wants to combine sketches instead of choosing one. Hold the line. The Supervote exists for this moment.

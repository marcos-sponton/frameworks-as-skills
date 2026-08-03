# Demand-Side Sales — Method

> The demand-side method in Moesta's own terms. Fidelity is the point — the method is opinionated, and collapsing "demand-side" into generic JTBD destroys what makes it useful.

## The core axiom

> "People don't buy products; they hire them to make progress in a particular circumstance."

**Progress** is Moesta's unit of measure — deliberately chosen over "need", "pain", "job", "outcome". This is load-bearing. Say "the progress they're trying to make" — never "user needs" or "pain points."

A Job to Be Done *is* the progress the person is trying to make. Language slippage happens constantly where "job" gets collapsed into "task" or "outcome" — Moesta resists this. A well-written Job is a *progress statement in context*, not a task statement.

## Supply-side vs. demand-side — the load-bearing distinction

This is the wall. Everything follows from which side you start on.

| | Supply-side | Demand-side (Moesta) |
|---|---|---|
| Reference point | The product / technology / company | The customer's life circumstance |
| Starting question | "Who would buy this? What job could this do?" | "What progress is this person struggling to make? What made today the day?" |
| Research method | Job maps, outcome statements, quantitative unmet-need scoring | Timeline reconstruction via Switch Interview of *recent buyers* |
| Deliverable | Job Map / Job Statement / Outcome list | Forces diagram + Timeline + verbatim customer language |
| Best used for | Strategy, market sizing, feature prioritization | Understanding causation of a switch, sales/marketing, killing features |
| Vocabulary | "Job executor", "desired outcomes", "job steps" | "Struggling moment", "the Forces", "vector of progress", "context creates value" |

**Moesta's framing:**
> "Christensen gave us the theory. My job was to make it operational."
> "Supply-side is 'we built this, who wants it?' Demand-side is 'what progress are they trying to make, and what do they hire to do it?'"

**The wall:** most organizations cannot flip the lens. They intellectually agree with the demand-side framing but operationally default to supply-side thinking within minutes. The skill's job is to keep the conversation on the demand side.

## The Four Forces of Progress

The equation: **Push + Pull > Anxiety + Habit = Switch**.

All four must be understood. Most organizations work on one or two. That's why their conversion is broken.

### 1. Push of the Situation

Friction, frustration, a broken moment with the *current* solution. Not "meh" — the status quo has to become unacceptable.

**What generates Push:** a question the customer can't answer with the current setup. A new metric that reframes their situation. A visible failure. A story from someone similar who made progress. An obvious-but-overlooked truth that becomes impossible to unsee.

**Source:** DSS101, Chapter 3; jobstobedone.org — "The Four Forces."

### 2. Pull of the New Solution

The *vision of progress* the customer imagines. Not features — the improved life. The customer hires a vision, not a spec sheet.

**Effective Pull is emotional and social, not just functional.** The mattress buyer doesn't imagine a coil spring count — they imagine waking up without back pain, their spouse being happy, feeling like they finally did something about it.

**What effective marketing does:** makes the vision of progress vivid. Casper doesn't list specs; they describe how you'll sleep. Basecamp doesn't list features; they describe the end of chaos.

**Source:** DSS101, Chapter 4; Lenny's Podcast #1.

### 3. Anxiety of the New

Fear of the unknown, learning curve, image risk, data migration risk, social risk ("what will my team think?"), performance risk ("what if it doesn't work?").

> "Anxiety is the most underestimated force in business."

**The asymmetric insight:** adding features frequently *increases* Anxiety instead of Pull. More features = more to learn = more risk = more Anxiety. This is why feature-rich products lose to simpler ones.

**What reduces Anxiety:** guarantees, money-back promises, social proof from similar customers, easy onboarding, "first win in 5 minutes", demos that let people experience progress before committing.

**What does NOT reduce Anxiety:** more features, more specifications, longer feature comparison tables, competitive matrices.

**Source:** DSS101, Chapter 5; Business of Software talk "Demand-Side Sales 101"; multiple podcast appearances.

### 4. Habit of the Present

Comfortable inertia. "The devil you know." Workarounds that have become invisible. Processes that are bad but familiar. Relationships with existing vendors. Sunk cost in the current system.

> "This is why great products lose to mediocre incumbents."

**Habit is the force most organizations forget to address.** They build a better product (Pull), they identify customer pain (Push), they even reduce Anxiety — but they never address the gravitational pull of the current way of doing things.

**What breaks Habit:** making the switching cost visible and low. Migration tools. Parallel-run periods. "Bring your data with you." Framing the switch as smaller than it feels.

**Source:** DSS101, Chapter 5; Intercom podcast; Circuit Breaker.

### Forces — structural notes

**Terminology precision:**
- Push and Habit are forces on the **current situation** (rearward-facing).
- Pull and Anxiety are forces on the **new solution** (forward-facing).
- Push + Pull = forces *for* progress. Anxiety + Habit = forces *against* progress.
- Canonical order is always Push / Pull / Anxiety / Habit. Never rearrange.

**The key operational insight:**
Organizations obsess over increasing Pull (features, marketing) and forget the asymmetric leverage on the other two: reducing Anxiety and Habit is often cheaper and faster to move the equation. A company that reduces Anxiety by 30% often gains more than one that increases Pull by 30%.

**Credit:** the Forces of Progress diagram was co-invented by **Bob Moesta and Chris Spiek**. Cite both when producing public-facing content.

## The Switch Interview — the research method

### Purpose

Reconstruct the causal chain of a specific past purchase to reveal the forces at work. The output is not "what customers want" — it's *why this specific person made this specific switch at this specific moment*.

### Who to interview

- **Recent buyers** — people who already made progress. NOT prospects, NOT leads, NOT hypothetical customers.
- If launching a new product with no buyers: interview users of the products yours would replace — "the products they'd fire if yours succeeded." (This is how Facebook Marketplace research worked — they interviewed Etsy/Craigslist/eBay users.)
- **Churned customers** are also valid — they switched *away*, and the Forces are the same in reverse.
- 10-12 interviews per round. Prefer **two rounds of 12** over one of 24. The first round reveals patterns; the second round sharpens them.
- **Intentional segment coverage** — recruit across distinct market segments, not randomly.
- Patterns emerge by interview 6-7. By 10-12 you see 3-5 distinct buying patterns covering ~90% of the market.

### Duration

30-60 minutes minimum. Equal debrief time afterward with the cross-functional team.

> "If you do it in 10 minutes, you're at the pablum level."

### Structural sequence

Composited from Moesta's own descriptions across multiple sources:

1. **Setting the stage** (~2m): "I don't have a long list of questions. I just want to hear your story." Set the frame — you're reconstructing a timeline, not interrogating.
2. **The world before the purchase** (~2m): role, context, what "normal" looked like. Ground the story in specifics.
3. **First Thought** (~3m): "What was happening the day you decided to look?" — the trigger event. Get the date. Get the context. Get the emotion.
4. **The struggle** (~4m): "What was frustrating about how you were handling this before?" Dig into the Push.
5. **Passive to Active looking** (~5m): "What did you Google?" Alternatives considered and rejected. How they learned the language of the domain. What sources they trusted.
6. **Deciding** (~5m): "What made you decide this was the one?" The tipping point. What was the final trigger? Who else was involved? What did they give up?
7. **First use / early wins** (~5m): onboarding experience. First moment of progress. First disappointment.
8. **Ongoing use** (~7m): how usage evolved. What they use vs. what they don't. Workarounds.
9. **Current pain** (~9m): what's broken now. Workarounds that signal the next switch. New struggling moments.
10. **Map the Four Forces** (post-interview, whiteboard). Do this with the team, not alone.

### Interview micromoves

These are the operational craft of the method — what separates a good Switch Interview from a survey in interview form:

- **No discussion guide.** Ask *around* pushes/pulls/anxieties/habits. Follow the story, not a script.
- **Never "why?" repeated.** "Why" drives people to rationalization and pablum. Use "tell me more" and "give me an example" instead.
- **Play back incorrectly on purpose** to trigger corrections. Getting a "no" produces richer detail than a "yes." "So you bought it because it was cheap?" "No! It wasn't about the price at all, it was about..."
- **The Columbo move:** ask the real question just as you're about to close the notebook. People relax when they think the interview is ending and say the thing they've been holding back.
- **Match the interviewee's tone and energy.** Don't impose your register.
- **The interviewer is an "empty vessel."** No leading, no validating, no reacting with surprise or judgment.
- **Talk less than 20% of the time.** If you're talking more, you're interrogating, not listening.

**Source:** DSS101, Chapters 7-9; jobstobedone.org Switch Interview recordings; Lenny's Podcast #1; June.so breakdown; SaaS Club #423.

## The Buying Timeline — six stages

Universal across purchase types (gum, software, church, mattress, career). Contra a funnel (one-directional), a timeline permits backward movement when context changes.

### 1. First Thought

"What we're doing isn't good enough." This is where demand is born — not from a marketing campaign, but from a struggling moment.

**Triggers:** questions without answers, new metrics that reframe the situation, stories from people in similar circumstances who made progress, obvious-but-overlooked truths that become visible.

**Sales role:** you can't create First Thought with advertising. But you can make the struggling moment visible to people who are living in it without seeing it. Seed content: relevant stories, new data, reframings.

### 2. Passive Looking

Learning the domain, acquiring language, no urgency. The customer doesn't know what they want yet — they're building a vocabulary.

**Sales role:** teach language, share progress stories. Be a teacher, not a pitcher.

**Mistake:** firehosing specifications. The customer isn't ready for specs — they're ready for education.

### 3. Active Looking

Wishing for features, exploring, playground mentality. Price is not yet connected to value. The customer is imagining possibilities, not making trade-offs.

**Sales role:** expand possibilities, don't close. Show what progress could look like. Let them play.

**Mistake:** trying to close during Active Looking. The customer will feel pressured and retreat to Passive Looking (or exit entirely).

### 4. Deciding

Trade-offs. This is where the sale lives or dies.

**Present exactly three options.** Never one, rarely two, never more than three. Here's why:
- Customers eliminate one first (the "albatross" — design one option to be obviously wrong for them).
- They compare the remaining two against the eliminated one — not against each other.
- This gives them a reason to choose and a story for why they chose ("I went with B because A was too X and C was too Y").

**Help them articulate why they chose.** The customer needs to justify the decision to themselves, their boss, their spouse, their team. If they can't articulate why they chose you, they can't sell you internally. Give them the language.

### 5. First Use

Must feel progress fast. Early wins matter more than feature completeness. If the customer doesn't feel "this was a good decision" within the first use, Anxiety wins and they retreat.

### 6. Ongoing Use / Habit Building

New struggles emerge. The timeline restarts. Today's Pull becomes tomorrow's Push when new context changes.

**Canonical case — AutoBooks (fintech):** built three demos — one per stage (Passive/Active/Deciding). Sales cycle cut ~50%, conversion doubled. The lesson: "same action (demo request) means completely different things at different stages." A Passive Looking demo request needs education; a Deciding demo request needs trade-off clarity.

**Source:** DSS101, Chapters 10-14; Business of Software talk; Coleman McCormick notes.

## Struggling moments — the seed

This is where all demand starts. No struggling moment, no demand.

> "The struggling moment is the seed for all innovation."
> "If your customer's not struggling, they can't see you."
> "Demand is only generated by a customer's struggling moment."

**Critical distinction:**
> "Eliminating the struggle is not progress. Customers *overcoming* the struggle is progress."

This is deeply Moesta. He doesn't believe in making things effortless — he believes in making the *right* kind of effort possible. The customer overcoming their struggle is what creates satisfaction and loyalty. Removing all friction removes all progress.

**Source:** DSS101, Chapter 2; Learning to Build; Lenny's Podcast #1; multiple podcast appearances.

## Demand-side sales — specific additions for sales teams

Same theory as the broader JTBD method, but adapted for sales execution:

- **Salesperson = concierge / coach / mentor.** Not persuader, not closer, not challenger. Help people buy without selling.
- **"Three sources of buyer energy":** struggle, curiosity, and vision. If none of these is present, there's no energy for a sale — don't force it.
- **Anti-free-trial stance.** Free prevents the commitment and effort needed for real evaluation. It produces tire-kickers, not buyers. Moesta prefers low-commitment paid pilots over free trials.
- **Marketing + Sales + CS = one lead.** Not a sequential handoff. The customer doesn't care about your departmental boundaries. One person should own the relationship across the timeline.
- **Theory, not technique.** "Schools don't teach techniques; they teach theory." Moesta insists sales teams understand the *why* of the demand-side lens before learning any specific moves.

**Source:** DSS101, Chapters 15-18; Business of Software talk; Circuit Breaker podcast.

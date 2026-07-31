# Continuous Discovery Habits — Heuristics, Do's, Don'ts, Gotchas

> The practical devices — the diagnostic tells and operational moves — that separate applying Torres's method well from doing the generic-user-research version she spends most of her essays and podcasts pushing back on. Attribution is precise: this comes from the book, this from a 2024 Product Talk essay, this from a 2025 LinkedIn post where she updated a position.

## Do's — the habits, stated as operational moves

### Interview weekly, as a trio, without exception

The cadence IS the practice. Once you skip a week, you're back to project-based discovery.

**Source:** *Continuous Discovery Habits*, 2021; the canonical definition of continuous discovery.

### Ground every interview in a specific past instance

Open with: **"Tell me about the last time you [X]"**. Not "tell me about your experience with X". Not "would you use X?". A specific instance from actual past behavior.

**Source:** [Story-Based Customer Interviews, Product Talk, Apr 2024](https://www.producttalk.org/2024/04/story-based-customer-interviews/).

### Walk the timeline

Once the participant is in a specific story: "Where were you? Then what happened next? What did you do after that?" Chronological, step-by-step. Follow the emotion (emotional memory is dense). Use silence.

### Redirect generalizations gently

When the participant flips from "the last time I did X" to "and that's usually what I do", pull them back to the specific instance. This is the critical interviewer skill Torres teaches in the Continuous Interviewing course and grades in her Interview Coach AI.

### Build and update the OST as a living artifact

Refresh the opportunity space every 3–4 interviews. If the tree hasn't changed in a month, either you've stopped interviewing or you've stopped listening.

**Source:** [Opportunity Solution Trees, Product Talk canonical](https://www.producttalk.org/opportunity-solution-trees/).

### Force at least 3 solutions per target opportunity

The diversity kills the "first idea = the idea" pathology. Torres's rule from the OST essay.

### Map assumptions across all 5 categories

Desirability, viability, feasibility, usability, ethical. Not just the 1–2 your team is biased toward.

**Source:** [Five Types of Assumptions, Product Talk](https://www.producttalk.org/five-types-of-assumptions/); [Torres on X, Apr 2024](https://x.com/ttorres/status/1782787771188285800).

### Test the riskiest assumption first

Not all assumptions. Not in random order. The riskiest — the one that, if wrong, kills the solution.

**And with the smallest test that would change your mind.** Torres's line: figure out something you can do in the next hour.

**Source:** [Assumption Testing, Product Talk](https://www.producttalk.org/assumption-testing/).

### Set product outcomes at the trio's span of control

Not business outcomes (revenue, retention — the trio can't move those alone). Not outputs (things shipped). Customer behavior changes the trio can influence with their product decisions.

**Source:** [Defining Product Outcomes, Product Talk](https://www.producttalk.org/defining-product-outcomes/).

### Include the engineer and designer in the interview

Not "the PM interviews and reports back". The whole trio hears the customer live. Shared context is the point.

### Use analytics for the number, use the interview for the story behind the number

People are unreliable narrators of "how often" or "how long". Analytics tells you the frequency; the interview tells you why.

## Don'ts — the interview and OST anti-patterns Torres calls out by name

### Don't ask opinions

*"What do you think of X?"* is not discovery. Opinions are cheap, cognitively biased, and don't predict behavior.

**Redirect:** ask about the last time they did the actual behavior.

### Don't ask about future or hypothetical behavior

*"Would you use this?"* is not discovery. People answer as an idealized version of themselves.

**Redirect:** ask about past behavior. "Tell me about the last time you tried to solve this problem."

### Don't ask for generalizations

*"Tell me about your experience with Netflix"* invites System-1 fast thinking and cognitive bias.

**Redirect:** anchor in a specific instance. *"Tell me about the last time you watched Netflix."*

### Don't rely on self-reported behavioral metrics

People say they exercise 4x/week when they exercise 1.5x/week. Don't ask "how often do you use X?" and treat the answer as data.

**Redirect:** get the number from analytics; use the interview to understand the story around a specific instance.

### Don't put features on the OST as opportunities

**The test:** "Is there more than one way to address this?" If no, it's a solution disguised as an opportunity.

**Example (Torres's recurring one):**
- ❌ "Customers can fast-forward through commercials" (that's a specific solution)
- ✅ "Customers don't like commercials" (that's an opportunity — multiple solutions possible)

**Source:** [Opportunity Solution Trees, Product Talk](https://www.producttalk.org/opportunity-solution-trees/).

### Don't do one-and-done research

A single research sprint at the start of a project = project-based discovery, not continuous.

**Diagnostic:** ask "is the interview happening this week, next week, and the week after, by the trio?" If not, it's not continuous.

### Don't assign business outcomes to product teams

Business outcomes (revenue, retention, ARR) are lagging indicators that require multiple functions to move. The trio can't own them alone. This is Mistake #3 in Torres's [8 Mistakes essay](https://www.producttalk.org/defining-product-outcomes/).

**Redirect:** translate to a product outcome (behavior change) that would drive the business outcome, and that the trio can influence.

### Don't send the PM alone to interviews

Handoffs — PM interviews, then reports back to trio — lose the shared context that makes the trio work. The engineer and designer being present is not optional.

### Don't skip assumption testing to go straight to A/B tests

A/B tests validate a shipped solution. Assumption tests reduce the risk *before* you ship. Torres: *"We rarely have time to run real experiments in discovery."* — use assumption tests instead.

### Don't dogmatize the method

Torres explicitly refuses to be turned into a recipe. When the user wants "step 1, step 2, step 3, exactly", reframe toward a practice they can start this week.

## Gotchas — things that go wrong even when you think you're doing it right

### The OST-without-interview-cadence gotcha

Team draws the tree. Team stops interviewing. Tree stops updating. Tree becomes a poster on the wall.

**Diagnostic:** ask "when was the last time this tree changed based on an interview?" If more than 2 weeks ago, the tree is dead.

### The "opportunity" that's actually a feature

Team fills the opportunity space with things like "add SSO", "improve dashboard performance", "AI-powered recommendations". Those are solutions. Torres's test: "is there more than one way to address this?"

**Redirect:** for each item, ask what customer need underneath drove someone to write that solution. Move the solution to Layer 3 (solutions) and put the underlying need in Layer 2 (opportunities).

### The wrong-altitude outcome

Two failure modes:
- **Too high** — a business outcome assigned to the trio. The trio can't move it alone.
- **Too narrow** — a hyper-specific traction metric (e.g., "increase clicks on the blue button by 5%") that leaves no room for exploration.

**Redirect:** a good product outcome describes a customer behavior change, at the trio's altitude, with room for multiple opportunities to feed it.

### NPS as sole outcome (Mistake #7 in the 8 mistakes essay)

Sentiment metrics tell you the temperature. They don't tell you what behavior to change.

**Redirect:** if you must use NPS, pair it with a behavioral outcome — "increase NPS AND increase weekly returning users completing X".

### Individual OKRs on top of the trio

The trio is team-based. Individual OKRs break the shared learning loop. (Note: this is where Torres's frame connects tightly with Perri's — see `applications.md`.)

**Redirect:** team-level OKRs, aligned to the product outcome.

### "We already interview our customers"

Almost always project-based, ad hoc, PM-solo. The diagnostic four questions:
1. Is the interview happening **this week**?
2. Is the **full trio** in it?
3. Was it a **story-based interview** (specific past instance)?
4. Did it **update the OST**?

If any answer is no, it's not continuous discovery — it's talking to users, which is different.

### The PM as note-taker, trio as observers

The trio is in the room but only the PM asks questions. Everyone else is a spectator. That's not trio-based discovery — the engineer and designer are not learning to interview.

**Redirect:** rotate who leads the interview across weeks. All three should build the muscle.

### The team that skips the "which assumption?" step

Team has 3 solutions on the tree. Skips assumption mapping. Jumps to prototyping the favorite. Ships it. Learns post-launch that the assumption they never named was wrong.

**Redirect:** for every solution being considered, spend 20 minutes as a trio naming assumptions across all 5 categories. Rank by risk. Test the top one this week.

### Falling in love with the first solution

The 3-solutions-minimum rule exists to prevent this. If the team keeps drifting to "yeah but the first one is obviously right", force them to steel-man solutions 2 and 3 before killing them.

### Story-based interviewing collapsed into "have a conversation"

Softest, most common gotcha. Team believes they're doing story-based interviewing because they "chat" with users. But they ask opinions, they ask hypotheticals, they let generalizations stand. The rules are strict; the technique is trained.

**Redirect:** send the team to the [Continuous Interviewing course](https://learn.producttalk.org) or have them practice against Torres's four rubric dimensions (opening with a story-based question, setting the scene, building the timeline, redirecting generalizations).

## Common misapplications (teams that *claim* they do continuous discovery)

### The team that ran discovery once and considers it "done"

Discovery was the phase at the start of the project. Now they're in "delivery mode". This is the exact project-based-discovery pattern Torres's method exists to replace.

### The team that "does" the OST monthly

The OST is a weekly-plus artifact tied to the interview cadence. Monthly updates = disconnected from real customer learning.

### The team where research runs discovery FOR the trio

Researcher does the interviews. Trio consumes the report. This is the specialist-model Torres warned about — researcher does the deep specialist study, trio does the weekly practice. When research does both, the trio never builds the muscle.

### The team that runs A/B tests as their only "assumption testing"

A/B tests answer "which variant wins?" after both variants ship. They don't reduce risk before build. Torres's assumption test is upstream of build, cheap, and targets ONE assumption at a time.

### The team that maps assumptions in only 2–3 categories

Engineers test feasibility. PMs test viability. Nobody tests ethical. Then the product ships and the ethical assumption that nobody named turns out to be wrong.

### The team that puts business outcomes on the OST

The trio can't move revenue alone. When the outcome is a business outcome, the tree can't help — every opportunity looks equally distant from moving the metric.

## Pro tips — accelerators Torres uses in her coaching and courses

### The "start with 30 minutes" onboarding

For teams new to continuous discovery: block off 30 minutes per week as trio time. That's the whole starting requirement. Not 3 hours; not a full sprint; 30 minutes. Habit precedes depth.

**Source:** Torres, multiple podcast appearances; the Product Talk Academy fundamentals course.

### The "3–4 interviews before you draw the tree" rule

Don't build an OST on top of no interviews. Do 3–4 first. Then draw. Then update every 3–4 more.

### The "next hour" assumption test rule

Team says they don't have time for assumption tests? Torres: figure out something you can do in the next hour to evaluate that risk. Break the "we need a whole sprint" mental frame.

### Rotate the interview lead across the trio

If only the PM ever leads, only the PM builds the muscle. Rotate. Engineers who have interviewed customers change how they think about code.

### Use the Interview Coach rubric to self-assess

Torres's own rubric (from the 2025 Interview Coach essay):
1. Did I open with a story-based question?
2. Did I set the scene?
3. Did I build the timeline?
4. Did I redirect generalizations?

Score yourself after every interview. That's the practice loop.

### The "would this be an outcome or an output?" gut check

For every proposed OKR / goal: "if I hit this, what changed for the customer?" If the answer is "we shipped a thing", it's an output. If it's "customers behaved differently", it's an outcome.

## Language and vocabulary — say this, not that

Small phrasing shifts Torres has been explicit about in her writing:

| Instead of | Use | Because |
|---|---|---|
| "Talk to users" | "Weekly story-based interviews with the trio" | Specificity is the method |
| "Would you use this?" | "Tell me about the last time you tried to [X]" | Future/hypothetical vs past/behavior |
| "What do you think of X?" | "Walk me through the last time you [X]" | Opinion vs behavior |
| "Do you like Netflix?" | "Tell me about the last time you watched Netflix" | Sentiment vs specific instance |
| "MVP" | "Small assumption test" or "concept test / concierge / Wizard of Oz" | MVP has been degraded to "small first version to ship" |
| "Business outcome" (assigned to a trio) | "Product outcome" | Trios can only move product outcomes; business outcomes need multiple functions |
| "Feature roadmap" | "Opportunity Solution Tree" | Features are solutions; the tree starts from outcomes and opportunities |
| "Do more research" | "Add a weekly customer touchpoint" | Habit vs project |
| "Run an experiment" | "Run a small assumption test" (in discovery) | Experiments test the whole idea; assumption tests target one risk |
| "The PM should do more discovery" | "The trio should do weekly discovery together" | Trio, not solo |
| "We need better user research" | "We need continuous discovery habits" | Research is a specialty; discovery is a habit |
| "Opportunity: add fast-forward" | "Opportunity: customers don't like commercials. Solution: add fast-forward" | Feature-as-opportunity is the disguise pattern |

## Voice reminders when applying this section

- Coach the practice, not the artifact. If the user wants a tree, first check the cadence and the trio.
- Hold the interview rules — don't paraphrase past behavior / specific instance / no opinions / no hypotheticals into "just have a conversation".
- Diagnose before prescribing. If the user says "we already do this", ask the 4 diagnostic questions.
- Warm about the humans; strict about the rules. Torres's own register.
- Cite. Every rule and gotcha has a source in her published work.

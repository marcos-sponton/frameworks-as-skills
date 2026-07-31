# Continuous Discovery Habits — Method

> The canonical description of Torres's method in her own terms. Fidelity is the point — softening any of these rules collapses continuous discovery into generic user research. Torres does not offer a linear process; she offers a set of habits that fit inside one visual artifact (the Opportunity Solution Tree), with the weekly trio-based interview cadence as the load-bearing habit and the OST as the visualization of what the habits produce.

## The definition of continuous discovery

Torres's operating definition, repeated across the book, essays, and podcasts:

> "At a minimum, weekly touchpoints with customers by the team building the product, where they're conducting small research activities in pursuit of a desired product outcome." — *Continuous Discovery Habits*, 2021.

Three words are non-negotiable:

- **"Weekly"** — the cadence IS the practice. Not monthly, not "when we can". If you skip a week, you are back to project-based discovery.
- **"By the team building the product"** — the product trio (PM + designer + engineer). Not a separate research team, not the PM alone with a summary meeting.
- **"Product outcome"** — the discovery has a direction: a specific behavior-change metric the trio owns and is trying to move.

## The 5 continuous discovery habits

Torres's summary of the practice:

1. **Interview at least one customer per week as a full product trio.**
2. **Map opportunities using an Opportunity Solution Tree.**
3. **Surface and test assumptions before building.**
4. **Run small experiments to validate ideas.** (Torres now prefers "small assumption tests" for the discovery phase — see below.)
5. **Involve the full product trio (not just researchers) in weekly discovery.**

## The Opportunity Solution Tree (OST)

Torres's central visual artifact. Introduced in 2016, formalized in the 2021 book, refined continuously. A living tree diagram that maps from a business need down to tested solutions.

Canonical reference: [Opportunity Solution Trees on Product Talk](https://www.producttalk.org/opportunity-solution-trees/).

**The 4 layers, top to bottom:**

### Layer 1 — Outcome (root)

- **Product outcome**, not business outcome, not traction metric.
- A **measure of customer behavior or sentiment** that, if it moves, will drive the business outcome.
- **One outcome per team.** Focus is the point. If a team has three outcomes, they have zero.
- Rule: it must be **within the trio's span of control** — the trio can influence it through the product decisions they make.

### Layer 2 — Opportunities (trunk & major branches)

Definition (Torres, canonical OST essay):
> "Unmet customer needs, pain points, and desires that, if addressed, will drive your desired outcome."

- Sourced from **story-based customer interviews** (see next section). Torres's prerequisite: **3–4 interviews minimum before you can populate the opportunity space honestly.**
- Framed as **customer needs / pain points / desires**, NOT solutions or features.
- **Update the opportunity space every 3–4 interviews.** The tree is a living artifact.
- Opportunities are hierarchical — big opportunities decompose into smaller, more specific ones.

**The test for whether an "opportunity" is really a solution in disguise:**
> "Is there more than one way to address this?" — Torres, canonical OST essay.

If there's only one way to address it, it's a solution. Reframe it as the underlying customer need.

**Example (Torres uses this repeatedly):**
- ❌ "Customers can fast-forward through commercials" (solution disguised as opportunity)
- ✅ "Customers don't like commercials" (real opportunity — multiple solutions possible: fast-forward, skip button, ad-free tier, shorter ads)

### Layer 3 — Solutions (secondary branches)

Definition (Torres):
> "A product, a feature, a service, a workflow, a process, documentation, or anything else we offer to address an opportunity."

- **Consider at least 3 solutions per target opportunity.** The diversity forces the team past their first idea.
- Start small — one solution should address one opportunity for continuous delivery.
- Solutions live *below* opportunities on the tree. Not on top. Not next to.

### Layer 4 — Assumption Tests (leaves)

- Each solution is broken down into the **assumptions** it depends on.
- The team identifies the **riskiest assumptions** and tests those first — not all assumptions, and not in random order.
- **Assumption tests are NOT full experiments** (see below).

**Prerequisites Torres names before you can even start building the tree honestly:**

1. A theory of the target customer.
2. A defined product outcome.
3. 3–4 story-based interviews.

**Rules across all layers:**

- Update the opportunity space every 3–4 interviews.
- One outcome per team.
- Distinguish opportunities from solutions using the "more than one way?" test.
- Test the riskiest assumption first, with the smallest test that would change your mind.
- The tree is **living** — updated weekly, not printed as a poster.

## Story-based interviewing

Torres's most operationally-detailed method. It has strict rules; paraphrasing into "just talk to your users" loses the method.

Canonical reference: [Story-Based Customer Interviews Uncover Much-Needed Context](https://www.producttalk.org/2024/04/story-based-customer-interviews/), Apr 2024.

### The opening question — the exact form

> "Tell me about the last time you [relevant behavior]."

Example (Torres's recurring pedagogical example): *"Tell me about the last time you watched Netflix."*

**This is not a template — it is THE opening.** It grounds the conversation in a specific past instance, not a generalization or an opinion.

### The core rules

1. **Ask about past behavior, never future or hypothetical.** Do NOT ask "would you use this?" — people answer as an idealized version of themselves, not as who they actually are.
2. **Never ask for opinions.** Opinions are cheap and cognitively biased; behavior is data.
3. **Never ask for generalizations.** "Tell me about your experience with Netflix" invites System-1 fast thinking and cognitive bias. Ground in a specific instance instead.
4. **Never ask closed / yes-no questions** during the story portion.
5. **Never rely on self-reported behavioral metrics** (frequency, duration). People are unreliable narrators. Use analytics for the number; use the interview for the story behind the number.
6. **The participant does most of the talking.** Torres, canonical essay: *"The art of the interview is knowing what to ask when in a way that encourages the participant to open up and share their experience."*

### The follow-up technique — walk the timeline

Once the participant is telling a specific story:

- **Start at the beginning.** "Where were you when you decided to open Netflix?"
- **Then what happened next?** Walk chronologically through the story.
- **Follow the emotion.** Emotional memory is dense; when the participant lights up or shows frustration, dig in.
- **Use silence.** Give the participant space to search their memory. Don't fill the pause.

### The critical skill — redirect generalizations

Torres names this explicitly as the skill that separates a good interviewer from a bad one:

**The pattern:** the participant is telling a specific story, then flips to generalization: *"...and that's usually what I do."* Or: *"...and I always find this frustrating."*

**The move:** gently guide them back to the specific instance. *"Interesting — but let's stay with that specific evening. What did you do next?"*

### The four teaching dimensions (from Torres's own Interview Coach AI)

In her 2025 essay on the Interview Coach AI she built for her course, Torres reveals the operational rubric she uses to grade practice interviews:

1. **Opening with a story-based question.**
2. **Setting the scene** (getting the participant into the specific instance).
3. **Building the timeline** (walking the story chronologically).
4. **Redirecting generalizations** (the critical skill above).

That's the rubric. If the assistant is coaching a user on interview technique, those four are the assessment dimensions.

## Assumption Mapping — the 5 categories

For each solution on the OST, Torres has teams map assumptions across 5 categories. Every product idea depends on assumptions in all 5.

Torres's canonical framing (from LinkedIn and Product Talk essays):
> "Every product idea is built upon a set of assumptions: Desirability, usability, feasibility, viability, and ethical assumptions."

### 1. Desirability
Do customers actually want this? Will they engage with it? Will they choose it over the alternatives (including doing nothing)?

### 2. Viability
Does it make business sense? Adequate returns? Aligned with business model? Sustainable economically?

### 3. Feasibility
Can we technically build it? Do we have the org capability? Can we ship it in a reasonable time?

### 4. Usability
Can customers actually use the solution? Cognitive load acceptable? Workflow fits their reality? Accessible?

### 5. Ethical
What harm could this cause — to customers, to non-users, to the company, to third parties? What second-order effects have we not thought through?

**Ethical is Torres's post-book addition.** The classic frame (from IDEO / d.school) has 3 categories (desirability, viability, feasibility); Torres extended to 5 by explicitly adding usability (already implicit) and ethical (a load-bearing addition). See `post-book.md`.

**Team bias to watch for:**
- Engineers over-test feasibility, under-test the other four.
- PMs over-test viability, under-test the ethical column.
- Designers over-test usability.
- Almost no one tests ethical until forced.

**Torres's rule:** explicitly name assumptions in ALL five categories, not just the two your team is biased toward.

### Story mapping as an assumption-surfacing technique

Torres recommends **story mapping** — laying out each step users have to take to get value from the solution — as the mechanic for surfacing assumptions. At every step, ask: **"What has to be true here?"** Those are the assumptions.

## Small Assumption Tests — NOT full experiments

Torres draws a sharp line between assumption tests and experiments.

Canonical reference: [Assumption Testing: Everything You Need to Know to Get Started](https://www.producttalk.org/assumption-testing/).

### The distinction

**Experiment** = tests the whole idea. "Does this solution work?"
**Assumption test** = tests ONE assumption in isolation. Faster, cheaper, teaches you which risk to worry about.

Torres, canonical essay:
> "An assumption test is a structured activity that we do to evaluate the risk in an assumption."

And, on why she prefers this over experiments in the discovery phase:
> "We rarely have time to run real experiments in discovery."

And:
> "Assumption testing makes it clear that we're testing a single assumption and not the whole idea."

### The rule for teams who "don't have time"

Torres's response, verbatim:
> "Take whatever solution you are working on right now... figure out something you can do in the next hour to evaluate that risk."

The point is not the depth of the test. The point is the **practice** — small tests, weekly, inside the same trio cadence that runs interviews.

### Common assumption test types

Torres draws on a broad palette (from the *Testing Business Ideas* / Osterwalder canon and elsewhere):

- **Concierge test** — manually deliver the value to one customer to see if they want it.
- **Wizard of Oz** — a fake interface behind human labor.
- **Concept test** — describe the idea to a user and see if they can articulate the value.
- **Landing page / smoke test** — measure sign-up interest before building.
- **Data walkthrough** — walk a real customer through their real usage data.
- **Prototype test** — a testable artifact focused on one assumption, not the whole product.

Match the test to the assumption category (desirability tests are different from feasibility tests).

## The Product Trio

- **PM + designer + engineer.** Three roles, jointly running discovery.
- **Replaces serial handoff** — the "PM defines, designer mocks, engineer builds" pipeline.
- All three participate in interviews. All three participate in OST maintenance. All three participate in assumption surfacing and testing.
- **Not "the PM does discovery and reports back".** The engineer being in the interview is not optional. That's how the technical assumptions get surfaced live, and how the trio builds a shared model of the customer.
- **Other roles cycle in** — data analysts, user researchers, product marketers, subject matter experts — but the trio is the standing team that owns the outcome.

Torres has acknowledged the pushback (from user-researchers especially) that the trio framing has been misused to justify eliminating dedicated research roles. Her position: **the trio does the weekly practice; specialist researchers do the deeper studies. Both, not either.** See `post-book.md`.

## Product outcome vs business outcome vs output

Torres's canonical distinctions:

- **Business outcome** — what the business needs (revenue, retention, ARR). **Lagging indicator.** Requires multiple functions to move. **Outside the trio's span of control.**
- **Product outcome** — a customer behavior change that drives the business outcome. **Leading indicator.** **Within the trio's span of control.** This is what the trio owns.
- **Output** — a thing shipped (feature, release, story point). Not an outcome, regardless of how it's framed.

Canonical piece: [Defining Product Outcomes: The 8 Most Common Mistakes You Should Avoid](https://www.producttalk.org/defining-product-outcomes/).

### The 8 mistakes Torres names when teams try to define product outcomes

1. **Disguising outputs as outcomes.** ("Build an Android app" is an output, not an outcome — it's a yes/no completion.)
2. **Not connecting outcomes to business value.** (An outcome that doesn't tie to strategy is orphaned.)
3. **Giving teams outcomes outside their span of control.** (Business outcomes assigned to trios; "grow revenue 30%" isn't something a product trio can move alone.)
4. **Hyper-focusing on a traction metric.** (Feature-specific metrics with no latitude for exploration.)
5. **Creating too many cross-team dependencies.** (Outcomes that require 4 teams to coordinate = no team owns it.)
6. **Measuring the action, not the value of the action.** (Number of logins ≠ value of logging in.)
7. **Setting sentiment outcomes (NPS) without behavioral direction.** (Sentiment tells you the temperature; it doesn't tell you what to do.)
8. **Setting outcomes without an accountability model that encourages learning.** (If missing the outcome = punishment, the team will pick easy outcomes and game the metric.)

## How the pieces integrate

The habits fit together this way:

- **Product outcome** sets the direction the trio is trying to move.
- **Story-based interviews** (weekly, by the trio) surface **opportunities** (customer needs) that could move the outcome.
- The **Opportunity Solution Tree** is the visualization of what the interviews have surfaced — mapped down to solutions and their assumptions.
- **Assumption mapping** across the 5 categories exposes what has to be true for each solution to work.
- **Small assumption tests** evaluate the riskiest assumptions first, in hours or days.
- The **product trio** does all of the above together, not in handoffs.

**If any habit is missing, the whole thing degrades:**

- No weekly cadence → back to project-based discovery, tree becomes a poster.
- No trio → PM interviews alone, engineer never hears the customer, shared context collapses.
- No story-based rules → interviews collect opinions and hypotheticals; opportunities are wishlists, not customer needs.
- No assumption tests → team goes straight to build; discovers post-launch that the assumption was wrong.
- No product outcome → the tree has no root; every opportunity looks equally valuable.

## What this method is NOT

Torres is explicit:

- **Not a linear process.** No "step 1, step 2". It's a set of habits that run continuously in parallel.
- **Not a poster.** The OST is a living artifact, updated weekly. A tree that hasn't been touched in a month is a poster.
- **Not user research as a specialty.** The trio does discovery. Dedicated researchers do deeper specialist studies. Both, not one replacing the other.
- **Not a substitute for strategy or PM function health.** Torres assumes the outcome has been set by a functional product organization above the trio. If that upstream layer is missing, see `applications.md` — you probably need Perri or Cagan first.
- **Not "just talk to your users".** The rules are strict for a reason. Softening the interview rules is the anti-pattern the method exists to prevent.
- **Not a recipe.** Torres actively refuses to be dogmatized. The habits are a scaffold; the specifics vary by context.

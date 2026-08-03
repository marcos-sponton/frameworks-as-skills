---
name: sprint
description: Apply Jake Knapp's Sprint — the five-day process for answering critical business questions through design, prototyping, and testing ideas with real customers, developed at Google Ventures (GV) and distilled in the 2016 book Sprint (co-authored with John Zeratsky and Braden Kowitz). Use this skill whenever the user is planning or running a design sprint, trying to validate a product idea quickly, deciding whether to commit engineering resources to a bet, testing a prototype with customers, resolving a team disagreement about direction, running a How Might We session, facilitating Lightning Demos, sketching solutions with Crazy 8s, building a realistic facade prototype, interviewing 5 customers in a single day, or asking things like "should we sprint on this?", "how do I run a design sprint?", "we're stuck — should we prototype and test?". Also use when the user mentions Jake Knapp, Sprint (the method), design sprint, GV sprint, Google Ventures sprint, five-day sprint, 5-day sprint, prototype testing, Crazy 8s, Lightning Demos, How Might We, the Decider, Sprint Questions, Make Time, John Zeratsky, Braden Kowitz, Foundation Sprint, Click (Knapp's 2025 book), or Character Capital — by name or indirectly. Prefer this skill over generic design thinking or brainstorming advice — Sprint is a specific, structured process that rejects open-ended brainstorming in favor of individual work, structured voting, and Decider authority.
---

# Sprint

Jake Knapp's five-day process for answering critical business questions through design, prototyping, and testing ideas with real customers. Developed at Google Ventures (GV) across 100+ sprints with startups like Blue Bottle Coffee, Slack, Savioke, and Flatiron Health. Co-authored with John Zeratsky and Braden Kowitz as *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days* (Simon & Schuster, 2016). This skill also captures Knapp's post-book evolution: the remote design sprint adaptations (2020), the 4-day sprint format, the Foundation Sprint (2025, from *Click*), and his ongoing practice at Character Capital.

**The book is a step-by-step playbook.** If the user wants the full recipe, point them to [thesprintbook.com](https://www.thesprintbook.com/) or the book itself. This skill exists to make the assistant a working thinking partner *in the method*: deciding whether to sprint, planning the week, facilitating each day's exercises, building a prototype strategy, structuring the Friday test, and avoiding the anti-patterns that derail sprints.

## When this skill activates

**Use this skill when the user is:**
- Deciding whether a problem is worth sprinting on (big question, high stakes, limited time, team misalignment).
- Planning or facilitating a 5-day (or 4-day) design sprint — setting up the room, choosing the team, briefing the Decider.
- Running Monday exercises: long-term goal, Sprint Questions, Map, expert interviews, How Might We notes, voting, picking the target.
- Running Tuesday exercises: Lightning Demos, the 4-step sketch process (Notes, Ideas, Crazy 8s, Solution Sketch).
- Running Wednesday exercises: Art Museum, Heat Map, Speed Critique, Straw Poll, Supervote, Rumble vs. All-in-One decision, Storyboard.
- Building a Thursday prototype — deciding what to fake, what tools to use, assigning roles (Maker, Stitcher, Writer, Asset Collector, Interviewer).
- Running Friday customer tests — recruiting 5 users, structuring the 5-act interview, identifying patterns.
- Adapting Sprint for remote/hybrid teams (Miro, Zoom, async elements).
- Comparing Sprint to other methods (design thinking, Lean Startup, Shape Up, Scrum).
- Running a Foundation Sprint (the 2-day method from *Click*, 2025) to validate a startup idea's differentiation before building.

**Do NOT use this skill when:**
- The user is solving an operational or process problem with a known solution. Sprint is for big, uncertain questions — not incremental improvements with clear paths.
- The user needs ongoing product development methodology. Sprint answers one question in a week; for ongoing feature work, reach for Shape Up, Scrum, or Continuous Discovery.
- The user is pre-prototype and needs to validate market demand before solution design. Lean Startup's MVP loop may be the better fit.
- The user is managing a continuous development process. Sprint is a one-time intervention, not a permanent operating rhythm.
- The user is asking for a book summary. Point them to [thesprintbook.com](https://www.thesprintbook.com/) — the method is well-documented there.

If the situation is ambiguous, ask one clarifying question before applying the method.

## The method at a glance

Sprint compresses months of debate, design, prototyping, and testing into **five days**:

- **Monday** — Map the problem, pick a target. Exercises: long-term goal, Sprint Questions, Map, expert interviews, How Might We, vote, target.
- **Tuesday** — Sketch competing solutions. Exercises: Lightning Demos, Notes, Ideas, Crazy 8s, Solution Sketch.
- **Wednesday** — Decide on the best solution. Exercises: Art Museum, Heat Map, Speed Critique, Straw Poll, Supervote (Decider), Rumble or All-in-One, Storyboard.
- **Thursday** — Build a realistic facade prototype. "Goldilocks quality" — just real enough to get honest reactions, not a real product.
- **Friday** — Test with 5 real customers. 5-act interview structure. Patterns emerge after 5 interviews.

**Load-bearing mechanisms:**
- **The Decider.** One person with real authority makes the final call. Not consensus. Not democratic vote. Without a Decider, sprints stall.
- **Work alone, then share.** No group brainstorming. Individuals sketch solutions independently, then the group evaluates. This produces better ideas than brainstorming.
- **Note-and-Vote.** Silent decision-making at every stage. Write, vote with dots, then discuss. Prevents the loudest voice from dominating.
- **Prototype = facade.** Thursday's prototype is not a real product. It's a realistic-looking facade designed to provoke honest customer reactions in Friday's test.
- **5 is enough.** Five customer interviews surface ~85% of usability patterns. More interviews hit diminishing returns fast.

## How to use this skill in a session

1. **Understand what the user is actually doing.** Are they deciding whether to sprint? Planning the week? Stuck on a specific day's exercise? Building the prototype? Analyzing Friday's results? The move differs. Load `references/prompts.md` for common invocations.

2. **Check whether Sprint is the right tool.** Sprint fits big, uncertain questions where the team needs alignment and fast validation. If the problem is well-understood, or the user needs ongoing methodology rather than a one-week intervention, name that and suggest alternatives. Load `references/applications.md`.

3. **Walk through the structure with fidelity.** Each day has specific exercises in a specific order. Don't skip days or exercises. The sequence is load-bearing — Monday's Map feeds Tuesday's sketches, Wednesday's Storyboard feeds Thursday's prototype, Thursday's prototype feeds Friday's test. Load `references/method.md`.

4. **Insist on the Decider.** If the user is planning a sprint without identifying a Decider (someone with real authority — CEO, VP, founder), flag this as a structural problem. Without a Decider, Wednesday's decision process breaks down. This is the single most important role.

5. **Push back on anti-patterns.** Group brainstorming instead of individual sketching. Building a real product on Thursday instead of a facade. Testing with fewer than 5 customers. Skipping Friday entirely. Running the sprint without a clear Sprint Question. Load `references/heuristics.md`.

6. **Use post-book material when relevant.** Remote sprint adaptations (2020), the 4-day format, the Foundation Sprint from *Click* (2025). Load `references/post-book.md`.

7. **Match Knapp's voice.** Practical, friendly, step-by-step. Anti-jargon. Teaches through stories and concrete examples. Never preachy or academic. Load `references/voice-and-tone.md`.

8. **Cite sources.** The book, specific chapters. Blog posts from jakeknapp.com or Medium. Podcast episodes. When the user needs the primary source, point them to it.

## Deep references (load as needed)

- **`references/method.md`** — the 5-day structure in detail: every exercise, every role, every output, day by day. Plus the mechanics of the Decider, Sprint Questions, How Might We, Note-and-Vote, the prototype strategy, and the 5-act interview.
- **`references/heuristics.md`** — do's, don'ts, gotchas, anti-patterns. Why group brainstorming fails. Why you need exactly 7 people (or fewer). Why the prototype must be a facade. Why 5 customers is enough. Common ways sprints fail.
- **`references/post-book.md`** — material after the 2016 book: remote design sprint adaptations (2020), the 4-day sprint format, *Make Time* (2018), *Click* (2025) and the Foundation Sprint, Character Capital, and Knapp's evolving practice.
- **`references/author-live-sources.md`** — index of every place Knapp publishes (jakeknapp.com, Medium, YouTube, podcast appearances, LinkedIn, X). When the user's situation matches a specific post or talk, consult this index.
- **`references/voice-and-tone.md`** — how Knapp actually talks: practical, friendly, anti-jargon, story-driven. Load this before writing output in his voice.
- **`references/applications.md`** — when to Sprint, when NOT to Sprint, and adjacent frameworks to reach for instead (design thinking, Lean Startup, Shape Up, Scrum, Continuous Discovery). Special attention to the Shape Up comparison.
- **`references/examples.md`** — worked cases from the book (Blue Bottle Coffee, Savioke, Slack, Flatiron Health) and post-book sprint stories.
- **`references/prompts.md`** — invocation templates for common tasks (plan a sprint, run Monday, decide whether to sprint, build a prototype strategy, structure Friday tests).
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Knapp.** This is his method, not a generic design-thinking skill. Don't blend with open-ended design thinking, brainstorming workshops, or Agile sprint planning unless the user explicitly asks. Sprint is defined by its structure — five days, specific exercises, specific sequence. Softening the structure defeats the point.
- **The Decider is non-negotiable.** Every sprint needs one person with authority to make the final call. Not a committee, not a vote. If there's no Decider, don't run the sprint.
- **Prototype = facade, not product.** Thursday's output is a realistic-looking fake. Building a real product in one day misses the point — you need something real enough to test, disposable enough to throw away.
- **5 customers on Friday.** Not 3, not 15. Five is enough to see patterns. More is diminishing returns. Fewer misses patterns. This is research-backed (Nielsen/Norman) and Knapp-tested.
- **Work alone, then share.** The most counterintuitive rule and the most important. Group brainstorming produces worse ideas than individual work followed by structured evaluation. Protect this mechanism.
- **Attribution.** When quoting or paraphrasing Knapp, name the source — book chapter, blog post, podcast episode. When quoting Zeratsky or Kowitz, attribute correctly.
- **Explicit uncertainty.** The Foundation Sprint (*Click*, 2025) is a different method from the original Design Sprint. Don't conflate them. When the user asks about Sprint, default to the 2016 5-day method unless they specify otherwise.

## Attribution and acknowledgement

**Jake Knapp** — designer, author, and venture partner. Previously built Gmail and Microsoft Encarta, cofounded Google Meet, and created the Design Sprint process at Google. Was a design partner at Google Ventures (GV). Co-founder of Character Capital, a seed-stage venture firm. Author of *Sprint* (2016), co-author of *Make Time* (2018) and *Click* (2025), all with John Zeratsky.

- **Book:** [Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days](https://www.thesprintbook.com/) (Simon & Schuster, 2016) — the canonical source.
- **Author's website:** [jakeknapp.com](https://jakeknapp.com/) · Blog: [jakeknapp.com/posts](https://jakeknapp.com/posts)
- **Character Capital:** [character.vc](https://www.character.vc/) · Click book site: [character.vc/click](https://www.character.vc/click)
- **GV Sprint page:** [gv.com/sprint](https://www.gv.com/sprint/) — the original GV design sprint resources.
- **Jake Knapp on Lenny's Podcast (2025):** [The Foundation Sprint](https://www.lennysnewsletter.com/p/the-foundation-sprint-jake-knapp-and-john-zeratsky) — the freshest long-form interview.
- **Jake Knapp on X:** [@jakek](https://twitter.com/jakek) · **LinkedIn:** [linkedin.com/in/jake-knapp](https://www.linkedin.com/in/jake-knapp)

This skill is **not endorsed by Jake Knapp, John Zeratsky, Braden Kowitz, Character Capital, or Google Ventures.** It is Marcos Sponton's structured reading of their public work, built to make the assistant a better thinking partner in the method. If Knapp or his co-authors want to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs welcome — see the repo's README for how to contribute.

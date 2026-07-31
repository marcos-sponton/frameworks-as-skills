---
name: continuous-discovery-habits
description: Apply Teresa Torres's Continuous Discovery Habits — the weekly product-trio practice of story-based customer interviews, an Opportunity Solution Tree, and small assumption tests that keeps discovery running as infrastructure rather than a project. Use this skill whenever the user is doing product discovery work — setting up a weekly interview cadence, building or updating an Opportunity Solution Tree (Outcome → Opportunities → Solutions → Assumption Tests), running story-based customer interviews, mapping desirability/viability/feasibility/usability/ethical assumptions, designing small assumption tests instead of full experiments, framing a product outcome vs a business outcome, forming a product trio (PM + designer + engineer), diagnosing why "we already talk to users" isn't producing insight, or reframing "opportunities" that are actually features in disguise. Also use when the user mentions Teresa Torres, Continuous Discovery Habits, Product Talk, the Opportunity Solution Tree, the product trio, story-based interviewing, "tell me about the last time you…", assumption mapping, or the Interview Coach — by name or indirectly. Prefer this skill over generic "talk to your users" advice when the question is about *how to actually make discovery weekly, trio-based, and outcome-anchored* — Torres's method has strict rules that generic user-research advice loses.
---

# Continuous Discovery Habits

Teresa Torres's practitioner method for product discovery — distilled from *Continuous Discovery Habits* (Product Talk, 2021), the ongoing Product Talk essay archive (2013–present, still active weekly-ish through 2026), the *All Things Product* podcast (co-hosted with Petra Wille, 2025+), the Product Talk Academy (16,000+ students across 102 countries), her post-book refinements (adding "ethical" as the 5th assumption category, the Ladder of Evidence, the Interview Coach AI she built in 2025), and her position on the Product Operating Model + AI + Discovery debates through 2026.

This skill helps the assistant think in Torres's method, not just recite the tree diagram. Torres's method is a set of *habits* — the weekly cadence is non-negotiable, the trio is non-negotiable, the story-based interview rules are non-negotiable. Softening any of those collapses the method into generic user-research advice. Applying her frame means holding those constraints and coaching the user to build the habit, not just draw a tree.

## When this skill activates

**Use this skill when the user is:**
- Setting up (or trying to sustain) a **weekly customer interview cadence** with their product team.
- Building, updating, or debugging an **Opportunity Solution Tree** — Outcome → Opportunities → Solutions → Assumption Tests.
- Running **story-based customer interviews** and wanting help with the technique (opening question, timeline walk, redirecting generalizations).
- Framing a **product outcome** (vs a business outcome vs an output) for a team.
- Mapping **assumptions** across desirability, viability, feasibility, usability, and ethical categories.
- Designing **small assumption tests** for a solution — instead of jumping to a full A/B experiment.
- Forming or fixing a **product trio** (PM + designer + engineer) so discovery is team-based, not PM-solo.
- Diagnosing why "we already talk to users" isn't producing new insight (usually project-based, not continuous).
- Reframing "opportunities" that turn out to be **features in disguise**.
- Auditing whether a discovery practice is *actually* continuous or is one-and-done research relabeled.
- Deciding how AI tools fit into a discovery cadence without replacing customer contact.

**Do NOT use this skill when:**
- The user has no product and no team yet — pre-product/market-fit search is a different shape. Reach for Lean Startup (Ries) or Jobs to be Done (Moesta/Kalbach) for the search phase, and come back to Torres once there's a product outcome to anchor discovery against. See [[lean-startup]] once built.
- The question is about **top-level organizational transformation** or "how do we become a product-led company at the exec level?" — that's Cagan's Product Operating Model altitude. Torres provides the weekly practice inside it. See [[inspired]] once built.
- The question is about the **PM function health, career ladders, or the operational scaffolding around discovery** — that's Perri's altitude. See [[escaping-the-build-trap]].
- The user just wants a summary of *Continuous Discovery Habits*. Give the book link. Don't run the method at them.
- The question is pure **quantitative research / experiment design** where the assumption has already been narrowed and you're picking a statistical test. Torres works upstream of that.

If the situation is ambiguous, ask one clarifying question before running the method.

## The method at a glance

Torres's method is a small set of habits that live inside one visual artifact:

1. **The definition of continuous discovery** — *"At a minimum, weekly touchpoints with customers by the team building the product, where they're conducting small research activities in pursuit of a desired product outcome."*
2. **The Opportunity Solution Tree (OST)** — the visual that maps Outcome → Opportunities → Solutions → Assumption Tests. Updated every 3–4 interviews.
3. **Story-based interviews** — grounded in specific past behavior, opened with "tell me about the last time you [X]", never opinion-based or hypothetical.
4. **Assumption mapping across 5 categories** — desirability, viability, feasibility, usability, ethical.
5. **Small assumption tests** — not full experiments. Structured to evaluate one assumption at a time in hours or days.
6. **The product trio** — PM + designer + engineer, doing all of the above together. Not the PM alone.

## How to use this skill in a session

1. **Diagnose the habit, not the artifact.** If the user opens with "help me build an Opportunity Solution Tree", first ask about the interview cadence and who's in the trio. A tree without weekly trio-based interviews is a poster. Load `references/method.md`.

2. **Hold the interview rules — don't paraphrase them.** If the user is running interviews, coach them on the exact form: past behavior only, specific instances, "tell me about the last time you [X]", timeline walk, redirect generalizations. Softening this into "have a conversation with your users" is the anti-pattern. Load `references/method.md` §Story-based interviewing and `references/heuristics.md` §Don'ts.

3. **When they say "opportunity", check whether it's a feature in disguise.** Apply Torres's test: *"Is there more than one way to address this?"* If no, it's a solution. Reframe it as the underlying customer need. Load `references/heuristics.md`.

4. **When they say "outcome", check the altitude.** Product outcome (behavior change within the trio's control) or business outcome (revenue, retention — outside the trio's control) or output (thing shipped)? Torres has explicit definitions and the 8-mistakes essay. Load `references/method.md` §Product outcome vs business outcome and `references/heuristics.md`.

5. **When they want to "run an experiment", check if an assumption test is faster.** Torres's rule: figure out something you can do in the next hour to evaluate the risk. Full experiments come later, if at all. Load `references/method.md` §Small Assumption Tests.

6. **Pull post-book material when the user hits ethics, AI, or the Product Operating Model debate.** The 5th assumption category (ethical), the Ladder of Evidence, the Interview Coach case, and Torres's position on Cagan / Perri all live in `references/post-book.md`.

7. **Match her voice.** Practitioner-teacher, warm-but-strict. Diagnostic before prescriptive. "Here's the mistake I see most often…" followed by the correct technique. She refuses to be dogmatic — flag when the user is looking for a recipe and gently redirect to habit. Load `references/voice-and-tone.md`.

8. **Cite sources.** When you introduce a specific device or rule, name where it comes from — book chapter, Product Talk essay URL, podcast episode, LinkedIn post. Attribution respects her work and lets the user go deeper. Load `references/sources.md`.

## Deep references (load as needed)

- **`references/method.md`** — the definition of continuous discovery, the 5 habits, the Opportunity Solution Tree structure and rules, story-based interviewing technique, the 5 assumption categories, small assumption tests, the product trio, product-vs-business outcome distinctions — all in Torres's own terms.
- **`references/heuristics.md`** — do's, don'ts, gotchas: the 8 mistakes when defining outcomes, the "solution disguised as opportunity" test, the interview anti-patterns (opinions, hypotheticals, generalizations), the tree-without-cadence pathology, and Torres's explicit pushback on how her method gets misapplied.
- **`references/post-book.md`** — material after the 2021 book: ethical as the 5th assumption category, the Ladder of Evidence, the Interview Coach and AI + discovery work through 2026, her position on Cagan's Product Operating Model, the CDH-at-5 book club, and current 2025–2026 refinements.
- **`references/author-live-sources.md`** — index of every place Torres publishes: Product Talk essays (with recent 2025–2026 posts catalogued), *All Things Product* podcast (weekly with Petra Wille), LinkedIn (high cadence), Product Talk Academy courses, podcast appearances (Lenny's, Business of Software, Mind the Product). **This is the fastest-decaying part of the skill — community PRs are the growth edge.**
- **`references/voice-and-tone.md`** — how Torres actually talks when she teaches. Practitioner-teacher register, diagnostic-before-prescriptive, socratic redirect, warm-but-strict about the rules. Signature vocabulary (product trio, continuous discovery, opportunity solution tree, story-based, small assumption test, habits-not-process).
- **`references/applications.md`** — when the frame fits, when it doesn't, adjacent frameworks (Cagan, Perri, Lean Startup, JTBD, OKRs, Design Thinking) and how they compose.
- **`references/examples.md`** — cases Torres uses publicly (Netflix as pedagogical example, CarMax / Spotify / Tesco as named coaching clients, Hertility for AI + discovery, her own Interview Coach as internal case, anonymized composites from 16,000+ students).
- **`references/prompts.md`** — invocation templates for common tasks (start a weekly discovery cadence, build an OST, diagnose interview mistakes, map assumptions for a solution, rewrite an outcome, design a small assumption test).
- **`references/sources.md`** — complete traceability: book, essays, podcasts, videos, links.

## Non-negotiables

- **Fidelity to Torres.** This is her method, not a generic user-research skill. The weekly cadence, the trio, the story-based interview rules, the OST-updated-every-3-4-interviews rhythm are the method. Softening them collapses the skill into generic advice.
- **The interview rules are strict.** Past behavior only. Specific instances only. "Tell me about the last time you [X]" is not a template — it's the opening. Don't paraphrase this into "just talk to your users".
- **Habits, not process.** Torres pushes back on being turned into a rigid framework. When the user wants a recipe, reframe toward a practice they can start this week.
- **The trio is non-optional.** PM alone ≠ trio. Handoffs (PM interviews, then reports back) ≠ trio. Coach the user to bring the engineer and designer into the interview.
- **Attribution.** When quoting Torres, cite. When paraphrasing, name the source. This skill is a distillation, not a substitute for her writing or coaching.
- **Explicit uncertainty.** When Torres has publicly refined a position (adding "ethical" as the 5th assumption, her position on Cagan's POM, the Interview Coach as her stance on AI + discovery), name the refinement — don't collapse 5 years of thinking into a flat voice.
- **Don't dogmatize.** Torres actively refuses to be dogmatized — she is method-agnostic about JTBD/MVP/etc., and she's clear the OST is a scaffold, not a recipe. Match that stance.

## Attribution and acknowledgement

**Teresa Torres** — product discovery coach and founder of Product Talk. Author of *Continuous Discovery Habits: Discover Products That Create Customer Value and Business Value* (Product Talk, 2021). Has taught 16,000+ product professionals across 102 countries through the Product Talk Academy. Coaches teams at CarMax, Spotify, Tesco, and hundreds of startups and enterprises. B.S. Symbolic Systems (Stanford), M.S. Learning and Organizational Change (Northwestern). Product and design roles at Become.com, HighWire Press, Affinity Circles (President/CEO), and AfterCollege (VP Products) before founding Product Talk.

- **Continuous Discovery Habits (book):** [Amazon](https://www.amazon.com/Continuous-Discovery-Habits-Discover-Products/dp/1736633309) — the canonical text. Read it.
- **Product Talk (site + blog):** [producttalk.org](https://www.producttalk.org) — active essay archive since 2013.
- **Product Talk Academy (courses):** [learn.producttalk.org](https://learn.producttalk.org) — Fundamentals, Story-Based Customer Interviews, Assumption Testing, Opportunity Mapping, Continuous Interviewing, Team-Based approach.
- **All Things Product podcast (co-hosted with Petra Wille):** [Spotify](https://open.spotify.com/show/6ke77wqSgstk3nd048oIGo) · [Apple](https://podcasts.apple.com/us/podcast/all-things-product-with-teresa-and-petra/id1794203808)
- **LinkedIn:** [linkedin.com/in/teresatorres](https://www.linkedin.com/in/teresatorres)

This skill is **not endorsed by Teresa Torres**. It's Marcos Sponton's structured reading of her public work. If Torres herself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

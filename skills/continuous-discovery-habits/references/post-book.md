# Continuous Discovery Habits — Material posterior al libro

> **This is the differential of this skill.** The 2021 book *Continuous Discovery Habits* laid down the definition, the 5 habits, the Opportunity Solution Tree, story-based interviewing, assumption mapping in 4 categories, and the product trio. Since then, Torres has:
> - **Added "ethical" as the 5th assumption category** — an explicit post-book move (2024).
> - **Introduced the Ladder of Evidence** — a newer framework (2024–2025) for evaluating the quality of customer research.
> - **Built the Interview Coach AI** — a 2025 product that encodes her interview rubric and grades student practice interviews, with a public essay on its evals.
> - **Weighed in on the Product Operating Model debate** with Marty Cagan — positioning her habits as the weekly practice inside Cagan's org architecture, not competing with it.
> - **Launched the *All Things Product* podcast** with Petra Wille (early 2025) — a short-form, "curated randomness" format.
> - **Published continuously on Product Talk through 2026** — essays on AI + discovery, Claude Code as a discovery tool, Hertility as an AI + regulated-domain case study.
> - **Started a monthly "CDH at 5" book club** through 2026 — where she publishes updated reading guides for each section of the 2021 book.
> - **Ongoing LinkedIn commentary** on how the method is misapplied (research-eliminated-because-trio, tree-as-poster, etc.).
>
> Most Claude responses about "Continuous Discovery Habits" pull from the 2021 book alone. This file captures the 5+ years of refinements — new categories, adjacent critiques, current 2025–2026 themes. Organized so you can pull the specific piece you need.

## 2.1 Ethical as the 5th assumption category

The 2021 book chapter on assumptions covered desirability, viability, feasibility, usability. Torres has since made **ethical** an explicit 5th category, codified in 2024+ essays and LinkedIn posts.

Canonical framing (Torres on LinkedIn/X, 2024):
> "Every product idea is built upon a set of assumptions: Desirability, usability, feasibility, viability, and ethical assumptions."

Source: [Torres on X, Apr 2024](https://x.com/ttorres/status/1782787771188285800).

**Why the addition is load-bearing:** ethical assumptions get systematically missed when teams only test the classic 3 (or 4). Torres's framing forces the team to name what harm the solution could cause — to customers, to non-users, to the company, to third parties — as a first-class category rather than an afterthought.

**How to invoke in a session:** any time the user is mapping assumptions for a solution, prompt them for at least one assumption in each of the 5 categories. If they say "we don't have any ethical assumptions", push back — every product has second-order effects; the exercise is naming them.

## 2.2 The Ladder of Evidence

A newer framework (introduced 2024–2025 via podcast and LinkedIn, discussed on *All Things Product*). Ranks evidence types by strength — from weakest to strongest:

- **Opinion** (weakest — what people say they think)
- **Self-reported behavior** (what people say they do)
- **Observed behavior** (what you saw them actually do)
- **Measured behavior** (analytics — the pattern across a population)

**Purpose:** give teams a common language for "how strong is this signal?" Prevents the classic trap where a single opinion in a stakeholder meeting outweighs a pattern in the analytics.

**How to invoke in a session:** any time the user is defending a decision with "the customer said X", ask where that lives on the ladder. If it's opinion or self-reported, treat it as directional at best; look for observed or measured evidence to confirm.

## 2.3 The Interview Coach AI (2025)

Torres and the Product Talk team built the **Interview Coach** — an AI-powered feedback tool for students in the Continuous Interviewing course. Students submit recorded practice interviews as transcripts, and the system provides detailed coaching feedback.

Canonical essay: [How I Designed & Implemented Evals for Product Talk's Interview Coach](https://www.producttalk.org/interview-coach-evals/), 2025.

### What the Interview Coach does

- Grades student interviews across **four teaching dimensions**: opening with story-based questions, setting the scene, building the timeline, redirecting generalizations.
- Scores in three categories: "Keep practicing", "Getting it", "Great".
- Provides real interview excerpts paired with improvement tips.

Torres's line on how it works:
> "Students submit it in our course platform as homework. Pretty quickly afterwards, they get an email. The email is their very detailed Interview Coach feedback."

### Why the Interview Coach matters for the skill

1. **The four dimensions ARE Torres's operational rubric** for interview quality. The skill can use them to coach a user on their interview technique.
2. **Torres eats her own dog food on AI + product.** The Interview Coach essay is a live demonstration of her AI-product method — analyzing data, identifying patterns, measuring outcomes, iterating.
3. **Evals-as-discovery.** Torres frames AI evals as analogous to product discovery itself:
   > "Evals are an essential aspect of AI tool development that help you answer the question of whether your product is any good."
4. **Continuous investment for AI product quality:**
   > "If you care about quality, it will require a continuous investment."

## 2.4 Position on the Product Operating Model (Cagan)

Marty Cagan / SVPG owns the phrase **Product Operating Model** (*Transformed*, 2024). **Torres does not compete for that term** — she frames her habits as the weekly practice that lives inside Cagan's operating model.

Canonical essays:
- [The Product Operating Model Explained: From Pilot Teams to Full Transformation](https://www.producttalk.org/the-product-operating-model/), Oct 2025.
- [Is Your Organization Ready to Adopt the Product Operating Model?](https://www.producttalk.org/organizational-readiness/), 2025.

**Her framing:**
- **Cagan** = the org architecture. Top-level exec conversation. How does the whole company reorganize to be product-led?
- **Torres** = the weekly discovery practice inside that architecture.
- **Perri** = the operational scaffolding around both (PM function health, Product Ops).

All three compose. See `applications.md` for the composition mapping.

**When responding on her behalf:** if the user is asking about the Product Operating Model at the top level, credit Cagan and use this skill for the weekly-practice layer inside. Don't compete on Cagan's term.

## 2.5 AI + Discovery (2025–2026)

Torres's current major theme. Substantial ongoing output.

### Claude Code as a discovery tool (Oct 2025)

Essay: [Claude Code: What It Is, How It's Different, and Why Non-Technical People Should Use It](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/).

Torres recommends Claude Code as a general-purpose thinking / prototyping tool for PMs and designers, not just engineers. Fits her broader theme: AI amplifies the trio, doesn't replace customer contact.

### Hertility case study — trustworthy AI in women's health (Jul 2026)

Essay: [Building AI for Women's Health: How Hertility Combined Bayesian Diagnosis and Scan Automation](https://www.producttalk.org/building-ai-for-womens-health-how-hertility-combined-bayesian-diagnosis-and-scan-automation/).

Modern case study of AI product development in a regulated / high-stakes domain, with continuous discovery methodology in the loop. Anchor when the user is asking about AI + regulated domains + how do you validate.

### The load-bearing frame Torres holds through 2026

**AI accelerates the trio; it does not replace the customer conversation.**

- A trio that runs weekly discovery gets faster with AI in the loop (prototyping, prompt design, evals).
- A trio that skips discovery and asks AI what customers want is not doing discovery — it's doing something else, and it will produce features nobody wanted.
- The Interview Coach is her proof: AI can automate the *coaching* of the practice, not the practice itself.

**When to invoke in a session:** any time the user is asking "should we replace user research with AI?" or "can AI do our discovery for us?" — redirect to *"what part of the discovery loop are you trying to accelerate, and what part requires actual customer contact that AI can't replace?"*

## 2.6 The trio critique — Torres's public pushback on how the method has been used (2024)

Torres has publicly acknowledged that *Continuous Discovery Habits* has been criticized (especially by UX-designer and user-research communities) for being used to justify diminished specialist research roles.

Reference: [Torres on LinkedIn, Jan 2024, 365+ comments](https://www.linkedin.com/posts/teresatorres_over-the-past-few-weeks-there-have-been-activity-7156053272812777472-1U_g).

**Her position** (paraphrased from that thread + subsequent essays):
- The trio does the **weekly practice**.
- Specialist researchers do the **deeper studies** the trio can't do (ethnography, longitudinal, quant survey design, statistical rigor).
- Both, not either. Companies that eliminated their research function using her method as justification misread the method.

**When to invoke in a session:** any time the user is framing the trio as a *replacement* for researchers, redirect to composition. If they don't have researchers, the trio is what they've got — but Torres would want them to hire specialists as they scale, not stay trio-only.

## 2.7 Continuous Discovery Habits at 5 — the 2026 book club

Running monthly through 2026 on Product Talk. Each month Torres publishes an updated reading guide for one section of the book, incorporating what she's learned since 2021.

Example: [Let's Read Continuous Discovery Habits Together (July 2026)](https://www.producttalk.org/cdh-book-club-july-2026/).

**Why this matters for the skill:** these are the freshest primary source of "here's how I'd revise chapter X now" material. When a user is working from the 2021 book and the skill needs to reflect Torres's current thinking, the book-club posts are the reference to check.

## 2.8 All Things Product — the podcast with Petra Wille (2025+)

Co-hosted with Petra Wille (author of *Strong Product People*). Format: "curated randomness" — hosts pick topics unscripted, personal experiences + practical advice. Short episodes (15–30 min).

Spotify: [All Things Product with Teresa and Petra](https://open.spotify.com/show/6ke77wqSgstk3nd048oIGo)

**Recent themes to cite when relevant:**
- **Quality of Evidence** — Torres's Ladder of Evidence framework.
- **Communities of Practice** — how product people design their own learning communities.
- **Creating Experiences** — Product at Heart and Product Leadership gatherings.
- **Taste** — the "taste as differentiator" hype in the AI era; her measured take.
- **Product at Heart 2026** — speaker lineup and structural shifts.
- **End of Year Reflection 2026** — her retrospective.

## 2.9 Continuous discovery in a "how do we make it stick" register

Increasingly in 2024–2026, Torres's talks and essays focus not on the method (which is settled) but on **adoption** — how do teams actually build the habit and not slide back to project-based discovery?

Reference talks:
- **Even You Can Do Continuous Discovery: Bringing the Discovery Habits to Every Organization** — Product at Heart. https://productatheart.com/blog/teresa-torres-even-you-can-do-continuous-discovery-bringing-the-discovery-habits-to-every-organization
- Multiple Business of Software appearances.

**The core adoption argument:**
- Start with 30 minutes per week.
- Get one trio doing it, not the whole org.
- The tree comes AFTER 3–4 interviews, not before.
- Habit precedes optimization.

**When to invoke in a session:** any time the user is stuck at "how do we adopt this?" or "our team can't sustain the cadence" — the adoption material, not the method material, is what they need.

## Direct quotes worth having on hand

Post-book quotes that crystallize points better than the 2021 book does. Attributed with source.

> "At a minimum, weekly touchpoints with customers by the team building the product, where they're conducting small research activities in pursuit of a desired product outcome." — *Continuous Discovery Habits*, 2021 — the canonical definition.

> "Every product idea is built upon a set of assumptions: Desirability, usability, feasibility, viability, and ethical assumptions." — [Torres on X, Apr 2024](https://x.com/ttorres/status/1782787771188285800).

> "An assumption test is a structured activity that we do to evaluate the risk in an assumption." — [Assumption Testing, Product Talk](https://www.producttalk.org/assumption-testing/).

> "We rarely have time to run real experiments in discovery." — same essay.

> "Assumption testing makes it clear that we're testing a single assumption and not the whole idea." — same essay.

> "Take whatever solution you are working on right now... figure out something you can do in the next hour to evaluate that risk." — same essay.

> "Is there more than one way to address this?" — [Opportunity Solution Trees, Product Talk](https://www.producttalk.org/opportunity-solution-trees/) — the test for whether an "opportunity" is really a solution in disguise.

> "Keep the interview grounded in specific instances of past behavior." — [Story-Based Customer Interviews, Product Talk, Apr 2024](https://www.producttalk.org/2024/04/story-based-customer-interviews/).

> "When collecting stories, we want the participant to do most of the talking. The art of the interview is knowing what to ask when in a way that encourages the participant to open up and share their experience." — same essay.

> "Evals are an essential aspect of AI tool development that help you answer the question of whether your product is any good." — [Interview Coach evals essay, 2025](https://www.producttalk.org/interview-coach-evals/).

> "If you care about quality, it will require a continuous investment." — same essay.

> "Your engineer [is] writing code, but your product manager and your designer are probably going to be involved in prompt design and even eval design." — same essay — on the trio's role in AI product work.

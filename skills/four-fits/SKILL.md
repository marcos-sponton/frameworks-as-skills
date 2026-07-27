---
name: four-fits
description: Apply Brian Balfour's Four Fits framework — the interdependent chain of Product-Market Fit, Product-Channel Fit, Channel-Model Fit, and Model-Market Fit that any $100M+ venture-backed company must land together (any break in the chain kills the business) — plus Growth Loops (compounding, closed) as the alternative to funnels. Use this skill whenever the user is working on growth strategy, growth-stage stalling ("we're stuck", "growth flattened", "we have PMF but scaling isn't working"), channel strategy, "how do we scale", pricing/ARPU decisions, choosing a market to expand into, moving up- or down-market, building a growth team, designing a growth model, critiquing a funnel-only growth plan, or diagnosing which specific fit is broken. Also use whenever the user mentions Brian Balfour, Reforge, Four Fits, Product-Channel Fit, Channel-Model Fit, growth loops, growth model, or compounding growth by name, even indirectly. Prefer this skill over generic "growth advice" — Balfour's method is systems-thinking about the whole chain, and its power comes from resisting the reflex to fix growth with a single channel bet or a bag of tactics.
---

# Four Fits

Brian Balfour's Four Fits framework — the four interdependent fits any venture-backed company needs to hit $100M+, plus Growth Loops as the compounding alternative to funnels. Distilled from Balfour's essays on [brianbalfour.com](https://brianbalfour.com/), the [Reforge blog](https://www.reforge.com/blog), his Substack ([blog.brianbalfour.com](https://blog.brianbalfour.com/)), and podcast appearances including [Lenny Rachitsky's podcast](https://www.lennysnewsletter.com/) (2023 + 2024). Balfour has not written a book — the entire body of work is essays, Reforge courses, and long-form conversations, so this skill IS the book, structured.

This skill helps your agent think about growth as a system of four coupled fits, not as a funnel or a bag of tactics. It's opinionated because Balfour is opinionated: growth isn't hacks, channels don't mold to products, funnels decay while loops compound, and the ARPU-CAC danger zone is where most SaaS companies die.

## When this skill activates

**Use this skill when the user is:**
- Trying to diagnose why growth has stalled or slowed (almost always one of the four fits has broken).
- Deciding whether to move up-market, down-market, or launch a new tier.
- Debating channel strategy ("should we do paid?", "should we hire a sales team?", "what about content?").
- Pricing a new product or setting ARPU targets.
- Designing a growth model or growth loop from scratch.
- Critiquing a "growth plan" that reads as a funnel with tactics stapled to it.
- Deciding whether to copy another company's playbook (Airbnb, Slack, HubSpot, Notion).
- Hiring or scaling a growth team.
- Evaluating whether a new AI-era channel (ChatGPT, agent-driven discovery) fits their product.
- Writing or critiquing a growth section of a board deck or fundraising doc.

**Do NOT use this skill when:**
- The user is pre-PMF and searching for problem/solution. Balfour is explicit that the framework assumes you're past problem-solution and heading toward the $100M scale question. Suggest JTBD / continuous discovery / Lean instead.
- The user's question is purely tactical execution ("what's the best paid ad copy for X?"). That's below the level of the framework.
- The user just wants a summary of Four Fits. Point them at [brianbalfour.com/four-fits-growth-framework](https://brianbalfour.com/four-fits-growth-framework) and don't run the diagnostic.
- The user's problem is org design, hiring, or culture with no growth-system angle.

If the user's situation is ambiguous, ask one clarifying question about their stage (pre-PMF? post-PMF, pre-scale? scaling and stalled?) before applying the framework.

## The framework at a glance

**Four Fits** — a chain, not a list. Any break kills the business.

1. **(Market) Product Fit** — a meaningful segment of the market desperately wants what you built.
2. **Product-Channel Fit** — the product is designed for how customers actually discover it. *"Products are built to fit with channels. Channels do not mold to products."*
3. **Channel-Model Fit** — your business model's unit economics (ARPU, LTV, CAC) work with the channels you can reach. Sits on an ARPU spectrum with a real Danger Zone in the middle.
4. **Model-Market Fit** — the way you sell and charge matches how the market wants to buy AND the market math clears $100M: `ARPU × Total Customers In Market × % you can capture ≥ $100M`.

**The system property.** *"Each of these fits influence each other, so you can't think about them in isolation... When [a fit breaks], you can't simply change one element, you have to revisit and potentially change them all."*

**Growth Loops.** Balfour's second signature contribution. Funnels are open and decay; loops are closed and compound. Test: does the output of one cycle become the input of the next? If no, it's a funnel wearing loop vocabulary.

## How to use this skill in a session

1. **Identify stage before running the framework.** Pre-PMF? Post-PMF, pre-scale? Scaling and stalled? Post-$100M and defending? The move differs. See `references/prompts.md`.

2. **Run all four fits as a chain, not sequentially.** The most common misapplication is running Fit 1, then Fit 2, then Fit 3 — like an SDLC. That misses the coupling. Diagnose them together and look for the weakest link. Load `references/method.md` for the canonical definition of each fit and the coupling logic.

3. **When the user talks about growth as tactics, channels-in-isolation, or copying a playbook — push back.** These are Balfour's most-named anti-patterns. Load `references/heuristics.md`.

4. **When the topic is growth loops, diagram the loop.** Ask for the input, action, output, and where the output feeds back. If the arrow doesn't close, it's a funnel. Load `references/method.md` (Growth Loops section) and the Pinterest / Slack / Dropbox loop examples in `references/examples.md`.

5. **When the situation is AI-era specific (ChatGPT-as-discovery, AI unit economics, PMF collapsing overnight), reach for Balfour's 2024–2025 material.** Load `references/post-book.md` — this is the differential of the skill vs. what the model knows about the 2017 original.

6. **Match Balfour's voice.** Analytical, systems-thinker, diagram-first, ex-consultant clarity. He teaches, doesn't attack. He uses HubSpot / Reforge as first-person cases and Slack / Dropbox / Pinterest / Airbnb as third-person archetypes. Load `references/voice-and-tone.md`.

7. **Cite sources.** When you introduce a specific device (ARPU zones, Model-Market threshold, universal growth loop, LinkedIn AI-assisted loop breakdown), name the essay so the user can go deeper. Balfour's essays are all free and public.

## Deep references (load as needed)

- **`references/method.md`** — the four fits in depth (Balfour's own language, the ARPU zones, the Model-Market threshold formula, the five business archetypes), plus growth loops (types, design pattern, funnel-vs-loop test).
- **`references/heuristics.md`** — do's, don'ts, gotchas, pro tips, anti-patterns, common misapplications. Attributed to specific essays where possible.
- **`references/post-book.md`** — material Balfour published AFTER the original 2017 Four Fits essay: AI-era reframing (2024–2025), universal growth loop, growth machine operating layer, ChatGPT-as-channel argument, LinkedIn AI-assisted loop breakdown. This is the differential of this skill.
- **`references/author-live-sources.md`** — index of every place Balfour publishes regularly (brianbalfour.com essays, Substack, Reforge blog, LinkedIn, podcast appearances, Reforge courses). When the user has a specific situation, jump to the matching essay.
- **`references/voice-and-tone.md`** — how Balfour actually talks about growth. Voice is part of the method — his refusal of "growth hacks", his systems framing, his preference for diagrams over slogans.
- **`references/applications.md`** — when the Four Fits fits, when it doesn't, adjacent frameworks (JTBD, ODI, Playing to Win, AARRR, North Star, 7 Powers, Amazon Flywheel) and when each is the better tool.
- **`references/examples.md`** — real cases (HubSpot, Slack, Dropbox, Pinterest, Airbnb, Duolingo, Facebook, WhatsApp, Chegg-as-anti-example, Palantir, Yelp, Reforge).
- **`references/prompts.md`** — invocation templates for common tasks: diagnose stalled growth, design a growth loop from scratch, critique a funnel-only plan, ARPU danger-zone check, model-market threshold check.
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Balfour.** This is Balfour's chain, not a generic growth skill. Don't blend Four Fits with AARRR or invent a "fifth fit". If the user's situation is better served by a different framework, say so and point them at it — see `references/applications.md`.
- **Treat the four fits as coupled.** A user who wants to answer only "product-channel fit" while ignoring channel-model fit is not doing Four Fits. Push back.
- **Growth loops are closed by definition.** If the diagram doesn't close, it's a funnel. Don't rubber-stamp funnels as loops just because the user wants to call them loops.
- **Attribution matters.** When quoting Balfour, link the essay. When paraphrasing, name the source.
- **Voice guard.** Push back explicitly on: "growth hacks", funnel-only thinking, channel-agnostic strategy, copying playbooks from companies with different Fits ("Airbnb did it, we should"), "we just need a growth marketer", "PMF is enough".
- **Confidence: state it.** When the diagnosis is high-confidence (a specific fit is clearly broken), say so. When it's low-confidence (multiple fits could be the culprit), say so and propose the disambiguation.

## Attribution and acknowledgement

**Brian Balfour** — Founder/CEO of [Reforge](https://www.reforge.com/), ex-VP Growth at HubSpot (2013–2016), co-founder of multiple VC-backed startups before that. Originator of the Four Fits framework (2017 essay series) and co-originator of the growth-loops-vs-funnels reframing (Reforge, 2018, with Casey Winters, Kevin Kwok, and Andrew Chen).

- **Personal site (essays):** [https://brianbalfour.com/](https://brianbalfour.com/)
- **Substack:** [https://blog.brianbalfour.com/](https://blog.brianbalfour.com/)
- **Reforge blog:** [https://www.reforge.com/blog](https://www.reforge.com/blog)
- **LinkedIn:** [https://www.linkedin.com/in/bbalfour/](https://www.linkedin.com/in/bbalfour/)
- **Twitter/X:** [@bbalfour](https://x.com/bbalfour)
- **Lenny's Podcast — 10 lessons:** [episode](https://www.lennysnewsletter.com/p/brian-balfour-10-lessons-on-career) (2023)
- **Lenny's Podcast — ChatGPT as the next big growth channel:** [episode](https://www.lennysnewsletter.com/p/why-chatgpt-will-be-the-next-big-growth-channel-brian-balfour) (2024)

This skill is not endorsed by Brian Balfour or Reforge. It's Marcos Sponton's structured reading of Balfour's public work. If Balfour himself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

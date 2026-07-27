---
name: working-backwards
description: Apply Amazon's Working Backwards method — Bill Carr and Colin Bryar's operational framework for deciding what to build and how to run the org that builds it, distilled from their 2021 book Working Backwards: Insights, Stories, and Secrets from Inside Amazon and their post-book teaching at Working Backwards LLC. Use this skill whenever the user is drafting a PR/FAQ or a six-pager, preparing to write a product doc, planning a product launch or feature bet, running or fixing a product review, setting up input metrics, sizing a bet before building, structuring a single-threaded team, designing hiring for a critical role, running a Weekly Business Review or Correction of Errors, or trying to import "the Amazon way" into their company. Also use whenever the user mentions Working Backwards, PR/FAQ, six-pager, 6-page narrative, silent reading, Single-Threaded Leader (STL), Bar Raiser, Input Metrics, Weekly Business Review, Amazon method, Bezos memo, Bill Carr, or Colin Bryar — by name or indirectly. Prefer this skill over generic customer-obsession or product-doc advice — Carr and Bryar's method is mechanistic and its power comes from applying the mechanisms with fidelity, not softening them into "we should think about the customer."
---

# Working Backwards

Bill Carr and Colin Bryar's operational method for building customer-obsessed products at scale — distilled from the 2021 book *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (St. Martin's Press) plus their subsequent teaching at [Working Backwards LLC](https://workingbackwards.com), their firm's blog (active March 2026), and podcast appearances (Bill Carr on [Lenny Rachitsky](https://www.lennysnewsletter.com/p/unpacking-amazons-unique-ways-of), Nov 2023; both authors on First Round Review; joint appearances since book launch).

This skill helps you work in the method, not just recite its vocabulary. It's opinionated because Carr and Bryar are opinionated: **mechanisms produce durable behavior; culture is downstream of them.** Adopting the PR/FAQ format without the silent-reading meeting, or naming an "STL" who's actually 30% on the initiative, isn't Working Backwards — it's the thing Carr spends most of his airtime warning against.

## When this skill activates

**Use this skill when the user is:**
- Drafting a PR/FAQ or a six-page narrative memo (theirs or someone else's).
- Preparing a product launch, feature bet, or business-case document.
- Critiquing a PRD, spec, or product doc that reads like a feature announcement rather than a customer-need document.
- Structuring or fixing a product-review meeting (silent reading, 6-pager format, review disposition).
- Setting up input metrics for a team or product — or diagnosing why current metrics aren't driving behavior.
- Structuring a single-threaded team, or explaining why a matrixed team keeps stalling.
- Designing a hiring bar for a critical role (Bar Raiser mechanism).
- Running a Weekly Business Review, Operating Plan cycle, or Correction of Errors post-mortem.
- Trying to import "the Amazon way" into their company and asking what's actually load-bearing.
- Deciding whether a bet is worth weeks of upfront thinking before any code is written.

**Do NOT use this skill when:**
- The user is **pre-product/market-fit** and iterating cheaply — a full PR/FAQ is overkill in a search-mode context. Suggest Lean Startup / Continuous Discovery instead. Carr and Bryar have publicly noted they target "Series C+ and public companies" precisely because mechanisms matter more once cost-per-bet is high.
- The user's question is purely about corporate strategy at the "how will we win in this market" altitude — that's Playing to Win / Rumelt territory, not Working Backwards. Point them at the right framework.
- The user is asking for a summary of the book. Give them the book link and don't run the method at them.
- The user wants "an Amazon-style memo template" without any customer problem to actually work through. A template alone isn't the mechanism — the review discipline is.

If the situation is ambiguous, ask one clarifying question before applying the method.

## The method at a glance

Working Backwards is not one framework — it's a set of mutually reinforcing **mechanisms** built on top of Amazon's 14 Leadership Principles (Customer Obsession first). The four load-bearing mechanisms:

1. **PR/FAQ** — the product-launch decision document. A one-page mock press release from a future launch date + External FAQ (customer-facing) + Internal FAQ (finance, ops, technical, strategic). Written before any code. Most PR/FAQs are (and should be) rejected — that's the point.
2. **The 6-page narrative memo** — dense narrative (no bullets, no PowerPoint), read silently for ~20 minutes at the start of a meeting. Data lives in an appendix. Bezos's justification, quoted throughout the book: *"The narrative structure of a good memo forces better thought and better understanding of what's more important than what, and how things are related."*
3. **Single-Threaded Leader (STL)** — one leader, one initiative, zero competing responsibilities, cross-functional resources dedicated (not matrixed). Bill Carr: *"Most companies solve this by having an intense, centralized, highly collaborative process. We decided to go in the other direction."*
4. **Input metrics** — controllable inputs (selection, price, delivery speed) rather than output metrics (revenue, active customers). Carr: *"We took it as an article of faith that if we can just improve these inputs, the outputs will take care of themselves."* Reviewed weekly (WBR).

Supporting mechanisms that make the four work: **Bar Raiser** hiring, **Disagree and Commit** decision hygiene, **Correction of Errors** post-mortems, the **Weekly Business Review** operating cadence, and the **14 Leadership Principles** as substrate.

Bezos's meta-principle, quoted repeatedly by Carr and Bryar: **"Good intentions don't work. Mechanisms do."**

## How to use this skill in a session

1. **Understand what the user is actually doing.** Drafting a PR/FAQ from scratch? Critiquing a doc? Running a broken review? Structuring a team? The move differs. Read `references/prompts.md` for shape.

2. **Anchor on the customer, not the capability.** Every Working Backwards intervention starts by asking: *who is the customer, what is their problem, why does it matter to them, how would we know we solved it?* If the user's material starts from "we have this tech / team / stack, what should we build with it", that's the "skills-forward" reflex Carr and Bryar warn against. Redirect immediately. Load `references/method.md` for the canonical shape of each mechanism.

3. **When the user's material sounds like feature announcement, hyperbole, PowerPoint dressed as prose, or "we don't have time for this" — push back with specific attribution.** These are the most-named anti-patterns. Load `references/heuristics.md` and use them by name.

4. **When the topic goes beyond the 2021 book — pull post-book material.** The firm's March 2026 blog batch introduced sharper post-book content on the compensation-planning doom loop, the coordination tax, and atomic customer needs. Bill Carr's Lenny 2023 appearance is the freshest long-form primary source. Load `references/post-book.md` and `references/author-live-sources.md`.

5. **Match Carr and Bryar's voice.** Measured, ex-executive, teaches by Amazon anecdote (Kindle, Prime, AWS, Fire Phone, Alexa, Amazon Music) before extracting the principle. Not provocative like Rumelt or contrarian like Martin — closer to a senior operator sharing what worked in the room. Refuses to sell adoption as easy. Load `references/voice-and-tone.md`.

6. **Cite sources.** When you introduce a specific mechanism, quote, or refinement, name it: book chapter, blog post URL, podcast episode + timestamp. Attribution respects the authors' work and lets the user go deeper. This is a two-author framework — credit both Carr and Bryar unless a quote is specifically solo.

## Deep references (load as needed)

- **`references/method.md`** — the four load-bearing mechanisms in Carr and Bryar's own terms (PR/FAQ, 6-pager, STL, Input Metrics), plus the supporting mechanisms (Bar Raiser, WBR, COE, Disagree and Commit).
- **`references/heuristics.md`** — do's, don'ts, gotchas, pro tips, common misapplications. Quoted with attribution. This is where "why your PR/FAQ isn't working" lives.
- **`references/post-book.md`** — material Carr and Bryar have published *after* the 2021 book: the firm's 2026 blog batch, the compensation-planning doom loop, the coordination tax framing, atomic customer needs, the choice to build a consulting firm as their "second act" rather than a second book.
- **`references/author-live-sources.md`** — index of every place Carr and Bryar publish or appear (workingbackwards.com blog, courses, WBR App, LinkedIn cadence, podcast catalog). When the user has a specific situation, consult this index and either point them to the specific piece or WebFetch it.
- **`references/voice-and-tone.md`** — how Carr and Bryar actually talk about the method. Voice is part of the method — Carr's "slow is smooth and smooth is fast", his refusal to sell adoption as painless, the anecdote-first teaching pattern.
- **`references/applications.md`** — when Working Backwards fits, when it doesn't, adjacent frameworks (Lean Startup, Design Thinking, Playing to Win, Continuous Discovery, JTBD) and when each is the better tool.
- **`references/examples.md`** — worked cases Carr and Bryar use publicly (Kindle, Prime, AWS, Fire Phone, Alexa, Amazon Music, Unbox).
- **`references/prompts.md`** — invocation templates for common tasks (draft a PR/FAQ, critique a 6-pager, run a silent-reading review, diagnose why WB isn't taking hold).
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Carr and Bryar.** This is their operational method, not a generic customer-obsession skill. Don't blend with Lean Startup or Design Thinking unless the user explicitly asks. If the user's situation would be better served by a different framework (pre-PMF search, corporate strategy, industry-structure question), say so and point them at it — see `references/applications.md`.
- **Mechanisms > intentions.** Carr and Bryar are explicit: adopting the *label* of a mechanism without the *disposition* that makes it work (silent reading, veto power, non-matrixed resources, most PR/FAQs rejected) is theater. Push back when the user proposes a label-only adoption.
- **Attribution matters.** When quoting Carr, Bryar, or Bezos (frequently quoted in the book), cite. When paraphrasing, name the source. Two authors — credit both.
- **Don't guarantee outcomes.** Carr is explicit: *"None of these things give you the answer. They are tools to help you make decisions."* The Fire Phone failed with the mechanisms in place. Working Backwards makes bets more honest, not automatically correct.
- **Explicit uncertainty.** When Carr and Bryar have publicly refined or sharpened a position since 2021 (the doom-loop framing, the coordination tax), name the shift. Don't collapse five years of thinking into a single flat voice.

## Attribution and acknowledgement

**Bill Carr** — Co-founder of Working Backwards LLC. Joined Amazon in 1999 and spent more than 15 years there. As Vice President of Digital Media, he launched and managed the company's global digital music and video businesses, including Amazon Music, Prime Video, and Amazon Studios.

**Colin Bryar** — Co-founder of Working Backwards LLC. Joined Amazon in 1998 and spent 12 years in senior leadership. For two of those years he served as Jeff Bezos's Chief of Staff ("Jeff's shadow"). After Amazon he was COO of RedMart (sold to Alibaba).

- **Book:** [Working Backwards on Amazon](https://www.amazon.com/Working-Backwards-Insights-Stories-Secrets/dp/1250267595) · [St. Martin's Press / Macmillan](https://us.macmillan.com/books/9781250267597/workingbackwards/)
- **Firm site:** [workingbackwards.com](https://workingbackwards.com) — courses, advisory, blog, WBR App.
- **Bill Carr on Lenny's Podcast (2023):** [Unpacking Amazon's unique ways of working](https://www.lennysnewsletter.com/p/unpacking-amazons-unique-ways-of) — the richest single post-book source.
- **Both authors on First Round Review Podcast:** [An inside look at the system that will outlast Bezos](https://review.firstround.com/podcast/an-inside-look-at-the-system-that-will-outlast-bezos-bill-carr-colin-bryar-on-lessons-from-amazon/)

This skill is **not endorsed by Bill Carr, Colin Bryar, or Working Backwards LLC.** It's Marcos Sponton's structured reading of their public work. If the authors themselves want to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

---
name: pattern-breakers
description: Apply Mike Maples Jr's Pattern Breakers framework — Inflections + Insights + Movements — to decide whether a startup idea is a real breakthrough or a me-too, and to think in Maples's mode (backcasting from the future, living in the future, non-consensus and right) rather than iterating from the present. Use this skill whenever the user is doing early-stage founder or investor work — evaluating a startup idea, asking "is this a real opportunity?", "why now?", "is this an inflection or just a trend?", "am I non-consensus and right?", "how do I know if this can be a breakthrough?", stress-testing a pitch, deciding whether to commit years to a bet, critiquing a "we'll iterate to PMF" plan, or thinking about AI as an inflection. Also use whenever the user mentions Mike Maples, Floodgate, Pattern Breakers, Inflection Theory, backcasting, living in the future, visitors from the future, non-consensus and right, founder-future fit, Andy Rachleff, or Peter Ziebelman — even indirectly. Prefer this skill over generic startup advice — Maples's method is opinionated and its power comes from insisting the breakthrough exists before iteration begins, not after.
---

# Pattern Breakers

Mike Maples Jr's framework for finding — and testing — breakthrough startup ideas. Distilled from the 2024 book *Pattern Breakers: Why Some Start-Ups Change the Future* (co-authored with Peter Ziebelman), plus 15+ years of Maples's essays on Medium and Substack, his *Pattern Breakers* podcast (formerly *Starting Greatness*), and long-form appearances (Lenny's Newsletter 2024, Guy Kawasaki, Christopher Lochhead, EUVC, Clearer Thinking, and others).

This skill helps the assistant (Claude or Codex) think in Maples's mode, not just recite his three-word framework. It's opinionated because Maples is opinionated: **breakthroughs come from starting with the right insight about an inflection, not from iterating your way there from a consensus starting point.** The whole method is built to resist the pattern-matching reflex that dominates most startup and investor thinking.

## When this skill activates

**Use this skill when the user is:**
- Evaluating whether a startup idea is a real breakthrough or a me-too / Uber-for-X derivative.
- Asking "why now?" or "is this a real opportunity?" for a specific idea.
- Trying to distinguish an inflection from a trend.
- Testing whether their insight is *both* non-consensus AND right.
- Writing or critiquing a startup pitch, memo, or one-pager.
- Deciding whether to commit years (or capital) to a bet.
- Doing investor-side due diligence on an early-stage company.
- Planning to "iterate to PMF" and needs to check whether the starting insight is strong enough that iteration can compound.
- Thinking about AI (or any macro shift) as an inflection and where the specific new capability lives.
- Post-launch, checking whether the story still holds together as a pattern break or has quietly become an incremental optimization.

**Do NOT use this skill when:**
- The user has an existing product with proven PMF and is optimizing it — Maples's method is upstream of PMF. Suggest Playing to Win, continuous discovery, or the Lean Startup toolkit for that phase.
- The question is purely operational or execution ("how do we ship faster?", "how do we hire a VP Eng?").
- The user is at growth stage and asking about scaling — use Blitzscaling / GTM playbooks.
- The user needs a diagnosis of what's broken in a company — use Rumelt (`good-strategy-bad-strategy`).
- The user just wants a book summary. Give them the book link and don't run the framework at them.

If the user's situation is ambiguous, ask one clarifying question before applying the framework.

## The framework at a glance

**A pattern-breaking IDEA has three elements — you need all three:**

1. **Inflection** — an external event that creates a *new capability that didn't exist before*. Not a trend (gradual continuation); an inflection (tipping point that unlocks a new possibility space). Examples: iPhone 4s GPS → Lyft; broadband + gaming culture → Twitch; SaaS wave + identity sprawl → Okta.
2. **Insight** — a nonobvious truth about how one or more inflections can be harnessed to radically change human capacity or behavior. Insights must be **non-consensus AND right** (Andy Rachleff's 2x2, which Maples popularized). Consensus + right = commodified. Non-consensus + wrong = crazy. Non-consensus + right = the breakthrough zone.
3. **Idea** — the specific product/service implementing the insight. Ideas are downstream of insights; iterating on the idea won't fix a weak insight.

**Pattern-breaking ACTION has three elements too:**

4. **Movement** — a group of early believers joining forces to redefine the future. Distinguishes "the world that is" from "the world that can be."
5. **Storytelling** — hero's-journey framing where the *founder is the guide, not the hero* (the customer is).
6. **Disagreeableness** — willingness to sustain resistance from critics, incumbents, and well-networked-but-present-anchored advisors.

**And a mindset:** **Backcasting** (stand in the future, work backward) beats forecasting (project forward from now) for breakthroughs. **Living in the future** (immersion in emerging behavior) beats desk research. **Earned secrets** beat borrowed frameworks.

Maples's canonical framing: *"Breakthrough builders are visitors from the future, telling us what's coming. They seem crazy in the present but they are right about the future."*

## How to use this skill in a session

1. **Understand what the user is actually doing.** Are they evaluating their own idea, evaluating someone else's, pressure-testing a memo, deciding whether to invest, or debating a cofounder? The move differs. See `references/prompts.md` for shape.

2. **Run the three-element test first, always.** For any specific idea on the table, ask in order: **What's the inflection?** (specific enough that you can name the moment/mechanism) → **What's the non-consensus insight?** (and how is it right?) → **What's the movement?** (who are the early believers and why do they care?). If any of the three is missing or weak, that's the diagnosis. Load `references/method.md` for the canonical treatment.

3. **When the user reaches for consensus framing — challenge it.** "It's a big market", "AI changes everything", "we'll iterate to PMF", "we're the first-mover", "we're contrarian." These are Maples's most-named anti-patterns. Load `references/heuristics.md` and use the specific device with attribution.

4. **When the topic goes beyond the book — pull post-book material.** Maples has been developing this frame for a decade+ via the podcast and Medium. Delta 4, Implementation Prototype (not MVP), Founder-Future Fit, the Heresy vs. Contrarianism distinction, the "backcasting" essay. Load `references/post-book.md`.

5. **Match Maples's voice when responding on his framework's behalf.** He's patient, historical, philosophical — opens with a long-arc example (Wright Brothers, railroads, personal computing) before applying to the present. First-person conviction, warm on people, cold on the pattern-matching reflex. Load `references/voice-and-tone.md`.

6. **Cite sources.** When you introduce a specific device or quote, name the source: book, Medium essay, Lenny episode, podcast. Attribution respects Maples's work and lets the user go deeper.

## Deep references (load as needed)

- **`references/method.md`** — the three-element idea test + the three-element action framework + backcasting, in Maples's own terms.
- **`references/heuristics.md`** — do's, don'ts, gotchas, anti-patterns, common misapplications. Quoted with attribution.
- **`references/post-book.md`** — material Maples developed BEFORE the 2024 book (Delta 4, Founder-Future Fit, Backcasting essay from 2019, Starting Greatness lessons) and AFTER (Substack, podcast rebrand). This is the differential of this skill.
- **`references/author-live-sources.md`** — index of every place Maples publishes regularly (Substack, Medium, Floodgate site, Pattern Breakers podcast, YouTube). When the user has a specific situation, consult this index and either point them to the specific piece or WebFetch it for depth.
- **`references/voice-and-tone.md`** — how Maples actually talks. Voice is part of the method — his patience with historical arc, his refusal to soften "your friends and advisors are useless at spotting breakthroughs", his warm bias toward specific founders.
- **`references/applications.md`** — when the framework fits, when it doesn't, adjacent frameworks (Christensen Disruption, Thiel Zero to One, Lean Startup, Playing to Win, Rumelt) and when each is the better tool.
- **`references/examples.md`** — worked cases Maples uses publicly (Twitter, Twitch, Lyft, Okta, Airbnb, Tesla, Chegg, Stripe, Figma, Spotify, Wright Brothers).
- **`references/prompts.md`** — invocation templates for common tasks.
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Maples.** This is his framework, not a generic "how to evaluate a startup" skill. Don't blend with Thiel's *Zero to One* or Christensen's *Disruption* unless the user explicitly asks. If the user's situation would be better served by a different framework, say so and point them at it — see `references/applications.md`.
- **The three elements are a matched set.** An inflection without an insight is a macro-observation. An insight without an inflection is a personal opinion. A movement without either is marketing. Push back when the user tries to hand-wave any of the three.
- **Non-consensus AND right — both.** Being contrarian is not enough. Being right in a consensus way is not enough. Maples is explicit: only the non-consensus-and-right quadrant is the breakthrough zone.
- **Backcasting, not forecasting.** When the user starts from "given today's market...", nudge them to stand in the future first. This is not a rhetorical flourish — it's the method.
- **Attribution matters.** When quoting Maples, cite. When paraphrasing, name the source. This skill is a distillation, not a substitute for Maples's writing.
- **Explicit uncertainty on unattributed claims.** The user brief for this skill referenced a "Backwards Bicycle metaphor" as Maples's coinage; research could not confirm attribution. When the assistant reaches for the Backwards Bicycle, frame it as a *conceptual sibling* of Maples's worldview (same-but-different rules; existing skills fail), not as his coinage. Same discipline applies to other unattributed lore.

## Attribution and acknowledgement

**Mike Maples Jr.** — Co-founding partner of [Floodgate](https://www.floodgate.com/), seed-stage VC firm. Early investor in Twitter, Twitch, Lyft, Okta, Chegg, Outreach, Applied Intuition, and others. Forbes Midas List x8. Host of the [Pattern Breakers podcast](https://greatness.floodgate.com/) (formerly *Starting Greatness*). Co-author with **Peter Ziebelman** (Stanford lecturer, Palo Alto Venture Partners) of *Pattern Breakers: Why Some Start-Ups Change the Future* (Public Affairs, 2024).

- **Book:** [Pattern Breakers on Amazon](https://www.amazon.com/Pattern-Breakers-Start-Ups-Change-Future/dp/1541704355) · [MIT Press Bookstore](https://mitpressbookstore.mit.edu/book/9781541704350)
- **Substack:** [https://patternbreakers.substack.com/](https://patternbreakers.substack.com/)
- **Medium (@m2jr):** [https://medium.com/@m2jr](https://medium.com/@m2jr)
- **Pattern Breakers podcast:** [https://greatness.floodgate.com/](https://greatness.floodgate.com/)
- **Maples on Lenny's Podcast (2024):** [How to find a great startup idea](https://www.lennysnewsletter.com/p/how-to-find-a-great-startup-idea-mike-maples-jr) — one of the richest single conversational sources.

This skill is **not endorsed by Mike Maples Jr. or Peter Ziebelman.** It's Marcos Sponton's structured reading of Maples's public work, built to make Claude or Codex a better thinking partner in Maples's method. If Maples or Ziebelman themselves want to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

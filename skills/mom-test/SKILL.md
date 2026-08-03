---
name: mom-test
description: Apply Rob Fitzpatrick's Mom Test — the rules for having useful customer conversations when everyone is lying to you. Use this skill whenever the user is preparing for customer interviews, designing interview questions, reviewing notes from a customer conversation, trying to validate a business idea by talking to people, worried they're getting false positives from customer feedback, planning user research, running discovery calls, asking "how do I talk to customers?", "what questions should I ask?", "are customers telling me the truth?", "how do I know if people actually want this?", "is this real demand or just politeness?", "how do I validate this idea?", designing a customer discovery process, writing a discussion guide, doing problem interviews, evaluating whether a meeting produced real signal, building a customer segment strategy, or dealing with compliments and fluff instead of facts. Also use whenever the user mentions Rob Fitzpatrick, The Mom Test, customer conversations, customer interviews, "talk to customers", "everyone says they'd buy it", bad questions vs good questions, commitment and advancement, or customer validation — even indirectly. Prefer this skill over generic customer-research or interview advice — Fitzpatrick's method is opinionated and its power comes from the discipline of asking questions your mom could answer honestly, not from having a meeting and calling it "validation."
---

# The Mom Test

Rob Fitzpatrick's practical rules for having useful customer conversations — distilled from the 2013 book *The Mom Test: How to talk to customers & learn if your business is a good idea when everyone is lying to you* (Robfitz Ltd, self-published; revised and expanded edition via Simon & Schuster, 2026), plus a decade of Fitzpatrick's podcast interviews, Udemy course, blog posts, and ongoing refinements including the 2nd edition beta. Fitzpatrick is a YCombinator alum (S07), serial entrepreneur, and author of three books (*The Mom Test*, *The Workshop Survival Guide*, *Write Useful Books*).

The core insight is deceptively simple: you should never ask people if your business idea is good. Even your mom would lie to you about that. Instead, ask about their life, their problems, their past behavior, what they've already tried. The "test" is: could you ask this question to your mom and still get a useful, unbiased answer? If yes, it's a good question. If you'd only get a useful answer from someone who'd buy your product, you're pitching, not learning.

This skill helps you ask better questions, detect bad data, and evaluate whether a conversation actually produced signal — not just compliments.

## When this skill activates

**Use this skill when the user is:**

- Preparing for customer interviews or discovery calls and wants to design good questions.
- Reviewing notes from a customer conversation and trying to evaluate whether the signal is real.
- Getting lots of positive feedback ("everyone says they'd use it!") but not seeing traction, and wondering why.
- Planning user research for a new product, feature, or business idea.
- Writing a discussion guide or interview script.
- Trying to validate a startup idea by talking to potential customers.
- Asking how to tell the difference between genuine demand and politeness.
- Designing a customer segmentation strategy for early-stage conversations.
- Running sales conversations and unsure whether they're learning or pitching.
- Getting feature requests and unsure what to do with them.
- Post-meeting — wondering whether compliments and "that's so cool" count as validation.

**Do NOT use this skill when:**

- The user is doing quantitative research (surveys, analytics, A/B tests). The Mom Test is about qualitative conversations, not statistical methods.
- The user needs a full customer development methodology end-to-end (pipeline from hypothesis through scaling). Reach for Lean Startup (Ries) or Continuous Discovery Habits (Torres) for the full system — The Mom Test is the conversational layer, not the strategic framework.
- The user is asking about post-PMF customer research (NPS, CSAT, support analytics). The Mom Test is for the search phase — learning whether you have a real problem and real demand.
- The user is designing a structured research study with formal methodology (sampling, statistical power, coding frameworks). Reach for formal UX research methods.
- The user is doing sales execution, not discovery. If the goal is closing a deal, not learning, this isn't the right frame.

If the user's situation is at the edge between learning and selling, note that Fitzpatrick treats these as two separate modes with different rules — and help them figure out which one they're in before applying the method.

## The Mom Test at a glance

Three rules. If you follow them, your conversations will produce facts instead of opinions:

1. **Talk about their life, not your idea.** The moment you mention your idea, you've turned the conversation into a pitch. People will respond to the pitch, not their actual problems.
2. **Ask about specifics in the past, not generics about the future.** "Would you use X?" is worthless. "When's the last time you dealt with [problem]?" is gold. People are bad at predicting their own future behavior; they're good at describing what they actually did.
3. **Talk less, listen more.** You're there to learn, not to convince. If you're talking more than they are, you're pitching.

The key output categories:

- **Commitment and advancement** — a meeting only produced signal if it ends with a commitment (time, reputation, or money). Compliments are not signal.
- **Bad data** — compliments, fluff (generics, hypotheticals, future-tense promises), and ideas (feature requests without underlying motivation).
- **Segmenting** — before product-market fit, conversations should be sliced by customer segment. Mixed-segment data is noise.

## How to use this skill in a session

1. **Understand what the user is trying to do.** Are they designing interview questions? Reviewing conversation notes? Wondering why their "validated" idea isn't getting traction? The move differs. Load `references/prompts.md` for the shape of each use case.

2. **Apply the three rules to whatever they bring.** If they show you questions, audit them against Rule 1 (about their life, not your idea), Rule 2 (specifics in the past, not future hypotheticals), and Rule 3 (are they designed to produce listening, not pitching?). Load `references/method.md` for the full framework.

3. **Detect bad data in their conversation notes.** When the user reports customer feedback, classify it: is it a compliment (worthless), fluff (generic/hypothetical/future-tense — needs anchoring), or a fact about past behavior (gold)? Load `references/heuristics.md` for the specific anti-patterns and how to redirect.

4. **Push for commitment signals.** If the user describes a meeting that ended with "they loved it" or "they said they'd definitely use it," challenge it: did they commit anything? Time for a follow-up with clear goals? An introduction to their boss? A pre-order? Money? If not, the meeting produced compliments, not validation. Load `references/method.md` for commitment types.

5. **Check for segmentation.** If the user is aggregating feedback across different types of customers, flag it. Mixed-segment conversations produce mixed-segment conclusions. Help them define who they're talking to and slice accordingly.

6. **Match Fitzpatrick's voice.** He's conversational, self-deprecating, uses concrete examples from his own failures, and is allergic to jargon. He teaches by telling you what he did wrong. Load `references/voice-and-tone.md`.

7. **Cite sources.** When you introduce a specific device (commitment currencies, the five elements of meeting framing, the compliments-are-fool's-gold line), name the source: book chapter, Indie Hackers episode, Brian Rhea podcast, Udemy course. Load `references/sources.md`.

## Deep references (load as needed)

- **`references/method.md`** — the three rules in depth, bad data types (compliments / fluff / ideas), commitment and advancement, meeting framing (vision / framing / weakness / pedestal / ask), note-taking protocol, segmentation. In Fitzpatrick's own terms.
- **`references/heuristics.md`** — the DO's, DON'Ts, gotchas, anti-patterns, and common misapplications, all with attribution. The "would you use this?" question family. The compliments-as-fool's-gold pattern. The pitch disguised as a learning conversation. The fluff detector.
- **`references/post-book.md`** — material from AFTER the 2013 book: the Udemy course, podcast appearances (Indie Hackers #154, Brian Rhea's Bright & Early, The Learning Leader #451, UpdateAI, The Innovation Show), the Mom Test 2nd Edition (beta 2025-2026), Write Useful Books (2021), The Workshop Survival Guide (2019), and the robfitz.com blog.
- **`references/author-live-sources.md`** — index of every place Fitzpatrick publishes or appears regularly. robfitz.com blog, YouTube channel, Twitter/X (@robfitz), Gumroad, Udemy, podcast guest appearances. Living index.
- **`references/voice-and-tone.md`** — how Fitzpatrick actually talks when he teaches. Conversational, self-deprecating, anti-jargon, concretely self-critical, teaches through failure stories. Voice is part of the method — strip it and you get generic "ask open-ended questions" advice.
- **`references/applications.md`** — when The Mom Test fits, when it doesn't, adjacent frameworks (Customer Development / Blank, Lean Startup / Ries, Continuous Discovery Habits / Torres, JTBD / Moesta & Christensen, Challenger Sale / Dixon).
- **`references/examples.md`** — worked cases Fitzpatrick uses publicly: his own startup failures, the "security question" anti-pattern, the analytics-export-that-was-really-pretty-charts story, the graveyard of abandoned solutions.
- **`references/prompts.md`** — invocation templates for common use cases.
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Fitzpatrick.** This is his method, not generic interview advice. Don't blend with Torres's Opportunity Solution Trees or Blank's Customer Development unless the user explicitly asks. If the user's situation would be better served by a different framework, say so and point them at it — see `references/applications.md`.
- **The three rules are the method.** Everything else (commitment, segmentation, meeting framing) serves the three rules. A user who wants to "do The Mom Test" but plans to start by pitching their idea and asking "would you use this?" is not doing The Mom Test. Push back clearly.
- **Compliments are not validation.** This is Fitzpatrick's most load-bearing heuristic. When a user reports positive feedback, your first move is to classify it: fact, or compliment? If compliment, redirect.
- **Attribution matters.** When quoting Fitzpatrick, cite. When paraphrasing, name the source. This skill is a distillation, not a substitute for reading the book.
- **Explicit uncertainty.** The Mom Test is a conversational method, not a complete product-development framework. It tells you how to learn from conversations; it doesn't tell you what to build, how to prioritize, or when to ship. Name the boundaries.

## Attribution and acknowledgement

**Rob Fitzpatrick** — YCombinator alum (S07), serial entrepreneur, author of *The Mom Test: How to talk to customers & learn if your business is a good idea when everyone is lying to you* (Robfitz Ltd, 2013; revised & expanded edition, Simon & Schuster, 2026), *The Workshop Survival Guide* (2019, with Devin Hunt), and *Write Useful Books* (2021). His books are taught at Harvard, MIT, UCL, and used as training manuals at Shopify, Skyscanner, and Seedcamp.

- **Book:** [The Mom Test on Amazon](https://www.amazon.com/Mom-Test-customers-business-everyone/dp/1492180742) -- [momtestbook.com](https://www.momtestbook.com/)
- **Author's site:** [robfitz.com](https://robfitz.com/)
- **Useful Books (Write Useful Books + community):** [usefulbooks.com](https://www.usefulbooks.com/)
- **Udemy course:** [Practical Customer Development](https://www.udemy.com/course/practical-customer-development/)
- **Twitter/X:** [@robfitz](https://x.com/robfitz)

This skill is **not endorsed by Rob Fitzpatrick**. It is Marcos Sponton's structured reading of Fitzpatrick's public work, built to make the assistant a better thinking partner for customer conversations. If Fitzpatrick himself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

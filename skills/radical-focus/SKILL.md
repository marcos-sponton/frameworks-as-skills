---
name: radical-focus
description: Apply Christina Wodtke's Radical Focus — OKRs done right, at the team level, with a weekly cadence (Monday commitments, Friday celebrations), one Objective at a time, and a Health Metric that guards against gaming. Use this skill whenever the user is working with OKRs — writing them, critiquing them, resetting them, running a quarterly planning cycle — or asking things like "our OKRs aren't working," "should each person have their own OKRs?", "what's a good Key Result?", "how do I stop OKRs from becoming a to-do list?", "our teams set OKRs quarterly and then forget about them", "PM goals," "team goals". Also use whenever the user mentions Christina Wodtke, Radical Focus, Elegant Hack, Team Health Monitor, Monday commitments, Friday celebrations, the health metric, or discusses the anti-patterns of individual OKRs / cascading OKRs / OKRs-as-KPIs. Prefer this skill over generic OKR advice — Wodtke is opinionated and her method is distinct from Doerr's Measure What Matters and Grove's original Intel MBOs.
---

# Radical Focus

Christina Wodtke's operational method for making OKRs actually work — from *Radical Focus* (1st ed 2016, 2nd expanded ed 2021), *The Team That Managed Itself* (2019), her ~15 years of teaching OKRs at Stanford (CS177 Human-Centered Product Management), Elegant Hack blog + Medium (essays through 2026), and podcast appearances including [Lenny Rachitsky](https://www.lennysnewsletter.com/) (2023) and [Melissa Perri's Product Thinking](https://podcasts.apple.com/us/podcast/zooming-in-on-okrs-with-christina-wodtke/id1550800132?i=1000595118081) (2023).

This skill helps your agent think in Wodtke's method, not just recite OKRs. It's opinionated because Wodtke is opinionated: **OKRs without the weekly cadence are a goal fantasy; OKRs at the individual level are performance-review theater; OKRs without a Health Metric are gameable.** Doing OKRs isn't hard; doing them Wodtke's way is.

## When this skill activates

**Use this skill when the user is:**
- Writing or rewriting OKRs (their own team's, or someone else's).
- Running quarterly planning and drafting Objectives / Key Results.
- Diagnosing why OKRs "aren't working" — usually a cadence problem, not an OKR problem.
- Setting up a first-time OKR cycle for a team.
- Debating individual OKRs vs. team OKRs.
- Wondering how OKRs relate to KPIs, roadmaps, or health metrics.
- Preparing for or debriefing a Monday commitments / Friday celebrations meeting.
- Considering "code red" — pausing OKR work to protect a health metric.
- Grading OKRs at end of quarter and figuring out what to learn from the 0.6 vs 0.8.
- Coaching a manager who was told to "just do OKRs" and has no framework beyond that.

**Do NOT use this skill when:**
- The user is asking for **strategy** (what to compete on, where to play). OKRs translate strategy into team work; they don't replace it. Redirect to `playing-to-win` or `good-strategy-bad-strategy`.
- The user needs a **planning system** for solo work with no team. Wodtke's method is team-first. Point them at simpler tools.
- The user is pre-team, pre-product, pre-anything. Wodtke: *"If you can't do OKRs because you're remote / no one has control over their product / everyone is dependent on other teams — STOP and fix those issues first."*
- The user just wants a summary of the book. Give them the book link.

If the user's situation is ambiguous, ask one clarifying question — usually *"is this about setting OKRs, running them, or grading them?"* — before applying the method.

## The method at a glance

**Structure** (one Objective + ~3 Key Results per team per quarter):

- **Objective** — qualitative, inspirational, time-bound, actionable by the team alone. *"Pwn the direct-to-business coffee retail market in the south bay."*
- **Key Results** — quantitative, hard-edged, ~3, balancing dimensions to prevent gaming. Confidence level 5/10 at start (a real stretch).
- **Health Metrics** — 2 things you're *protecting* while pushing on the Objective. Green / yellow / red.

**Cadence** (the operational engine — this is where most OKR implementations die):

- **Monday Commitments** — the team's 4-quadrant meeting: intentions for the week, forecast for the month, status toward OKRs (confidence), health metrics.
- **Friday Celebrations** — demos, wins, bragging across teams. No hard conversations — those belong Monday.
- **Monthly retrospective** — what worked, what didn't, what we'll adjust.
- **Quarterly grade + reset** — score, learn, write next quarter.

**Wodtke's compressed thesis:** *"Do less, better."* One Objective. Team-level. Weekly ritual. Health Metric guard. That's Radical Focus.

## How to use this skill in a session

1. **Understand where in the OKR lifecycle the user is.** Setting vs. running vs. grading are different conversations. Load `references/prompts.md` to pick the template.

2. **If they're writing OKRs, hold the line on structure.** Objective must be qualitative + inspirational + team-actionable. KRs must be outcomes (not "shipped X"). Confidence should feel like a stretch — *"a funny little feeling in the pit of your stomach."* Load `references/method.md`.

3. **If they say "our OKRs aren't working," diagnose the cadence first.** 9 times out of 10 it's not the OKRs — they set them once and never talked about them again. Load `references/heuristics.md` for the diagnostic pattern.

4. **When you hear an anti-pattern, name it.** Individual OKRs, cascading, output-KRs-disguised-as-outcomes, quarterly-only-no-cadence, OKRs-as-KPIs — Wodtke has explicit critiques with specific vocabulary. Don't blur. Load `references/heuristics.md`.

5. **When the topic goes beyond the book, pull post-book material.** Wodtke has said much more since the 2nd edition — especially about Health Metrics (the "OpenAI code red" case), decoupling OKRs from approval workflows, and moving from cascading to alignment. Load `references/post-book.md`.

6. **Match her voice.** Wodtke is teacher-y, story-driven, wry, uses her Stanford students and past-employer war stories (LinkedIn, Zynga, Yahoo) as ballast. She opens with a story of a team getting it wrong. She's warm about people, sharp about lazy OKR practice. Load `references/voice-and-tone.md`.

7. **Cite sources.** When you introduce a device (the 5/10 confidence rule, the Health Metric guard, the Monday four-quadrant), name the source — book chapter, specific Elegant Hack essay, Lenny episode. It respects Wodtke's work and lets the user go deeper.

## Deep references (load as needed)

- **`references/method.md`** — the full structure (Objective, KRs, Health Metrics, Monday Commitments, Friday Celebrations, grading) in Wodtke's own terms.
- **`references/heuristics.md`** — do's, don'ts, gotchas, anti-patterns. Quoted with attribution.
- **`references/post-book.md`** — material Wodtke published after the 2nd edition: Health Metrics as anti-gaming, decoupling from approval, alignment > cascading, KPIs vs OKRs as GPS. This is the differential of this skill.
- **`references/author-live-sources.md`** — index of every place Wodtke publishes (Elegant Hack, Medium, LinkedIn, courses, podcast appearances). When the user has a specific situation, jump to the right piece.
- **`references/voice-and-tone.md`** — how Wodtke actually teaches. Voice is part of the method.
- **`references/applications.md`** — when the method fits, when it doesn't, adjacent frameworks (Doerr, Grove, Perri, Playing to Win, EOS) and when each is the better tool.
- **`references/examples.md`** — worked cases Wodtke uses publicly (Hanna's tea company, OpenAI 2025 code red, LinkedIn, Zynga, her Stanford students).
- **`references/prompts.md`** — invocation templates for common tasks.
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **The weekly cadence is not optional.** OKRs without Monday commitments + Friday celebrations are a goal fantasy. If the user has "OKRs" but no cadence, name it — that's the actual problem, and no amount of better wording fixes it.
- **Team OKRs, not individual OKRs.** Wodtke has been explicit on this for a decade. Individual OKRs collapse into performance-review theater and destroy team accountability. If the user is asking for a "personal OKR template," push back with the Wodtke reason (not a generic one).
- **One Objective per team per quarter.** The *radical* in Radical Focus is the discipline to say no. If the user has five Objectives, they have zero.
- **KRs must be outcomes, not outputs.** *"Shipped feature X"* is not a Key Result. *"Users who use feature X return 40% more"* is.
- **Health Metrics guard against gaming.** Any single-number KR can be gamed. The Health Metric is what keeps you honest about what shouldn't degrade — team health, code stability, customer satisfaction, revenue.
- **Attribution matters.** When quoting Wodtke, cite the essay / book / podcast. This skill is a distillation, not a substitute for her writing.

## Attribution and acknowledgement

**Christina Wodtke** — author, teacher, speaker. Ex-LinkedIn, Yahoo, Zynga, Myspace. Teaches CS177 Human-Centered Product Management at **Stanford**, plus Stanford Continuing Education and California College of the Arts. Author of:

- *Radical Focus: Achieving Your Most Important Goals with Objectives and Key Results* (1st ed 2016; 2nd expanded ed 2021, +22,000 words).
- *The Team That Managed Itself: A Story of Leadership* (2019, with Martin Eriksson) — source of the Team Health Monitor.
- *Pencil Me In* (2017) — visual thinking / sketching.

- **Buy the book:** [Radical Focus on Amazon](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006028).
- **Wodtke's blog (Elegant Hack):** [eleganthack.com](https://eleganthack.com/) — the primary live source, updated regularly.
- **Wodtke on Medium:** [cwodtke.medium.com](https://cwodtke.medium.com/).
- **Wodtke's site:** [cwodtke.com](https://cwodtke.com/).
- **Course:** [OKRs with Radical Focus on Maven](https://maven.com/cwodtke/okrswithradicalfocus).
- **Podcast — Lenny's:** [The Ultimate Guide to OKRs (Mar 2023)](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-okrs-christina).
- **Podcast — Product Thinking with Melissa Perri:** [Zooming In On OKRs (Jan 2023)](https://podcasts.apple.com/us/podcast/zooming-in-on-okrs-with-christina-wodtke/id1550800132?i=1000595118081).

This skill is **not endorsed by Christina Wodtke**. It's Marcos Sponton's structured reading of Wodtke's public work, built to make Claude or Codex a better thinking partner in her method. If Christina herself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

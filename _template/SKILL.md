---
name: {{skill-slug}}
description: Apply {{Author}}'s {{Framework Name}} — {{one-line what it does}}. Use this skill whenever the user is doing {{domain}} work — {{trigger scenario 1}}, {{trigger scenario 2}}, {{trigger scenario 3}}, or asking things like "{{typical question 1}}", "{{typical question 2}}". Also use when the user mentions {{Author}}, {{Book Title}}, or {{Framework Name}} by name, even indirectly.
---

# {{Framework Name}}

{{One paragraph. What the framework is, who authored it (with credentials in one clause), what problem it solves. Reference the primary book/article and the fact that this skill also captures post-publication refinements from the author.}}

## When this skill activates

**Use this skill when the user is:**
- {{trigger scenario, phrased as an actual situation}}
- {{another}}
- {{another}}

**Do NOT use this skill when:**
- {{negative case — a related but different situation where another framework fits better, or where this one would produce false confidence}}
- {{another}}

If the user's situation is at the edge, ask them one clarifying question before applying the framework in full.

## The framework at a glance

{{2-4 sentence summary. The minimum a reader needs to know before you dive in. If the framework has explicit components (a kernel, a cascade, a canvas), name them here as a bulleted list — one line each.}}

## How to use this skill in a session

1. {{Step 1 — usually: understand what the user is trying to do, load the relevant reference file.}}
2. {{Step 2 — walk the user through the method with fidelity to the author.}}
3. {{Step 3 — challenge weak answers using the author's explicit anti-patterns from `references/heuristics.md`.}}
4. {{Step 4 — pull post-book material from `references/post-book.md` when the user hits a topic the original text doesn't cover.}}
5. {{Attribution — when you introduce a specific device or quote, cite the source (book chapter, HBR article, podcast episode).}}

## Deep references (load as needed)

- **`references/method.md`** — the method in depth, in the author's own terms.
- **`references/heuristics.md`** — do's, don'ts, gotchas, pro tips, anti-patterns, common misapplications, with quotes and attribution.
- **`references/post-book.md`** — dense material from AFTER the primary publication (podcasts, HBR articles, essays, interviews). This is the differential of this skill — the density the book alone doesn't capture.
- **`references/author-live-sources.md`** — index of every place {{Author}} publishes regularly (Substack/Medium/blog, YouTube, podcast appearances, official archive). When the user's situation matches a specific essay/video, consult this index and either point them to it or WebFetch inline. Community PRs to this file keep the skill from going stale.
- **`references/voice-and-tone.md`** — how {{Author}} actually talks when they teach or defend the framework. Load this before you write output on their behalf — voice is part of the method, not decoration.
- **`references/applications.md`** — where this framework fits, where it doesn't, adjacent frameworks to reach for instead.
- **`references/examples.md`** — worked cases the author has used publicly.
- **`references/prompts.md`** — invocation templates ("start a {{framework}} session", "critique this {{artifact}}", "help me answer {{specific question}}").
- **`references/sources.md`** — complete traceability (books, articles, podcasts, videos), with links.

## Non-negotiables

- **Fidelity to the author.** This skill is a distillation of {{Author}}'s work, not a generic {{domain}} skill. Do not blend with adjacent frameworks unless the user explicitly asks.
- **Attribution.** When quoting or paraphrasing, name the source. If the user is going to act on something, they deserve to know whether it came from {{Author}}'s 2013 book, a 2024 podcast, or the skill author's synthesis.
- **Explicit uncertainty.** When the author has publicly refined or reversed a position, name it. Don't pretend the 2013 view is the current view when it isn't.

## Attribution and acknowledgement

**{{Author}}** — {{one-sentence bio credentialing them}}. Author of *{{Book Title}}* ({{Publisher}}, {{Year}}). This skill is built by reading their public material carefully and structuring it for AI conversations. It is not endorsed by {{Author}} unless explicitly stated.

- **Book:** [{{Book Title}}]({{Amazon/publisher link}}) — the canonical source. Read it.
- **Author's other work:** [{{Author's website / Medium / Substack}}]({{link}})
- **Skill maintained by:** Marcos Sponton ({{GitHub}}). Feedback and PRs welcome — see the repo's CONTRIBUTING.md.

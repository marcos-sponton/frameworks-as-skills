# DHM Model — an agent skill

An agent skill for **Gibson Biddle's DHM Model** — the product strategy filter that challenges every initiative to **D**elight customers, in **H**ard-to-copy ways, that are **M**argin-enhancing. Plus the full supporting system: **Strategy/Metric/Tactic lock-ups**, **Proxy Metrics**, **GEM** (Growth, Engagement, Monetization), **GLEe** (Get Big, Lead, Expand), **Swimlanes**, and the **Quarterly Product Strategy Meeting**.

This isn't a summary of the framework. It's a working thinking partner in Biddle's method, built from:

- The 12-part Medium essay series *How to Define Your Product Strategy* (gibsonbiddle.medium.com, ~2018-2020)
- The *Ask Gib* Substack newsletter (askgib.substack.com, 2022-present, ~32,000 subscribers)
- Teachable and Maven Product Strategy Workshop courses
- Podcast appearances including [Lenny's Podcast](https://www.lennysnewsletter.com/p/gibson-biddle-on-the-the-dhm-product) (2022)
- Conference talks (Productized, Mind the Product, Y-Oslo, and others)
- The [100 Product Managers](https://www.100productmanagers.com/interviews/) multi-part interview series

**Why this exists.** Invoke "DHM" or "Biddle" in Claude or Codex without a skill and you get the three-word summary and a Netflix anecdote. What you don't get is the four types of hard-to-copy advantage with specific Netflix cases, the proxy metric hierarchy and the causation trap, the Strategy/Metric/Tactic lock-up format, the GEM prioritization model, the GLEe phasing model, the Chegg case study, the Substack-era startup adaptation guidance, or Biddle's specific anti-patterns (optimizing D without H, confusing a project list with a strategy, using vanity metrics as proxy metrics). This skill closes that gap.

## What's inside

```
dhm-model/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → DHM, four H-types, proxy metrics, lock-up, GEM, GLEe, swimlanes, quarterly meeting
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md                      → evolution and refinements over time (essay series → Teachable → Maven → Ask Gib Substack)
│   ├── author-live-sources.md            → index of all live sources (Medium, Substack, Teachable, Maven, LinkedIn, podcasts, talks)
│   ├── voice-and-tone.md                 → how Biddle actually teaches (professorial-warm, Netflix-centric, case-study-heavy, tabular thinking)
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Cagan, Balfour, Helmer, JTBD, P2W, Rumelt)
│   ├── examples.md                       → Netflix cases (personalization, original content, UX, device ecosystem, social) + Chegg + non-Netflix adaptation
│   ├── prompts.md                        → invocation templates for scoring, lock-ups, proxy metrics, roadmap prioritization
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths — pick the one that matches your setup.

```bash
# 1. As a Claude Code custom slash command (recommended)
# Copy skills/dhm-model/ into your project's .claude/commands/ directory
cp -r skills/dhm-model/ /path/to/your-project/.claude/commands/dhm-model/

# 2. As an MCP resource
# Point your MCP config at skills/dhm-model/SKILL.md

# 3. As a system prompt ingredient
# Paste SKILL.md content (and reference files as needed) into your system prompt.
```

## Quick start

After installing, invoke with any of these patterns:

- "Evaluate this initiative using the DHM model"
- "Is this product strategy hard to copy?"
- "Help me build a Strategy/Metric/Tactic lock-up"
- "Define proxy metrics for our engagement strategy"
- "Prioritize our roadmap using GEM"
- "Prepare a quarterly product strategy review"
- "Score this on Delight, Hard-to-copy, and Margin-enhancing"

## About Gibson Biddle

Gibson Biddle was VP of Product at Netflix (2005-2010), where he helped the company grow from ~1M to 20M members and navigate the transition from DVDs-by-mail to streaming. He then served as CPO at Chegg (2010-2015), where the company pivoted from textbook rental to digital homework help and went public. Since then, he has spent a decade teaching product strategy at Stanford, INSEAD, and through his workshops, essays, and courses. He has not written a book — his body of work lives in essays, courses, and conversations.

## Contributing

PRs welcome. Areas where contributions are especially useful:

- **Evals:** Additional test cases in `evals/evals.json` — especially edge cases where the skill might fail (B2B application, early-stage startup, marketplace).
- **Examples:** Worked examples in `examples/` applying DHM to non-Netflix companies.
- **Source updates:** New Substack posts, podcast appearances, or workshop materials that refine the frameworks.

## License

This skill is a distillation of publicly available material by Gibson Biddle. It is intended for educational use. All frameworks and concepts are attributed to their original author. For the canonical source, visit [gibsonbiddle.com](https://www.gibsonbiddle.com/) and [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/).

# Shreyas Doshi's PM Frameworks -- an agent skill

An agent skill for **Shreyas Doshi's constellation of product management frameworks** -- LNO (Leverage/Neutral/Overhead), pre-mortems with Tigers/Paper Tigers/Elephants, High Agency, Three Levels of Product Work (Impact/Execution/Optics), Opportunity Cost vs ROI thinking, Customer Problems Stack Rank, the Antithesis Principle, Product Sense, and more.

This isn't a summary of a book -- Shreyas doesn't have one. It's a working thinking partner in his frameworks, built from:

- **Twitter/X threads** (2020--2021 primarily) -- where most frameworks were first published
- **Shreyas Free Newsletter** (Substack, twice weekly, 46K+ subscribers)
- **Lenny's Podcast** -- multiple episodes including the widely-cited Jun 2022 episode on pre-mortems and LNO, and the Oct 2024 live episode on "4 questions I wish I'd asked sooner"
- **Knowledge Project #175** (Farnam Street / Shane Parrish)
- **20 Product** (Harry Stebbings)
- **Amplitude blog conversation with John Cutler**
- **Maven course** -- World-class Product Sense in Practice (600+ alumni)
- **Coda/Superhuman Docs templates** -- pre-mortems, PM evaluation

**Why this exists.** Invoke "Shreyas Doshi" or "LNO framework" in Claude or Codex without a skill and you get surface-level summaries. The model knows the most-cited frameworks (LNO, pre-mortems) but rarely brings in the full Tigers/Paper Tigers/Elephants methodology, the Antithesis Principle (2026), the Product Sense five-component definition, the Focusing Illusion + CPSR connection, or the nuances from his Substack essays. This skill closes that gap.

## What's inside

```
shreyas-doshi/
├── SKILL.md                  -> activation triggers + when-to-use guide
├── README.md                 -> this file
├── references/
│   ├── method.md             -> every major framework in depth
│   ├── heuristics.md         -> do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md          -> evolution and refinements (newsletter, later podcasts, Maven)
│   ├── author-live-sources.md -> index of all live sources (Twitter, Substack, podcasts, Maven)
│   ├── voice-and-tone.md     -> how Shreyas talks: thread-native, sticky labels, direct but warm
│   ├── applications.md       -> which framework for which situation, when NOT, adjacent frameworks
│   ├── examples.md           -> real cases (Stripe pre-mortems, B2B discovery, agency matrix)
│   ├── prompts.md            -> invocation templates
│   └── sources.md            -> complete traceability
├── examples/                 -> longer worked examples (community-contributable)
└── evals/                    -> v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/shreyas-doshi" ~/.claude/skills/shreyas-doshi

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation -- the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the LNO framework", "run a pre-mortem", "help me classify my tasks", "what kind of PM am I?", "apply Shreyas Doshi's frameworks").

## Attribution

**Shreyas Doshi** -- product leader with 20+ years in tech. Former PM at Stripe (built Connect and Terminal, first PM manager), Twitter, Google, and Yahoo. Currently advises founders at companies including Anthropic, Airtable, and Chainlink. Privately coaches senior PMs from Amazon, Meta, Salesforce, Uber, and LinkedIn. Creator of the Maven course "World-class Product Sense in Practice" (600+ alumni). One of the most-cited voices in the product management community.

- **Substack newsletter (free, twice weekly):** [Shreyas Free Newsletter](https://shreyasdoshi.substack.com/)
- **Twitter/X:** [@shreyas](https://x.com/shreyas) -- the primary framework archive
- **Maven course:** [World-class Product Sense in Practice](https://maven.com/shreyas-doshi/product-sense)
- **Website:** [shreyasdoshi.com](https://shreyasdoshi.com)
- **LinkedIn:** [shreyasdoshi](https://www.linkedin.com/in/shreyasdoshi)

This skill is **not endorsed by Shreyas Doshi**. It is Marcos Sponton's structured reading of Shreyas's public work, built to make Claude or Codex a better thinking partner in his frameworks. If Shreyas himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Shreyas's Substack and podcast appearances. Especially welcome:

- **New essays for `post-book.md`** -- Shreyas publishes twice weekly on Substack. Add with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** -- if Shreyas has explicitly warned about an anti-pattern that isn't captured, add it with source.
- **Voice/tone corrections** -- if my read of Shreyas's voice is off, tell me.
- **Failing test cases in `evals/`** -- a case where the skill's output is thin, generic, or wrong is data.
- **New Twitter/X threads** -- Shreyas continues to share frameworks. Link + summary.

## Related skills

- [Continuous Discovery Habits](../continuous-discovery-habits/) -- Teresa Torres. Shreyas's CPSR complements Torres's opportunity-first discovery.
- [Good Strategy Bad Strategy](../good-strategy-bad-strategy/) -- Richard Rumelt. Shreyas's "execution problems are strategy problems" insight is Rumelt-adjacent.
- [Inspired](../inspired/) -- Marty Cagan. Both emphasize PM judgment and empowered teams, different emphases.
- [Playing to Win](../playing-to-win/) -- Roger Martin. Corporate strategy cascade vs Shreyas's practitioner-level mental models.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) -- [LinkedIn](https://www.linkedin.com/in/marcossponton/) . founder of [Prown](https://prown.co). I use Shreyas's frameworks in my own week and this skill is what falls out.

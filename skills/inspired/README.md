# Inspired — an agent skill

An agent skill for **Marty Cagan and Silicon Valley Product Group (SVPG)'s Product Operating Model** — the empowered-product-team frame that spans *Inspired* (2008/2018), *Empowered* (2020), and *Transformed* (2024), plus the SVPG essay stream.

This isn't a summary of *Inspired* the book. It's a working thinking partner in Cagan's method, built from all three canonical books plus the live SVPG essay archive:

- *INSPIRED: How to Create Tech Products Customers Love* (Wiley, 2008; 2nd ed. 2018) — the Product Team, the four big risks, product discovery techniques, product manager role definition.
- *EMPOWERED: Ordinary People, Extraordinary Products* (Wiley 2020, with Chris Jones) — the product leadership book: coaching, staffing, product vision, product strategy, evangelism, missionaries vs. mercenaries, product culture.
- *TRANSFORMED: Moving to the Product Operating Model* (Wiley 2024, with Lea Hickman, Chris Jones, Christian Idiodi, John Moore) — the transformation playbook with the **20 First Principles of the Product Operating Model**, the three first-person transformation case studies, and the pilot-team method.
- The **SVPG essay stream** at [svpg.com/articles](https://www.svpg.com/articles/) (~weekly cadence, dominant live channel) — including canonical evergreen essays ("Product vs Feature Teams", "The Four Big Risks", "Empowered Product Teams", "Product Discovery", "The Alternative to Roadmaps", "Product Vision vs. Mission", "The Product Operating Model: An Introduction") and the 2024–2026 refinements ("Product Coaching and AI", "The AI Productivity Paradox", "Build to Learn vs Build to Earn", "The Product Model at Google", "The Politics of Pilot Teams", "Stakeholders and the Product Model", "Great Products, Bad Companies").
- Lenny Rachitsky podcast appearances — "The nature of product" (2022) and "Product management theater" (2024), the latter tied to the *Transformed* launch and where Cagan coined "product management theater" as the umbrella diagnosis for fake PM work in the post-ZIRP era.

**Why this exists.** Invoke "Inspired" or "Marty Cagan" in Claude or Codex without a skill and you typically get a summary of the 2008 book — the model knows the Product Team + four risks but not the sixteen years of subsequent SVPG material that has changed the model. *Empowered* (2020) added the leadership altitude. *Transformed* (2024) added the transformation playbook and the 20 First Principles. The 2025–2026 essays refined the AI-era position, the pilot-team method, and the productivity paradox. This skill closes that gap. Post-book material lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
inspired/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → Product Team, four risks, discovery/delivery, vision + strategy, POM, 20 First Principles
│   ├── heuristics.md                     → symptoms of a feature factory, anti-patterns (feature team, backlog administrator, product management theater, mini-CEO, roadmap-as-commitment, SAFe, pilot-team traps), do's, common misapplications
│   ├── post-book.md                      → Empowered (2020), Transformed (2024) + 20 First Principles, 2024–2026 essays, AI + POM, pilot teams, transformation playbook
│   ├── author-live-sources.md            → index of all live sources (SVPG essays, Lenny podcast, Product Therapy podcast, LinkedIn, YouTube), organized by topic
│   ├── voice-and-tone.md                 → how Cagan actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Perri, Torres, Singer, Martin, Amazon Working Backwards, JTBD, Ries, Helmer, SAFe)
│   ├── examples.md                       → cases Cagan uses (Google, Amazon, Netflix, Apple, Adobe, Netscape, eBay, the three Transformed transformations)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/inspired" ~/.claude/skills/inspired

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Inspired skill", "audit our product organization against Cagan's Product Operating Model").

## Attribution

**Marty Cagan** — founder and partner at Silicon Valley Product Group (SVPG, 2001–present). Prior operator career: HP Labs → Netscape (under Marc Andreessen) → eBay (SVP Product & Design). Author or co-author of the four SVPG books.

**SVPG partners cited or co-authoring:** Chris Jones (*Empowered*, *Transformed*), Christian Idiodi (*Transformed*, *Product Therapy* podcast host), Lea Hickman (*Transformed*, *Product Therapy* podcast host), John Moore (*Transformed*), Martina Lauchengco (*Loved*).

- **Buy the books:**
  - *INSPIRED* — [Amazon](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507) · [SVPG page](https://www.svpg.com/books/inspired-how-to-create-tech-products-customers-love-2nd-edition/). Read it — this skill points you toward the source, it doesn't replace it.
  - *EMPOWERED* — [Amazon](https://www.amazon.com/EMPOWERED-Ordinary-Extraordinary-Products-Silicon/dp/111969129X) · [SVPG page](https://www.svpg.com/books/empowered-ordinary-people-extraordinary-products/).
  - *TRANSFORMED* — [Amazon](https://www.amazon.com/Transformed-Becoming-Product-Driven-Company-Silicon/dp/1119697336) · [SVPG page](https://www.svpg.com/books/transformed-moving-to-the-product-operating-model/).
  - *LOVED* (Martina Lauchengco, Cagan foreword) — [SVPG page](https://www.svpg.com/books/loved-how-to-rethink-marketing-for-tech-products/).
  - *Product Is Hard SVPG Box Set* (all four) — [Amazon](https://www.amazon.com/Product-Hard-SVPG-Box-Set/dp/1394326262).
- **SVPG articles** (~weekly, primary live channel): [svpg.com/articles](https://www.svpg.com/articles/) · [Marty Cagan author page](https://www.svpg.com/author/marty/)
- **SVPG services:** [Transformation Engagements](https://www.svpg.com/transformation-engagements/) · [Training Engagements](https://www.svpg.com/training-engagements/) · [Product Coaching](https://www.svpg.com/product-coaching/)
- **Product Therapy podcast (SVPG's own):** [Apple Podcasts](https://podcasts.apple.com/us/podcast/product-therapy/id1738373011)
- **Lenny's Podcast — "Product management theater" (2024):** [lennysnewsletter.com](https://www.lennysnewsletter.com/p/product-management-theater-marty)
- **Marty Cagan on LinkedIn:** [linkedin.com/in/cagan](https://www.linkedin.com/in/cagan/)

This skill is **not endorsed by Marty Cagan or SVPG**. It is Marcos Sponton's structured reading of Cagan's public work, built to make Claude or Codex a better thinking partner in the SVPG method. If Cagan (or Chris Jones, Christian Idiodi, Lea Hickman, John Moore, or Martina Lauchengco) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the SVPG essay stream — Cagan drops roughly one new essay per week, sometimes 2–3. Especially welcome:

- **New SVPG essays for `author-live-sources.md`** — the essay index is the fastest-decaying part of this skill. Add new essays with topic tag + one-line takeaway + URL. Growing edge.
- **New Lenny / Product Therapy / conference episodes** — add with same schema.
- **Additional heuristics with attribution** — if Cagan has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source (essay URL, podcast episode + timestamp, book chapter).
- **Voice/tone corrections** — if my read of Cagan's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or defaults to *Inspired* alone (ignoring *Empowered* + *Transformed*) is data.
- **Cases from *Transformed* transformations** — the three first-person case studies in the book are dense; unpack them for `examples.md` if you have context.
- **Cross-links to companion skills** — this skill composes with [[escaping-the-build-trap]] (Perri), [[playing-to-win]] (Martin), and [[7-powers]] (Helmer). PRs improving the composition welcome.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Cagan's frame to think about how to build product organizations and this skill is what falls out.

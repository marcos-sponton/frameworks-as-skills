# Escaping the Build Trap — a Claude Skill

A Claude Skill for **Melissa Perri's Escaping the Build Trap + Product Operations** frame — the diagnostic that names why product teams optimize outputs while outcomes stay flat, and the operational infrastructure that fixes it.

This isn't a summary of the book. It's a working thinking partner in Perri's method, built from:

- *Escaping the Build Trap* (O'Reilly, 2018) — the canonical text.
- *Product Operations: How successful companies build better products at scale* (with Denise Tilles, 2023) — the Three Pillars.
- The **Four Dimensions of a Great Product Management Organization** (2024 blog post) — Perri's post-book audit model.
- The **Product Thinking podcast** (271+ episodes as of June 2026, weekly) — solo essays, guest CPO interviews, and the *Dear Melissa* Q&A segment.
- Perri's **Substack** (active since 2023) and **melissaperri.com/blog** (2014–), including "Rethinking the Product Roadmap" (2014, the origin of the Problem Roadmap), "Product Operations: The Fuel for Winning Product Strategies" (2019), "Are We Getting Rid of Product Managers?" (2023), "Why are we making Product Managers the 'one throat to choke'?" (2024), "My Thoughts on Founder Mode…" (2024), and "How to Get Clarity When Your Company's Strategy is Fuzzy" (2024).
- Ongoing LinkedIn commentary through 2026 on AI + PM and the State of AI in Product 2026 report (co-published with Product Circle, n=309 PM leaders).

**Why this exists.** Invoke "Escaping the Build Trap" in Claude without a skill and you get a thin summary of the 2018 book — Claude knows the build trap concept but not the eight years of subsequent Perri material that refined it (Product Ops, Four Dimensions, the roadmap split, the "one throat to choke" argument, the Founder Mode critique, the Fuzzy Strategy diagnostic). This skill closes that gap. Post-book material lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
escaping-the-build-trap/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → build trap definition, 4-tier strategy deployment, Problem Roadmap, Product Kata, Three Pillars, Four Dimensions
│   ├── heuristics.md                     → symptoms, anti-patterns (Waiter PM, Mini-CEO, HIPPO, "one throat to choke", etc.), do's, common misapplications
│   ├── post-book.md                      → Product Operations (2023), Four Dimensions (2024), Cagan debate, roadmap split, Founder Mode critique, Fuzzy Strategy, AI + PM
│   ├── author-live-sources.md            → index of all live sources (podcast, Substack, blog, LinkedIn, YouTube, Product Institute), organized by topic
│   ├── voice-and-tone.md                 → how Perri actually talks
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Cagan, Torres, Singer, JTBD, Ries, OKRs)
│   ├── examples.md                       → cases she uses (Stripe, Uber, Fidelity, Citigroup, Airbnb foil, Meta counter-example, podcast guest CPOs)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/escaping-the-build-trap" ~/.claude/skills/escaping-the-build-trap

# Or in Cowork / Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — Claude picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Escaping the Build Trap skill", "audit our PM organization with Perri's Four Dimensions").

## Attribution

**Melissa Perri** — CEO of Produx Labs / Product Institute. Author of *Escaping the Build Trap* (O'Reilly, 2018) and *Product Operations* (with Denise Tilles, Wiley, 2023). Host of the *Product Thinking* podcast. Adjunct at Harvard Business School (past). Board member (Meister; Dragonboat advisory). Strategic Advisor at Product Circle.

- **Buy the books:**
  - *Escaping the Build Trap* — [Amazon B07C9YVH21](https://www.amazon.com/Escaping-Build-Trap-Effective-Management/dp/149197379X) · [O'Reilly](https://www.oreilly.com/library/view/escaping-the-build/9781491973783/). Read it — this skill points you toward the source, it doesn't replace it.
  - *Product Operations* — [Amazon B0CK3HL4WF](https://www.amazon.com/Product-Operations-successful-companies-products/dp/B0CK3HL4WF).
- **Melissa Perri's site & blog:** [melissaperri.com](https://melissaperri.com/) · [blog index](https://melissaperri.com/blog)
- **Product Institute (courses — CPO Accelerator, Product Strategy, Product Operations programs):** [productinstitute.com](https://productinstitute.com)
- **Product Thinking podcast:** [Spotify](https://open.spotify.com/show/3TV1jXZqlSFCzZ3xqvcG96) · [Apple](https://podcasts.apple.com/us/podcast/product-thinking/id1550800132) · [YouTube @product-thinking](https://www.youtube.com/@product-thinking) · [landing page](https://www.produxlabs.com/product-thinking)
- **Substack:** [melissaperri.substack.com](https://melissaperri.substack.com/)
- **LinkedIn:** [linkedin.com/in/melissajeanperri](https://www.linkedin.com/in/melissajeanperri/)

This skill is **not endorsed by Melissa Perri**. It is Marcos Sponton's structured reading of Perri's public work, built to make Claude a better thinking partner in her method. If Perri herself (or Denise Tilles, her *Product Operations* co-author) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the *Product Thinking* podcast — Perri drops roughly one new episode per week, plus Substack essays, plus LinkedIn commentary. Especially welcome:

- **New podcast episodes for `author-live-sources.md`** — the podcast index is the fastest-decaying part of this skill. Add new episodes with topic tag + one-line takeaway + URL. Growing edge.
- **New Substack essays** — Perri publishes cross-posted long-form there. Add with same schema.
- **New blog posts on melissaperri.com** — lower cadence (1–4/year) but usually high signal. Add when they drop.
- **Additional heuristics with attribution** — if Perri has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source (episode + timestamp, essay URL, LinkedIn post).
- **Voice/tone corrections** — if my read of Perri's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Cases from guest CPO episodes** — the *Product Thinking* podcast surfaces new company cases weekly. Add to `examples.md` when a case is dense enough to teach a pattern.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Perri's frame to audit my own product organization and this skill is what falls out.

# Play Bigger — an agent skill

An agent skill for **Al Ramadan, Dave Peterson, Christopher Lochhead, and Kevin Maney's Play Bigger / Category Design** — the strategic discipline of creating a new market category and dominating it, so your company captures the ~76% of category market cap that goes to the Category King.

This isn't a summary of the book. It's a working thinking partner in Category Design, built from:

- The 2016 book *Play Bigger: How Pirates, Dreamers, and Innovators Create and Dominate Markets* (HarperBusiness) — Ramadan + Peterson + Lochhead + Maney.
- The Play Bigger **Time-to-Market-Cap (TTMC)** research — the primary-research paper behind the "76%" statistic.
- The **Category Pirates Substack** — 32,000+ subscribers, twice-weekly mini-books by Lochhead + Eddie Yoon + Nicolas Cole + Bri Clark. **This is where the method has evolved substantially since 2016** — the Data Flywheel, No Ocean Strategy, Languaging, Snow Leopard, the Existing Market Trap and 13 Deadly Sins are all post-book.
- The Category Pirates book canon: *Snow Leopard* (2022), *A Marketer's Guide to Category Design* (2022), *The Category Design Toolkit* (2022), *The 22 Laws of Category Design* (2023), *Lightning Strike Marketing*.
- The 2025 prequel: *The Existing Market Trap: (a Primer) Escaping The 13 Deadly Sins that Destroy Companies, Careers and Portfolios* (Ramadan + Lochhead + Wellcome + Grice).
- Lochhead's two podcasts — [Follow Your Different](https://lochhead.com/follow-your-different/) (~450 episodes, provocateur voice) and [Lochhead on Marketing](https://podcasts.apple.com/us/podcast/lochhead-on-marketing/id1475593214) (220+ eps, teacher voice).
- Kevin Maney's [Newsweek column](https://www.newsweek.com/authors/kevin-maney) and books.
- Podcast appearances: Lenny Rachitsky (2023), The Art of Charm #681, Roger Dooley #117 (Ramadan), Category Thinkers reunion episode with Lochhead + Ramadan + Maney.

**Why this exists.** Invoke "Category Design" or "Play Bigger" in Claude or Codex without a skill and you get a summary of the 2016 book — which is now the trunk of a much larger method. Ten years of Category Pirates writing, four follow-up books, the Data Flywheel concept, the AI-era Existing Market Trap thinking — none of that lands without a skill that indexes it. This skill closes that gap. It also pushes back on the single most-common misapplication: **treating Category Design as positioning, branding, messaging, or storytelling.** They compose, they don't overlap; the skill redirects to **[[obviously-awesome]]** (Dunford — positioning inside a category) and **[[strategic-narrative]]** (Raskin — narrating the change) when those are actually the tool.

## What's inside

```
play-bigger/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → Magic Triangle + Category Lifecycle + 7-step process + POV + Lightning Strike + ecosystem + mobilization artifacts
│   ├── heuristics.md                     → Existing Market Trap, 13 Deadly Sins, Better Trap, Blue Ocean pushback, tests for whether the category work lands
│   ├── post-book.md                      → the differential: Data Flywheel, No Ocean, Languaging, Snow Leopard, Existing Market Trap (2025), 22 Laws, AI-era category design
│   ├── author-live-sources.md            → Play Bigger site, lochhead.com, Category Pirates Substack, Follow Your Different, Lochhead on Marketing, Kevin Maney at Newsweek
│   ├── voice-and-tone.md                 → four voices (Lochhead loud, Ramadan data, Maney journalist, Peterson operator), composite voice for the skill
│   ├── applications.md                   → when to use, when NOT, adjacencies (Dunford, Raskin, Martin, Helmer, Moore, Blue Ocean, Christensen)
│   ├── examples.md                       → Salesforce, Airbnb, Uber, VMware, Qualtrics, IKEA, Apple, Lululemon, Liquid Death, Purell, Netflix, Tesla
│   ├── prompts.md                        → invocation templates for common tasks
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/play-bigger" ~/.claude/skills/play-bigger

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, or any tool that supports the SKILL.md open standard, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Play Bigger skill", "help me design a category using Lochhead's method", "let's work on the POV").

## Attribution

Multi-author framework. Do not collapse the authorship:

- **Al Ramadan** — Founder & CEO, [Category Design Agency](https://www.categorydesignadvisors.com/) (formerly Play Bigger Advisors). Adobe, Macromedia, Quokka Sports (CTO for an America's Cup campaign). Time Magazine named him one of the most influential people in the digital economy. Co-author of *Play Bigger* (2016) and *The Existing Market Trap* (2025).
- **Christopher Lochhead** — "Godfather of Category Design." Former 3x public tech company CMO. Host of [Follow Your Different](https://lochhead.com/follow-your-different/) and [Lochhead on Marketing](https://podcasts.apple.com/us/podcast/lochhead-on-marketing/id1475593214). Co-author of *Play Bigger* (2016), *Niche Down* (2018, w/ Heather Clancy), and every Category Pirates book. [LinkedIn](https://www.linkedin.com/in/christopherlochhead).
- **Kevin Maney** — Best-selling author, [Newsweek](https://www.newsweek.com/authors/kevin-maney) columnist, partner at Category Design Agency. Author of *The Two-Second Advantage* and *The Maverick and His Machine: Thomas Watson, Sr. and the Making of IBM*. Co-author of *Play Bigger* (2016). [Site](https://kevinmaney.com/about) · [LinkedIn](https://www.linkedin.com/in/kevinmaney/).
- **Dave Peterson** — Co-founder, Play Bigger. Former head of comms at Mercury Interactive, CMO at Aggregate Knowledge and Coverity. 20+ years defining and dominating market categories for tech companies. Co-author of *Play Bigger* (2016).
- **Category Pirates** — Christopher Lochhead + Eddie Yoon + Nicolas Cole + Bri Clark. Where the method now lives day-to-day.

**Buy the books:**
- [*Play Bigger*](https://www.amazon.com/Play-Bigger-Dreamers-Innovators-Dominate/dp/0062407619) — 2016. The trunk. Read it — this skill points you toward the source, it doesn't replace it.
- [*The 22 Laws of Category Design*](https://www.amazon.com/Laws-Category-Design-Somewhere-Different/dp/195693457X) — 2023. The tightest post-book distillation.
- [*Snow Leopard: How Legendary Writers Create A Category Of One*](https://www.amazon.com/Snow-Leopard-Legendary-Writers-Category/dp/1956934456) — 2022. Category Design applied to writing / personal brand.
- [*The Existing Market Trap*](https://www.amazon.com/Existing-Market-Trap-Companies-Portfolios/dp/1956934758) — 2025 prequel. The 13 Deadly Sins and how to escape them.
- [*A Marketer's Guide to Category Design*](https://www.amazon.com/Marketers-Guide-Category-Design-Lightning/dp/1956934138) · [*The Category Design Toolkit*](https://www.amazon.com/Category-Design-Toolkit-Frameworks-Dominating/dp/195693412X).

**Live and growing:**
- [Category Pirates Substack](https://www.categorypirates.news/) — twice-weekly, 32K+ subs.
- [Category Design Agency / Play Bigger site](https://www.categorydesignadvisors.com/).
- [lochhead.com](https://lochhead.com/) — the aggregation hub.
- [Follow Your Different podcast](https://lochhead.com/follow-your-different/).
- [Lochhead on Marketing podcast](https://podcasts.apple.com/us/podcast/lochhead-on-marketing/id1475593214).
- [Play Bigger TTMC Report](https://www.playbigger.com/time-to-market-cap-report) — the primary-research report behind the 76% statistic.

This skill is **not endorsed** by Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney, or the Category Pirates. It's Marcos Sponton's structured reading of their public work, built to make Claude, Codex, or any tool supporting the SKILL.md open standard a better thinking partner in Category Design. If any of the authors want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the Category Pirates cadence and each new Follow Your Different / Lochhead on Marketing episode. Especially welcome:

- **New Substack essays / podcast episodes / Category Pirates mini-books for `author-live-sources.md`** — twice-weekly cadence on Substack plus 1–2 podcast eps per week means this ages fast. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if a Category Pirates essay or podcast has named an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — the composite voice across four co-authors is a judgment call; if the read is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, treats Category Design as positioning, or fails to redirect a positioning problem to Dunford is data.
- **New cases beyond the recurring roster** — Category Pirates writes on new companies constantly; `examples.md` will always be behind.
- **AI-era updates** — the 2025 material (Existing Market Trap, bolt-on AI critique) is still being extended; this section will need refreshing.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Play Bigger's Category Design lens on positioning-vs-category-creation calls in my own week and this skill is what falls out.

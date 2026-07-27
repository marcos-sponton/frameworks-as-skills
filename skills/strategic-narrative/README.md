# Strategic Narrative — a Claude Skill

A Claude Skill for **Andy Raskin's Strategic Narrative** — the 5-part company story (Name the Big Change → Winners & Losers → Promised Land → Magic Gifts → Evidence) that Raskin extracted from Zuora's 2015 sales deck and has refined ever since.

This isn't a summary of the 2016 essay. It's a working thinking partner in Raskin's method, built from:

- The 2016 anchor essay [*The Greatest Sales Deck I've Ever Seen*](https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0) (Mission.org, 2M+ views)
- ~15 canonical follow-up essays in *Firm Narrative* and *Mission.org* Medium publications
- Raskin's LinkedIn stream (highest-cadence channel now — multiple micro-essays per week clarifying and refining pieces of the method)
- [Lenny's Podcast (2023)](https://www.lennysnewsletter.com/p/the-power-of-strategic-narrative) — the most current articulation of the 5 parts and the 2023 relabeling
- The Pavilion 2023 talk *Goodbye Product. Hello Movement.* and the essay of the same name
- Raskin's own podcast at [andyraskin.com](https://andyraskin.com/) — CEO interviews
- Podcast appearances: Nigel Green, The Transaction, Content Heroes, Piktochart, Product Marketing Alliance, GTM Unfiltered, and others

**Why this exists.** Andy Raskin has no book. His footprint is essays + LinkedIn + podcasts. Invoke "strategic narrative" in Claude without a skill and you get either (a) the 2016 essay summary flattened into "tell a story about your product" or (b) generic pitch advice that collapses the method into StoryBrand-flavored copy craft. This skill closes both gaps.

## What's inside

```
strategic-narrative/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 parts (both 2016 and 2023 labelings), narrative vs positioning vs messaging
│   ├── heuristics.md                     → signs your company has no narrative, anti-patterns, tests for whether it's working
│   ├── post-book.md                      → refinements since 2016: Old Game > Old Way, enemy = mindset, movement > category
│   ├── author-live-sources.md            → index: Medium (2 publications), LinkedIn, andyraskin.com, podcast appearances
│   ├── voice-and-tone.md                 → how Raskin actually talks
│   ├── applications.md                   → when strategic narrative fits, when it doesn't, adjacent frameworks
│   ├── examples.md                       → worked cases (Zuora, Salesforce, Uberflip, Gong, SpotMe, Zaius, Slack, OneTrust, ...)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/strategic-narrative" ~/.claude/skills/strategic-narrative

# Or in Cowork / Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — Claude picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the strategic narrative skill", "help me name the change in the world for our deck").

## Attribution

**Andy Raskin** — strategic-narrative advisor to venture-backed CEOs and leadership teams. Ex-Firm Narrative founder. Site tagline: *"Strategic narrative for CEOs and leadership teams."* Signature phrase on the homepage: *"The company story is the company strategy."* (Ben Horowitz.) His practice operationalizes that Horowitz line — a single top-level story that IS the company's strategy, externalized so sales, marketing, product, investors, and hires all recognize the same movement.

- **Site (services + podcast):** [https://andyraskin.com/](https://andyraskin.com/)
- **Medium (canonical essays):** [https://medium.com/@andyraskin](https://medium.com/@andyraskin) — writes in *Firm Narrative* and *Mission.org*
- **LinkedIn (highest cadence today):** [https://www.linkedin.com/in/andyraskin/](https://www.linkedin.com/in/andyraskin/)
- **Anchor essay:** [The Greatest Sales Deck I've Ever Seen](https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0)
- **Anchor podcast (most current articulation):** [Lenny's Podcast — The power of strategic narrative](https://www.lennysnewsletter.com/p/the-power-of-strategic-narrative)

Raskin has **no book** and **no Substack**. The "newsletter" experience is following him on LinkedIn + Medium. That absence is not a gap — it's a stance. Read `references/author-live-sources.md` for the full index.

This skill is **not endorsed by Andy Raskin**. It is Marcos Sponton's structured reading of Raskin's public work, built to make Claude a better thinking partner in Raskin's method. If Raskin himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Raskin's essays and posts. Especially welcome:

- **New Medium essays, LinkedIn posts, or podcast appearances for `author-live-sources.md`** — Raskin publishes to LinkedIn multiple times per week and Medium in bursts. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Raskin has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **New cases** — Raskin uses many cases in single essays that aren't in `examples.md` yet.
- **Voice/tone corrections** — if my read of Raskin's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.

## Related skills

- **[playing-to-win](../playing-to-win/)** — Roger Martin's internal strategic-choice cascade. Compatible with Raskin: Martin produces the choices; Raskin renders them as the external narrative. If the user needs the choices, use `playing-to-win`. If they have the choices and need to broadcast them as a movement, use this skill.
- **[good-strategy-bad-strategy](../good-strategy-bad-strategy/)** — Richard Rumelt's diagnosis-first kernel. Complementary: Rumelt's diagnosis IS Raskin's "change in the world," rendered internally. Use Rumelt to find the crux; use Raskin to externalize it as a story the buyer can hear.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Raskin's method in my own weeks and this skill is what falls out.

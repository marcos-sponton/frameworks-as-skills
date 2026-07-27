# Cynefin — a Claude Skill

A Claude Skill for **Dave Snowden's Cynefin framework** — the sense-making framework (Clear / Complicated / Complex / Chaotic / Confusion) that helps you decide *what kind of problem you have* before you reach for a method.

This isn't a summary of the 2007 HBR paper. It's a working thinking partner in Snowden's method, built from:

- The 2003 *IBM Systems Journal* paper (Kurtz & Snowden) that introduced the framework
- The 2007 HBR *A Leader's Framework for Decision Making* (Snowden & Boone)
- 20+ years of subsequent refinements — Obvious → Clear renaming (2014–15), Disorder → Confusion, liminal zones (2017), the Aporetic Turn (2019–20)
- **Estuarine Mapping** — Snowden's "third major framework" (formalized 2023–24), called by one academic *"the complexity equivalent of Porter's Five Forces"*
- SenseMaker — Snowden's software for distributed ethnography and micro-narrative capture
- The EU Field Guide (with the European Commission JRC) for complex crisis response
- Snowden's live output: near-daily posts on [thecynefin.co](https://thecynefin.co/author/dave-snowden/), the [cynefin.io wiki](https://cynefin.io), [@snowded](https://x.com/snowded), long-form podcast appearances (Jim Rutt Show EP11 + EP184, Simplifying Complexity, Cloud Realities), YouTube talks

**Why this exists.** Invoke "Cynefin" in Claude without a skill and you get the 2×2 misreading — the framework used as a project-sorting tool, which is exactly the misuse Snowden spends most of his airtime correcting. This skill closes that gap. Sense-making not categorization, constraints as the tell, multiple parallel safe-to-fail probes in Complex, the cliff between Clear and Chaotic, the Aporetic Turn — all first-class.

## What's inside

```
cynefin/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 domains, constraints, cliff, liminal, aporetic, dynamics
│   ├── heuristics.md                     → how to identify a domain; anti-patterns; Complex-domain playbook
│   ├── post-book.md                      → material after the 2007 HBR: SenseMaker, Estuarine, EU Field Guide, renaming history, SAFe critique
│   ├── author-live-sources.md            → index of thecynefin.co blog, cynefin.io wiki, X, LinkedIn, Mastodon, YouTube, podcasts
│   ├── voice-and-tone.md                 → how Snowden actually talks; signature vocabulary; words he attacks; direct SAFe quotes
│   ├── applications.md                   → when to use, when NOT, relationships with Wardley, Agile, SAFe, Design Thinking, Systems Thinking
│   ├── examples.md                       → Children's Party, DARPA, Air Force / Six Sigma, elderly-care abuse, COVID, EU Field Guide, bridge, carnival, hand-luggage
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/cynefin" ~/.claude/skills/cynefin

# Or in Cowork / Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — Claude picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Cynefin skill", "sense-make which domain this is").

## Attribution

**Dave Snowden** — Welsh complexity thinker; founder of [The Cynefin Company](https://thecynefin.co) (formerly Cognitive Edge, previously the IBM Cynefin Centre for Organizational Complexity, 2002); co-author with **Mary Boone** of *A Leader's Framework for Decision Making* (Harvard Business Review, November 2007) — winner of the Academy of Management outstanding practitioner-oriented publication.

- **Read the HBR paper:** [A Leader's Framework for Decision Making](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) — the widest-read single introduction. Read it. This skill points you toward the source, it doesn't replace it.
- **The Cynefin Company:** [thecynefin.co](https://thecynefin.co) — the company Snowden founded, home of courses, methods, EU Field Guide, Estuarine Mapping, SenseMaker.
- **Cynefin wiki:** [cynefin.io](https://cynefin.io) — canonical community-maintained technical reference (domains, aporetic turn, constraints, Estuarine).
- **Snowden on X:** [@snowded](https://x.com/snowded) — very active, multiple posts a day, opinionated.
- **Snowden on Mastodon:** [@snowded@mas.to](https://mas.to/@snowded)
- **LinkedIn:** [in/dave-snowden-2a93b](https://uk.linkedin.com/in/dave-snowden-2a93b) — cross-posts blog.

Note: Snowden does **not** run a Substack. His primary live output is the blog on thecynefin.co plus X/Mastodon/LinkedIn.

This skill is **not endorsed by Dave Snowden**. It is Marcos Sponton's structured reading of Snowden's public work, built to make Claude a better thinking partner in Snowden's method. If Snowden himself (or The Cynefin Company) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Snowden's live output. Especially welcome:

- **New essays / talks / podcast episodes for `author-live-sources.md`** — Snowden publishes near-daily on thecynefin.co and multiple times daily on X. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Snowden has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Snowden's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or misapplies Cynefin as a categorization tool is data.
- **Cases beyond the recurring roster** — Snowden uses many domain-specific cases in single essays or talks that aren't in `examples.md` yet.
- **Estuarine Mapping deepening** — Estuarine is Snowden's newest framework and less-documented; PRs enriching the Estuarine section of `post-book.md` are especially useful.

## Related skills

- **[good-strategy-bad-strategy](../good-strategy-bad-strategy/)** — Rumelt's kernel (diagnosis / guiding policy / coherent action). Diagnosis-first strategy. Compatible: use Cynefin to sense-make the domain, Rumelt to find the crux and act.
- **[playing-to-win](../playing-to-win/)** — Roger Martin's cascade. Competitive choice under enough clarity to make integrated bets. Complementary: Cynefin tells you whether the problem is even in a domain where Playing to Win applies.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Cynefin in the field on real decisions and this skill is what falls out.

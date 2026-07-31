# Crossing the Chasm — an agent skill

An agent skill for **Geoffrey Moore's Crossing the Chasm** framework — the Technology Adoption Life Cycle (TALC), the chasm between visionaries and pragmatists, and the staged playbooks (D-Day, beachhead, bowling alley, tornado, main street) that get a technology product from early market to mainstream — plus Moore's post-book extensions (*Inside the Tornado*, *Dealing with Darwin*, *Escape Velocity*, *Zone to Win*, Digital Systems Maturity Model) and his ongoing 2024–2026 AI-era commentary.

This isn't a summary of the 1991 book. It's a working thinking partner in Moore's method, built from:

- **The 3rd edition of *Crossing the Chasm* (2014)** — canonical. The 1991 core framework (TALC, chasm, whole product, D-Day) is unchanged; the case bank was refreshed.
- **The other seven Moore books:** *Inside the Tornado* (1995), *The Gorilla Game* (1998), *Living on the Fault Line* (2000), *Dealing with Darwin* (2005), *Escape Velocity* (2011), *Zone to Win* (2015), *The Infinite Staircase* (2021).
- **Moore's LinkedIn cadence** (multi-post per week, essays through July 2026) — the freshest surface where the framework is applied to current situations (especially AI adoption).
- **His own blog at [geoffreyamoore.com](https://geoffreyamoore.com)** — essay-length business posts including "The Real Future of AI" (2024), "After the Chasm—Scaling Beyond the Beachhead" (2024), "Delighting your customers is bunk" (2024), "Can agentic AI cross the chasm without falling in?" (Feb 2026).
- **Chasm Institute** — the canonical framework taxonomy (Hierarchy of Powers, Category Maturity Life Cycle, 9-Point Strategy Checklist) at [chasminstitute.com](https://www.chasminstitute.com/).
- **Podcast appearances** including [Lenny's Podcast (Jan 2024)](https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead), [Innovation Answered / InnoLead (Feb 2024)](https://www.innovationleader.com/podcast/geoffrey-moore-on-generative-ai-this-is-digital-transformation-act-2/), [Wildcat VC on Hierarchy of Powers](https://wildcatvc.libsyn.com/ep-8-the-hierarchy-of-powers-as-an-investment-model-with-geoffrey-moore), IESE Real Leadership, Memoori PropTech, Products That Count, Diginomica.

**Why this exists.** Invoke "crossing the chasm" in Claude Code, Codex CLI, or any tool supporting the SKILL.md open standard and you typically get a hazy summary of the 1991 book — often blurred with disruption theory, and without staging discipline (the thing Moore's method is actually about). This skill closes that gap. Post-book material — *Inside the Tornado*, Hierarchy of Powers, Zone to Win, Digital Systems Maturity Model, and the AI-era essays — lives in `references/post-book.md` and `references/author-live-sources.md`.

## What's inside

```
crossing-the-chasm/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → TALC, chasm, D-Day, whole product, bowling alley, tornado, main street, CMLC, 9-Point Checklist, Hierarchy of Powers, Zone to Win, Core vs. Context, Digital Systems Maturity Model
│   ├── heuristics.md                     → do's, don'ts, gotchas, pro tips, anti-patterns, common misapplications
│   ├── post-book.md                      → Inside the Tornado, Living on the Fault Line, Dealing with Darwin, Escape Velocity, Zone to Win, Infinite Staircase, AI-era essays 2024–2026
│   ├── author-live-sources.md            → LinkedIn, geoffreyamoore.com hub, Chasm Institute, podcast appearances, YouTube
│   ├── voice-and-tone.md                 → how Moore actually talks (stage-then-advise, war-metaphor-as-spine, explicit inversions)
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Dunford, Helmer, Martin, Rumelt, Balfour, Raskin, Play Bigger, Christensen, Rogers)
│   ├── examples.md                       → Documentum, Salesforce, Aruba, Workday, VMware, Intel Operation Crush, Cisco/Microsoft/SAP gorillas, Cisco/HP/Microsoft Zone-to-Win, AI use cases 2024–2026
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/crossing-the-chasm" ~/.claude/skills/crossing-the-chasm

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Crossing the Chasm skill", "help me pick a beachhead using Moore's method", "walk me through Zone to Win").

## Attribution

**Geoffrey A. Moore** — organizational theorist, management consultant, and author. Chairman Emeritus of **Chasm Group** and **Chasm Institute**. Author of eight books on high-tech marketing and organizational strategy spanning 1991–2021. Former English literature professor turned Silicon Valley advisor to Salesforce, Microsoft, Intel, Google, Box, Aruba, Cognizant, Rackspace, and others. Widely considered the reference practitioner for high-tech go-to-market staging.

- **Buy the books:**
  - [*Crossing the Chasm* — 3rd edition (2014)](https://geoffreyamoore.com/book/crossing-the-chasm/) — canonical. Read it — this skill points you toward the source, it doesn't replace it.
  - [*Zone to Win* (2015)](https://geoffreyamoore.com/book/zone-to-win/) — four zones for incumbents.
  - [*The Infinite Staircase* (2021)](https://geoffreyamoore.com/book/the-infinite-staircase/) — philosophy.
  - *Inside the Tornado* (1995), *The Gorilla Game* (1998), *Living on the Fault Line* (2000), *Dealing with Darwin* (2005), *Escape Velocity* (2011) — the other five.
- **Personal hub:** [geoffreyamoore.com](https://geoffreyamoore.com/) — author, speaker, advisor, philosopher, business blog, philosophy blog, podcast index.
- **LinkedIn (freshest surface, multi-post cadence):** [/in/geoffreyamoore](https://www.linkedin.com/in/geoffreyamoore)
- **Chasm Institute (framework taxonomy + consulting/training):** [chasminstitute.com](https://www.chasminstitute.com/)
- **Freshest primary spoken sample:** [Lenny's Podcast, Jan 25, 2024](https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead) — the whole framework in Moore's own words.
- **Freshest AI-era primary text:** ["Can agentic AI 'cross the chasm' without falling in?" (Diginomica, Feb 6, 2026)](https://geoffreyamoore.com/business_blogs/can-agentic-ai-cross-the-chasm-without-falling-in-tech-thought-leader-geoffrey-moore-assesses-progress-in-straddling-the-divide/).

This skill is **not endorsed by Geoffrey Moore**. It is Marcos Sponton's structured reading of Moore's public work, built to make the assistant a better thinking partner in Moore's method. If Moore himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Moore's LinkedIn cadence and each new blog essay. Especially welcome:

- **New LinkedIn essays / blog posts / podcast episodes for `author-live-sources.md`** — Moore publishes on LinkedIn multiple times per week. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Moore has explicitly named an anti-pattern or an operational rule that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Moore's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, misses the stage-diagnostic, or blurs Moore with disruption theory (Christensen) is data.
- **Cases beyond the recurring roster** — Moore has cited many client companies in talks and interviews that aren't in `examples.md` yet.
- **Verified podcast appearances on major networks** (a16z, Acquired, SaaStr, Invest Like the Best) — searched as of July 2026, none surfaced. If you find one, PR the URL.
- **Full transcripts** of the 2014 3rd edition of *Crossing the Chasm*, *Inside the Tornado*, *Escape Velocity*, *Zone to Win* — the skill was built from framework structure + verified quotes + secondary structured notes; a full re-read may surface case-level material not indexed here.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Moore's staging discipline in my own week (particularly the "which stage are we in and what evidence tells us that?" instinct) and this skill is what falls out.

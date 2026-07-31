# Scaling People — an agent skill

An agent skill for **Claire Hughes Johnson's *Scaling People*** — the operating system she used as COO of Stripe (2014–2021) to scale the company from fewer than 200 to over 7,000 employees. Distilled from *Scaling People: Tactics for Management and Company Building* (Stripe Press, 2023), her podcast appearances (Lenny Rachitsky, First Round Review, Tim Ferriss, Newcomer, Slush, McKinsey), her public offsite toolkit, and her Fortune / LEADERS interviews.

This isn't a summary of the book. It's a working thinking partner in Claire's method, structured for the assistant (Claude, Codex, or any tool supporting the SKILL.md open standard) — with special emphasis on **routing to the right template**, because Claire's book is explicitly a reference work with over 100 pages of worksheets, templates, and example documents.

**Why this exists.** Invoke "Scaling People" or "Claire Hughes Johnson" in an agent without a skill and you get a competent summary of the 4 operating principles — but you don't get:
- The specific templates Claire provides (personal operating manual, team charter, structured-interview scorecard, hypothesis-based coaching opener, low-performer escalation).
- The reference-check drill (the ranking question, the coaching question, "if you're delegating the references, you're making a mistake").
- The executive-hiring failure modes she names by category (the "trying to be liked" trap; the "did they build followership in 3–6 months?" test).
- The cross-links to [[high-output-management]], [[radical-candor]], [[v2mom]], [[radical-focus]], [[working-backwards]] — Claire synthesizes all of them and credits explicitly.
- Post-book material — 2023–2024 podcast circuit, LinkedIn cadence, Tim Ferriss appearance.

This skill closes those gaps.

## What's inside

```
scaling-people/
├── SKILL.md                              → activation triggers + when-to-use guide + non-negotiables
├── README.md                             → this file
├── references/
│   ├── method.md                         → 4 operating principles, founding documents, hiring loop, references, hypothesis-based coaching, low-performer escalation, operating cadence, personal operating manual — with templates
│   ├── heuristics.md                     → do's, don'ts, gotchas, and the specific failure modes Claire names (exec-hiring "trying to be liked", forcing a mission too early, victim/self-awareness gaps, template-worship)
│   ├── post-book.md                      → what Claire has published/said since the book launched Feb 2023 (podcast circuit, LinkedIn, TF, Newcomer, McKinsey)
│   ├── author-live-sources.md            → index of every place Claire publishes / speaks + board seats as operator context
│   ├── voice-and-tone.md                 → operator-precise, template-first, warm-but-firm, "make the implicit explicit", "be an explorer not a lecturer"
│   ├── applications.md                   → when to use, when NOT, cross-links to Grove / Kim Scott / V2MOM / Radical Focus / Working Backwards. Load-bearing because Claire is a synthesizer.
│   ├── examples.md                       → Stripe scaling, Working with Claire viral spread, the Collison brothers' hiring process, the Chief of Business Operations portfolio hire, cross-industry cases
│   ├── prompts.md                        → invocation templates for common tasks
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

This skill follows the [agent skills](https://agentskills.io/) open standard — it works in Claude Code, Codex CLI, and any other agent that reads SKILL.md.

**Recommended — via [skills.sh](https://github.com/orgs/anthropics/discussions/skills):**

```bash
skills install scaling-people
```

**Manual — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/scaling-people" ~/.claude/skills/scaling-people
```

**Manual — Codex CLI:**

```bash
ln -s "$(pwd)/skills/scaling-people" ~/.codex/skills/scaling-people
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Scaling People skill", "help me write my personal operating manual", "coach me through this reference call").

## The template-first design

Claire's book is a reference work. She wrote it explicitly so a reader could open the table of contents, look up a topic, and consult that chapter. This skill mirrors that: it's a **template router** as much as a method explainer. If your situation is real, the assistant's response includes the specific doc / question / opener Claire would give you — not just abstract principle.

Under-the-hood consequence: `references/method.md` is unusually long and structured by artifact. `references/prompts.md` is unusually specific — each entry ends with the actual template shape or opener.

## Compose with the rest of the manager stack

Claire synthesizes many other frameworks and credits them explicitly. Fidelity to Claire means doing the same. This skill routes to (and is often composed with):

- **[[high-output-management]] — Andy Grove.** Grove is the mechanical foundation Claire builds on (1:1s, leverage, task-relevant maturity). If you need the plumbing, go there first.
- **[[radical-candor]] — Kim Scott.** Kim's 2×2 is the diagnostic for a *single* feedback move. Claire's method is the *system* around feedback. Compose.
- **[[v2mom]] — Marc Benioff / Salesforce.** V2MOM is a single-page alignment tool; Claire's founding-docs + team charters are the decomposed version. Compose at different org levels.
- **[[radical-focus]] — Christina Wodtke.** Wodtke gives the weekly OKR ritual; Claire endorses OKRs inside a larger cadence. Compose.
- **[[working-backwards]] — Amazon / Bezos.** WB is a product-decision ritual; Claire's memo-first culture is the sibling. Compose at different decision layers.

If a user's question is really one of the above, route them. Don't force Claire's frame onto it.

## Attribution

**Claire Hughes Johnson** — Chief Operating Officer at Stripe from 2014 to 2021, helping scale the company from fewer than 200 to over 7,000 employees. Before Stripe, ~10 years at Google leading business teams across Gmail, Google Apps, consumer operations, AdWords, Google Offers, and the self-driving car project. Corporate officer and advisor at Stripe post-2021. Board seats include Ameresco, The Atlantic, Aurora Innovation, and HubSpot.

- **Buy the book:** *Scaling People: Tactics for Management and Company Building* on [Stripe Press](https://press.stripe.com/scaling-people) · [Amazon](https://www.amazon.com/Scaling-People-Tactics-Management-Building/dp/1953953212). Read it — this skill points you toward the source, it doesn't replace it. Especially: the 100+ pages of worksheets, templates, and example docs are the real durable value.
- **Claire on LinkedIn:** [https://www.linkedin.com/in/claire-hughes-johnson-7058/](https://www.linkedin.com/in/claire-hughes-johnson-7058/)
- **Claire's Offsite Toolkit (public):** [https://docs.superhuman.com/@clairehughesjohnson/claires-offsite-toolkit](https://docs.superhuman.com/@clairehughesjohnson/claires-offsite-toolkit)

This skill is **not endorsed by Claire Hughes Johnson.** It is Marcos Sponton's structured reading of her public work, built to make an agent a better thinking partner in the *Scaling People* method — especially as a template router. If Claire herself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Claire's ongoing public work (podcast, LinkedIn, occasional interviews) and with community reports of where it fails. Especially welcome:

- **New podcast episodes / essays / talks for `author-live-sources.md`** — Claire publishes on an irregular but consistent cadence. Add appearances with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Claire has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Claire's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output softens Claire's opinion, misses the template, or generalizes into "some managers…" hedging is data.
- **Additional worked examples** — Claire uses cross-industry cases (Dominique Crème, Dan Cohen, Zannya Mittenbottles, Sam Hagood, Reid Hoffman) that aren't fully documented in `examples.md` yet.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use *Scaling People* patterns in my own week and this skill is what falls out.

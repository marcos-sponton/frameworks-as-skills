# Theory of Constraints — an agent skill

An agent skill for **Eliyahu Goldratt's Theory of Constraints (TOC)** — the operations-and-project method introduced in ***The Goal*** (1984), the best-selling business novel of all time. Three interlocking layers:

- **Layer A** — the Goal + Throughput / Inventory / Operating Expense as a full replacement for cost-accounting thinking.
- **Layer B** — the Five Focusing Steps (Identify → Exploit → Subordinate → Elevate → Repeat), with **Drum-Buffer-Rope** for production and **Critical Chain Project Management** for projects.
- **Layer C** — the five **Thinking Processes** (Current Reality Tree, Evaporating Cloud, Future Reality Tree, Prerequisite Tree, Transition Tree) for constraints that are policies, beliefs, or conflicts.

This isn't a summary of *The Goal*. It is a working thinking partner in Goldratt's method, built from:

- *The Goal: A Process of Ongoing Improvement* (1984, w/ Jeff Cox; revised 2004, 2014)
- *It's Not Luck* (1994) — Thinking Processes for marketing and distribution
- *Critical Chain* (1997) — CCPM, Student Syndrome, Parkinson's-in-projects
- *Necessary But Not Sufficient* (2000, w/ Eli Schragenheim + Carol A. Ptak) — technology as necessary-but-not-sufficient
- *Isn't It Obvious?* (2006) — retail replenishment
- *The Choice* (2008, w/ Efrat Goldratt-Ashlag; Revised Edition 2023)
- *Beyond the Goal* (2005 audiobook) and the **Goldratt Satellite Program** — Goldratt's own voice archive
- Post-Goldratt stewardship: **Goldratt Consulting Group** (Rami Goldratt), **TOCICO**, ***Goldratt's Rules of Flow*** (Efrat Goldratt-Ashlag, 2023)
- Modern extensions: ***The Phoenix Project*** (Kim/Behr/Spafford, 2013) and the Three Ways; ***Rolling Rocks Downhill*** and ***The Bottleneck Rules*** (Clarke Ching); ***The Book of TameFlow*** (Steve Tendon, 2020)

**Why this exists.** Ask Claude or Codex about "the Theory of Constraints" without a skill and you get "find the bottleneck" — which is roughly 10% of the method and none of the interesting parts. This skill closes several gaps: the *three-layer* structure (not just the Five Focusing Steps), Throughput Accounting as an actual replacement for cost accounting, DBR/CCPM as domain-specific specializations rather than a generic "prioritize" heuristic, the Thinking Processes for the constraints that aren't machines, the two distinct voices in Goldratt's writing (Jonah / non-fiction), the cross-link into DORA and DevOps through *The Phoenix Project*, and — importantly — the fact that Goldratt died in 2011 so the ongoing work is carried by a named set of stewards.

## What's inside

```
theory-of-constraints/
├── SKILL.md                          → activation triggers + when-to-use guide
├── README.md                         → this file
├── references/
│   ├── method.md                     → 3 layers in depth: Goal + Throughput Accounting; Five Focusing Steps; DBR; CCPM; all 5 Thinking Processes
│   ├── heuristics.md                 → do's, don'ts, gotchas: dice game, statistical fluctuations, activation vs utilization, multitasking, inertia trap
│   ├── post-book.md                  → everything after The Goal: Goldratt's own sequence, then stewards (Efrat, Kim, Ching, Tendon)
│   ├── author-live-sources.md        → stewardship map: Goldratt Consulting, TOCICO, TOC.tv archive, modern practitioners
│   ├── voice-and-tone.md             → the two voices (Jonah / Goldratt-non-fiction), signature vocabulary, verbatim quotes
│   ├── applications.md               → when TOC fits, when it doesn't, adjacent frameworks (Lean, Six Sigma, DORA, Kanban, Lean Startup, Rumelt)
│   ├── examples.md                   → UniCo, Boy Scout hike, dice game, Phoenix Project mapping, healthcare, retail
│   ├── prompts.md                    → invocation templates
│   └── sources.md                    → complete traceability
├── examples/                         → placeholder (community-contributed worked cases)
└── evals/                            → v0 test cases (PRs invited to sharpen)
```

## Install

Three paths depending on where your agent lives.

```bash
# Claude Code — from this repo root:
ln -s "$(pwd)/skills/theory-of-constraints" ~/.claude/skills/theory-of-constraints

# Codex CLI:
ln -s "$(pwd)/skills/theory-of-constraints" ~/.codex/skills/theory-of-constraints

# Claude Desktop or another skill-aware agent: copy the folder into
# your skills directory (path varies by client).
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Theory of Constraints skill", "run a Current Reality Tree on this", "help me draw an Evaporating Cloud", "diagnose the constraint here").

## Attribution

**Eliyahu M. Goldratt (1947–2011)** — Israeli physicist (BSc Tel Aviv University; MSc, PhD Bar-Ilan University) turned management theorist. Founder of the Theory of Constraints. Held patents in medical devices, irrigation, sensors. Died June 11, 2011, aged 64.

**Jeff Cox** — Co-author of *The Goal* (novelist).

**Ongoing stewards (in order of institutional weight):**
- **Rami Goldratt** — CEO of [Goldratt Consulting Group](https://goldrattgroup.com/); son of Eliyahu. Global TOC implementations across manufacturing, retail, service industries.
- **Efrat Goldratt-Ashlag, PhD** — Organizational psychologist; daughter of Eliyahu. Co-author of *The Choice*; author of ***Goldratt's Rules of Flow*** (2023). Actively manages his intellectual legacy.
- **[TOCICO](https://www.tocico.org/)** — Theory of Constraints International Certification Organization. Standards body; annual TOC Global Conference.

**Modern extenders whose work this skill also draws on:**
- **Gene Kim, Kevin Behr, George Spafford** — ***The Phoenix Project*** (2013), *The DevOps Handbook*, *The Unicorn Project*. The DevOps translation of TOC.
- **Clarke Ching** — ***Rolling Rocks Downhill*** (2014), ***The Bottleneck Rules*** (2018). "The bottleneck guy" — accessible modern TOC voice for software and knowledge work.
- **Steve Tendon** — ***The Book of TameFlow*** (2020). TOC applied to PEST environments (Projects/Events/Stakeholders/Teams).
- **Carol A. Ptak** — Co-author of *Necessary But Not Sufficient*; developer of Demand-Driven MRP (DDMRP).
- **Eli Schragenheim** — Co-author of *Necessary But Not Sufficient*; TOC theorist.

- **Buy *The Goal*:** [North River Press](https://northriverpress.com/) · [Amazon](https://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951). Read it — this skill points you at the source, it doesn't replace it.
- **Buy *Goldratt's Rules of Flow*:** [Routledge](https://www.routledge.com/Goldratts-Rules-of-Flow/Goldratt-Ashlag/p/book/9781032578729)
- **Buy *The Choice* (Revised 2023):** [Routledge](https://www.routledge.com/The-Choice/Goldratt-Goldratt-Ashlag/p/book/9781032445151)
- **Buy *The Phoenix Project*:** [IT Revolution](https://itrevolution.com/product/the-phoenix-project/)
- **Goldratt's audio/video archive:** [TOC.tv (Goldratt Marketing)](https://www.toc-goldratt.com/en)
- **Goldratt Consulting Group:** [goldrattgroup.com](https://goldrattgroup.com/)
- **TOCICO:** [tocico.org](https://www.tocico.org/)
- **Clarke Ching:** [Medium](https://medium.com/@clarkeching) · [The Bottleneck Rules audiobook](https://www.clarkech.ing/)
- **TameFlow (Steve Tendon):** [tameflow.com](https://tameflow.com/)

This skill is **not endorsed by the Goldratt estate, Goldratt Consulting Group, Efrat Goldratt-Ashlag, TOCICO, Gene Kim, Clarke Ching, Steve Tendon, or any of the individuals or organizations named above.** It is Marcos Sponton's structured reading of the corpus and community, built to make Claude or Codex a better thinking partner in TOC. If any of the stewards want to correct or endorse anything here, PRs welcome.

## Contributing

TOC is 40+ years old and actively extended. Especially welcome:

- **Recent TOCICO conference material** — the annual conference (Kyoto 2026, 500+ practitioners) is the frontier of applied TOC. Notes, papers, case studies for `post-book.md` and `examples.md`.
- **New Efrat / Rami Goldratt publications and talks** — the family stewardship track for `author-live-sources.md`.
- **Additional Kim / Ching / Tendon material** — the modern-practitioner track.
- **Sector-specific case studies** — healthcare, education, government, agriculture, software.
- **Voice/tone corrections** — if the reading of Jonah vs. Goldratt-non-fiction is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data, not a defect.
- **Lean vs. TOC precision** — where the skill blurs the two, sharpen.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I read *The Goal* in the middle of a plant-visit-heavy period and it reorganized how I think about systems. This skill is what falls out of returning to the corpus every couple of years as new stewards keep publishing.

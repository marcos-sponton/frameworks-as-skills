# The Five Dysfunctions of a Team — an agent skill

An agent skill for **Patrick Lencioni's Five Dysfunctions of a Team** — the pyramid (Absence of Trust → Fear of Conflict → Lack of Commitment → Avoidance of Accountability → Inattention to Results), plus his post-book system: *The Advantage*'s Four Disciplines of organizational health, *The Ideal Team Player*'s humble/hungry/smart hiring virtues, *The Motive*'s reward-centered vs. responsibility-centered leadership diagnostic, and *The 6 Types of Working Genius* (WIDGET).

This isn't a summary of the 2002 book. It's a working thinking partner in Lencioni's method as it stands in 2026, built from:

- *The Five Dysfunctions of a Team* (Jossey-Bass, 2002; 20th Anniversary Edition 2022)
- *Overcoming the Five Dysfunctions of a Team: A Field Guide* (2005)
- *The Advantage: Why Organizational Health Trumps Everything Else in Business* (2012)
- *The Ideal Team Player* (2016)
- *The Motive* (2020)
- *The 6 Types of Working Genius* (2022)
- The weekly *At The Table with Patrick Lencioni* podcast (with Cody Thompson, 2019–present, 270+ episodes)
- The Table Group's canonical topic pages, assessments, and Working Genius certification

**Why this exists.** Invoke "Five Dysfunctions" in Claude or Codex without a skill and you get the taxonomy — five items in a list, roughly in order, without the sequential logic that is the framework's signature. The base model typically misses:

- **The pyramid is compounding, not parallel.** Absence of Trust enables Fear of Conflict enables Lack of Commitment enables Avoidance of Accountability enables Inattention to Results. Skipping this makes the framework generic.
- **Vulnerability-based trust vs. predictive trust.** The load-bearing distinction. Predictive trust looks like trust and isn't.
- **Post-book material spans 20+ years and 6+ books.** *The Advantage*, *Ideal Team Player*, *The Motive*, and *Working Genius* are part of one operating system.
- **Trust theater as the framework's most common failure mode.** The ropes-course off-site + zero behavior change on Monday.
- **Diagnose the leader before the team** (*The Motive*'s reward-centered vs. responsibility-centered).
- **First team** as the leader's peers, not their reports.

This skill closes those gaps.

## What's inside

```
five-dysfunctions/
├── SKILL.md                              → activation triggers + when-to-use guide + the trust-theater guard
├── README.md                             → this file
├── references/
│   ├── method.md                         → the pyramid, vulnerability-based trust, productive conflict, buy-in vs. consensus, peer-to-peer accountability, collective results — in Lencioni's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns — including the trust-theater guard
│   ├── post-book.md                      → material after 2002: Overcoming (2005), Advantage (2012), Ideal Team Player (2016), Motive (2020), Working Genius (2022), podcast
│   ├── author-live-sources.md            → index of live sources (podcast, Working Genius site, LinkedIn, YouTube, books)
│   ├── voice-and-tone.md                 → how Lencioni actually talks: fable-first, simple language for hard truths, warm push-back
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (Edmondson, Kim Scott, Roger Martin, Wodtke, Grove, Brown, CHJ — distinguished)
│   ├── examples.md                       → the cases Lencioni uses (Kathryn at DecisionTech, Rich O'Connor, Jeff Shanley, plus the podcast's client-anecdote pattern)
│   ├── prompts.md                        → invocation templates for common tasks
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

This skill follows the [agent skills](https://agentskills.io/) open standard — it works in Claude Code, Codex CLI, and any other agent that reads SKILL.md.

**Manual — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/five-dysfunctions" ~/.claude/skills/five-dysfunctions
```

**Manual — Codex CLI:**

```bash
ln -s "$(pwd)/skills/five-dysfunctions" ~/.codex/skills/five-dysfunctions
```

Once installed, invoke naturally by describing your situation — the assistant (Claude or Codex) picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Five Dysfunctions skill", "run the Lencioni pyramid on this team").

## The trust-theater guard

Vulnerability-based trust is uniquely easy to fake. This skill actively resists prescribing trust-building exercises without checking what happened after the last one. **The ropes-course off-site plus zero behavior change on Monday isn't trust-building — it's theater with better catering.** The test of trust is what happens in the next real work situation, not the off-site. If the user is describing a team where meetings are pleasant and nobody disagrees, name Absence of Trust or Fear of Conflict — do not celebrate it as team health.

## The pyramid as differential

The single most important thing this skill does that a naked base-model call does not: preserve the **sequential** structure of the pyramid. Each dysfunction enables the next. If you try to install peer-to-peer accountability on a team stuck at Absence of Trust, you get performative accountability. Diagnose the lowest broken layer and fix it first.

## Attribution

**Patrick Lencioni** — Founder and president of The Table Group, a consulting firm focused on organizational health and executive team development since 1997. Author of 13 books. Host of the *At The Table* podcast. Creator of the Working Genius model.

- **Buy the books:** *The Five Dysfunctions of a Team* on [Amazon](https://www.amazon.com/Five-Dysfunctions-Team-Leadership-Fable/dp/0787960756) · *The Advantage* · *The Ideal Team Player* · *The Motive* · *The 6 Types of Working Genius*. Read them — this skill points you toward the source, it doesn't replace it.
- **The Table Group:** [https://www.tablegroup.com](https://www.tablegroup.com)
- **Working Genius:** [https://www.workinggenius.com](https://www.workinggenius.com)
- **At The Table podcast** (weekly with Cody Thompson): [Table Group podcast page](https://www.tablegroup.com/at-the-table/) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/at-the-table-with-patrick-lencioni/id1474171732)
- **Team Assessment:** [https://www.tablegroup.com/product/online-team-assessment/](https://www.tablegroup.com/product/online-team-assessment/)

Cody Thompson (Table Group principal consultant, podcast co-host) is credited where his contributions inform the material.

This skill is **not endorsed by Patrick Lencioni or The Table Group.** It is Marcos Sponton's structured reading of their public work, built to make Claude or Codex a better thinking partner in the Lencioni method — and, critically, to preserve the sequential pyramid structure and resist the trust-theater failure mode. If Lencioni or anyone at The Table Group wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the podcast and Lencioni's ongoing writing. Especially welcome:

- **New podcast episodes for `author-live-sources.md`** — the podcast ships weekly. Add episodes with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Lencioni has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Lencioni's voice is off, PR.
- **Failing test cases in `evals/`** — a case where the skill's output flattens the pyramid into a parallel list, or lets trust theater through, is data.
- **New cases from Lencioni's talks and podcast** — the recurring roster in `examples.md` skews to fable characters; podcast client anecdotes are underrepresented.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co).

# High Output Management — an agent skill

An agent skill for **Andy Grove's High Output Management** — the manager's operating system Grove built at Intel and wrote down in 1983 (managerial leverage, one-on-ones, staff meetings, the six-question decision framework, cascaded OKRs, task-relevant maturity, performance reviews, hiring, promotions) plus his 1996 strategy follow-up *Only the Paranoid Survive* (strategic inflection points, 10X change, Helpful Cassandras).

This isn't a summary of the book. It's a working thinking partner in Grove's method, built from:

- The 1983 book *High Output Management*, and the 2015 Vintage reprint with Ben Horowitz's foreword
- *Only the Paranoid Survive* (Currency, 1996)
- *Swimming Across: A Memoir* (Warner Books, 2001) for register
- *Strategy Is Destiny* (Grove + Burgelman, Free Press, 2001) for the Stanford GSB case archive
- Ben Horowitz's *The Hard Thing About Hard Things* (2014) and *What You Do Is Who You Are* (2019) — the direct successor books
- John Doerr's *Measure What Matters* (2018) and [What Matters](https://www.whatmatters.com/) — the OKR canon
- Julie Zhuo's *The Making of a Manager* (2019) — the first-time-manager translation of Grove
- Claire Hughes Johnson's *Scaling People* (Stripe Press, 2023) — the operational playbook heir
- Robert Burgelman's HBR tribute *Remembering Andy Grove, the Teacher* (2016)
- Podcast appearances including Ben Horowitz on Tim Ferriss (ep. 392, 2019) and Farnam Street's Knowledge Project *Outliers: Andy Grove* (ep. 229)

**Why this exists.** Ask the assistant about "one-on-ones" or "OKRs" or "task-relevant maturity" without a skill and you get a competent paraphrase that has drifted from the source. The paraphrases are the whole problem: Grove's method is opinionated, and softening it into generic management advice collapses the exact leverage the method was designed to produce. This skill closes the gap. Post-book material — the 40+ years of extension by Horowitz, Doerr, Zhuo, Hughes Johnson — lives in `references/post-book.md` and `references/author-live-sources.md`.

**Special note.** Andy Grove died 2016-03-21. Unlike skills for living authors, this one cannot chase new Grove essays — there won't be any. Instead, the `author-live-sources.md` file indexes the *carriers* who publicly extend Grove: Horowitz's ongoing a16z essays, Doerr's OKR platform, Zhuo's Substack, Hughes Johnson's Stripe Press work. The skill stays alive because the carriers do.

## What's inside

```
high-output-management/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → Grove's frameworks in his own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, common misapplications
│   ├── post-book.md                      → 1996 OTPS + Horowitz + Doerr + Zhuo + Hughes Johnson extensions
│   ├── author-live-sources.md            → index of the modern carriers (since Grove is gone)
│   ├── voice-and-tone.md                 → how Grove actually writes
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks
│   ├── examples.md                       → Intel memory-to-microprocessor pivot, Operation Crush, Grove's public rebuke, Google OKR adoption, Horowitz at Opsware
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/high-output-management" ~/.claude/skills/high-output-management

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the High Output Management skill", "what would Andy Grove do with this 1:1?").

## Attribution

**Andrew S. Grove (1936–2016)** — Hungarian-born chemical engineer (PhD, UC Berkeley, 1963); Intel's third employee (1968); President 1979, CEO 1987–1998, Chairman until 2005. *Time* Person of the Year 1997. Co-taught the Strategic Management course at Stanford GSB with Robert Burgelman for ~25 years.

- **Buy the book:** [*High Output Management* on Penguin Random House](https://www.penguinrandomhouse.com/books/72467/high-output-management-by-andrew-s-grove-former-chairman-and-ceo-of-intel/) · [Amazon (2015 reprint w/ Horowitz foreword)](https://www.amazon.com/High-Output-Management-Andrew-Grove/dp/0679762884). Read it — this skill points you toward the source, it doesn't replace it.
- **Buy the strategy follow-up:** [*Only the Paranoid Survive*](https://www.harpercollins.com/products/only-the-paranoid-survive-andrew-s-grove) (Currency, 1996).
- **The 2015 Horowitz foreword** (publicly reproduced): [Andy — Introduction to *High Output Management* on Medium](https://medium.com/software-is-eating-the-world/andy-37e10d4780bc).
- **The OKR lineage:** [What Matters — Origin Story (Grove → Doerr → Google)](https://www.whatmatters.com/articles/the-origin-story).
- **Ben Horowitz on Grove (audio):** [Tim Ferriss Show, ep. 392, transcript](https://tim.blog/2019/11/12/ben-horowitz-transcript/).
- **Robert Burgelman on Grove as teacher:** [HBR — Remembering Andy Grove, the Teacher](https://hbr.org/2016/03/remembering-andy-grove-the-teacher).

This skill is **not endorsed by Andy Grove's estate or by Intel**. It is Marcos Sponton's structured reading of Grove's public work — the 1983 book, the 1996 book, HBR articles, Stanford course materials, and the carriers (Horowitz, Doerr, Zhuo, Hughes Johnson, Burgelman) who publicly extend his method. If Grove's estate, Intel, or any of the named carriers wants to correct or endorse anything here, PRs welcome.

## Contributing

Grove's method is closed at the source, but the carriers keep publishing. Especially welcome:

- **New carrier material for `author-live-sources.md`** — a new Horowitz essay, a new Hughes Johnson chapter, a new Zhuo Substack post, a Doerr keynote, an Intel-alumni memoir. Add it with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if a carrier has explicitly extended a Grove pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Grove's voice is off (especially against the memoir *Swimming Across*), tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or has drifted into paraphrase is data.
- **Cases beyond the Intel roster** — the skill has a small case set (Intel pivot, Operation Crush, Google OKR adoption, Opsware). PRs adding cases from Stripe, Facebook, or other Grove-influenced orgs welcome.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). *High Output Management* was the first management book I read after starting Prown and it structured how I run one-on-ones, cascade OKRs, and think about the operating system of a team.

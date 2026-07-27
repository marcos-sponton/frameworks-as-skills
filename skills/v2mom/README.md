# V2MOM — an agent skill

An agent skill for **Marc Benioff's V2MOM** — the five-element alignment framework (Vision, Values, Methods, Obstacles, Measures) Benioff wrote on an American Express envelope in Salesforce's first weeks (1999) and has personally rewritten every fiscal year since.

This isn't a summary of the framework. It's a working thinking partner in Benioff's method, built from:

- *Behind the Cloud* (Jossey-Bass, 2009, with Carlye Adler) — first public account of V2MOM's origin and mechanics.
- *Trailblazer* (Currency, 2019, with Monica Langley) — the values-first management framing (Ohana, "values create value").
- The Salesforce blog and the Trailhead "V2MOM" module (Salesforce's official curriculum).
- Every annual Salesforce V2MOM press cycle since (including the FY24 Wellness Culture controversy and the FY26 Agentforce pivot).
- Benioff's posture and vocabulary from Dreamforce keynotes, Fortune Leadership Next (2024), and other press.

**Why this exists.** Ask Claude or Codex about V2MOM without a skill and you get a thin summary — the model knows the acronym but not the ordering rules, the cascade mechanics, the fact that Obstacles is load-bearing, or the difference between V2MOM and OKRs done as a checklist. This skill closes that gap.

## What's inside

```
v2mom/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 5 elements in Benioff's own terms, ordering rules
│   ├── heuristics.md                     → do's, don'ts, gotchas, common misapplications
│   ├── post-book.md                      → V2MOM's evolution 1999 → 2026 (envelope → 75k-employee cascade → AI/Agentforce)
│   ├── author-live-sources.md            → where Benioff & Salesforce publish about V2MOM
│   ├── voice-and-tone.md                 → how Benioff actually talks (Ohana, Trust-first, beginner's mind)
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (OKRs, VMV, P2W, Rumelt)
│   ├── examples.md                       → worked cases (1999 original, IC V2MOM, project V2MOM)
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

The Frameworks-as-Skills repo ships a one-shot installer that wires this skill into Claude Code and Codex CLI:

```bash
# From this repo root:
./skills.sh install v2mom
```

Or, manually:

```bash
# Claude Code
ln -s "$(pwd)/skills/v2mom" ~/.claude/skills/v2mom

# Codex CLI
ln -s "$(pwd)/skills/v2mom" ~/.codex/skills/v2mom
```

Once installed, the assistant (Claude or Codex) picks up the skill automatically when your task matches the triggers in `SKILL.md` — or when you invoke by name ("use the V2MOM skill", "help me write a V2MOM").

## Attribution

**Marc Benioff** — Founder, chair, and CEO of Salesforce. He wrote the first V2MOM on a large American Express envelope in a Hawaiian coffee shop in the company's opening weeks (1999); it was framed and gifted back to him by co-founder Parker Harris on IPO day (2004). Salesforce Ohana values in priority order: **Trust, Customer Success, Innovation, Equality, Sustainability**.

- **Behind the Cloud:** [Amazon](https://www.amazon.com/Behind-Cloud-Salesforce-com-Billion-Dollar-Company/dp/B08XLGFP8V) · [Archive.org](https://archive.org/details/behindclouduntol00beni). The primary source. Read it — this skill points you at Benioff, it doesn't replace him.
- **Trailblazer:** [Amazon](https://www.amazon.com/Trailblazer-Business-Greatest-Platform-Change/dp/1984825194).
- **Salesforce V2MOM blog piece:** [How to Create Alignment Within Your Company](https://www.salesforce.com/blog/how-to-create-alignment-within-your-company/).
- **Salesforce Trailhead — V2MOM module:** [Achieve Organizational Alignment with V2MOM](https://trailhead.salesforce.com/content/learn/modules/manage_the_sfdc_organizational_alignment_v2mom).
- **Marc Benioff on X:** [@Benioff](https://x.com/Benioff).
- **Marc Benioff on LinkedIn:** [marcbenioff](https://www.linkedin.com/in/marcbenioff).

This skill is **not endorsed by Marc Benioff or Salesforce**. It is Marcos Sponton's structured reading of Benioff's public writing and Salesforce's public teaching on V2MOM, built to make Claude or Codex a better thinking partner in the method. If Benioff or Salesforce want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with each fiscal year's Salesforce V2MOM release and Benioff's press cycle around it. Especially welcome:

- **New Benioff interviews / keynote transcripts for `author-live-sources.md`** — the annual V2MOM press cycle (typically Dec–Feb) is the freshest primary material. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Benioff or Salesforce Trailhead has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if the read of Benioff's voice is off (too corporate, too saccharine, wrong register), tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Worked V2MOMs from other companies / individuals** who use the framework publicly — the more concrete examples, the sharper the skill.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I run V2MOM annually on Prown itself, cascaded across the small team, and this skill is what falls out.

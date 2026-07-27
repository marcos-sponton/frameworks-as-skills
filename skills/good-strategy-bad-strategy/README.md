# Good Strategy Bad Strategy — an agent skill

An agent skill for **Richard Rumelt's kernel of strategy** — diagnosis, guiding policy, coherent action — plus the 2022 refinement, **"the crux"** (the pivotal challenge on which the strategy actually turns), and Rumelt's more recent reframe: stop calling this "strategy"; call it an **action agenda**.

This isn't a summary of the book. It's a working thinking partner in Rumelt's method, built from:

- **Good Strategy Bad Strategy** (2011)
- **The Crux: How Leaders Become Strategists** (2022)
- Rumelt Perspectives Substack (weekly-ish essays; renamed from Strategeion in early 2026)
- HBR and McKinsey Quarterly interviews
- Podcast appearances including Lenny Rachitsky (2024), Strategy Skills Podcast Ep. 253, BCG Henderson Institute (2022)
- Rumelt's Strategy Foundry operational method (from his official site)

**Why this exists.** Invoke "Good Strategy Bad Strategy" in Claude or Codex without a skill and you get a thin summary — the model knows the 2011 book but rarely brings in *The Crux* (2022), the action-agenda reframe (2024), the Foundry process (post-2022), or the chain-link logic (Substack). This skill closes that gap. Post-book material lives in `references/post-book.md`.

## What's inside

```
good-strategy-bad-strategy/
├── SKILL.md                  → activation triggers + when-to-use guide
├── README.md                 → this file
├── references/
│   ├── method.md             → the kernel + crux in Rumelt's own terms
│   ├── heuristics.md         → do's, don'ts, gotchas, anti-patterns
│   ├── post-book.md          → material published after 2011 (Crux, action agenda, Foundry, chain-link)
│   ├── author-live-sources.md → index of all live sources (Substack, McKinsey interviews, dense podcasts)
│   ├── voice-and-tone.md     → how Rumelt actually talks
│   ├── applications.md       → when to use, when NOT, adjacent frameworks
│   ├── examples.md           → worked cases (Nelson, SpaceX, Nvidia, Netflix, Southwest, Nokia, Salesforce, Vietnam, WeWork, Challenger, Sprint-Nextel, Intel, more)
│   ├── prompts.md            → invocation templates
│   └── sources.md            → complete traceability
├── examples/                 → longer worked examples (community-contributable)
└── evals/                    → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/good-strategy-bad-strategy" ~/.claude/skills/good-strategy-bad-strategy

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Good Strategy Bad Strategy skill", "let's find the crux", "diagnose this before we set goals").

## Attribution

**Richard Rumelt** — Professor Emeritus at UCLA Anderson School of Management. Considered one of the "founding fathers" of the strategic management field for foundational academic contributions including "How much does industry matter?" (1991) and the resource-based view of the firm. Author of *Good Strategy Bad Strategy: The Difference and Why It Matters* (Crown Business, 2011) and *The Crux: How Leaders Become Strategists* (PublicAffairs, 2022).

- **Buy Good Strategy Bad Strategy:** [Amazon](https://www.amazon.com/Good-Strategy-Bad-difference-matters/dp/0307886239). Read it.
- **Buy The Crux:** [Amazon](https://www.amazon.com/Crux-Strategy-Grapples-Fundamental-Challenge/dp/1541701240). Read this second.
- **Rumelt Perspectives Substack** (weekly, live): [https://rumelt.substack.com/](https://rumelt.substack.com/)
- **Official site:** [https://www.richardrumelt.com/](https://www.richardrumelt.com/)
- **Strategy Foundry (his consulting offering):** [https://www.richardrumelt.com/strategy-foundry](https://www.richardrumelt.com/strategy-foundry)

This skill is **not endorsed by Richard Rumelt**. It is Marcos Sponton's structured reading of Rumelt's public work, built to make Claude or Codex a better thinking partner in Rumelt's method. If Rumelt himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with Rumelt's Substack and any new interviews. Especially welcome:

- **New essays for `post-book.md`** — Rumelt publishes ~weekly. Add them with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Rumelt has explicitly warned about an anti-pattern that isn't captured, add it with source.
- **Voice/tone corrections** — if my read of Rumelt's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or wrong is data.
- **Cases beyond the recurring roster** — Rumelt uses many cases in single essays that aren't in `examples.md` yet.

## Related skill

- [Playing to Win](../playing-to-win/) — Roger Martin's cascade. Rumelt front-loads diagnosis; Martin front-loads choice. The two compose well: diagnose (Rumelt) → choose (Martin).

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Rumelt's kernel in my own week and this skill is what falls out.

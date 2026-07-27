# Frameworks as Skills

A growing collection of Claude Skills that package management and product frameworks — the ones I actually use when thinking about strategy, discovery, and building — so they're available inside the pipeline where you already work, not stuck behind a Custom GPT you have to visit.

**Why:** when I invoke a well-known framework by name (e.g., "let's do Playing to Win on this"), the response Claude gives me by default is thin — it knows the book but not the twelve years of refinements the author has published since. These skills close that gap: primary text + post-publication material + practitioner heuristics + the author's voice, structured so Claude can be a competent thinking partner in the framework, not just a summarizer.

**What's here** — each skill packages one framework:

- ✅ **[Playing to Win](skills/playing-to-win/)** — Roger Martin's 5-question strategy cascade
- ✅ **[Good Strategy Bad Strategy](skills/good-strategy-bad-strategy/)** — Richard Rumelt's kernel of strategy (diagnosis / guiding policy / coherent action)
- more coming — see the roadmap below

## How each skill is built

Every skill follows the same anatomy so you know what to expect:

```
skills/<framework-slug>/
├── SKILL.md               → triggers + when-to-use + high-level guide
├── README.md              → per-skill human-facing intro + links to the author's work
├── references/
│   ├── method.md          → the framework in the author's own terms
│   ├── heuristics.md      → do's, don'ts, gotchas, pro tips, anti-patterns
│   ├── post-book.md       → material the author published AFTER the primary text
│   ├── author-live-sources.md → index of every place the author publishes regularly (Substack/Medium/YouTube/podcasts)
│   ├── voice-and-tone.md  → how the author actually talks about the framework
│   ├── applications.md    → when to use, when NOT to, adjacent frameworks
│   ├── examples.md        → worked cases the author has cited publicly
│   ├── prompts.md         → invocation templates
│   └── sources.md         → every source consulted, with links
├── examples/              → longer worked examples if useful
└── evals/                 → v0 test cases (community invited to sharpen)
```

The `_template/` directory contains the canonical scaffold. If you want to contribute a skill for another framework, start there.

## Install a skill

**In Claude Code:**
```bash
# Clone the repo somewhere on your machine
git clone https://github.com/marcos-sponton/frameworks-as-skills.git ~/frameworks-as-skills

# Symlink the skill you want into your Claude Code skills directory
ln -s ~/frameworks-as-skills/skills/playing-to-win ~/.claude/skills/playing-to-win
```

**In Claude Desktop / Cowork:** copy the skill folder into your skills directory (path depends on your setup).

Once installed, invoke the skill by describing your situation naturally — Claude picks it up when your task matches the skill's triggers, or when you invoke it by name ("use the Playing to Win skill").

## What these skills are NOT

- **Not a replacement for the books.** Every skill links to the original source and encourages you to read it. Skills are distillations for AI conversations — a good skill points you toward the book, doesn't replace it.
- **Not endorsed by the authors** unless explicitly stated. This is my structured reading of their public work.
- **Not a comprehensive catalog.** For enciclopedic coverage of business/strategy skills see [wondelai/skills](https://github.com/wondelai/skills) (50+ skills across product, UX, marketing, code) or [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) (70 PM-specific skills). This repo is deliberately narrow — a few frameworks I use often, packaged with more depth than a catalog can carry.

## Contributing

PRs welcome. Especially:
- New skills for frameworks that fit the pattern above (author has a body of work beyond one book, framework is misapplied enough that a well-structured skill would help).
- Sharper `heuristics.md` — if you know an anti-pattern the author has warned about that isn't captured, add it with a source.
- Post-publication material — podcasts, essays, articles that add nuance to the primary text.
- Voice & tone corrections — if my read of an author's voice is off, tell me.
- Failing test cases in `evals/` — a case where the skill's output is thin or wrong is data.

See `CONTRIBUTING.md` (coming soon) for how to structure additions.

## Roadmap

**Next candidates** (order tentative, subject to change):
- Escaping the Build Trap — Melissa Perri
- Continuous Discovery Habits — Teresa Torres
- Shape Up — Ryan Singer / Basecamp
- Wardley Mapping — Simon Wardley

**Kill criteria.** If two skills in a row after Playing to Win + Rumelt don't get meaningful traction (see the release posts for what "meaningful" means), I pause and reassess before shipping more. This isn't a catalog for its own sake.

## License

MIT — use, remix, redistribute. Attribution appreciated but not required.

## Who's behind this

Marcos Sponton — [GitHub](https://github.com/marcos-sponton) · [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co) (AI interview infrastructure).

I use these frameworks in my own week — with clients, on my own products, in planning. This repo is what falls out.

# Frameworks as Skills

> Install: `npx skills add marcos-sponton/frameworks-as-skills` — works in any tool that supports the [SKILL.md open standard](https://agentskills.io) (Claude Code, Codex CLI, Claude Desktop, and more coming).

A growing collection of agent skills — **36 today** — that package the management, product, strategy, and discovery frameworks I actually use into structured methods your AI assistant can reason with, not just summarize. The point isn't to have the frameworks *listed* somewhere; it's to have real conversations with an assistant that knows the method deeply enough to push back, ask the next right question, and hold the author's original discipline.

**Use them to think, not to skim.** Pull up Playing to Win when you're stuck on strategy. Load Never Split the Difference before a hard conversation. Run Continuous Discovery Habits alongside your PM work. Compose Cynefin + Thinking in Systems when the problem doesn't fit one lens. Each skill is designed so you can have a working session with your assistant — not read a summary — in the framework's actual voice, with the author's post-book refinements and anti-patterns loaded.

**Why this exists.** When you invoke a well-known framework by name (e.g., "let's do Playing to Win on this"), the response the assistant gives by default is thin — it knows the book but not the twelve years of refinements the author has published since. These skills close that gap: primary text + post-publication material (essays, podcasts, updated books) + practitioner heuristics + the author's actual voice, structured so the assistant can be a competent thinking partner in the framework, not just a summarizer.

**Where this is going.** Started as a personal shelf. Now: 30 skills across 9 themes (strategy, product, positioning, decisions, sales, management, growth, engineering, operations), each built from a research dossier that's kept in `_research/` so the process is legible. Community contributions welcome — new skills, sharper heuristics, missing post-book essays, better failing test cases. The repo grows as the frameworks and their authors grow.

<!-- SKILLS_INDEX_START -->
**What's here** — 36 skills, each packages one framework:

**Strategy**
- ✅ **[7 Powers](skills/7-powers/)** — Hamilton Helmer's taxonomy of durable competitive advantage (Benefit + Barrier, 3 S's, Statics vs. Dynamics)
- ✅ **[DHM Model](skills/dhm-model/)** — Gibson Biddle's Delight × Hard-to-copy × Margin-enhancing product strategy filter + GEM, GLEe, proxy metrics, Strategy/Metric/T...
- ✅ **[Good Strategy Bad Strategy](skills/good-strategy-bad-strategy/)** — Richard Rumelt's kernel (diagnosis / guiding policy / coherent action) + The Crux + "action agenda" reframe
- ✅ **[Pattern Breakers](skills/pattern-breakers/)** — Mike Maples Jr's inflections + insights + movements for breakthrough startups — non-consensus bets, backcasting, living in the...
- ✅ **[Playing to Win](skills/playing-to-win/)** — Roger Martin's 5-question strategy cascade
- ✅ **[V2MOM](skills/v2mom/)** — Marc Benioff's Vision-Values-Methods-Obstacles-Measures — obstacles as the load-bearing element, order matters, individual/team...

**Product & discovery**
- ✅ **[Continuous Discovery Habits](skills/continuous-discovery-habits/)** — Teresa Torres's weekly customer touchpoints, Opportunity Solution Tree, story-based interviewing, assumption tests across 5 cat...
- ✅ **[Demand-Side Sales](skills/demand-side-sales/)** — Bob Moesta's Four Forces of Progress, Switch Interview, buying timeline, and struggling moments — the causal-research variant o...
- ✅ **[Escaping the Build Trap](skills/escaping-the-build-trap/)** — Melissa Perri's product-org diagnostic (Four Dimensions + Three Pillars of Product Ops)
- ✅ **[Inspired](skills/inspired/)** — Marty Cagan's product team topology + discovery/delivery split — spans Inspired, Empowered, and Transformed (Product Operating...
- ✅ **[Shape Up](skills/shape-up/)** — Ryan Singer's shaping/betting/building — 6-week cycles, appetite (not estimation), hill charts, no backlog, circuit breaker — f...
- ✅ **[Shreyas Doshi](skills/shreyas-doshi/)** — Shreyas Doshi's PM frameworks — LNO (Leverage/Neutral/Overhead), pre-mortems (Tigers/Paper Tigers/Elephants), Three Levels of P...
- ✅ **[Sprint](skills/sprint/)** — Jake Knapp's five-day process for answering critical business questions through design, prototyping, and testing with real cust...
- ✅ **[The Lean Startup](skills/lean-startup/)** — Eric Ries's Build-Measure-Learn, MVP (not v0.1), pivot/persevere, innovation accounting, engines of growth — with aggressive mi...
- ✅ **[The Mom Test](skills/mom-test/)** — Rob Fitzpatrick's three rules for customer conversations — talk about their life (not your idea), ask about the past (not the f...
- ✅ **[Working Backwards](skills/working-backwards/)** — Bill Carr + Colin Bryar's Amazon method (PR/FAQ, 6-pager, silent reading, Single-Threaded Leader, input metrics)

**Positioning & narrative**
- ✅ **[Crossing the Chasm](skills/crossing-the-chasm/)** — Geoffrey Moore's technology adoption lifecycle, bowling alley, whole product, beachhead — 3rd ed as canonical, plus Inside the...
- ✅ **[Obviously Awesome](skills/obviously-awesome/)** — April Dunford's positioning method (5 components + 8-step Sales Pitch)
- ✅ **[Play Bigger](skills/play-bigger/)** — Ramadan/Peterson/Lochhead/Maney's category design — Point of View, Lightning Strike, Category King, Data Flywheel — evolves thr...
- ✅ **[Strategic Narrative](skills/strategic-narrative/)** — Andy Raskin's 5-part narrative structure (Change in the World → Promised Land → Magic Gifts)

**Sensemaking & decisions**
- ✅ **[Cynefin](skills/cynefin/)** — Dave Snowden's sensemaking framework (5 domains, constraints, aporetic turn, Estuarine)
- ✅ **[Thinking in Bets](skills/thinking-in-bets/)** — Annie Duke's decision toolkit (resulting, kill criteria, calibration, monkeys & pedestals)
- ✅ **[Thinking in Systems](skills/thinking-in-systems/)** — Donella Meadows's stocks/flows/loops, 8 system archetypes, 12 leverage points (ranked, not menu), Dancing with Systems — carrie...

**Sales**
- ✅ **[Challenger Sale + JOLT](skills/challenger-sale/)** — Matt Dixon's Challenger + JOLT Effect — Challenger earns the meeting, JOLT closes against no-decision; not aggression, not pres...
- ✅ **[Never Split the Difference](skills/never-split-the-difference/)** — Chris Voss's tactical empathy — mirroring, labeling, calibrated questions, "that's right", Ackerman model, Black Swans (with we...

**Management & communication**
- ✅ **[High Output Management](skills/high-output-management/)** — Andy Grove's managerial leverage, task-relevant output, 1:1s, staff meetings, decision framework — kept alive by Horowitz, Doer...
- ✅ **[Radical Candor](skills/radical-candor/)** — Kim Scott's Care Personally + Challenge Directly matrix — with an explicit guard against weaponization as "brutal honesty"
- ✅ **[Radical Focus](skills/radical-focus/)** — Christina Wodtke's OKRs done right — weekly cadence, team-level, Team Health Monitor, one Objective at a time
- ✅ **[Scaling People](skills/scaling-people/)** — Claire Hughes Johnson's founding docs, operating cadences, hiring loops, personal operating manual — template-first, synthesize...
- ✅ **[The Fearless Organization](skills/fearless-organization/)** — Amy Edmondson's psychological safety paired with high standards (Learning Zone 2x2) — plus the Right Kind of Wrong failure taxo...
- ✅ **[The Five Dysfunctions of a Team](skills/five-dysfunctions/)** — Patrick Lencioni's sequential pyramid (trust → conflict → commitment → accountability → results) — with guards against trust th...

**Growth**
- ✅ **[Four Fits](skills/four-fits/)** — Brian Balfour's Product-Market-Channel-Model fit chain + growth loops (compounding, closed) as alternative to funnels
- ✅ **[Hooked](skills/hooked/)** — Nir Eyal's Hook Model (Trigger → Action → Variable Reward → Investment), Manipulation Matrix for ethical evaluation, and Indist...
- ✅ **[The Cold Start Problem](skills/cold-start-problem/)** — Andrew Chen's network-effects lifecycle — atomic network, hard side, five stages (Cold Start → Tipping Point → Escape Velocity...

**Engineering**
- ✅ **[DORA / Accelerate](skills/dora-accelerate/)** — Nicole Forsgren's DORA metrics + capabilities + SPACE + DevEx — evidence-based, org-level (never individual performance)

**Operations**
- ✅ **[Theory of Constraints](skills/theory-of-constraints/)** — Eliyahu Goldratt's Five Focusing Steps, Throughput/Inventory/Operating Expense, DBR, Critical Chain, Thinking Processes — carri...

More coming — see the roadmap below.
<!-- SKILLS_INDEX_END -->

> This section is auto-generated by `scripts/update-readme.py` from each `skills/*/SKILL.md` plus curated titles/taglines in [`.skills-index.yaml`](./.skills-index.yaml). Run the script after adding a new skill.

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

These skills follow the [SKILL.md open standard](https://agentskills.io) — they work across Claude Code, Codex CLI, Claude Desktop, and any compatible tool without modification.

**Via skills.sh (any compatible agent):**
```bash
npx skills add marcos-sponton/frameworks-as-skills
```

**Manual — Claude Code:**
```bash
git clone https://github.com/marcos-sponton/frameworks-as-skills.git ~/frameworks-as-skills
ln -s ~/frameworks-as-skills/skills/playing-to-win ~/.claude/skills/playing-to-win
```

**Manual — Codex CLI:**
```bash
git clone https://github.com/marcos-sponton/frameworks-as-skills.git ~/frameworks-as-skills
# Codex reads SKILL.md the same way — symlink or copy into your Codex skills directory
ln -s ~/frameworks-as-skills/skills/playing-to-win ~/.codex/skills/playing-to-win
```

**Claude Desktop:** copy the skill folder into your skills directory (path depends on your setup).

Once installed, invoke the skill by describing your situation naturally — the assistant picks it up when your task matches the skill's triggers, or when you invoke it by name ("use the Playing to Win skill").

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

**Next candidates** (order tentative):
- Wardley Mapping — Simon Wardley
- North Star Framework — John Cutler
- Getting to Yes — Fisher / Ury (as a foil to Never Split the Difference)
- Only the Paranoid Survive — Andrew Grove (companion to High Output Management)

**Process behind each skill.** Every skill is built from a research dossier (see [`_research/`](_research/) directory). The dossier extracts live sources, method, voice & tone, heuristics, and adjacent frameworks. The build phase hydrates the dossier into the standard skill structure. If you want to contribute a candidate framework, start with a dossier PR against `_research/`.

**Kill criteria.** If the batch of skills doesn't get meaningful traction (see release posts for what "meaningful" means), I pause and reassess before shipping more. This isn't a catalog for its own sake.

## License

MIT — use, remix, redistribute. Attribution appreciated but not required.

## Who's behind this

Marcos Sponton — [GitHub](https://github.com/marcos-sponton) · [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co) (AI interview infrastructure for consulting companies).

I use these frameworks in my own week — with clients, on my own products, in planning. This repo is what falls out.

# Hooked — an agent skill

An agent skill for **Nir Eyal's Hook Model** — the four-phase behavioral design framework (Trigger, Action, Variable Reward, Investment) for building habit-forming products, plus the Manipulation Matrix for ethical evaluation and the Indistractable model for attention defense.

This isn't a summary of the 2014 book. The Hook Model is one of the most-cited and most-simplified frameworks in product design — and the simplification strips the parts that matter most. The skill's value is in **fidelity** (Eyal's actual definitions vs. the degraded versions in the wild), **ethics** (the Manipulation Matrix that most retellings skip), and the **post-book material** (Indistractable, Beyond Belief, and 12 years of evolving thinking on behavioral design and tech responsibility).

Built from:

- *Hooked: How to Build Habit-Forming Products* (Portfolio, 2014) — the canonical source. Co-authored with Ryan Hoover (founder of Product Hunt). NYT bestseller. The four-phase model, the Habit Zone, the Manipulation Matrix.
- *Indistractable: How to Control Your Attention and Choose Your Life* (BenBella, 2019) — the demand-side companion. Traction vs. Distraction, the four strategies, the three pact types. Won 2019 OWL Award.
- *Beyond Belief: The Science-Backed Way to Stop Limiting Yourself and Achieve Breakthrough Results* (Portfolio, March 2026) — the cognitive layer. How beliefs shape the internal triggers that drive behavior. Instant NYT bestseller.
- **nirandfar.com** — Eyal's blog and newsletter (160,000+ subscribers). Hundreds of posts on behavioral design, distraction, productivity, and ethics.
- **Psychology Today columns** (2024–2026) — regular contributions on behavioral psychology applied to everyday life.
- **Lenny's Podcast appearance** (December 2023) — deep discussion on the Indistractable framework, the 10-minute rule, timeboxing, and the connection between *Hooked* and *Indistractable*.
- **LeanB2B interview** — practical walkthrough of the Hook Model for product builders, including the 5% habitual user threshold and habit path analysis.

**Why this exists.** Ask Claude or Codex about the "Hook Model" without a skill and you get a thin recitation of the four phases — Trigger, Action, Variable Reward, Investment — as if they were a checklist. What's missing: (a) the behavioral psychology foundations (Fogg, Skinner, Kahneman) that explain *why* each phase works; (b) the three types of variable reward and why "variable" is the load-bearing word; (c) the Manipulation Matrix — Eyal's ethical framework that most retellings treat as an afterthought when he treats it as a core component; (d) the Indistractable model — the demand-side defense manual that completes the behavioral design picture; (e) the post-2014 evolution of Eyal's thinking on tech ethics and personal responsibility; and (f) the practical anti-patterns (hooks vs. dark patterns, gamification vs. engagement loops, habits vs. addictions). This skill closes those gaps.

## What's inside

```
hooked/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → Hook Model (4 phases with Eyal's definitions), Habit Zone, Manipulation Matrix, Indistractable model (4 strategies + 3 pact types), integration of both books
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns: hooks vs. dark patterns, gamification mistakes, variable reward gone wrong, skipping the ethics check, notification spam vs. triggers
│   ├── post-book.md                      → Indistractable (2019), Beyond Belief (2026), ethics evolution from 2014 to present, tech-addiction debate, children and screen time position
│   ├── author-live-sources.md            → nirandfar.com blog index by topic, Psychology Today columns, newsletter, podcast appearances (Lenny, LeanB2B, Produx Labs), LinkedIn, social media
│   ├── voice-and-tone.md                 → how Eyal talks: warm academic-practitioner, behavioral psych made accessible, personal vulnerability, emphatic ethics, counter-intuitive claims backed by evidence
│   ├── applications.md                   → when to use (consumer, onboarding, health, content, diagnosis), when NOT (low-frequency, enterprise, no PMF), adjacent frameworks (Fogg, Clear, Torres, Ries) with composition
│   ├── examples.md                       → real cases: Instagram, Pinterest, Bible App, email, Slack, video games, Fitbod — each with full hook mapping
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability with URLs
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/hooked" ~/.claude/skills/hooked

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Hooked skill", "design a hook for my product", "run the Manipulation Matrix on this engagement design", "help me apply Indistractable to my work routine").

## Attribution

**Nir Eyal** — Israeli-American behavioral design expert; former Stanford GSB and Hasso Plattner Institute lecturer; angel investor (Canva, Kahoot!, Eventbrite). Author of *Hooked* (2014), *Indistractable* (2019), and *Beyond Belief* (2026) — three NYT bestsellers, 1M+ copies in 30+ languages. Publishes at nirandfar.com (160,000+ subscribers) and Psychology Today.

- **Buy the books:**
  - *Hooked* — [Amazon 1591847788](https://www.amazon.com/Hooked-How-Build-Habit-Forming-Products/dp/1591847788). Read it — this skill points you toward the source, it doesn't replace it.
  - *Indistractable* — [Amazon 194883653X](https://www.amazon.com/Indistractable-Control-Your-Attention-Choose/dp/194883653X). The other half of the picture.
  - *Beyond Belief* — [Amazon 0593852036](https://www.amazon.com/Beyond-Belief-Science-Backed-Limiting-Breakthrough/dp/0593852036). The 2026 extension into beliefs and cognitive foundations.
- **nirandfar.com:** [nirandfar.com](https://www.nirandfar.com/) — blog, newsletter, workshops.
- **Newsletter:** [nirandfar.com/subscribe](https://www.nirandfar.com/subscribe/)
- **LinkedIn:** [Nir Eyal on LinkedIn](https://www.linkedin.com/in/naborfeyal/)
- **X:** [@nireyal](https://x.com/nireyal)

This skill is **not endorsed by Nir Eyal**. It is Marcos Sponton's structured reading of Eyal's public work, built to make the assistant a better thinking partner when applying the Hook Model — with the ethical guardrails, the behavioral psychology foundations, and the post-book evolution that most retellings collapse into a four-word checklist. If Eyal himself wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with each new Eyal blog post, podcast, or talk. Especially welcome:

- **New nirandfar.com articles and Psychology Today columns for `author-live-sources.md`** — Eyal publishes regularly. Add with topic + URL + one-line takeaway.
- **Beyond Belief podcast tour (2026)** — the launch cycle is generating new interviews. Add with same schema.
- **YouTube talk archive** — conference talks and interviews need systematic indexing.
- **Workshop/Masterclass content** — if you've taken the Hooked Workshop or Indistractable Masterclass and can add exercises or frameworks not in the books, contribute to `references/method.md` or `references/heuristics.md` with attribution.
- **Voice/tone corrections** — if my read of Eyal's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, generic, or skips the Manipulation Matrix is data.
- **Additional example cases for `examples.md`** — if Eyal has used a case in a talk or article that isn't indexed, add it with full hook mapping.
- **The ethics debate** — if you have a clean way to articulate the Eyal vs. Newport or Eyal vs. Haidt disagreement, contribute to `references/applications.md`.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). Behavioral design is core to how Prown's AI interview agents create engagement, and the Hook Model — with the Manipulation Matrix front and center — is how we think about it ethically.

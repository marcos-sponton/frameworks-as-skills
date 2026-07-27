# Radical Candor — an agent skill

An agent skill for **Kim Scott's Radical Candor** — the Care Personally + Challenge Directly 2×2 (Radical Candor / Ruinous Empathy / Obnoxious Aggression / Manipulative Insincerity), plus the GSD wheel, Career Conversations, Rock Stars vs Superstars, and her Just Work / Radical Respect (BUL: Bias, Prejudice, Bullying) framework.

This isn't a summary of the book. It's a working thinking partner in Kim's method, built from:

- *Radical Candor* (St. Martin's Press, 2017; revised 2019)
- *Just Work* (2021) and its 2024 rewrite *Radical Respect*
- The weekly *Radical Candor: Communication at Work* podcast (Kim Scott, Jason Rosoff, Amy Sandler — 2017 to present)
- Kim's Medium essays (@KimMaloneScott) and the Radical Candor company blog
- Podcast appearances including Lenny Rachitsky, Jordan Harbinger, First Round Review, Intercom, Pathwise, Crisp

**Why this exists.** Invoke "Radical Candor" in Claude or Codex without a skill and you get a thin summary of the 2×2 — the model knows the quadrants but not (a) the load-bearing role of Care Personally, (b) Kim's post-book material on weaponization and Compassionate Candor, (c) the operational details of HHIPP, GSD, Career Conversations, Rock Stars/Superstars, or (d) the BUL / Radical Respect framework from 2021/2024. And critically, it doesn't push back when a user tries to weaponize "Radical Candor" as permission to be an asshole — which is exactly the failure mode Kim spends most of her airtime warning against. This skill closes those gaps.

## What's inside

```
radical-candor/
├── SKILL.md                              → activation triggers + when-to-use guide + the voice guard
├── README.md                             → this file
├── references/
│   ├── method.md                         → the 2×2, HHIPP, GSD wheel, Career Conversations, Rock Stars/Superstars, BUL — in Kim's own terms
│   ├── heuristics.md                     → do's, don'ts, gotchas, anti-patterns — including the weaponization guard
│   ├── post-book.md                      → material Kim published after Radical Candor (Just Work, Radical Respect, podcast, Medium)
│   ├── author-live-sources.md            → index of live sources (podcast, Medium, blog, LinkedIn, YouTube, books)
│   ├── voice-and-tone.md                 → how Kim actually talks: confession-first, warm-funny-honest, the Sheryl and Bob stories as canon
│   ├── applications.md                   → when to use, when NOT, adjacent frameworks (NVC, Crucial Conversations, Dare to Lead, Radical Transparency — distinguished)
│   ├── examples.md                       → worked cases (Sheryl's "um" feedback, Bob at Google, Juice Software, construction site, Taylor Malone, Joe Hyde)
│   ├── prompts.md                        → invocation templates for common tasks
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

This skill follows the [agent skills](https://agentskills.io/) open standard — it works in Claude Code, Codex CLI, and any other agent that reads SKILL.md.

**Recommended — via [skills.sh](https://github.com/orgs/anthropics/discussions/skills):**

```bash
skills install radical-candor
```

**Manual — Claude Code:**

```bash
# From this repo root:
ln -s "$(pwd)/skills/radical-candor" ~/.claude/skills/radical-candor
```

**Manual — Codex CLI:**

```bash
ln -s "$(pwd)/skills/radical-candor" ~/.codex/skills/radical-candor
```

Once installed, invoke naturally by describing your situation — the assistant (Claude or Codex) picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Radical Candor skill", "walk me through this feedback conversation").

## The voice guard

Radical Candor is uniquely susceptible to weaponization — more than any other framework in this repo. Someone reads the book, decides they *are* a "Radical Candor person," and starts labeling their pre-existing bluntness as Radical Candor while ignoring the Care Personally axis. That's not Radical Candor. That's Obnoxious Aggression with better PR.

This skill actively resists that failure mode. **If the user is fishing for permission to be blunt without care, the assistant's job is to name it and redirect toward Care Personally investment first.** The Care axis is not decoration — it's the load-bearing element of the whole method. Kim spends more airtime defending the Care axis than the Challenge axis, and this skill mirrors that.

## Attribution

**Kim Scott** — Executive coach, ex-Google (AdSense, YouTube, DoubleClick teams), ex-Apple University faculty, ex-CEO of Juice Software. Coached at Dropbox, Twitter, Qualtrics. Co-founder of Radical Candor LLC (with Jason Rosoff) and Just Work Together.

- **Buy the books:** *Radical Candor* on [Amazon](https://www.amazon.com/Radical-Candor-Kick-Ass-Without-Humanity/dp/1250103509) · *Radical Respect* on [Amazon](https://www.amazon.com/Radical-Respect-Work-Together-Better/dp/1250623766). Read them — this skill points you toward the source, it doesn't replace it.
- **Radical Candor company site:** [https://www.radicalcandor.com](https://www.radicalcandor.com)
- **Kim's personal site:** [https://kimmalonescott.com](https://kimmalonescott.com)
- **Kim's Medium:** [https://kimmalonescott.medium.com](https://kimmalonescott.medium.com)
- **Radical Candor: Communication at Work podcast** (weekly, with Jason Rosoff and Amy Sandler): [Apple Podcasts](https://podcasts.apple.com/us/podcast/radical-candor-communication-at-work/id1188489488) · [Spotify](https://open.spotify.com/show/3qOmzC2JoWv5wX9YZIqXGx)

Career Conversations, as covered in this skill, are attributed to **Russ Laraway** — Kim's Candor Inc. co-founder, ex-Google, ex-Twitter. He credits Kim; Kim credits him. See his book *When They Win, You Win* for the deeper treatment.

This skill is **not endorsed by Kim Scott, Jason Rosoff, Amy Sandler, or Russ Laraway.** It is Marcos Sponton's structured reading of their public work, built to make Claude or Codex a better thinking partner in the Radical Candor method — and, critically, to resist the weaponization failure mode Kim warns against. If Kim herself (or any of the above) wants to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows with the podcast and Kim's ongoing writing. Especially welcome:

- **New podcast episodes / essays / talks for `author-live-sources.md`** — the podcast ships weekly. Add episodes with topic tag + one-line takeaway + URL.
- **Additional heuristics with attribution** — if Kim has explicitly warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Voice/tone corrections** — if my read of Kim's voice is off, tell me.
- **Failing test cases in `evals/`** — a case where the skill's output softens the Care Personally axis, or lets weaponization through, is data.
- **New cases beyond the recurring roster** — Kim uses many cases in the podcast that aren't in `examples.md` yet.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Radical Candor in my own week and this skill is what falls out.

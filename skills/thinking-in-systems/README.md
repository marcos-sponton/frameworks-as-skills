# Thinking in Systems (Donella Meadows) — an agent skill

An agent skill for **Donella Meadows's systems thinking method** — stocks and flows, feedback loops, delays, bounded rationality, system archetypes, the 12 Leverage Points, and Dancing with Systems as the governing humility posture.

This is not a summary of *Thinking in Systems*. It's a working thinking partner in Meadows's method, built from:

- **Thinking in Systems: A Primer** (Chelsea Green, 2008) — Meadows's **posthumous** book, drafted around 1993 and edited by Diana Wright at the Sustainability Institute for publication seven years after Meadows's death in 2001.
- **Leverage Points: Places to Intervene in a System** (Whole Earth 1997, Sustainability Institute 1999) — Meadows's canonical essay. Arguably better known than the book, most invoked when someone name-drops "Meadows."
- **Dancing with Systems** (1998/99) — the humility companion essay. Non-optional.
- **The Limits to Growth** (1972) and its updates (1992, 2004) — the framework's founding real-world application at planetary scale.
- **Global Citizen columns** (weekly, 1985–2001) — Meadows's public voice.
- The [Academy for Systems Change](https://academyforchange.org/) (formerly the Sustainability Institute Meadows founded in 1996) — the organizational continuation.
- Meadows-lineage practitioners: Diana Wright, Dennis Meadows, Sara Schley, Linda Booth Sweeney, and the modern descendants (Kate Raworth's *Doughnut Economics*, Johan Rockström's planetary boundaries).

**Why this exists.** "Meadows" is one of the most name-dropped and shallowest-applied names in the systems space. Invoke her without a skill and the assistant will parrot the 12 Leverage Points as a list without the ranking's diagnostic point, cite "systems thinking" without the archetypes, or translate her into corporate optimization advice — which strips out the ecological register and the paradigm-level critique that make the method load-bearing. This skill closes that gap. The value is in identifying **which leverage point** and **which archetype** apply to the specific situation on the table — with fidelity to Meadows's own posture: warm about people, precise about systems, humble about control.

**On the posthumous status.** Meadows died in February 2001. She has published nothing since. The book that made her a household name in systems circles came out seven years after her death, assembled from her drafts by Diana Wright. There is no live blog, Substack, X, LinkedIn, or podcast from Meadows — do not fabricate. Modern extensions of her work (planetary boundaries, doughnut economics, degrowth) are the work of practitioners in her lineage; attribute them accurately.

## What's inside

```
thinking-in-systems/
├── SKILL.md                              → activation triggers + when-to-use guide
├── README.md                             → this file
├── references/
│   ├── method.md                         → systems fundamentals; 8 archetypes with escape routes; 12 Leverage Points; Dancing with Systems
│   ├── heuristics.md                     → how to place an intervention on the leverage ladder; archetype-recognition workflow; anti-patterns
│   ├── post-book.md                      → Leverage Points essay (1997/99), Dancing with Systems, Limits to Growth 30-Year Update (2004), Academy for Systems Change, Meadows-lineage practitioners, modern descendants (Raworth, Rockström)
│   ├── author-live-sources.md            → the ARCHIVE (donellameadows.org), organizational continuation (Academy for Systems Change), Meadows-lineage practitioners, adjacent publications; what does NOT exist
│   ├── voice-and-tone.md                 → essayistic, humane, ecosystem-first; everyday example → system insight; what Meadows pushes back on; Dancing-with-Systems humility as method
│   ├── applications.md                   → when the method fits; when it doesn't; relationship to Cynefin, Theory of Constraints, Fifth Discipline, ecological economics, planetary boundaries
│   ├── examples.md                       → the bathtub, thermostat, compound interest, grocery-store oscillation, fisheries collapse, standardized testing, drug policy, corporate quarterly-earnings pressure, Limits to Growth itself
│   ├── prompts.md                        → invocation templates
│   └── sources.md                        → complete traceability
├── examples/                             → longer worked examples (community-contributable)
└── evals/                                → v0 test cases (PRs invited to sharpen)
```

## Install

```bash
# From this repo root:
ln -s "$(pwd)/skills/thinking-in-systems" ~/.claude/skills/thinking-in-systems

# Or in Codex CLI (~/.codex/skills/), Claude Desktop, copy the folder into your skills directory.
```

Once installed, invoke naturally by describing your situation — the assistant picks it up when your task matches the triggers in `SKILL.md`, or when you invoke by name ("use the Thinking in Systems skill", "which leverage point is this?", "which system archetype does this look like?").

## Attribution

**Donella "Dana" Meadows** (March 13, 1941 – February 20, 2001) — American biophysicist, environmental studies professor at Dartmouth College for 29 years, MacArthur Fellow (1994), Pew Scholar in Conservation and Environment (1991), lead author of *The Limits to Growth* (1972, with Dennis Meadows, Jørgen Randers, William Behrens III), author of the weekly *Global Citizen* newspaper column (1985–2001), founder of the **Sustainability Institute** in Hartland, Vermont (1996; now the **Academy for Systems Change**), co-founder of the **Cobb Hill** cohousing / ecovillage community. Died 2001, age 59, from bacterial meningitis.

- **Read the essay first:** [Leverage Points: Places to Intervene in a System](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/) — the single most cited Meadows text. Read it before the book.
- **Then the humility companion:** [Dancing with Systems](https://donellameadows.org/archives/dancing-with-systems/) — non-optional pair with the leverage points.
- **Then the book:** [*Thinking in Systems: A Primer*](https://www.chelseagreen.com/product/thinking-in-systems/) — Chelsea Green, 2008. Posthumous. Edited by Diana Wright.
- **Then the founding case:** [*The Limits to Growth* (1972)](https://donellameadows.org/) — the planetary-scale application that gave the method its urgency.
- **The archive:** [The Donella Meadows Project — donellameadows.org](https://donellameadows.org/) — a project of the Academy for Systems Change.
- **The organizational continuation:** [Academy for Systems Change](https://academyforchange.org/) — formerly the Sustainability Institute.
- **Adjacent publication:** [The Systems Thinker](https://thesystemsthinker.com/) — free online resource in the Senge / MIT system-dynamics tradition; features archived Meadows articles.

Note: Meadows does **not** have a live blog, Substack, X/Twitter, LinkedIn, Mastodon, or podcast. She died in 2001. Do not fabricate.

This skill is **not endorsed by the Meadows estate or by the Academy for Systems Change.** It is Marcos Sponton's structured reading of Meadows's public work and the lineage that carries it. If Diana Wright, Dennis Meadows, or the Academy for Systems Change want to correct or endorse anything here, PRs welcome.

## Contributing

The skill grows through PRs. Especially welcome:

- **Meadows-lineage practitioners publishing today** — Diana Wright, Sara Schley, Linda Booth Sweeney, Academy for Systems Change Fellows, and others extending the work. Add them to `references/author-live-sources.md` with URL and one-line context.
- **Additional worked examples for `examples/`** — cases where the archetype-plus-leverage-point diagnosis produced a clearly better intervention than the default. Include enough context that the pattern is legible.
- **Sharper heuristics with attribution** — if Meadows warned about an anti-pattern that isn't in `heuristics.md`, add it with source.
- **Failing test cases in `evals/`** — a case where the skill's output is thin, corporate-flavored, or misuses the leverage points as a menu is data.
- **Extensions of Meadows's method into modern contexts** — planetary boundaries (Rockström), doughnut economics (Raworth), degrowth literature. Attribute correctly to the modern authors, not to Meadows.
- **Voice / tone corrections** — if the read of Meadows's voice is off (too corporate, too engineering-mechanical, insufficiently humble), flag it.

## Related skills

- **[cynefin](../cynefin/)** — Dave Snowden's sense-making framework (Clear / Complicated / Complex / Chaotic / Confusion). Sits upstream: use Cynefin to sense-make which domain you're in, then use Meadows to diagnose leverage points and archetypes within the Complex or Complicated domain. Note: Snowden has publicly critiqued "systems thinking" as engineering-mechanical — the critique lands hardest on Senge / Fifth Discipline, less on Meadows herself, but the framing tension is real. See `references/applications.md`.
- **[good-strategy-bad-strategy](../good-strategy-bad-strategy/)** — Rumelt's kernel (diagnosis → guiding policy → coherent action). Diagnosis-first strategy. Rumelt's "crux" concept overlaps with Meadows's leverage points — the place where effort produces disproportionate result.
- **[playing-to-win](../playing-to-win/)** — Roger Martin's cascade. Competitive choice, downstream of the systems diagnosis Meadows enables.
- **theory-of-constraints** — Goldratt's applied systems thinking for operations. Tighter tool than Meadows for throughput / bottleneck work in ordered systems. Cross-linked from Meadows's `references/applications.md` — [[theory-of-constraints]] — awaiting its own skill file.

## Skill author

[Marcos Sponton](https://github.com/marcos-sponton) — [LinkedIn](https://www.linkedin.com/in/marcossponton/) · founder of [Prown](https://prown.co). I use Meadows on real decisions and this skill is what falls out.

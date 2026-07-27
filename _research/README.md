# Research dossiers — process material

> Every skill in this repo starts life as a research dossier: a dense, structured extract of the author's live sources, method, voice, and heuristics. The dossier is written by a research subagent following a standard brief (see below) and then hydrated by a build subagent into the actual skill files.
>
> **This directory keeps the dossiers** so the process itself is legible — someone can see how a skill was built, and community contributors can propose new skills by writing a new dossier as PR.

## Files

- `hamilton-helmer.md`
- `melissa-perri.md`
- `bob-moesta.md`
- `april-dunford.md`
- `andy-raskin.md`
- `dave-snowden.md`
- `annie-duke.md`

Each dossier corresponds to a skill in `skills/` (once built). Some dossiers may be here without a built skill yet (queue).

## The standard research brief

Every dossier follows this structure:

1. **Live sources** — every place the author publishes regularly (Substack/Medium/blog, YouTube, podcast propio, LinkedIn cadence, newsletter, podcast appearances). Densely enumerated with URLs and cadence. This is the differential — a skill that doesn't index live sources goes stale fast.
2. **Method in detail** — the framework in the author's own terms, with post-book refinements explicit.
3. **Voice & tone** — how the author actually talks: register, recurring rhetorical moves, signature vocabulary, words they push back on, how they disagree, analogies, how they teach. Voice is part of method, not decoration.
4. **Heuristics / do's / don'ts / gotchas** — practical operational devices, anti-patterns, common misapplications, all with attribution.
5. **Real cases** the author uses publicly.
6. **Relationship to other frameworks** — what the author endorses, critiques, composes with.

Every quote is attributed to a source with URL. Every claim is verifiable.

## The build brief

Once a dossier is ready, a build subagent takes the dossier + the [`_template/`](../_template/) canonical structure + an existing skill (typically Playing to Win) as blueprint and produces:

```
skills/<slug>/
├── SKILL.md
├── README.md
├── references/
│   ├── method.md
│   ├── heuristics.md
│   ├── post-book.md
│   ├── author-live-sources.md
│   ├── voice-and-tone.md
│   ├── applications.md
│   ├── examples.md
│   ├── prompts.md
│   └── sources.md
└── evals/
    └── evals.json
```

## Iterating on this process

The point of keeping dossiers is to improve the process itself. If:

- A dossier missed a live source that the built skill needed → update the research brief.
- A dossier had material that didn't survive translation into skill files → adjust the build brief.
- A skill went stale because the author kept publishing → update the dossier (via `author-live-sources.md` PR).

PRs adding new dossiers (candidate authors), or improving existing ones, are welcome.

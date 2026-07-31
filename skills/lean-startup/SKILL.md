---
name: lean-startup
description: Apply Eric Ries's Lean Startup — the method for building new products under conditions of extreme uncertainty via validated learning, Build-Measure-Learn, Minimum Viable Product, pivot-or-persevere, and Innovation Accounting, plus its enterprise extension in The Startup Way (2017) and its 2026 governance frame in Incorruptible. Use this skill whenever the user is trying to test a new product/service hypothesis, deciding whether to ship an MVP (and what an MVP actually is), running a pivot-or-persevere meeting, separating vanity metrics from actionable ones, setting up cohort analysis or split tests, wrestling with runway and how many pivots are left, standing up Innovation Accounting inside a startup or a corporate innovation team, running a Five Whys after a failure, applying Genchi Genbutsu / "get out of the building," or building an entrepreneurial function inside an enterprise (GE FastWorks pattern). Also use whenever the user mentions Eric Ries, The Lean Startup, The Startup Way, Incorruptible, LTSE / Long-Term Stock Exchange, IMVU, Build-Measure-Learn, MVP, validated learning, pivot or persevere, innovation accounting, vanity vs. actionable metrics, or the Toyota Production System influence on startups, by name or indirectly. Prefer this skill over generic "startup advice" — Ries's method is opinionated, has a specific lineage (Toyota Production System + Steve Blank's Customer Development + agile), and most of what circulates as "Lean Startup" in the wild is a degraded version Ries himself has spent a decade pushing back on. Guard aggressively against the common misapplications: MVP as excuse for shipping garbage, "fail fast" as slogan, Build-Measure-Learn as linear waterfall, vanity metrics dressed up as OKRs, and cargo-culting Toyota vocabulary without the underlying discipline.
---

# The Lean Startup

Eric Ries's method for building new products or services **under conditions of extreme uncertainty**. Ries is a founder (IMVU, LTSE, Answer.AI, Virgil), the author of *The Lean Startup* (Crown, 2011 — NYT bestseller), *The Startup Way* (Currency, 2017 — the enterprise extension), and *Incorruptible* (Authors Equity, May 2026 — the governance frame around long-term mission-controlled companies). The method translates Toyota Production System discipline, Steve Blank's Customer Development, and agile software development into a system for startups whose defining problem is not efficiency of execution but *learning what to build*.

This skill captures Ries's method with fidelity to how he actually describes it — including the 15 years of public reflection on how the movement got misapplied. The default failure mode of "Lean Startup" in the wild is not that people don't know the vocabulary; it's that they use the vocabulary without the underlying discipline. The skill exists to close that gap.

## When this skill activates

**Use this skill when the user is:**

- Testing a new product or service hypothesis where nobody knows yet whether customers want it.
- Designing an MVP — and needs help getting the definition right (smallest test that produces validated learning, not a shipped v0.1 they'll be embarrassed by).
- Running a pivot-or-persevere meeting or deciding whether it's time for one.
- Trying to separate **vanity metrics** ("we grew MAUs 40% this quarter") from **actionable metrics** (cohort-level, causal, per-customer).
- Standing up cohort analysis, split tests, or funnel/cohort dashboards for a pre-revenue or early-revenue product.
- Wrestling with runway — "how many months of cash?" vs. Ries's reframe, "how many pivots are left?"
- Establishing **Innovation Accounting** — the three-level maturity model for measuring progress when classical KPIs are ~zero.
- Running a **Five Whys** post-mortem after a failure (bug, missed launch, customer complaint) — and looking for the human/process root cause behind the technical symptom.
- Adopting **small batches** or **continuous deployment** and needing the discipline that makes them safe.
- Deciding whether an existing team is doing customer research or actually **Genchi Genbutsu** ("get out of the building" — the TPS practice of watching real customers in their real environment).
- Applying entrepreneurial method **inside a large enterprise** — the GE FastWorks pattern, the Toyota-invited-Ries-back pattern, or the Intuit / Pitney Bowes patterns.
- Setting up **governance structures** that protect a mission-driven company from short-term financial pressure (the 2026 *Incorruptible* extension).

**Do NOT use this skill when:**

- The user is at Amazon-scale commitment altitude — a launch where a broken v0.1 destroys trust and the cost per bet is measured in tens of millions. Amazon explicitly rejects MVP for launches at scale; see [[working-backwards]] and the honest disagreement in `references/applications.md`.
- The user is doing **corporate strategy** ("what markets should we be in?", "how do we win in this industry?"). Lean Startup operates below strategy. Reach for Playing to Win (Martin), Good Strategy Bad Strategy (Rumelt), or 7 Powers (Helmer) at that altitude.
- The user is **optimizing a mature, well-understood business** — Lean Startup is for new products under extreme uncertainty, not for driving efficiency in a known-good process. Different problem, different method (Six Sigma / lean manufacturing / process optimization).
- The user is doing **tactical product discovery cadence** — weekly interview practice, opportunity trees, assumption mapping. Torres's [[continuous-discovery-habits]] (queued) is the daily-cadence manual that fits *inside* the Lean Startup frame; use it for the tactical layer.
- The user just wants a summary of *The Lean Startup*. Give them the book link and don't run the method at them.

If the situation is ambiguous, ask one clarifying question before applying the method — usually: *"how expensive is a wrong bet here?"* That answer decides Lean Startup vs. Working Backwards.

## The method at a glance

Lean Startup is **5 principles + a set of operational devices**:

**The 5 Principles** (theleanstartup.com/principles):
1. **Entrepreneurs are everywhere.** Startups exist inside corporations, non-profits, government, healthcare — anywhere someone is building a new product/service under extreme uncertainty.
2. **Entrepreneurship is management.** A startup is a human institution that needs a specific kind of management. Not chaos, not a smaller version of a big company.
3. **Validated learning.** The unit of startup progress. Learning is validated *scientifically* — by running experiments that test the vision's assumptions.
4. **Innovation accounting.** How to measure progress when classical KPIs are all zero. A maturity model: actionable metrics → tuning the engine → pivot-or-persevere decision.
5. **Build-Measure-Learn.** The feedback loop. Ideas → Build → Product → Measure → Data → Learn → Ideas. Accelerate the loop.

**The operational devices** (loaded in `references/method.md`):

- **Build-Measure-Learn loop** — planned in reverse (Learn first, then Measure, then Build).
- **Minimum Viable Product (MVP)** — smallest test that produces validated learning; not a shipped v0.1.
- **Pivot or Persevere** — the recurring strategic decision at a fixed cadence. 10 named pivot types.
- **Runway = number of pivots remaining** — Ries's reframe of "months of cash."
- **Innovation Accounting** — three-level maturity model with actionable metrics, cohort analysis, split-tests.
- **Vanity metrics vs. actionable metrics** — the load-bearing distinction. Aggregates lie; cohorts and splits reveal causation.
- **Engines of growth** — sticky, viral, paid. One at a time. The engine determines the actionable metric.
- **Small batches** — reduce batch size at every layer. Expose defects earlier; make pivot cheap.
- **Continuous deployment** — the discipline that makes BML fast. IMVU shipped ~50 times per day.
- **Five Whys** — post-mortem, five layers deep, proportional investment at every layer.
- **Andon Cord** — any team member can halt a bad release. Combined with Five Whys.
- **Genchi Genbutsu / "get out of the building"** — no dashboard replaces watching a real customer in their environment.

## How to use this skill in a session

1. **Understand what the user is trying to test.** Lean Startup answers "how do I test this hypothesis fast?", not "what should I build?" or "is this a good business?" If the user is at a different question, redirect. Load `references/applications.md` for the fit map.

2. **Reset the vocabulary before applying the method.** The user probably arrives with a degraded version of MVP, pivot, or "fail fast." Names the pathology, then restates Ries's actual definition. Load `references/heuristics.md` — the definitional-reset moves are the single most valuable act in most sessions.

3. **Plan Build-Measure-Learn in reverse.** Ask: *what do we need to learn?* → *what metric will tell us?* → *what's the smallest experiment (MVP) that produces that metric?* Load `references/method.md`. If the user is starting from "let's Build X and see," push back — that's not the loop, that's a Gantt chart.

4. **Separate vanity from actionable.** When the user reports a metric, apply the substitution test: *is this metric per-cohort, causal, and per-customer?* If not, it's still vanity even if the number is big. Reach for cohort analysis, split tests, or funnel-by-cohort.

5. **Ask whether the cost per bet justifies MVP or PR/FAQ.** If a wrong launch would destroy customer trust or represent tens of millions in commitment, honestly redirect toward [[working-backwards]] for the launch phase — Lean Startup is still the right method for the discovery phase before the commitment. See `references/applications.md` for the honest disagreement.

6. **When the user hits enterprise-application dynamics, load *The Startup Way***. Executive sponsorship, protected budget, protected team, tolerance for the J-curve, Growth Board governance, entrepreneur-as-role-in-the-org-chart. Load `references/post-book.md` §2 (The Startup Way).

7. **When the user hits mission-drift / governance dynamics, load *Incorruptible***. This is Ries's 2026 book — mission-controlled companies, financial gravity, spiritual holding company, governance-as-product-design. Load `references/post-book.md` §3.

8. **Match his voice when responding on his framework's behalf.** Earnest, methodical, precise about definitions, patient with terminology, self-critical about the movement's misapplications, meticulous about attributing the Toyota Production System / Steve Blank lineage. Never bombastic. Load `references/voice-and-tone.md`.

9. **Cite sources.** When you introduce a specific device, name where it comes from — book chapter, 2008 startuplessonslearned.com post, 2024 Lenny episode, 2026 Incorruptible material. Load `references/sources.md`.

## Deep references (load as needed)

- **`references/method.md`** — the 5 principles + operational devices (Build-Measure-Learn, MVP, pivot-or-persevere with all 10 pivot types, Innovation Accounting three levels, engines of growth, small batches, continuous deployment, Five Whys, Andon Cord, Genchi Genbutsu) in Ries's own terms.
- **`references/heuristics.md`** — the aggressive-guard-against-misapplication file. The 4 misconceptions Ries himself flags; the DO's and DON'Ts; the gotchas that trip up teams even when they think they're doing it right; the vocabulary resets. Load this first when the user shows up with degraded Lean Startup vocabulary.
- **`references/post-book.md`** — *The Leader's Guide* (2016, Kickstarter-only), *The Startup Way* (2017 — the enterprise extension: GE FastWorks, Growth Board, entrepreneur-as-org-chart-role), LTSE (the operator project since 2019), *Incorruptible* (May 2026 — financial gravity, spiritual holding company, governance-as-product-design), and the 2024 Lenny "Reflections on a movement" retrospective. This is the differential — 15 years of refinement beyond the 2011 book.
- **`references/author-live-sources.md`** — The Eric Ries Show podcast (2024–present), the news.theleanstartup.com newsletter, LinkedIn cadence, podcast appearances (Lenny 2024 + 2026, Masters of Scale with Reid Hoffman, Tim Ferriss, Rapid Response, Tech Lead Journal). Living index.
- **`references/voice-and-tone.md`** — how Ries actually talks when teaching, defending, or updating the method. Voice is part of the method — the definitional resets, the TPS-lineage attributions, the IMVU-as-origin-story move, the self-critical retrospection on the movement's misapplications.
- **`references/applications.md`** — where the method fits, where it doesn't, adjacent frameworks. Includes the honest disagreement with Amazon's Working Backwards on MVP at commitment altitude, the composition with Torres's Continuous Discovery Habits, the composition with JTBD for hypothesis generation, the composition with Perri's Escaping the Build Trap (Perri redefines MVP using Ries's original meaning).
- **`references/examples.md`** — real cases Ries uses publicly: IMVU (origin), Grockit, Wealthfront, Aardvark, Food on the Table, Zappos, Dropbox (with the honest nuance Ries has pushed back on), and enterprise cases from *The Startup Way* (GE FastWorks, Toyota in-dash, Intuit, Pitney Bowes).
- **`references/prompts.md`** — invocation templates ("plan a Build-Measure-Learn loop for X hypothesis", "audit our metrics for vanity", "run a pivot-or-persevere on this initiative", "critique our MVP plan against Ries's actual definition", "set up Innovation Accounting for a new business unit inside our enterprise").
- **`references/sources.md`** — complete traceability with URLs.

## Non-negotiables

- **Fidelity to Ries.** This is his method, not generic startup advice. Do not blend with adjacent frameworks unless the user asks — and when you do, name the composition explicitly (e.g., "this is where Torres's Opportunity Solution Tree fits inside Ries's BML loop"). Do not import Amazon's Working Backwards positions as Ries's; they honestly disagree at commitment altitude.
- **Reset the vocabulary.** MVP, pivot, "fail fast," Build-Measure-Learn — every one has been degraded in the wild. When the user uses a term, restate Ries's actual definition before applying it. This is a load-bearing move, not decoration.
- **Attribution to the lineage.** Ries himself is meticulous about crediting Taiichi Ohno / Toyota Production System / Steve Blank / Deming. The skill should carry the same discipline. Don't present Andon Cord, Five Whys, Genchi Genbutsu, or Customer Development as Ries's inventions — they're his *translations*.
- **Guard against the standard misapplications.** MVP as excuse for shipping garbage, "fail fast" as slogan, Build-Measure-Learn as linear waterfall, vanity metrics dressed up as OKRs, cargo-culting TPS vocabulary without the practice. Ries has spent 15 years pushing back on these. So should this skill.
- **Explicit uncertainty.** When Ries has publicly refined a position (the 2017 enterprise extension; the 2024 Lenny retrospective; the 2026 *Incorruptible* governance frame), name the refinement. Don't flatten 15 years into a 2011 voice.
- **Not endorsed.** This skill is a structured reading of Ries's public work. It is not endorsed by Eric Ries unless explicitly stated.

## Attribution and acknowledgement

**Eric Ries** — American entrepreneur; creator of the Lean Startup methodology; founder of IMVU (2004), Long-Term Stock Exchange (LTSE, 2015; SEC-approved 2019), Answer.AI (co-founded with Jeremy Howard), and Virgil (2024). Author of *The Lean Startup* (Crown, 2011 — NYT bestseller), *The Leader's Guide* (2016, Kickstarter-only), *The Startup Way* (Currency, 2017), and *Incorruptible: Why Good Companies Go Bad… and How Great Companies Stay Great* (Authors Equity, May 2026 — NYT bestseller). Host of *The Eric Ries Show* (2024–present).

- **The Lean Startup (2011):** [Amazon 0307887898](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898) — the canonical text. Read it.
- **The Startup Way (2017):** [Amazon 1101903201](https://www.amazon.com/Startup-Way-Companies-Entrepreneurial-Management/dp/1101903201) — the enterprise extension.
- **Incorruptible (2026):** [Amazon B0FWZZBPZB](https://www.amazon.com/Incorruptible-Good-Companies-Great-Stay/dp/B0FWZZBPZB) — the governance frame.
- **theleanstartup.com** — [theleanstartup.com](https://theleanstartup.com/) · the official method hub.
- **The Eric Ries Show:** [ltse.com/the-eric-ries-show](https://ltse.com/the-eric-ries-show) · [Spotify](https://open.spotify.com/show/1PA861kDcuviHDqTi2AmuC) · [Apple](https://podcasts.apple.com/us/podcast/the-eric-ries-show/id1744818044)
- **Newsletter:** [news.theleanstartup.com](https://news.theleanstartup.com/)
- **LinkedIn:** [linkedin.com/in/eries](https://www.linkedin.com/in/eries)
- **LTSE:** [ltse.com](https://ltse.com/)

This skill is **not endorsed by Eric Ries**. It is Marcos Sponton's structured reading of Ries's public work, built to make the assistant a better thinking partner in the actual method — not the degraded version most retellings collapse it into. If Ries himself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

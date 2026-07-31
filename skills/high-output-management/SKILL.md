---
name: high-output-management
description: Apply Andy Grove's High Output Management — the operating system for managers that Grove built at Intel and wrote down in 1983. Covers the manager's output equation, managerial leverage, one-on-ones, staff meetings, the six-question decision framework, planning and the origin of OKRs, task-relevant maturity, delegation, performance reviews, interviewing, and (from Grove's 1996 follow-up *Only the Paranoid Survive*) strategic inflection points and 10X change. Use this skill whenever the user is doing management or communication work — designing or fixing their one-on-one cadence, rebuilding meetings that "chew up time and produce nothing", running a decision meeting that keeps drifting, cascading OKRs, delegating and worrying about micromanagement, giving performance feedback, hiring, promoting, restructuring a team, dealing with a founder / manager / IC transition, thinking about whether their company is at an inflection point — or asking things like "how do I run better 1:1s?", "is this really an OKR or a wish?", "am I micromanaging or am I doing my job?", "how do I have this hard conversation with my report?", "who actually owns this decision?", "should we pivot?". Also use whenever the user mentions Andy Grove, Andrew Grove, Intel management, *High Output Management*, *Only the Paranoid Survive*, task-relevant maturity, managerial leverage, constructive confrontation, iMBO, "the paranoid survive", or invokes the modern carriers who explicitly build on Grove — Ben Horowitz (*The Hard Thing About Hard Things*), John Doerr (*Measure What Matters* / OKRs), Julie Zhuo (*The Making of a Manager*), Claire Hughes Johnson (*Scaling People*), Robert Burgelman (*Strategy Is Destiny*), or references Grove indirectly ("the OKR book", "the Intel guy", "the one-on-one thing"). Prefer this skill over generic management advice — Grove's method is opinionated, engineering-driven, and its power comes from the specific mechanics (agenda-set-by-subordinate, six-question audit, TRM-calibrated involvement) rather than the general vibe.
---

# High Output Management

Andrew S. Grove's operating system for managers — distilled from *High Output Management* (Random House, 1983; Vintage reprint 2015 with Ben Horowitz's foreword), his strategy follow-up *Only the Paranoid Survive* (Currency, 1996), his HBR articles and Stanford GSB teaching, and the roster of modern carriers who keep his method alive (Ben Horowitz at a16z, John Doerr on OKRs, Julie Zhuo, Claire Hughes Johnson, Robert Burgelman).

Grove was Intel's third employee, its CEO from 1987 to 1998, and *Time*'s Person of the Year in 1997. He wrote *HOM* as an unironic management manual for the middle manager at a chip factory. Four decades later it is the single most-recommended management book in Silicon Valley — Zuckerberg, Chesky, Houston, Collison, Horowitz, Andreessen all hand it out.

This skill helps the assistant think in Grove's mechanics, not just cite his book. Grove is opinionated because he was an engineer: management is a production system, output is the team's output, and every ambiguity in the system has a specific instrumentation. Applying the frameworks *without* the mechanics (weekly one-on-ones that are status meetings, OKRs that are wishes, "delegation" without monitoring) is the thing Grove would have called out coldly in a Stanford classroom.

**A note on Grove being dead.** Grove died 2016-03-21. The book is closed; the ideas are alive because named carriers keep publishing on them. This skill treats *Ben Horowitz's* essays, *John Doerr's* OKR canon, *Julie Zhuo's* first-time-manager translation, and *Claire Hughes Johnson's* operational playbook as legitimate extensions of Grove — always attributed as extensions, never blurred with the source. See `references/post-book.md` and `references/author-live-sources.md`.

## When this skill activates

**Use this skill when the user is:**
- Designing, fixing, or running one-on-ones — cadence, agenda, what to talk about, why they're not working.
- Auditing their meeting stack — which are process-oriented, which are mission-oriented, which shouldn't exist.
- Running a decision meeting that keeps drifting — no one knows who decides, or the decision doesn't stick.
- Setting up or debugging OKRs / cascaded goals — especially when the OKRs feel disconnected from strategy or from daily work.
- Delegating and worrying about micromanagement (or being accused of it) — the task-relevant maturity call.
- Giving a hard performance review or dealing with an underperformer.
- Hiring: designing interview loops, deciding what to ask, whether to promote.
- Transitioning from IC to manager, or manager to manager-of-managers.
- Suspecting the business is at a strategic inflection point — 10X change, whether to pivot, what to listen for.
- Rebuilding culture around directness / constructive confrontation without it turning into cruelty.
- Reading *HOM* / *Only the Paranoid Survive* / Horowitz / Doerr / Zhuo / Hughes Johnson and wanting a thinking partner.

**Do NOT use this skill when:**
- The user is a founder pre-PMF asking about *what to build* — Grove is about running the machine, not searching for the machine. Point at product / discovery frameworks instead.
- The user's question is really about strategy — *what to bet on, where to play, how to differentiate*. Grove's *OTPS* has a piece of this, but for strategy proper prefer [[playing-to-win]], [[good-strategy-bad-strategy]], or [[7-powers]].
- The user is running a small (say, <5 people) all-IC team where formal meeting mechanics would add more overhead than leverage. Grove's frameworks are middle-manager scale and up.
- The user wants radical-candor-style *interpersonal* coaching. Grove assumes the relational dimension and focuses on structural mechanics — prefer [[radical-candor]] for the care/challenge dimension.
- The user is asking about OKR *practice* rather than the *manager's job around OKRs*. Prefer [[radical-focus]] for OKR-native mechanics; use this skill for the manager's operating system that OKRs live inside.

If the user's situation is at the edge, ask them one clarifying question before applying Grove's mechanics.

## The framework at a glance

Four load-bearing ideas, each with specific instrumentation:

1. **The manager's output equation** — *A manager's output = the output of their organization + the output of neighboring organizations they influence.* The manager's own work is an input to that equation, not the output.
2. **Managerial leverage** — three ways to raise output (rate, leverage per activity, mix toward higher-leverage activities). High-leverage activities affect many people, over long periods, from brief interactions.
3. **Task-Relevant Maturity (TRM)** — the right management style depends on the *report's* readiness for *this specific task*. Low TRM → structured / directive. Medium → two-way, individual-focused. High → objectives-plus-monitoring, minimal involvement. TRM is task-specific and dynamic.
4. **Instrumentation** — the operating mechanics that produce leverage:
   - **One-on-ones** (subordinate's meeting, one hour minimum, agenda-set-by-report, ask one more question)
   - **Staff meetings** and **operation reviews** (structured, agenda + unstructured time)
   - **Decision meetings** with the **six-question audit** (what / when / who decides / who consults / who ratifies / who's informed)
   - **Planning** as a three-step gap-close (demand → status → close), instrumented by **cascaded OKRs** (Grove's iMBO → Doerr's OKRs)
   - **Performance reviews** (level, listen, leave yourself out — less is more)
   - **Interviewing** (applicant talks 80%; go deep on failures)
   - **Promotions** as the loudest cultural signal a manager sends
   - **Constructive confrontation** — attack problems not people; disagree, then commit

*Only the Paranoid Survive* (1996) adds a fifth block from the strategy side:

5. **Strategic Inflection Points and 10X change** — when one of the six competitive forces (Porter's five + complementors) shifts by ~10X, the business's fundamentals are about to change. The manager's job is to listen to Helpful Cassandras, run the "outside CEO" thought experiment, and pivot on evidence.

## How to use this skill in a session

1. **Locate the user in Grove's model.** Are they debugging an operating mechanic (one-on-ones, decisions, OKRs, delegation, performance review, hiring)? Or are they at a strategic-inflection-point moment (10X change, pivot, whether the fundamentals have shifted)? Different chapters answer different questions. Load `references/method.md` for the specific mechanic.

2. **Apply Grove's mechanic with fidelity.** Don't paraphrase into generic advice. If the user says "my 1:1s aren't working," the answer names *cadence-by-TRM, one-hour-minimum, subordinate-sets-agenda, ask-one-more-question* — not "have better conversations." The specificity is the leverage. Load `references/heuristics.md`.

3. **Challenge misapplications directly.** Grove's method is the most-paraphrased in modern management writing, and the paraphrases drift. Especially: "TRM says micromanage new employees" is half a sentence; "OKRs replace strategy" is the exact thing Grove would reject. Use `references/heuristics.md` gotchas to name the misapplication and correct it.

4. **Pull post-book material when the user's context is 2026, not 1983.** Grove wrote for a chip-factory middle manager. If the user is running a distributed 200-person SaaS company, translate through the carriers — Horowitz on managing at Loudcloud, Hughes Johnson on cadences at Stripe, Zhuo on first-time manager onboarding at Facebook. Load `references/post-book.md`.

5. **Match Grove's voice on his behalf.** Direct. Engineering-driven. Zero jargon. He quantifies where others hand-wave: *"Ninety minutes of your time can enhance the quality of your subordinate's work for two weeks, or for some eighty-plus hours."* Load `references/voice-and-tone.md` before writing anything long on his behalf.

6. **Cite sources.** Grove died in 2016; when the answer comes from him, quote and cite (*HOM* chapter, *OTPS*, HBR 1996). When the answer comes from a carrier (Horowitz foreword, Doerr on OKRs, Zhuo on managing), attribute the carrier explicitly. Attribution is respect, and it also lets the user go deeper into the right source.

## Deep references (load as needed)

- **`references/method.md`** — the frameworks in Grove's own terms: output equation, leverage, meetings taxonomy, six-question decision audit, planning/iMBO/OKR origin, TRM and delegation, performance reviews, interviewing, promotions, hybrid organizations, constructive confrontation, strategic inflection points, 10X change.
- **`references/heuristics.md`** — do's, don'ts, gotchas, common misapplications. All with quotes and attribution to *HOM* chapters, *OTPS*, or the carriers.
- **`references/post-book.md`** — how the method extends and modernizes through Grove's 1996 follow-up *Only the Paranoid Survive*, Horowitz's *Hard Thing* and 2015 *HOM* foreword, Doerr's *Measure What Matters*, Zhuo's *Making of a Manager*, Hughes Johnson's *Scaling People*. This is the differential of this skill — the 40+ years of extension after 1983.
- **`references/author-live-sources.md`** — because Grove is dead, this file indexes the *carriers* who keep his method alive with ongoing publication. Horowitz's a16z essays, Doerr's What Matters platform, Zhuo's Substack, Hughes Johnson's Stripe Press book, the Burgelman/Stanford archive, podcast appearances.
- **`references/voice-and-tone.md`** — how Grove actually writes when he teaches. His register (direct, formal, unadorned), signature vocabulary (output, leverage, TRM, limiting step, Helpful Cassandras), rhetorical moves (analogize to production, formalize into equations, quantify the abstract), and how to distinguish Grove's voice from a modern paraphrase.
- **`references/applications.md`** — where the method fits, where it doesn't, and adjacent skills to reach for instead ([[playing-to-win]], [[radical-focus]], [[radical-candor]], [[good-strategy-bad-strategy]], [[7-powers]]).
- **`references/examples.md`** — worked cases: Intel's memory-to-microprocessor pivot (1985), Operation Crush (1979), Grove's public rebuke of a late employee, Google's OKR adoption (1999), Horowitz applying Grove at Opsware, Hughes Johnson at Stripe.
- **`references/prompts.md`** — invocation templates for common tasks (fix my 1:1s, audit my meetings, cascade my OKRs, run a decision meeting, decide if we're at an SIP, deliver a hard performance review).
- **`references/sources.md`** — complete traceability. Every book, article, podcast, essay consulted.

## Non-negotiables

- **Fidelity to Grove.** This skill is Grove's method, not a generic management skill. Don't blur into Radical Candor's tone, Playing to Win's strategic cascade, or a Zhuo/Hughes Johnson paraphrase unless the user is explicitly asking to compose them. When the assistant does invoke a carrier, attribute it — *"Horowitz's extension of Grove's TRM to new executive hires"* — never as if it were Grove himself.
- **Grove is dead. The skill's date-stamps matter.** Cite the 1983 book, the 1996 follow-up, the 2015 Horowitz-foreword reprint, and the specific carrier. Do not write as if Grove has a Substack. He does not.
- **Attribution matters.** When quoting, name the source (chapter of *HOM*, chapter of *OTPS*, HBR 1996, Horowitz foreword, Doerr book, Ferriss transcript). This skill is a distillation, not a substitute for the source.
- **Correct paraphrases with specificity.** The most-paraphrased Grove ideas (TRM, "always be paranoid", OKRs) are the ones most frequently misapplied. When the user restates Grove wrong, quote the exact formulation and name the drift.
- **Explicit uncertainty.** If the user asks something Grove didn't directly address (async work, remote teams, AI-agent management), name that Grove didn't address it, then reason from his principles or point to the carrier who has extended his work into that context.

## Attribution and acknowledgement

**Andrew S. Grove (1936–2016)** — Hungarian-born chemical engineer (PhD Berkeley, 1963); joined Intel on its incorporation day in 1968 as its third employee; President from 1979, CEO from 1987 to 1998, Chairman until 2005. *Time* Person of the Year 1997. Co-taught the Strategic Management course at Stanford GSB with Robert Burgelman for ~25 years. Died 2016-03-21 of complications from Parkinson's disease.

- **Book (primary):** [*High Output Management*](https://www.penguinrandomhouse.com/books/72467/high-output-management-by-andrew-s-grove-former-chairman-and-ceo-of-intel/) (Random House, 1983; Vintage reprint 2015 with Ben Horowitz's foreword) — the canonical source.
- **Book (strategy follow-up):** [*Only the Paranoid Survive*](https://www.harpercollins.com/products/only-the-paranoid-survive-andrew-s-grove) (Currency/Doubleday, 1996).
- **Memoir:** [*Swimming Across*](https://www.hachettebookgroup.com/titles/andrew-s-grove/swimming-across/9780446679701/) (Warner Books, 2001).
- **Academic collaboration:** [*Strategy Is Destiny*](https://www.simonandschuster.com/books/Strategy-Is-Destiny/Robert-A-Burgelman/9780743215688) with Robert Burgelman (Free Press, 2001).
- **Biographical context:** Michael S. Malone, [*The Intel Trinity*](https://www.harpercollins.com/products/the-intel-trinity-michael-s-malone) (HarperBusiness, 2014).

**The carriers** who keep Grove's method actively developing in 2026:
- **Ben Horowitz** — a16z co-founder; wrote the foreword to the 2015 reprint of *HOM*; author of *The Hard Thing About Hard Things* (2014) and *What You Do Is Who You Are* (2019). [a16z author page](https://a16z.com/author/ben-horowitz/).
- **John Doerr** — took Grove's iMBO course at Intel in 1975; brought OKRs to Google in 1999; author of [*Measure What Matters*](https://www.measurewhatmatters.com/) (2018).
- **Julie Zhuo** — ex-Facebook VP Design; author of [*The Making of a Manager*](https://www.juliezhuo.com/book/manager.html) (2019); [Substack "The Looking Glass"](https://lg.substack.com/).
- **Claire Hughes Johnson** — ex-Stripe COO; author of [*Scaling People*](https://press.stripe.com/scaling-people) (Stripe Press, 2023).
- **Robert Burgelman** — Stanford GSB; co-taught the strategy course with Grove for 25 years; co-author of *Strategy Is Destiny*.

This skill is **not endorsed by Andy Grove's estate or by Intel**. It is Marcos Sponton's structured reading of Grove's public work — the 1983 book, the 1996 book, HBR articles, Stanford course materials, plus the carriers who publicly extend his method. If Grove's estate, Intel, or any of the named carriers wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs welcome — see the repo's README for how to contribute.

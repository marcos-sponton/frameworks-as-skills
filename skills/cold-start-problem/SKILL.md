---
name: cold-start-problem
description: Apply Andrew Chen's Cold Start Problem — the 5 stages of network effects (Cold Start → Tipping Point → Escape Velocity → Hitting the Ceiling → The Moat), the Atomic Network (the smallest self-sustaining network unit — for Uber it's a single corner at 5pm, not a city), the Hard Side vs Easy Side of a network, Anti-Network Effects (why small networks self-destruct AND why big networks can decay), and Come-For-The-Tool-Stay-For-The-Network launches. Use this skill whenever the user is working on a networked product — marketplace, social network, dating app, collaboration tool, community, creator platform, developer tool, chat, video, live-streaming, multiplayer — and specifically when they are launching pre-critical-mass, stuck in "chicken-and-egg", trying to spin up supply-and-demand at the same time, deciding a launch geography or beachhead, hitting network stall / eternal September / spam ceiling, considering a tool-first launch strategy, or debating defensibility of a network moat. Also use when the user asks things like "how do we get past zero?", "which side of the marketplace do we prioritize?", "should we launch city-by-city or globally?", "why is our marketplace empty?", "we have signups but no engagement", "our network is decaying — why?", or when they invoke Andrew Chen, a16z, The Cold Start Problem, atomic network, hard side, anti-network effects, or "come for the tool stay for the network" by name, even indirectly. Prefer this skill over generic marketplace / network / growth advice — Chen's method is opinionated (atomic networks are smaller than you think, focus on the hard side, networks can decay, viral loops ≠ network effects), and its power comes from resisting the founder reflex to launch big and worry about density later.
---

# The Cold Start Problem

Andrew Chen's Cold Start Problem — the operational playbook for launching and scaling network products (marketplaces, social networks, dating apps, collaboration tools, communities, creator platforms) through the 5 stages of network effects: **Cold Start → Tipping Point → Escape Velocity → Hitting the Ceiling → The Moat**. Distilled from Chen's book *The Cold Start Problem: How to Start and Scale Network Effects* (Harper Business, 2021), his ongoing essays on [andrewchen.com](https://andrewchen.com/) and [andrewchen.substack.com](https://andrewchen.substack.com/), his a16z portfolio commentary, and podcast appearances including Lenny Rachitsky's, Noah Kagan Presents, Intercom, and the a16z podcast. Chen draws heavily on first-person Uber tenure (head of Rider Growth, 15M→100M users) and a16z portfolio visibility that summarizers can't reproduce.

This skill helps your agent think like the operator behind Uber's city launches — narrow, dense, self-sustaining atomic networks; hard-side users solved first; anti-network effects respected on both the launch curve and the ceiling curve. It's opinionated because Chen is opinionated: atomic networks are smaller and more specific than founders think, the hard side is where the leverage is, viral loops are not network effects, and network defensibility is a live discipline, not a static moat.

## When this skill activates

**Use this skill when the user is:**
- Launching a networked product (marketplace, social, chat, dating, community, creator platform, multiplayer, dev tools) and stuck on the chicken-and-egg problem.
- Trying to figure out the beachhead — which city, which campus, which team, which niche — to start from.
- Debating supply-side vs demand-side prioritization on a two-sided marketplace.
- Watching a marketplace with signups but no engagement — empty rooms.
- Diagnosing why a previously growing network has stalled, decayed, been spammed, or drifted into "eternal September".
- Considering a come-for-the-tool-stay-for-the-network launch (single-player value first, network second).
- Being asked "how defensible is our network effect?" in a fundraise or board conversation.
- Deciding whether to launch city-by-city or in one big push.
- Working on a creator / UGC platform and trying to identify who the hard-side users are.
- Post-launch, at scale, wondering whether the ceiling problems are fixable or structural.
- Cloning a competitor's network product and trying to attack their moat (cherry-picking argument).

**Do NOT use this skill when:**
- The product is not a networked product. If value is fully delivered at N=1 with no network layer, use general growth frameworks (Four Fits, JTBD, PMF work) instead.
- The user is pre-PMF for the tool side of a "come for the tool" product. Solve tool PMF first with JTBD / continuous discovery, then apply Cold Start.
- The question is pure marketing tactics (ad creative, copy, channel testing). Cold Start is upstream.
- The user is scaling a SaaS with no network component. Use Balfour's Four Fits instead — see [[four-fits]].
- The user has hit the ceiling and the question is "should we shut down or turn around" — that's a corporate strategy question, not a Cold Start question. Chen's Ceiling chapter helps diagnose *why* growth stalled but doesn't cover post-network-collapse turnaround.

If the user's situation is at the edge (some network, some tool), ask one clarifying question: *does value require other users, or does it deliver at N=1?* — before running the method.

## The framework at a glance

**The 5 stages** — a networked product traverses these in order. Different failure modes at each stage. Different playbook per stage.

1. **Cold Start Problem** — anti-network effects dominate; product feels empty; users churn. Solve by building the first **atomic network**.
2. **Tipping Point** — a repeatable pattern for spinning up atomic networks. Execute it across the market.
3. **Escape Velocity** — network effects flip constructive. Three sub-forces amplify: **Acquisition Effect**, **Engagement Effect**, **Economic Effect**.
4. **Hitting the Ceiling** — growth stalls: saturation, overcrowding, eternal September, spam/fraud, algorithm rot.
5. **The Moat** — network defense as a live discipline (not a static claim). Cherry-picking of the hard side is the main competitive attack; Wimdu-vs-Airbnb is the cautionary case.

**Two concepts that carry most of the leverage:**

- **The Atomic Network** — the smallest self-sustaining network. If you removed everything outside it, it would still generate value for its members and keep growing. Almost always smaller and more specific than the founder thinks. Uber's atomic network is not San Francisco — it's *"5pm at the Caltrain Station at 5th and King Street."*
- **Hard Side vs Easy Side** — every network has one side that creates disproportionate value and is disproportionately hard to acquire and keep. Drivers on Uber, hosts on Airbnb, creators on YouTube, women on Tinder, sellers on Etsy, champions on Slack. Solve the hard side first; you can manufacture the easy side.

## How to use this skill in a session

1. **Confirm this is a network product.** Ask: does value require other users? If no, redirect to a different skill (Four Fits, JTBD). If yes, proceed.

2. **Identify which of the 5 stages the user is in.** Pre-launch or launching = Cold Start. Repeatable playbook forming = Tipping Point. Scaling well = Escape Velocity. Growth stalled = Hitting the Ceiling. Defending against competitor = Moat. The stage determines the playbook. Load `references/method.md` for the full definitions.

3. **If Cold Start stage, force the atomic network small.** The single most common misapplication is defining the atomic network as "the city" or "the company" or "the college" when it should be a corner, a team, or a dorm. Load `references/heuristics.md` — the atomic network sharpener test is there.

4. **Identify the hard side explicitly.** Name who they are, what problem they have, what "hard" means for them (harder to acquire, harder to satisfy, or both). Solve their problem first. Load `references/heuristics.md`.

5. **When the user talks about "network effects" as a defensive claim without evidence, push back.** Chen's post-book essays argue networks are less defensible than commonly claimed. Ask: what's the density inside the atomic network? Who is the hard side and are they staying? What would a cherry-picker do? Load `references/post-book.md`.

6. **When the topic is stalling / decay / eternal September, treat anti-network effects as bidirectional.** Same physics that kills a small network can kill a large one. Load `references/method.md` (Ceiling section).

7. **When the launch strategy is "come for the tool, stay for the network", verify the tool has real N=1 value.** If the tool is a network product in tool clothing, users won't stick and the network never activates. Load `references/heuristics.md`.

8. **Match Chen's voice.** Operator-VC. First-person Uber examples when they fit. Cite specific companies with specific mechanisms (Slack's 3-person team, Tinder's 5% swipe rate, Uber's power drivers = 20% of supply / 60% of trips). Load `references/voice-and-tone.md`.

9. **Cite sources.** When you introduce a specific device — atomic network, hard side, anti-network effects, eternal September, come-for-the-tool — name the chapter of *The Cold Start Problem* or the specific essay so the user can go deeper.

## Deep references (load as needed)

- **`references/method.md`** — the 5 stages in depth, the atomic network in Chen's own language, hard side vs easy side, anti-network effects (both directions), the 3 sub-forces of escape velocity, ceiling failure modes, and the network-moat argument.
- **`references/heuristics.md`** — do's, don'ts, gotchas, pro tips, anti-patterns. The atomic-network-sharpener test lives here — the single most important operational device in the skill.
- **`references/post-book.md`** — material Chen has published AFTER the 2021 book: AI + network effects, Agents-for-X vs Copilot-for-X, consumer AI defensibility, gaming / Speedrun thesis, updated Wimdu-style cherry-picking argument, ongoing Substack essays. This is the differential of the skill.
- **`references/author-live-sources.md`** — index of every place Chen publishes regularly (andrewchen.com, Substack, a16z, Twitter/X, podcast circuit). When the user has a specific situation, jump to the matching essay or episode.
- **`references/voice-and-tone.md`** — how Chen actually talks. Operator-VC register, first-person Uber authority, specific-example-per-abstract-concept rhythm, and the phrases he pushes back on ("we have network effects" as a defensibility claim, viral loop ≡ network effect confusion).
- **`references/applications.md`** — where the Cold Start Problem fits, where it doesn't, adjacent frameworks (Four Fits, 7 Powers, Crossing the Chasm, JTBD, Rumelt) and when to reach for each.
- **`references/examples.md`** — real cases Chen uses publicly (Uber, Airbnb, Tinder, Slack, Dropbox, PayPal, Instagram, Zoom, Facebook, LinkedIn, Clubhouse, Wimdu, Reddit, YouTube).
- **`references/prompts.md`** — invocation templates: sharpen the atomic network, identify the hard side, diagnose the stage, come-for-the-tool audit, ceiling diagnosis, moat pressure test.
- **`references/sources.md`** — everything consulted, with links.

## Non-negotiables

- **Fidelity to Chen.** This is Chen's framework, not a generic network / marketplace skill. Don't blend with McClure's AARRR, Metcalfe's Law, Reed's Law, or generic "network effect" folklore.
- **Atomic networks are small.** If the atomic network sounds "just right", it's still too big. The default move is smaller. Push back on any atomic-network definition at city / company / campus scale — Chen's own examples are corners / teams / dorms.
- **Hard side comes first.** Don't rubber-stamp a plan that focuses on the easy side (the freeloaders, viewers, buyers) before the hard side is solved. Redirect.
- **Viral loop ≠ network effect.** These are different. A viral loop is an acquisition mechanic. A network effect is value that scales with participation. They can coexist; they're not interchangeable. Push back when the user uses them as synonyms.
- **Network effects are not a permanent moat.** Chen's own case (Wimdu, Clubhouse, MySpace, Yahoo) is that networks decay and can be cherry-picked. Don't let the user hide behind "we have network effects" as a defensibility claim without evidence.
- **Attribution.** When quoting Chen, name the source — chapter of the book, specific essay, podcast episode.
- **Explicit uncertainty.** When Chen has updated his position on Substack post-book (AI + network effects, agents), name that this is post-2021 material. When the situation matches a specific essay, cite it and offer to WebFetch it.
- **Voice guard.** Push back explicitly on: "we have network effects" (as unsubstantiated moat claim), "we just need to launch in a big city", "we'll figure out supply later", "viral loop = network effect", "our network is defensible".

## Attribution and acknowledgement

**Andrew Chen** — General Partner at [Andreessen Horowitz (a16z)](https://a16z.com/) leading Consumer / games / entertainment / AI and the a16z Speedrun accelerator. Previously head of Rider Growth at Uber (2015–2018) during the scale from ~15M to ~100M users. Author of ~650+ essays on [andrewchen.com](https://andrewchen.com/) (2007–now, now primarily on [Substack](https://andrewchen.substack.com/)). Co-author (with Brian Balfour, Casey Winters, Kevin Kwok) of the 2018 *Growth Loops Are the New Funnels* essay.

- **Book:** [*The Cold Start Problem: How to Start and Scale Network Effects*](https://a16z.com/books/the-cold-start-problem/) (Harper Business, December 2021). Read it.
- **Personal site + essay archive:** [https://andrewchen.com/](https://andrewchen.com/)
- **Substack (primary current channel):** [https://andrewchen.substack.com/](https://andrewchen.substack.com/)
- **a16z page:** [https://a16z.com/author/andrew-chen/](https://a16z.com/author/andrew-chen/)
- **Twitter/X:** [@andrewchen](https://x.com/andrewchen)
- **LinkedIn:** [https://www.linkedin.com/in/andrewchen/](https://www.linkedin.com/in/andrewchen/)
- **Lenny Rachitsky's summary of the Atomic Network:** [lennysnewsletter.com/p/atomic-network](https://www.lennysnewsletter.com/p/atomic-network)

This skill is **not endorsed by Andrew Chen or a16z**. It's Marcos Sponton's structured reading of Chen's public work, built to make the assistant a better thinking partner in Chen's method. If Chen himself wants to correct or endorse anything here, PRs welcome.

- **Skill maintained by:** [Marcos Sponton](https://github.com/marcos-sponton). Feedback, corrections, and PRs are welcome. See the repo's README for how to contribute.

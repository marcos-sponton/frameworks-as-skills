# The Cold Start Problem — Worked examples

> Cases Andrew Chen has used publicly to illustrate the framework. Each case names the source (book chapter, essay, podcast) so the user can verify. Structured so the assistant can pull the case that matches the user's situation.

## Case index by situation

| If the user is working on... | Reach for... |
|---|---|
| Hyperlocal marketplace launch (city-by-city) | **Uber** |
| Two-sided marketplace with SEO | **Airbnb** |
| Dating app with sharp hard-side asymmetry | **Tinder** |
| B2B collaboration / viral team-invitation | **Slack** |
| Come-for-the-tool referral loop | **Dropbox** |
| Manufactured atomic network via paid referral | **PayPal** |
| Come-for-the-tool with feed-network layered on | **Instagram** |
| Freemium tool with 2-person atomic network | **Zoom** |
| Invite-only college-by-college expansion | **Facebook** |
| Invite-only professional network | **LinkedIn** |
| Ceiling / eternal-September case | **Clubhouse** |
| Cherry-picking-neglected-the-hard-side failure | **Wimdu** |
| Ceiling / overcrowding / algorithm curation | **Reddit** |
| Creator platform hard-side dynamics | **YouTube**, **Twitch**, **TikTok** |
| Network product with weak defensibility | **MySpace** (historical anti-example) |
| Manufactured atomic network at accelerator scale | **a16z Speedrun** (Chen's own) |

## Uber — the anchor case across the whole framework

**Where Chen uses it:** *The Cold Start Problem* throughout (Chen's own first-person source); Stripe Atlas marketplaces essay; multiple podcasts; a16z Podcast "Kickstarting Network Effects."

**Which stages:** all 5. Chen's own operator experience covers Cold Start (early cities), Tipping Point (city-launch playbook), Escape Velocity (rider growth 15M → 100M), Ceiling (regulatory + saturation), Moat (ongoing driver retention against Lyft, Bolt, Didi).

**Atomic network:** NOT San Francisco. NOT "the Bay Area." It was **"5pm at the Caltrain Station at 5th and King Street"** — a specific corner, a specific time, enough drivers cruising to give a plausible ETA. Internal ops tool "Starcraft" coordinated drivers around narrow moments.

**Hard side:** drivers. Uber's power drivers = **~20% of supply, ~60% of trips.** Hard problem: idle time = lost income. Uber's dispatching algorithm optimizes to minimize idle time.

**Easy side:** riders. Manufactured with subsidies, in-app promotions ("Uber Ice Cream" localized launches), price cuts.

**Tipping point playbook:** city-launch teams with a codified playbook — hire local GM, seed supply with driver bonuses, spike demand with promos, repeat.

**Ceiling failure modes:** regulatory (multiple markets), saturation in mature cities, power-driver retention against competitors.

**Chen's line:**
> "Uber's early atomic networks were not cities... '5pm at the Caltrain Station at 5th and King Street' is more accurate."

**Instructive:** the marketplace atomic network is HYPERLOCAL. Founders systematically overscope. Chen's Uber-Caltrain is the canonical calibration point.

---

## Airbnb — two-sided marketplace, SEO loop, host as hard side

**Where Chen uses it:** *The Cold Start Problem* Moat chapter (Wimdu comparison); Stripe Atlas marketplaces essay; multiple podcasts.

**Atomic network:** enough listings **per city** that a searching traveler finds a plausible match — hundreds of listings, not thousands. Not the whole global platform.

**Hard side:** hosts. Getting people to list their homes was harder than getting people to search for accommodations. Airbnb designed for host onboarding (photography services, pricing tools, calendar integration, guest vetting).

**Cold Start launch tactic:** Craigslist cross-posting (famously). Manufactured demand from an existing network.

**Moat argument:** Airbnb won Europe against Wimdu because Airbnb had stronger hard-side quality (host vetting, community, support). Wimdu had funding but neglected hosts. Networks that neglect the hard side collapse.

**Instructive:** in most marketplaces, supply IS the hard side. "Figure out supply later" is the death sentence Chen has warned against.

---

## Tinder — hard side as women, hard problem as harassment risk

**Where Chen uses it:** *The Cold Start Problem* Ch. 8 "Solve a Hard Problem" (posted publicly on andrewchen.com).

**Atomic network:** a **college campus** — originally USC / SMU parties in LA. Enough young singles in one place that swiping produces matches within days. Not "the whole city."

**Hard side:** **women.** Women swipe on ~5% of profiles. The 95% of matches concentrated in 5% of swipes = extreme power-law dynamics.

**Hard problem:** harassment risk from unsolicited messages. Earlier dating sites felt like "work" and exposed women to unwanted contact. Tinder's structural fix:
- **Swipe mechanic** — women choose who they engage with; low-friction rejection.
- **Match-required-to-message** — no unsolicited messages before mutual interest.
- **Facebook integration** — trust signals + mutual friend verification.
- **GPS location** — nearby users only.
- **In-app messaging** — unmatching disables further contact.

**Chen quote (via Sean Rad, Tinder co-founder):**
> "Tinder was different — it made dating fun. You could sign up without filling in a bunch of forms."

**Instructive:** the hard side (women) had a specific hard problem (harassment / friction / trust). Tinder solved it structurally, not with UX polish. This is what Chen means by "solve a hard problem."

---

## Slack — B2B viral, team as atomic network

**Where Chen uses it:** *The Cold Start Problem*; Lenny Rachitsky Atomic Network summary; multiple essays.

**Atomic network:** a **single team of ~3 people** inside one company sending enough messages to keep the room alive. NOT "the company." A team.

**Hard side:** the **champion / power user** who brings Slack into the team and pulls colleagues in. The hard problem: getting colleagues to switch from email + existing chat tools.

**Cold Start solved via:** super-slick single-team onboarding, integrations that made Slack immediately useful (GitHub, JIRA, etc.), viral invitation mechanic (once one team was in, they invited across companies).

**Escape velocity mechanics:**
- **Acquisition Effect:** teams invite adjacent teams inside the same company; companies invite external collaborators.
- **Engagement Effect:** deeper feature use (channels, integrations, threads) as team density grows.
- **Economic Effect:** per-seat pricing scales with team expansion.

**Instructive:** the atomic network in B2B is the *team*, not the company. Companies with one Slack team that dies are common; companies with several dense teams win.

---

## Dropbox — come-for-the-tool, referral loop

**Where Chen uses it:** *The Cold Start Problem* Ch. on Come-for-the-Tool; multiple essays.

**Atomic network:** manufactured via **demo video on Hacker News** — spike in single-player-tool users (file sync across your own devices) created enough density that shared-folder network effects could form on top.

**Come-for-the-tool:** file sync solo utility → shared folders network. Real N=1 value in the tool.

**Referral loop:** paired storage bonus (both parties get more storage). This is a viral loop, layered on top of the come-for-the-tool foundation.

**Chen's honest caveat:** many Dropbox users joined as solo tool users and never engaged in sharing. But users who used sharing were significantly more valuable — the network layer, when it activated, drove the compounding.

**Instructive:** come-for-the-tool works when the tool has real N=1 value (Dropbox did). Cosplay come-for-the-tool (network product in tool clothing) doesn't.

---

## PayPal — manufactured atomic network via $5 referral

**Where Chen uses it:** *The Cold Start Problem* Ch. on Cold Start launches.

**Atomic network:** manufactured via **$5 for referrer + $5 for referee** — extraordinary CAC economics as a one-time investment to reach critical density on eBay.

**Hard side:** eBay power sellers. PayPal solved their payment friction; once power sellers used PayPal, buyers followed.

**Instructive:** the first atomic network can be manufactured at extraordinary cost. That cost is a bootstrapping investment, not a scalable channel. PayPal's $5 bounty was not "the PayPal acquisition strategy" — it was "the way we punched through the cold start."

---

## Instagram — come-for-the-tool (photo filter → feed network)

**Where Chen uses it:** *The Cold Start Problem* Come-for-the-Tool chapter.

**Come-for-the-tool:** photo filter tool (better Hipstamatic). N=1 value — take a filtered photo, share externally (Facebook, Twitter). Sharing to Facebook created a soft distribution channel that fed users into the tool.

**Network layer added later:** internal feed, follows, hashtags, discover.

**Instructive:** the tool must be genuinely useful at N=1. Instagram's filter was. The network layer became the moat, but it wasn't required for launch.

---

## Zoom — 2-person atomic network

**Where Chen uses it:** *The Cold Start Problem*; multiple podcasts.

**Atomic network:** **2 people.** A single one-to-one video call has value. This is the smallest atomic network Chen cites in the book.

**Cold Start:** freemium — free tier with 40-minute call limit. Enough to demonstrate value at N=2 without cost pressure.

**Escape velocity:** COVID-era (2020) massive acceleration.

**Instructive:** if the atomic network is 2 people, the product has structural advantage — every new user finds a plausible partner instantly.

---

## Facebook — one dorm, then one campus

**Where Chen uses it:** *The Cold Start Problem*.

**Atomic network:** originally **one dorm at Harvard**. Then one campus. Then invite-only expansion to other Ivies. Then broader.

**Cold Start playbook:** invite-only exclusivity + campus-by-campus expansion. Density inside a campus was more valuable than dilute presence across many campuses.

**Instructive:** even Facebook — later 3B+ users — started with one dorm. Founders scoping "we'll launch to college students" as the atomic network are still 100x too big.

---

## LinkedIn / Gmail — invite-only launch

**Where Chen uses it:** *The Cold Start Problem* Ch. on invite-only strategies.

**Atomic network:** LinkedIn = founders' networks (professionals in tech / Silicon Valley). Gmail = Google employees + invited early users.

**Cold Start playbook:** invite-only preserves density and quality during the cold-start phase. Scarcity signals value; invited users have a soft social obligation to engage.

**Instructive:** invite-only is one of the manufactured-atomic-network moves. Extreme selection preserves the hard side's quality.

---

## Clubhouse — cautionary case (ceiling / eternal September / hype cycle)

**Where Chen uses it:** post-book Substack + podcast commentary. a16z was an early investor.

**Trajectory:** hit escape velocity in 2020 (COVID + audio-first + celebrity guests) → hit the ceiling hard on eternal September (mainstream audience diluted the tech-conference-hallway feeling that made early Clubhouse special) + creator burnout (rooms became work, not organic conversations) + platform-shift (Twitter Spaces, LinkedIn Live copied fast).

**Which failure modes:** eternal September + power-user burnout + platform-shift competition. Multiple ceiling modes stacked.

**Instructive:** even a portfolio company Chen was close to hit the ceiling brutally. Escape velocity does not guarantee moat.

---

## Wimdu — cautionary case (cherry-picking neglected the hard side)

**Where Chen uses it:** *The Cold Start Problem* Moat chapter.

**Trajectory:** heavily funded Airbnb clone in Europe. Threw money at both sides. Neglected quality of the hard side (hosts) — no vetting, no community, no support. Bad hosts → bad guest experiences → guests churn → hosts churn → network collapses.

**Instructive:** the *strategy* Wimdu attempted (attack an incumbent via replication + funding) is the wrong shape. The strategy that actually works against incumbent networks is **cherry-picking the hard side** — peel off the top hosts / creators / drivers with better economics or better product for them specifically. Wimdu targeted the easy side and failed.

**Chen's takeaway on defense:** watch hard-side health obsessively; cherry-picking is silent and fast.

---

## Reddit / Yelp — UGC / SEO ceiling dynamics

**Where Chen uses it:** *The Cold Start Problem* Ceiling chapter.

**Trajectory:** UGC + Google indexing drove long compounding growth. Hit ceiling modes over time — overcrowding (too many subreddits, hard to discover), eternal September (mainstream audience diluted early community — Reddit's Digg-refugee community was distinctive), spam / bot content (moderation burden), power-user burnout (mod exodus 2023).

**Ceiling fixes deployed:**
- Algorithmic feed curation (personalized ranking).
- Sub-network structures (subreddits, private communities).
- Trust systems (karma, moderation tools, ban systems).

**Instructive:** UGC / SEO networks compound long and then hit multiple ceiling modes simultaneously. The re-engineering (algo + sub-networks + trust) is where Ceiling-stage products earn survival.

---

## YouTube / Twitch / TikTok — creator platform hard-side dynamics

**Where Chen uses it:** across essays + a16z portfolio commentary.

**Hard side:** creators. Power-law extreme — top 1% of creators = majority of watched content.

**Cold Start:** each of these platforms manufactured the first creator networks via seeding (YouTube paid partners, Twitch Amazon partnerships, TikTok algorithmic push for new creators).

**Ceiling modes:** creator burnout (economics don't sustain participation), algorithm dependency (creators complain about opaque algo changes), platform-shift risk (creators move to whichever platform pays best or discovers them fastest).

**Instructive:** creator platforms live and die on hard-side economics. When creators can't make a living, the network collapses even if viewer numbers stay high.

---

## a16z Speedrun — Chen's live experiment in manufactured atomic networks

**Where Chen uses it:** a16z posts + podcast commentary.

**The situation:** Chen leads Speedrun accelerator at a16z. Cohorts of ~60 companies. Started in gaming; expanded to tech / entertainment / AI by 2025.

**Cold Start applied to accelerator design:** Speedrun IS a manufactured atomic network of ~60 founders per cohort. The alumni network compounds with each cohort. Chen has publicly said the value of Speedrun grows with alumni density.

**Hard side:** the founders themselves — they generate the case studies, war stories, referrals, and pattern language that make the network valuable to future cohorts.

**Instructive:** Cold Start thinking applies to accelerator design, community building, cohort programs. Not just consumer products.

---

## Cross-case pattern: atomic networks are always smaller than founders think

Chen's repeated pattern across cases: Uber = one corner, Slack = 3 people, Zoom = 2 people, Facebook = one dorm, Tinder = one campus, Airbnb = hundreds of listings per city. **In every case, the atomic network is orders of magnitude smaller than the "obvious" launch scope.**

**When the user says "our atomic network is [big thing]":** apply the sharpener test. Cut it in half. Cut it again. Cite Uber-Caltrain as the calibration.

## Cross-case pattern: cherry-picking is the main competitive attack

Chen's repeated pattern in the Moat chapter: incumbents rarely get displaced by identical-shape clones (Wimdu failed against Airbnb). They get displaced by attackers who cherry-pick the hard side (better creator economics on new platform, better driver bonuses from Lyft / Didi / Bolt, better host tools from vertical marketplaces).

**When the user says "we have network effects, we're defensible":** ask what happens if a competitor peels off their top 20% of the hard side.

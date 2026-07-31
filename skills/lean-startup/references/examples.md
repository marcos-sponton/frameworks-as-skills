# The Lean Startup — Examples

> Real cases Eric Ries uses publicly, with the underlying pattern each case teaches. Includes the **honest nuance Ries has publicly pushed back on** for cases the wider industry has flattened (Dropbox especially).

## Origin case: IMVU (2004–~2007)

**Ries's own company** and the origin proof of the whole method.

**Setup:** Ries co-founded IMVU in 2004 with Will Harvey. IMVU built 3D animated instant-messaging avatars. Steve Blank, an IMVU investor, required IMVU executives to audit his Customer Development class at UC Berkeley. Ries picked up Blank's method of fast customer feedback and applied it inside IMVU alongside lean software development (small batches, continuous deployment, unit testing).

**The wrong first product:** IMVU spent months building a 3D chat add-on for existing IM networks (AIM, Yahoo Messenger, etc.). They shipped ~40,000 lines of code. **Customers didn't want it.** They wanted a standalone product where they could actually meet new people.

**The pivot:** IMVU threw away the 40k lines of code and rebuilt as a standalone product. Customer-need pivot.

**The deployment cadence:** IMVU deployed to production **~50 times per day** — highly unusual in 2004–2007. Backed by unit tests, continuous integration, monitoring, and Five Whys post-mortems.

**Result:** grew to ~$10M revenue by 2007. IMVU still exists (2026).

**Pattern this case teaches:**
- The first product hypothesis is usually wrong.
- Customer development + small batches + continuous deployment enable fast pivots.
- Ries's authority comes from having made these mistakes personally.

**Source:** *The Lean Startup*, prologue and chapter 3; [Steve Blank SiriusXM Ch 111 Episode 2 (2015)](https://steveblank.com/2015/07/07/episode-2-on-sirius-xm-channel-111-eric-ries-and-jon-sebastiani/); [Shortform IMVU history](https://www.shortform.com/blog/imvu-history-eric-ries-lean-startup/).

## Grockit (GRE / GMAT test prep, ~2007–2013)

Used by Ries as an early case for **cohort analysis and split-testing under uncertainty**. Grockit built adaptive test prep software; the team ran extensive per-cohort experiments to isolate which features moved actionable metrics vs. which felt effective but weren't.

**Pattern:** cohort analysis + split tests as the workhorse of Innovation Accounting.

**Source:** *The Lean Startup*, chapter 7.

## Wealthfront (formerly kaChing, ~2008–2011)

**The pivot:** started as **kaChing**, a virtual stock-trading game where users could follow simulated portfolios. Pivoted to **Wealthfront**, real automated wealth management. **Customer-need pivot** (kept the user segment — retail investors — but changed the problem being solved).

**Pattern:** the same customer can have a different problem worth solving than the one you initially served. Pivot on axis, not on everything at once.

**Source:** *The Lean Startup*, chapter 8.

## Aardvark (social Q&A, 2007–2010, acquired by Google)

**Wizard of Oz MVP** — the founders manually routed early questions to answerers via IM before building any automation. The "app" appeared automated to users; humans were behind the curtain making it work.

**Purpose:** validate demand for social Q&A without building the routing infrastructure. If users cared, build the automation. If they didn't, walk away with weeks of learning instead of years of engineering.

Aardvark got demand signals, built the automation, and was acquired by Google in 2010.

**Pattern:** MVP does not require code. When the hypothesis is "will people use this service?", the smallest test is often to provide the service manually to a small set of users.

**Source:** *The Lean Startup*, chapter 6; widely cited in lean-startup canon.

## Food on the Table (~2008–2012)

**Concierge MVP** — the founders **literally showed up at customers' houses with meal plans**. No app. No software. Manual concierge service delivered to a small set of users, so the founders could learn what worked in the value proposition before building anything.

Later scaled into a software product once the underlying service was validated.

**Pattern:** concierge MVP. Deliver the value proposition by hand to a tiny set of users; learn what actually matters; build only what the manual delivery proved was necessary.

**Source:** *The Lean Startup*, chapter 6.

## Zappos (~1999, pre-book but canonical Lean Startup case)

**Landing-page-first MVP.** Nick Swinmurn photographed shoes at local Bay Area shoe stores, listed them on a website, and when someone bought a pair, he'd walk back to the store, buy the shoes at retail, and ship them. **Zero inventory. Zero warehouse. Zero fulfillment infrastructure.**

**Purpose:** validate the hypothesis that customers would buy shoes online, before building any of the operational infrastructure.

Once demand was validated, Zappos built the operational business. Sold to Amazon in 2009 for $1.2B.

**Pattern:** the smallest test that produces validated learning is often a landing page with a real transaction, not a v0.1 product.

**Source:** *The Lean Startup*, chapter 3; 2024 Lenny "Reflections on a movement" retrospective.

## Dropbox (~2007–2008) — with the honest nuance Ries has pushed back on

**The famous story:** Drew Houston made a **3-minute explainer video** showing how Dropbox would work. He posted it. Email signups on the beta list spiked from ~5,000 to ~75,000 overnight. This became a canonical MVP story.

**The honest nuance Ries has publicly pushed back on:** Houston built real product too. The video was the **demand-validation piece**, not "the entire MVP for a year." The story became more monolithic in the retelling than it was in reality. The video worked as a specific test for a specific hypothesis (would people sign up for a cloud-sync product?) — it was not the whole product-development approach.

**Why the nuance matters:** teams reading "Dropbox was an MVP video" often conclude "we should make a video and call it a day." That's the misapplication. The right read is: **for the specific hypothesis "will people sign up?", a video was the smallest test that produced the answer.**

**Pattern:** the MVP is scoped to a specific hypothesis, not to "the whole product for a year." Multiple hypotheses require multiple MVPs.

**Source:** *The Lean Startup*, chapter 6; [2024 Lenny retrospective](https://www.lennysnewsletter.com/p/reflections-on-a-movement-eric-ries) for the pushback context.

## Enterprise cases from *The Startup Way* (2017)

### GE FastWorks (2012–~2018+, partially unwound post-Immelt)

Ries's canonical enterprise proof. See `post-book.md` §2 for the full case. Highlights:

- CEO Jeff Immelt sponsored the transformation.
- Viv Goldstein and Janice Semper co-led with Ries and David Kidder.
- Trained the top 5,000 GE leaders.
- Growth Board governance installed at multiple business units.
- **One gas turbine developed 2 years faster and ~40% cheaper** than GE's traditional process.
- **300+ initiatives influenced by 2015.**
- Ethnographic-research-led neonatal incubator for Indian clinics.
- Later expanded to FastWorks Everyday across HR, legal, finance.
- **Partially unwound after Immelt's departure** — validating Ries's 2026 *Incorruptible* thesis that governance surviving executive transition is what protects the method.

**Pattern this case teaches:**
- Lean Startup works in enterprises when the scaffolding is right (executive sponsorship, protected budget, Growth Board, tolerance for the J-curve).
- **Without governance surviving executive transition, the method is at the mercy of whoever's in charge this year.** Bridge from *The Startup Way* to *Incorruptible*.

**Source:** *The Startup Way*, chapters 5–8; [FastWorks retrospective on leanstartup.co](https://leanstartup.co/resources/articles/fastworks-reflecting-origin-evolution/); [Collective Campus case study](https://www.collectivecampus.io/blog/how-ge-saved-80-in-development-costs).

### Toyota (in-dash electronics system, ~2015)

**Toyota itself asked Ries to help apply Lean Startup principles to a new in-car electronics system.** The framework Toyota gave the world (Toyota Production System) returned to Toyota through Ries's translation to startups.

**Pattern:** the TPS-derived Lean Startup translates back to Toyota when applied to a new-product-under-uncertainty problem inside a company otherwise expert at known-process execution.

**Source:** *The Startup Way*; multiple Ries podcast appearances.

### Intuit

Chairman Brad Smith publicly endorsed *The Startup Way*. Intuit uses variants of the method for internal innovation.

### Pitney Bowes

One of the four year-long transformation clients Ries names in book publicity around *The Startup Way*.

### Amazon, Facebook, Airbnb, Twilio

Cited more lightly in *The Startup Way* as tech-native examples of the entrepreneurial-management pattern.

**Note on Amazon specifically:** while Ries cites Amazon as a case of entrepreneurial management at scale, Amazon *itself* has a distinct product methodology (Working Backwards / PR-FAQ) that explicitly rejects MVP for launches at commitment altitude. See `applications.md` for the honest disagreement.

## Cases from *Incorruptible* (2026)

The book's cases are largely mission-controlled organizations contrasted against companies "surgically deboned" post-IPO or post-acquisition. Named cases are dispersed across the book; podcast interviews from May–July 2026 name several by category:

### Patagonia (the 2022 restructuring)

The most-cited case in the *Incorruptible* cycle. In 2022 Yvon Chouinard restructured Patagonia so that the Chouinard family gave away ownership: all non-voting stock (~98%) transferred to the **Holdfast Collective**, a climate-focused non-profit; voting stock transferred to the **Patagonia Purpose Trust** to protect the mission. Ries treats this as an operational instance of a "spiritual holding company."

**Pattern:** the mission is owned by a structure separate from the operating entity, insulated from short-term shareholder pressure.

### LTSE listings (Twilio, Asana)

Twilio and Asana **dual-listed on LTSE in August 2021**, adopting LTSE's long-term governance commitments (long-term voting weight, restrictions on short-term-oriented compensation, mandatory disclosure of long-term operating strategy).

**Pattern:** companies making a public governance commitment to long-term operating principles.

### Founder-ousting patterns (implicitly)

*Incorruptible* uses category-level rather than name-and-shame patterns for founder-ousting cases, but the podcast cycle references Sam Altman / OpenAI (2023) and older cases (Jobs / Apple, Musk-style board tensions) as examples of governance-design failure.

**Pattern:** if the mission is defended by a specific founder rather than by governance, the mission is one boardroom vote away from being abandoned.

## Additional cases from Ries's podcast and interviews (2024–2026)

Cases surfaced through *The Eric Ries Show* guests and 2024–2026 interviews:

- **Asana (Dustin Moskovitz)** — mission-driven scaling; LTSE-listed since 2021.
- **Gumroad (Sahil Lavingia)** — bootstrapped alternative operating model; radical transparency; small-team.
- **Duolingo (Luis von Ahn)** — mission-driven product at scale; free-tier commitment as mission-protection.
- **Devoted Health (Todd Park)** — healthcare mission at scale.
- **Craigslist (Craig Newmark)** — decades of resisting the pull of extraction.
- **iRobot (Rodney Brooks)** — technology ethics; long-run robotics.
- **Slack (2024 Lenny retrospective mention)** — Ries has referenced as an example of pivoting from a failed game (Glitch) to a communication product. Zoom-out-then-zoom-in pivot pattern.
- **Pinterest (2024 Lenny retrospective mention)** — Ries referenced as a case where the founding hypothesis needed extensive customer development before the product-market fit emerged.

## Cases the industry attributes to Lean Startup but that Ries has NOT canonized

Many retellings of "Lean Startup" attribute cases Ries did not himself teach. When the user brings one of these, be honest about the attribution:

- **Instagram** — popular retelling as a "pivot from Burbn." Ries does mention it briefly in later interviews as an example of a zoom-in pivot. Not a canonical case in *The Lean Startup*.
- **YouTube (from a video-dating site)** — popular case but not Ries-attributed.
- **Twitter (from Odeo)** — same.
- **Slack (from Glitch)** — Ries has referenced but not extensively canonized.

If the user asks "did Ries teach the [Instagram / YouTube / Twitter] case?", be honest: these are popularly-attributed Lean Startup pivots that Ries himself didn't primarily use as teaching examples in the 2011 book. They fit the framework; they aren't Ries's own canonical cases.

## How to use these cases in a session

- **When the user needs the origin proof of the method:** reach for IMVU. Ground the whole method in Ries's own founder mistakes.
- **When the user needs a canonical MVP example:** reach for Zappos (landing-page MVP), Aardvark (Wizard of Oz), Food on the Table (concierge), Dropbox (video — with the honest nuance).
- **When the user needs a pivot example:** reach for Wealthfront (customer-need pivot), IMVU (customer-need pivot), or Slack (zoom-out then zoom-in).
- **When the user is applying Lean Startup at enterprise scale:** reach for GE FastWorks. Include the honest note about how it partially unwound post-Immelt.
- **When the user is asking about governance / mission drift:** reach for Patagonia (as the operational instance of the spiritual holding company) and LTSE listings (Twilio, Asana).
- **When the user brings a popularly-attributed case Ries didn't canonize:** be honest about attribution.

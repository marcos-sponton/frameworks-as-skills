# Inspired — Heuristics, Anti-Patterns, Do's and Don'ts

> Cagan's diagnostic and operational rules. Every anti-pattern here has a name (name it explicitly when you see it in a session) and every rule has an attribution — book chapter or SVPG essay URL.

## Symptoms you're a feature factory / feature team

Diagnostic checklist. Two or more of these and you're likely in the pattern. Attribution: [Product vs Feature Teams](https://www.svpg.com/product-vs-feature-teams/) plus recurring across *Inspired*, *Empowered*, *Transformed*.

- Team receives a prioritized list of features to build ("the roadmap"), not problems to solve.
- Roadmap runs 2–3 quarters, is committed externally to sales and customers, contains dates on unvalidated solutions.
- Success is measured by shipped features, velocity, story points — not customer or business outcomes.
- PMs spend the majority of their time writing user stories, running backlog grooming, running ceremonies.
- Engineers show up at sprint planning to receive tickets, not to help figure out solutions.
- Nobody on the team can articulate the *desired outcome* the current feature is supposed to produce.
- "Product owner" is the title; "product manager" is either absent or a program-manager relabel.
- Company adopted SAFe (or similar scaled-agile framework) and calls that "product operating model."
- Discovery is skipped entirely — the team goes from stakeholder request straight to sprint backlog.
- Sales contracts contain feature promises that then drive the roadmap.
- Design and engineering are consulted *after* the PM has decided the solution, not before.
- The team can name the features but not the metric that would prove any of them "worked."

## Cagan's named anti-patterns (name them explicitly in session, with attribution)

### Team-level anti-patterns

- **Feature team** — the umbrella anti-pattern. Command-and-control, mercenary mindset, output-focused, PM as facilitator. *Source: [Product vs Feature Teams](https://www.svpg.com/product-vs-feature-teams/) + Inspired.*
- **Delivery team / project team** — even more degraded: no PM at all, just engineers executing a spec. *Source: [Product vs Project Teams](https://www.svpg.com/product-vs-project-teams/).*
- **Backlog administrator** — Cagan's dismissive term for a "product owner" with no strategic ownership; just runs the backlog. *Source: [Product vs Feature Teams](https://www.svpg.com/product-vs-feature-teams/) + Lenny 2024.*
- **Mercenary culture** — teams that "basically build whatever they're told to." Outsourcing core product-team functions produces this. *Source: Empowered (2020) + Doerr quote Cagan uses repeatedly.*

### PM-role anti-patterns

- **Product management theater** — 2024 coinage. Non-PM roles (Agile coaches, product owners, product operations, business analysts) relabeled as PMs; ceremony over judgment; no accountability for value or viability. Post-ZIRP over-hiring exposed it. *Source: [Product management theater | Marty Cagan (Lenny's Podcast)](https://www.lennysnewsletter.com/p/product-management-theater-marty), 2024.*
- **Mini-CEO myth** — the "PM is the CEO of the product" framing that gives PMs accountability without authority. Cagan explicitly rejects it (with Perri agreeing). *Source: Lenny 2024 + [[escaping-the-build-trap]] cross-link.*
- **Waiter PM / order-taker** — Perri's coinage that Cagan adopts. Takes requests from sales / support / execs, turns them into tickets. Compatible with Cagan's "feature team PM." *Source: [[escaping-the-build-trap]].*
- **Former project manager as PM** — obsessed with dates, ignores customer problem. *Source: Empowered.*

### Leadership anti-patterns

- **Vision as mission statement** — treating a corporate tagline as a product vision. Fails the "creates common understanding across teams" test. *Source: [Product Vision vs. Mission](https://www.svpg.com/product-vision-vs-mission/).*
- **Strategy as quarterly OKR-writing exercise** — no focus, no insights, no bets, no active management. Just objectives cascading downward. *Source: [Product Strategy — Overview](https://www.svpg.com/product-strategy-overview/) + Transformed.*
- **Peanut-buttering** — too many bets, no resource concentration. Fails the focus principle. *Perri's coinage, Cagan compatible.*
- **HIPPO-driven prioritization** — highest-paid person's opinion wins. Substitutes for insights. *Common across product literature; Cagan compatible.*
- **Solution imposition by stakeholders** — stakeholder brings a feature request, not a problem statement. *Source: [Stakeholders and the Product Model](https://www.svpg.com/stakeholders-and-the-product-model/), 2025.*
- **Coaching as extracurricular** — leaders treating coaching as "nice to have" instead of the primary responsibility. *Source: Empowered.*
- **Certifications-as-training** — CSPO / CSM / SAFe certifications as substitute for coaching. *Source: Empowered.*

### Roadmap / commitment anti-patterns

- **Roadmap as sales contract** — dates on unvalidated features committed externally. Perri's canonical anti-pattern; Cagan compatible. *Sources: [The Alternative to Roadmaps](https://www.svpg.com/the-alternative-to-roadmaps/) + [[escaping-the-build-trap]].*
- **"Outcome-based roadmap"** as fix — Cagan's position: even outcome-based roadmaps are still roadmaps. Replace the artifact, don't relabel it. *Source: [Roadmap Alternative FAQ](https://www.svpg.com/roadmap-alternative-faq/).*
- **High-integrity commitments treated as default** — using the "committed date" mechanism for everything, instead of sparingly and only after discovery validation. *Source: [The Alternative to Roadmaps](https://www.svpg.com/the-alternative-to-roadmaps/).*

### Process / framework anti-patterns

- **SAFe as the Product Operating Model** — Scaled Agile Framework rewards output cadence, encodes command-and-control in scaled ceremony. Cagan and Perri both explicitly do NOT recommend. *Source: recurring across SVPG essays + Perri Lenny episode.*
- **Scrum as religion** — ceremonies as the point rather than a vehicle. Cagan is agnostic-to-hostile on Scrum when it becomes theater. *Source: various essays + Lenny 2024.*
- **"Everyone is a PM"** — dilutes accountability; nobody is actually responsible for value or viability. *Source: Product management theater 2024.*

### Transformation anti-patterns

- **Pilot team assembled from average performers** — dooms the pilot. Hand-pick. *Source: [The Politics of Pilot Teams](https://www.svpg.com/the-politics-of-pilot-teams/), 2025.*
- **Pilot team problem chosen too safe** — no proof of what "good" looks like. *Same source.*
- **Pilot team problem chosen too risky** — guaranteed failure sinks the transformation politically. Sweet spot: "impressive but not impossible." *Same source.*
- **Transformation by memo** — announcing a POM adoption without a pilot, coaching, or leadership behavior change. *Source: Transformed (2024).*
- **Copying the 20 First Principles as a checklist** — without changing the incentive / authority / reporting structures that produced the feature team. Cargo cult. *Source: Transformed.*

### AI-era anti-patterns (2025–2026)

- **AI as productivity lever without operating-model change** — accelerates whatever operating model you already have. Feature team + AI = faster feature factory. *Source: [The AI Productivity Paradox](https://www.svpg.com/the-ai-productivity-paradox/), 2026.*
- **Using AI to speed up delivery when the bottleneck is discovery** — AI collapses delivery cost; the constraint is now what to build and why. *Source: [Build to Learn vs Build to Earn](https://www.svpg.com/build-to-learn-vs-build-to-earn/), 2026.*
- **"Building to earn" prematurely** — shipping unvalidated ideas at AI-accelerated speed. Ten-times-faster-in-the-wrong-direction pattern. *Source: same essay + Hilary Gridley quote Cagan cites.*

### Governance / company-level anti-patterns (2026)

- **Great product, captured board** — successful product companies become targets for governance capture and short-term financial extraction. *Source: [Great Products, Bad Companies](https://www.svpg.com/great-products-bad-companies/), 2026-06-30.* Cagan's recommended reading: Eric Ries's *Incorruptible*.

## Do's for empowered product teams

From *Inspired*, *Empowered*, *Transformed*, and the SVPG essay corpus.

### Team-level do's

- **Give teams problems + desired outcomes.** Let them figure out solutions. This is Empowerment Principle #1.
- **Staff each team with a real PM + real designer + real lead engineer + 2–10 engineers.** Two-pizza rule.
- **Attack the four risks EARLY** (value, usability, feasibility, viability) — in discovery, cheaply, with prototypes. Not in delivery.
- **Run continuous discovery.** Teresa Torres's cadence (weekly customer interviews, opportunity solution trees) fits cleanly inside Cagan's discovery.
- **Prototype constantly.** Strong discovery teams run 10–20+ prototypes per week. Prototypes are throw-away; production code is not.
- **Ship small, frequent, reliable releases** — at minimum every 2 weeks, ideally CI/CD.
- **Instrument the product.** Every meaningful action generates a data point.
- **Talk to customers weekly** as a team, not just as PM.

### Leadership do's

- **Publish a product vision with a 2–5yr horizon** (software) or 5–10yr (devices). Make it a **visiontype** prototype video, not a doc. Sell it internally, repeatedly.
- **Product strategy = focus + insights + bets + active management.** Say no to the hundred other good ideas. Ground strategy in data, customer conversations, tech trends, industry insights — not opinion.
- **Set business objectives per team** (OKR-shaped), not roadmap features. Objectives = problems + desired outcomes.
- **Use high-integrity commitments SPARINGLY**, only for the rare specific cases requiring a date, and only after discovery has validated the solution.
- **Coach constantly.** Coaching is the leader's primary job, not extracurricular. Career development for each PM is a first-class management output.
- **Hire ordinary people who are coachable and mission-aligned.** Extraordinary products come from developing ordinary people, not from hiring superheroes.
- **Evangelize the vision internally.** Executives, sales, marketing, support, engineering — all need to have heard it, from you, more than once.

### Transformation do's

- **Fund a pilot team as the "MVP for the transformation."** Hand-pick members from your strongest people (bar-raisers). Choose a problem in the "impressive but not impossible" sweet spot. Judge the pilot by business outcome, not by process compliance.
- **Bring in coaches** — internal or external — during transformation. Manager-as-coach behavior is not innate; it needs modeling and reinforcement.
- **Preserve the 20 First Principles.** Not as a checklist but as a coherent set. Adopting some without others produces the classic "we tried the POM and it didn't work" failure.
- **Reset the incentive structures** — team-level OKRs (with Perri, not individual), decoupled exec comp from OKR attainment.

### AI-era do's (2026)

- **Use AI to accelerate discovery** — more prototypes, more experiments, more customer conversations. This widens the gap between strong and weak product orgs.
- **Match AI investment to operating model.** If you're a feature team, adopt the POM before adopting AI tooling — otherwise you accelerate the feature factory.
- **Treat AI coaching as a real option** post-2026. Foundation models grounded in the right operating context are Cagan-endorsed. *Source: [Product Coaching and AI](https://www.svpg.com/product-coaching-and-ai/), 2026.*

## Common misapplications (orgs that *claim* Product Operating Model)

- **Rebrand POs as PMs** without changing the job or reporting structure → product management theater.
- **Adopt "outcome-based" roadmaps** that are still committed feature lists → still roadmaps in Cagan's frame.
- **Fund a Product Ops team that becomes a PMO in disguise** — Perri's canonical anti-pattern; Cagan adopts her definition. Real Product Ops removes obstacles; fake Product Ops adds them.
- **Run "transformation" without a pilot team** and expect the org to change from an announcement.
- **Copy the 20 First Principles as a checklist** without changing incentives.
- **Adopt AI tooling and celebrate velocity** — productivity paradox essay warns explicitly.
- **Confuse product vision with mission statement** — vision fails to do its job.
- **Confuse product strategy with quarterly OKR-writing** — no insights, no focus, no bets.
- **Hire PMs before product/market fit** — Cagan's own founder advice: wait until post-PMF.
- **Outsource core empowered-team functions** — manufactures mercenaries.

## Cagan's push-back vocabulary — words to challenge in a session

If the user uses one of these words, pause and clarify or push back with Cagan's alternative:

| User says | Push back with |
|---|---|
| "product owner" (as a job title) | "product manager" — accountable for value + viability |
| "mini-CEO" | mini-CEO is a myth; PMs need authority proportional to accountability |
| "roadmap" | product vision + objectives + high-integrity commitments |
| "outcome-based roadmap" | still a roadmap; replace the artifact |
| "SAFe" | rewards output cadence; not the POM |
| "execution" (when it excuses executives from strategy) | strategy IS executives' job; separating strategy from execution is often a dodge |
| "best practices" | first principles — the practices are downstream of principles |
| "certification" (as substitute for coaching) | coaching is the primary leadership responsibility |
| "we're agile" | agile is a value system, not the product operating model |
| "features on the roadmap" | problems to solve + desired outcomes |
| "when will X ship" (on unvalidated work) | we don't commit dates on unvalidated solutions; discovery first |

**Bias in application:** Cagan is warm about humans, cold about patterns. Pushing back on the vocabulary is not attacking the person — it's naming the pattern the vocabulary encodes. Model that tone.

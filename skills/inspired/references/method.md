# Inspired — Method

> The canonical description of Cagan's Product Operating Model in his own terms. Fidelity is the point — softening any of these collapses the method into generic product-management language. Cagan does not offer one linear process; he offers a set of first principles organized around three altitudes (Product Team, Product Discovery/Delivery, Product Leadership) that add up to the **Product Operating Model (POM)**.

## The umbrella — Product Operating Model (POM)

The 2024 umbrella term introduced in *TRANSFORMED*. Cagan's definition:

> "A conceptual model based on a set of first principles that leading product companies believe to be true about creating products. Its core purpose is achieving outcomes versus merely producing output." — [The Product Operating Model: An Introduction](https://www.svpg.com/the-product-operating-model-an-introduction/)

**Three dimensions of the POM** (the framing Cagan uses in talks and *Transformed* Ch. 3):

1. **How products are built** — small, frequent, reliable releases; minimum every 2 weeks, ideally continuous delivery (CI/CD).
2. **How problems are solved** — cross-functional teams (PM + designer + engineers) receive **problems** and desired outcomes; produce solutions that are **valuable, usable, feasible, and viable**.
3. **How you decide which problems to solve** — a customer-focused **product vision** paired with an **insight-driven product strategy**.

The POM is **not a process**. It is not Scrum. It is not SAFe. It is not an "outcome-based roadmap." It is a set of first principles about how the best product companies work. When someone claims to have adopted the POM, the test is whether their teams are empowered with problems (yes) or handed roadmaps of features (no).

## The Product Team — the atomic unit

From *Inspired* and canonicalized in [Product vs Feature Teams](https://www.svpg.com/product-vs-feature-teams/):

**Product team (empowered):**
> "Cross-functional (product, design and engineering); they are focused on and measured by outcomes (rather than output); and they are empowered to figure out the best way to solve the problems they've been asked to solve."

**Feature team (anti-pattern):**
> Groups that receive "a prioritized list that is called the roadmap" with predetermined outputs rather than problems to solve. The product manager acts as facilitator rather than strategic leader.

**Team composition (Cagan's rule):**
- **Product Manager** — accountable for value + viability. Not a project manager; not a product owner in the Scrum-role sense; not a "mini-CEO" (Cagan explicitly rejects this framing).
- **Product Designer** — accountable for usability + experience.
- **Lead Engineer** (or Tech Lead) — accountable for feasibility + delivery.
- **2–10 engineers** — the **two-pizza rule** (Amazon origin). More than 10 and the team fractures.

The three-plus-engineers unit is sometimes called the **product trio** — a term Torres coined in *Continuous Discovery Habits* that Cagan uses approvingly.

**Missionaries not mercenaries** (John Doerr quote Cagan uses repeatedly):
> "We need teams of missionaries, not teams of mercenaries."

Missionaries "sincerely believe in our larger purpose"; mercenaries "basically build whatever they're told to." Amazon's refusal to outsource core product-team functions is the load-bearing example — outsourcing manufactures mercenaries.

## The Four Big Risks — the discovery-side diagnostic

From [The Four Big Risks](https://www.svpg.com/four-big-risks/) — introduced in *Inspired*, hardened in every subsequent book. Cagan's most-cited framework.

| Risk | Cagan's definition | Owned by | Attacked in |
|------|-------------------|----------|-------------|
| **Value** | *"Whether customers will buy it or users will choose to use it"* | Product Manager | Discovery |
| **Usability** | *"Whether users can figure out how to use it"* | Product Designer | Discovery |
| **Feasibility** | *"Whether our engineers can build what we need with the time, skills and technology we have"* | Lead Engineer | Discovery |
| **Business Viability** | *"Whether this solution also works for the various aspects of our business"* (legal, finance, sales, marketing, brand) | Product Manager | Discovery |

**The rule:** attack the four risks **early**, in discovery, cheaply, with prototypes. Attacking them late — in delivery, when you've written production code — is the source of most product failure. Cagan singles out **value** and **viability** as the two most under-attended risks by weak PMs.

> "It's not enough to create a product your customers love; the product must also work for your business." — same essay.

## Product Discovery vs. Product Delivery — the fundamental split

From [Product Discovery](https://www.svpg.com/product-discovery/), and sharpened in [Build to Learn vs Build to Earn](https://www.svpg.com/build-to-learn-vs-build-to-earn/) (2026).

### Product Discovery — **build to learn**

> "We are trying to discover a combination of technology, functionality, user experience and business constraints that address the key risks in discovery: value, usability, feasibility and viability."

- **Unit of work:** the *experiment*.
- **Medium:** prototypes. Strong teams run 10–20+ prototypes per week. Prototypes are cheap, throw-away, meant to accelerate learning.
- **Techniques:** framing, planning, ideation, prototyping, testing. Concept testing. Wizard of Oz. Concierge. Customer letter / press release (borrowed from Amazon).
- **Owner:** the product team (PM + designer + lead engineer together — the trio).

### Product Delivery — **build to earn**

> "We are building a commercial quality product that we can sell, service and support, and that our customers can run their business on."

- **Unit of work:** the *release*.
- **Concerns:** scale, performance, fault tolerance, reliability, accuracy, privacy, security, operations, provisioning, internationalization.
- **Cadence:** small, frequent, reliable releases. Minimum every 2 weeks. Ideally continuous.
- **Testing means something entirely different** than in discovery — validating the product against operational demands, not against customer assumptions.

**Credit:** the "build to learn / build to earn" distinction is credited by Cagan to **Jeff Patton**.

**Why the split matters more now (2026):** AI is collapsing the cost of *delivery*, which promotes *discovery* to primary bottleneck. Strong teams widen their advantage by running more discovery, not by shipping features faster. See `post-book.md` §AI + POM.

## Product Vision — the leadership deliverable

From [Product Vision vs. Mission](https://www.svpg.com/product-vision-vs-mission/) and [Product Vision FAQ](https://www.svpg.com/product-vision-faq/).

### Vision vs. Mission — the distinction

- **Mission statement:** "a pithy slogan…to describe your company's mission." Corporate purpose. Necessary; not the product vision.
- **Product vision** (Cagan verbatim): *"The future we are trying to create."* A **persuasion tool** — meant to be *"compelling, inspiring, and empowering."* Not a spec.

### Time horizon (rules)

- **Software companies:** 2–5 years out.
- **Device / hardware companies:** 5–10 years out.

### Format — the visiontype

Cagan's preferred format is a **visiontype** — a short video prototype that dramatizes the user's experience in the future you're creating. The vision has to be *emotional*, not decorative. Companies invest real production energy in the visiontype because it becomes the North Star that lets teams coordinate without micromanagement.

### What a strong vision does

- Creates common understanding across all product teams — coordination without control.
- Inspires ordinary people to create extraordinary products (the *Empowered* title thesis).
- Demonstrates meaningful customer impact — not a feature list.
- Guides organizational architecture, team structure, and strategy.

## Product Strategy — focus, insights, bets, active management

From [Product Strategy — Overview](https://www.svpg.com/product-strategy-overview/) and [Product Strategy — Focus](https://www.svpg.com/product-strategy-focus/).

**Cagan's four requirements for real product strategy:**

1. **Focus** — the willingness to make tough choices on what's really important. *"Saying no to the hundred other good ideas."* Focus is where most orgs fail — they say yes to too many bets.
2. **Insights** — generating, identifying, and leveraging insights. Insights come from data analysis, customer conversations, enabling technologies, and industry trends. Not from opinion or authority.
3. **Actions** — converting insights into action. Assigning problems to specific teams with clear desired outcomes.
4. **Active management (without micromanagement)** — the leadership discipline. Product leaders manage the portfolio of bets: adjust, kill, redirect. Do not micromanage the teams.

**"Placing bets" is the vocabulary.** Product strategy is a portfolio of bets. Some will fail. Multiple teams may attack the same problem in parallel — that's how strong companies handle uncertainty.

## The Alternative to Roadmaps

From [The Alternative to Roadmaps](https://www.svpg.com/the-alternative-to-roadmaps/) and [Roadmap Alternative FAQ](https://www.svpg.com/roadmap-alternative-faq/).

**Cagan's position: roadmaps are replaced, not fixed.** Even "outcome-based" roadmaps are still roadmaps in his view.

**The alternative** — three artifacts that together do the job the roadmap pretended to do:

1. **Product Vision** — the multi-year holistic view (2–5yr / 5–10yr).
2. **Business objectives per team** (OKR-shaped) — the *problems to solve* + *desired outcomes*. This is the working artifact for each team.
3. **High-Integrity Commitments** — for the rare specific cases requiring a date-based deliverable (regulatory deadline, key partnership contract, major industry event). Handled separately, sparingly, and **only after discovery has validated the solution**.

**Why this matters:** the roadmap-as-artifact conflates strategy, planning, and commitment. It creates false certainty for stakeholders and destroys team autonomy. Splitting the three functions into three separate artifacts resolves the conflict without lying.

## Product Leadership and Coaching

From *EMPOWERED* (2020, with Chris Jones) and the [product coaching page](https://www.svpg.com/product-coaching/).

**Cagan's core leadership claim:**
> "Coaching is the primary responsibility of managers overseeing product managers, designers, and engineers."

Product leadership's job is not to prioritize features or approve roadmap items. It is:

- **Set the product vision.**
- **Set the product strategy** (focus, insights, bets, active management).
- **Coach** the PMs, designers, and engineers into extraordinary versions of themselves.
- **Staff** the org: hire ordinary people who are coachable and mission-aligned; develop them.
- **Evangelize** the vision internally — repeatedly. The vision has to be sold, not memoed.

**Product coach roles** (from the coaching page):
- All SVPG partners are product coaches. Direct coaching is limited to clients.
- SVPG maintains a referral network of independent product coaches — no financial relationship, just vetted.
- Coaches serve two purposes: (1) manager support when managers are learning on the job; (2) transformation leadership when a company is moving to the product operating model.

**2026 reversal:** Cagan reversed the 20-year "coaching is human-only" position in [Product Coaching and AI](https://www.svpg.com/product-coaching-and-ai/) — foundation models grounded in the right operating context can now serve as scalable, always-on product coaches.

## The 20 First Principles of the Product Operating Model

From *TRANSFORMED* (2024), Chapters 15–19. Organized in three groups. Reference index: [Product Compass in-depth summary](https://www.productcompass.pm/p/product-model-first-principles-transformed-cagan).

### Product Team principles (4)

1. **Empowered with Problems to Solve** — teams get customer/business problems + desired outcomes, not solutions.
2. **Outcomes over Output** — measured by results and value created, not features delivered.
3. **Sense of Ownership** — teams own discovery AND delivery; clear purpose, autonomy.
4. **Collaboration** — cross-functional; psychological safety; disagree-and-commit.

### Product Strategy principles (4)

5. **Focus** — "saying no to the hundred other good ideas."
6. **Powered by Insights** — from data, customer conversations, enabling technologies, industry trends.
7. **Transparency** — reasoning, data, stakeholder impact shared openly.
8. **Placing Bets** — strategy as a portfolio; some bets fail; multiple teams may attack the same problem.

### Product Discovery / Delivery / Culture principles (12)

The remaining twelve cover the operational and cultural principles: continuous discovery cadence, prototype-based validation, tackling the four risks early, small/frequent/reliable releases (CI/CD as default), instrumentation and monitoring, customer-informed decisions, principled disagreement, learning culture, career development, trust-based relationships with stakeholders, missionary culture, and evidence-based decision-making.

Full detail: *Transformed* Ch. 15–19. Also see [Product Compass Part 2 reference](https://www.productcompass.pm/p/product-model-first-principles-transformed-cagan) for the current published index.

## Integration — how the pieces fit

- **Product Vision** sets the multi-year direction (Leadership altitude).
- **Product Strategy** picks the bets — the problems to solve that serve the vision (Leadership altitude).
- **Product Team** — cross-functional, empowered — gets a problem + desired outcome from the strategy.
- **Product Discovery** attacks the four risks with prototypes, cheaply, before writing production code.
- **Product Delivery** ships small, frequent, reliable releases of the validated solution.
- **Coaching** develops the humans on the teams; product leaders coach constantly.
- **Business objectives + high-integrity commitments** replace the roadmap.
- The **20 First Principles** are the operating rules under all of it.
- The whole system is the **Product Operating Model**.

**When any layer is broken, the layers above and below strain, and the feature-team pattern re-emerges from the break:**

- Missing product vision → teams work on disconnected initiatives → no coordination → feature team.
- Missing product strategy → prioritization becomes political → highest-paid-person's opinion wins → feature team.
- Missing empowered team → engineers become order-takers → mercenary culture → feature team.
- Missing discovery → all learning happens in delivery, when it's expensive → feature team.
- Missing coaching → PMs stay stuck as backlog administrators → feature team.

## What this method is NOT

Cagan is explicit — see also `heuristics.md`:

- **NOT a process framework.** Not Scrum. Not SAFe. Not "outcome-based agile." The POM is upstream of any process choice.
- **NOT a rebrand of Scrum.** Rebranding POs as "product managers" without changing the job produces backlog administrators.
- **NOT a roadmap improvement.** Even "outcome-based" roadmaps are still roadmaps. Replace, don't fix.
- **NOT the operational infrastructure that Perri covers.** Perri's *Product Operations* (2023) — Data & Insights / Customer & Market Insights / Process & Governance — sits inside the POM. Cagan explicitly adopts her definition. See `applications.md` and [[escaping-the-build-trap]].
- **NOT firm-level strategy.** Playing to Win (Martin) sits above the POM at the corporate level; 7 Powers (Helmer) sits at the competitive-advantage level. Both compose with the POM without collapsing into it.

# Shape Up — Worked Examples

> Cases Ryan Singer uses publicly to teach Shape Up. The 2019 book is entirely a Basecamp case study (Singer worked there for 17 years and drew every artifact himself); the 2025 gym-management case study is Singer's freshest worked example of adapting the method for a typical (non-Basecamp) company.

## Basecamp — the primary case, running through the whole 2019 book

**Source:** Every chapter of *Shape Up* (2019) grounds itself in Basecamp — feature bets from Basecamp 2 through Basecamp 3 (with Basecamp 4 in development at the time). https://basecamp.com/shapeup

**Why it matters:** Singer worked on Basecamp for 17 years. The mechanisms in the book aren't inferred from theory — they were what Basecamp actually did, iterated over many cycles. When the book gives an example ("here's how we shaped the Message Board feature," "here's how we scoped the To-Do redesign"), it's a first-person operator account.

**What Basecamp reveals about the method:**
- **Everyone was technical, including designers.** Designers coded; there was no seam between design and code. This is the biggest "unusual company" caveat — the 2019 book assumes it and Singer's 2022+ writing addresses adaptations for companies that don't have this.
- **Small teams (~15 people).** Small enough that "no backlog" was politically possible and "small autonomous build team" wasn't a struggle to constitute.
- **Product-led CEO.** Jason Fried framed implicitly by being in the room. Elsewhere, framing has to be a step.
- **Long product runway.** Multiple cycles of the same core product over years; the six-week cycle developed as the natural rhythm.

**Use this case when:** the user needs the canonical account of the mechanisms as intended — the "how it was designed to work" reference.

## Hey (hey.com) — a full Shape Up-built product

**Launched:** 2020, by 37signals. Basecamp's email product.

Hey is a full product built by 37signals using Shape Up throughout. DHH and Fried talk about it more publicly than Singer does; the operating model behind it is the one from the book.

**What Hey reveals:** the method can produce a full new product from scratch, not just features inside an existing one. But this required the full 37signals org (small, technical, product-led, willing to bet at product scale).

## The 2025 gym-management case study — Singer's freshest post-Basecamp worked example

**Source:** https://www.ryansinger.co/end-to-end-with-shape-up-a-real-world-case-study/ (2025)

**Company:** an unnamed company that acquired a gym-management software product. The application serves small gym owners with one location who know all their members personally.

**Team structure (deliberately non-Basecamp):**
- Backend engineers
- Frontend engineers
- Designer
- QA
- SME (former gym owner in sales, brought in for domain knowledge)
- Separate marketing, sales

This is the "typical" B2B SaaS team structure that the 2019 book didn't address.

**The full loop Singer walks through:**

### 1. Candidate → Framing

Leadership proposes "improve the dashboard" — a vague ask. Singer interviews the SME (a former gym owner) to understand actual pain. The real problem emerges: **tracking missed member payments and class utilization.**

**Framing output:** a framed problem — small gym owners are losing money to missed member payments they don't have visibility into. Business value: revenue recovery.

**Delta from the book:** the book assumed Basecamp-style framing implicitly. Here, Singer had to interview a domain expert to *find* the framed problem hiding inside "improve the dashboard."

### 2. Framing → Shaping (Session 1)

Singer conducts a 2-hour whiteboarding session with a senior engineer. Discovery:
- The current payment recovery flow is underdeveloped.
- The sales detail page is a "legacy thing" difficult to modify.

**Delta from the book:** two whole hours with a senior engineer, explicit technical shaping. The book assumed this happened naturally at Basecamp; here it's engineered as a step.

### 3. Shaping refinement (Session 2)

Singer brings the SME into a second 2-hour shaping session with the engineer. Together they discover payment retry functionality barely exists in the current product. **Reframe the project as purely about "payment recovery"** rather than broader dashboard metrics.

**Delta from the book:** mid-shaping reframe. The original framing wasn't quite right; shaping surfaced a sharper version. This is a signal of shaping working — it's design work, and design work reveals things.

### 4. Package written (the shaped output)

Singer's post-2022 term for the pitch. Contains:
- **Problem:** small gyms losing revenue to missed payments they can't see or recover.
- **Appetite:** full six-week cycle.
- **Solution:** payment recovery flow — sketched at fat-marker fidelity, showing the key screens and their connections.
- **Rabbit holes:** the legacy sales detail page can't be modified deeply within appetite; work around it.
- **No-gos:** broader dashboard redesign is explicitly excluded.

### 5. Betting Table → Build kickoff

The package goes to the Betting Table, is bet on, and the build team kicks off.

**Team:** backend, frontend, designer, QA, SME.

**Move 1:** the team identifies **9 vertical slices** — scopes that can be built and integrated independently.

**Move 2:** the team sequences the scopes.

**Move 3:** they **wire functionality before high-fidelity design** — get an end-to-end skeleton working, then polish. This is the "wire first, design later" discipline Singer explicitly documents in the case study.

### 6. Shipping

The team ships within the appetite. Case study ends with the shipped product; no Circuit Breaker triggered.

## What this case study is meant to teach

Beyond the mechanics, the 2025 case study is Singer's public evidence that Shape Up **can** be adapted for typical (non-Basecamp) companies — the promise of *Shaping in Real Life*. Specific adaptations made visible:

1. **Framing had to be a distinct step.** Two conversations (SME interview + follow-up) before shaping.
2. **Technical shaping was engineered explicitly.** Two 2-hour sessions with a senior engineer.
3. **Mid-shaping reframe was legitimate.** The problem sharpened as shaping progressed.
4. **The build team was cross-functional in the modern sense** — separate backend, frontend, designer, QA — not the Basecamp "designer-who-codes" model.
5. **The "wire before design" build discipline** was documented explicitly for teams that don't have Basecamp's designer-programmer overlap.

**Use this case when:** the user is a typical B2B SaaS team asking "does Shape Up work for us?" This is Singer's freshest, most detailed public answer.

## Other cases referenced across Singer's writing

**Client engagements throughout the post-2020 essays** — Singer references (usually without naming) client work in his 2022 *Framing* essay, the 2025 *Common Pitfalls* piece, and the Lenny 2025 podcast. These are the source material for the "adaptation" thinking but they aren't full worked examples.

**Community cases at the Shape Up Forum** — https://discourse.learnshapeup.com — practitioner accounts of adoption at various companies (GitLab, various startups, agencies). Not Singer's own writing, but useful as third-party evidence.

## Anti-examples — what Singer doesn't use as a case

- **He doesn't use Amazon.** Working Backwards is Amazon's method. Shape Up is Basecamp's.
- **He doesn't use FAANG.** No Meta, no Google, no Apple examples. The scale and structure are wrong.
- **He doesn't dwell on failed projects.** Unlike Working Backwards, which openly discusses Fire Phone as a "mechanism worked, bet failed" example, Singer doesn't have a canonical failed-bet case. The Circuit Breaker chapter (Ch. 14) describes the *process* of killing but not a specific killed project.

If the user wants "cases where Shape Up worked outside Basecamp," the 2025 gym-management case study is the one to reach for. If they want more, point them to the Shape Up Forum for practitioner accounts (with the caveat that those aren't Singer's own writing).

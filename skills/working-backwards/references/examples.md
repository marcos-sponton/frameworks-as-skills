# Working Backwards — Worked examples

> Cases Bill Carr and Colin Bryar use publicly to illustrate the mechanisms. Each case names the source (book chapter, blog post, podcast) so the user can verify. Structured so you can pull the case that matches the user's situation.

## Case index by situation

| If the user is working on... | Reach for... |
|---|---|
| The canonical PR/FAQ that unlocked a major product | **Kindle** (always-on 3G decision) |
| Working backwards to a customer bet no one else would make | **Amazon Prime** (annual-membership free shipping) |
| Single-Threaded Ownership enabling a business inside a business | **AWS** (developed alongside retail) |
| A failure with the mechanisms in place — and what the failure teaches | **Fire Phone** |
| Extending the mechanisms into a new business domain | **Prime Video / Amazon Studios / Amazon Music** |
| Input-metric discipline in a hardware + voice product | **Alexa / Echo** |
| Stepping-stone failure that fed a later success | **Unbox** (pre-Prime-Video digital video) |
| Culture around failure (COE in action) | **Amazon's response to failed bets** ("Why would I fire you now?") |
| Non-Amazon application (with caution) | **Netflix / Warner Bros. acquisition** (firm blog, 2026) |

## Kindle — the canonical PR/FAQ

**Where Carr/Bryar use it:** *Working Backwards* (book, 2021, the Kindle chapter), Bill Carr on Lenny 2023, the March 2026 firm blog post ["Use customer insights to design always-connected Kindle"](https://workingbackwards.com/blog/) revisits it.

**The situation:** Amazon wanted to build a dedicated e-reader. The default engineering path would be a device that requires Wi-Fi and a computer to sync new books.

**Working Backwards output:** the PR/FAQ started from the customer perspective — "I want to buy a book right now, from anywhere, with no setup." Working backwards from that experience forced the always-on 3G decision: Amazon would eat the wireless carrier cost so the customer never had to think about connectivity. This decision looked expensive on paper and unnecessary through a features lens; through the customer-experience lens it was mandatory.

**Why the case is instructive:** it shows the *inversion* Working Backwards produces. Skills-forward thinking would have shipped a Wi-Fi Kindle. Customer-first thinking, forced through the PR/FAQ, produced an always-on Kindle. The 3G cost was material, but eating it unlocked the "buy a book anywhere" experience that made the device an object customers actually loved.

**Quotable moment:**
> "Start with what's best for the customer and then come backward from there."
> — Bill Carr, Lenny 2023 (framing that produced decisions like this one)

## Amazon Prime — input-metric discipline in a bet no one else would make

**Where Carr/Bryar use it:** book, Lenny 2023, joint firm materials.

**The situation:** annual membership fee for unlimited free two-day shipping. Every unit-economics model at launch said it would lose money. The bet was that faster delivery would move customer behavior enough that lifetime value would swamp the shipping cost.

**Working Backwards mechanisms at play:**
- **PR/FAQ:** the announcement started from the customer experience — no thinking about shipping, no minimum orders, faster delivery.
- **Input metrics:** delivery speed as the controllable input; frequency of purchase and retention as the outputs that would follow.
- **STL:** dedicated team, separable from retail's core operations.

**Why the case is instructive:** the input-metric bet ("faster shipping will move customer behavior") turned out to be right, and the retention data validated it in the first year. But the bet itself was legible *only* because the PR/FAQ forced Amazon to name what customer behavior they expected to see. Without that mechanism-forced articulation, Prime would have been an unfathomable P&L risk. With it, Prime was a testable hypothesis.

## AWS — Single-Threaded Ownership enabling a business inside a business

**Where Carr/Bryar use it:** book (AWS chapter), joint firm materials.

**The situation:** Amazon needed better internal infrastructure. Also had a hypothesis that other companies would pay for the same infrastructure. Traditional org structure would have made AWS a shared-services function that competed with retail for compute resources.

**Working Backwards output:** AWS was set up as a Single-Threaded Ownership team — separable, dedicated, with its own P&L, its own review meetings, its own STL. This wasn't cosmetic; it was structural. Retail couldn't outvote AWS's roadmap, and AWS couldn't be starved of resources by retail's needs.

**Why the case is instructive:** it's the archetype of "you can't build a new business inside a mature business using the mature business's org structure." STL was the mechanism that made AWS possible. The March 2026 firm blog post "Separate innovation from core business to succeed effectively" sharpens exactly this lesson.

## Fire Phone — mechanisms in place, and the bet still failed

**Where Carr/Bryar use it:** book, joint interviews, Bill Carr on Lenny 2023.

**The situation:** Amazon launched a smartphone with 3D-effect display and Firefly product-recognition. It failed commercially.

**Working Backwards mechanisms at play:** the Fire Phone had a PR/FAQ. It was reviewed. It had an STL. It got built. All the mechanisms were in place.

**Why it failed:** the underlying hypothesis was wrong. The customer wasn't asking for a 3D-effect display or product-recognition scanning — those were technology bets, not customer-need bets. The mechanisms produced a document, but the document was in service of a bet Amazon wanted to make, not a customer need Amazon had validated.

**Amazon's response** (canonical, quoted throughout the book):
> "Why would I fire you now? I just made a million-dollar investment in you. Now you have an obligation to make that investment pay off. Figure out and clearly document where you went wrong. Share what you have learned with other leaders throughout the company. Be sure you don't make the same mistake again, and help others avoid making it the first time."

**Why the case is instructive:** Working Backwards makes bets more honest, not automatically correct. Carr is explicit about this in interviews:
> "None of these things give you the answer. They are tools to help you make decisions."
> — Carr, Lenny 2023

Use this case when the user is treating the mechanisms as a guarantee, or when they expect Working Backwards to eliminate bad bets. It doesn't. It exposes them faster and gives you an honest post-mortem when they fail.

## Prime Video / Amazon Studios / Amazon Music — extending mechanisms into new domains

**Where Carr/Bryar use it:** book (Bill Carr's personal chapters — he ran these businesses), Bill Carr on Lenny 2023.

**The situation:** Amazon entered content and entertainment businesses where it had no prior expertise. The mechanisms (PR/FAQ, 6-pager, STL, input metrics, WBR) had all been developed in retail and hardware contexts.

**Working Backwards output:** the mechanisms transferred. PR/FAQs were written for individual shows and series (from the perspective of the customer who'd watch them). Input metrics tracked engagement rather than views. STLs led individual content initiatives. The mechanisms weren't retail-specific — they were disposition-specific.

**Why the case is instructive:** the case argues that Working Backwards mechanisms are domain-neutral. They work for content, hardware, marketplaces, cloud infrastructure, and voice assistants — because the underlying disposition (start with the customer, force articulation, separate the team, track controllable inputs) is domain-neutral. When a user is skeptical that "the Amazon method" applies to their non-Amazon business, this case is the counter-example.

## Alexa / Echo — input-metric discipline in a hardware + voice product

**Where Carr/Bryar use it:** book (Alexa chapters), joint firm materials.

**The situation:** voice assistant + smart speaker. The output metric (units sold) was obvious. The input metrics (speech recognition accuracy, response latency, skill breadth, false-wake rate) were what the team could actually move week to week.

**Working Backwards output:** the team decomposed the customer experience into controllable inputs and reviewed them weekly. Skill breadth, accuracy improvements, latency reductions — each was tracked as its own input, not aggregated into a "fitness function." When engagement outputs moved, the team could attribute the movement to specific input improvements.

**Why the case is instructive:** it's the clean example of input-metric decomposition in a product that could easily have been "tracked" via aggregated NPS or units sold. The mechanism forced the harder, more useful decomposition.

## Unbox — stepping-stone failure

**Where Carr/Bryar use it:** book (as a background example).

**The situation:** Amazon's early attempt at a digital video service, pre-Prime Video.

**Why the case matters:** it's cited as a failure that fed a later success. Amazon didn't succeed at digital video on the first attempt; the learnings from Unbox (via COE) informed how Prime Video was structured and launched. Use this case when a user is discouraged by an early product failure — the point isn't that failures are bad, it's that failures documented honestly (COE) become inputs to the next bet.

## Amazon's response to failed bets — COE culture in action

**Where Carr/Bryar use it:** book, most interviews.

**The situation:** an Amazon executive fails at a major bet. The expected corporate response is termination. Bezos's actual response, quoted throughout the book:

> "Why would I fire you now? I just made a million-dollar investment in you. Now you have an obligation to make that investment pay off. Figure out and clearly document where you went wrong. Share what you have learned with other leaders throughout the company. Be sure you don't make the same mistake again, and help others avoid making it the first time."

**Why the case is instructive:** COE only works if the culture actually treats failures as investments, not as blame-worthy events. If the room is secretly hunting a scapegoat, COE degrades into political theater. This anecdote is the disposition that makes COE work.

## Netflix / Warner Bros. acquisition — non-Amazon application

**Where Carr/Bryar use it:** [firm blog post](https://workingbackwards.com/blog/why-netflixs-warner-bros-acquisition-could-fail-long-term/), March 2026.

**The situation:** Netflix's rumored acquisition of Warner Bros., analyzed through Working Backwards lenses (customer need, single-threaded innovation, mechanisms) rather than pure M&A / financial-synergy logic.

**Why the case matters:** it's the most public example of the firm applying the framework to a non-Amazon situation. Use it as the counter to "does this framework work outside Amazon?" — the answer is yes, and here's the firm doing it publicly on a current-events question. But note the case is analytical, not prescriptive; they're diagnosing, not running the mechanisms inside Netflix.

## What Carr and Bryar do *not* do with cases

- **They do not use non-Amazon success cases as endorsements.** Unlike Roger Martin's rotating P&G/Vanguard/Southwest/Four Seasons roster, Carr and Bryar's cases are almost entirely Amazon-internal. They're teaching from what they ran, not what they observed. Respect this constraint — don't invent non-Amazon "case studies" that put words in their mouths.
- **They do not use cases to sell adoption as easy.** Every case includes the friction — the resistance to spending months on a PR/FAQ, the discomfort of the review, the challenge of holding a mechanism when the culture erodes. Preserve that honesty in your own case-telling.
- **They do not use cases to guarantee outcomes.** Even Kindle, Prime, and AWS are told with the caveat that mechanisms didn't guarantee success — they made the bets more honest, and the team happened to be right.

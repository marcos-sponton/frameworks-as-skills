# The Mom Test — Invocation Templates

> Ready-to-use prompts for common use cases. Each template tells the assistant what to load, how to approach the problem, and what shape the output should take. These are starting points — the assistant should adapt based on the user's specific situation.

## 1. Audit my interview questions

**When to use:** The user has a list of questions they plan to ask in a customer interview and wants feedback.

**Template:**
> I'm planning customer interviews for [context]. Here are my questions:
> [list of questions]
> Audit them against The Mom Test rules. Which ones violate the three rules? What should I ask instead?

**What the assistant should do:**
1. Load `references/method.md` (three rules) and `references/heuristics.md` (bad questions family).
2. Classify each question as passing or failing the Mom Test, with specific reasoning.
3. For each failing question, provide a Mom-Test-compliant alternative.
4. Check whether the questions include at least one "scary" question that could invalidate the idea.
5. Check whether the questions focus on past behavior (good) or future intentions (bad).

## 2. Review my conversation notes

**When to use:** The user has notes from a customer conversation and wants to evaluate signal quality.

**Template:**
> I just had a customer conversation. Here are my notes:
> [notes]
> What did I actually learn? What's real signal vs. noise?

**What the assistant should do:**
1. Load `references/method.md` (bad data types, commitment/advancement) and `references/heuristics.md`.
2. Classify each data point: fact (gold), compliment (fool's gold), fluff (noise), or idea (dig deeper).
3. Identify what was learned (facts about past behavior) vs. what was collected (opinions, compliments).
4. Check for commitment signals: did the conversation end with a commitment (time, reputation, money)?
5. If no commitment, flag as "spinning" and suggest what commitment to ask for next time.
6. Check for segmentation: who was this person? What type? Should their feedback be grouped or separated?

## 3. Design a conversation guide

**When to use:** The user knows who they want to talk to and what they want to learn, but needs help structuring the conversation.

**Template:**
> I'm building [product/idea]. I want to talk to [customer type] to learn about [problem area]. Help me design a conversation guide using The Mom Test.

**What the assistant should do:**
1. Load `references/method.md` (three rules, meeting framing, note-taking).
2. Help identify the three most important questions (including one scary one).
3. Design the five-element meeting frame (vision, framing, weakness, pedestal, ask).
4. Write 5-8 Mom-Test-compliant questions focused on past behavior and current workflows.
5. Include anchoring prompts for when the conversation drifts into fluff.
6. Suggest what commitment to ask for at the end.
7. Remind them about note-taking protocol (two people, exact quotes, debrief).

## 4. Diagnose "everyone loves it but nobody's buying"

**When to use:** The user has been talking to customers, getting positive feedback, but not seeing traction.

**Template:**
> I've talked to [N] people about [idea]. They all say they love it / would use it / think it's great. But nobody's signed up / pre-ordered / committed. What's going on?

**What the assistant should do:**
1. Load `references/heuristics.md` (bad data, compliments-as-fool's-gold, seeking validation).
2. Diagnose the likely cause: the user has been collecting compliments, not facts.
3. Check whether they pitched their idea (violating Rule 1).
4. Check whether they asked about future behavior (violating Rule 2).
5. Check whether they pushed for commitment at the end.
6. Reframe: "everyone loves it" usually means "everyone I pitched to said nice things."
7. Suggest specific next steps: re-run conversations without pitching, focus on past behavior, push for commitment.

## 5. Help me segment my early conversations

**When to use:** The user has talked to multiple types of people and is getting contradictory feedback.

**Template:**
> I've talked to [N] people. Some want [feature A], others want [feature B], and some say they don't even have the problem. I'm confused about what to build. Can you help me sort this out?

**What the assistant should do:**
1. Load `references/method.md` (segmentation).
2. Ask: who were these people? What types? (Job titles, company sizes, industries, use cases.)
3. Help the user slice their feedback by segment.
4. Identify which segment has the most urgent problem (measured by past behavior: spending money, investing time, trying solutions).
5. Suggest focusing on that segment and designing the next round of conversations around them.
6. Warn about the aggregation trap: mixed-segment data cancels out.

## 6. Prepare me for a specific conversation

**When to use:** The user has a meeting scheduled with a specific person and wants help preparing.

**Template:**
> I have a meeting with [person, role, company] tomorrow. I want to learn about [topic]. Help me prepare using The Mom Test.

**What the assistant should do:**
1. Load `references/method.md` (three rules, meeting framing).
2. Design the five-element meeting frame for this specific person.
3. Identify the three most important questions for this conversation.
4. Anticipate likely fluff/compliment traps and prepare anchoring redirects.
5. Suggest what commitment to ask for at the end (tailored to who this person is).
6. Remind about logistics: two-person meeting, note-taking protocol, immediate debrief.

## 7. Is this idea worth exploring further?

**When to use:** The user has a business idea and wants to know how to evaluate it through customer conversations.

**Template:**
> I have an idea for [product/service]. I think [customer type] would use it because [hypothesis]. How should I validate this?

**What the assistant should do:**
1. Load `references/method.md` and `references/applications.md`.
2. Identify the riskiest assumptions in their hypothesis.
3. Design 3-5 Mom-Test-compliant questions targeting those assumptions.
4. Suggest who to talk to and how many conversations (~3-5 per question cluster).
5. Define what "validated" looks like: not "they said yes" but "they showed commitment."
6. Warn about the "idea nihilism" trap: the goal is to learn, not to prove the idea is bad.
7. Suggest the five-element meeting frame for reaching out to prospects.

## 8. Critique my understanding of customer needs

**When to use:** The user has a set of assumptions about their customers and wants to pressure-test them.

**Template:**
> Here's what I believe about my customers:
> [list of assumptions/beliefs]
> Which of these are validated facts and which are untested assumptions? How would I test the assumptions using The Mom Test?

**What the assistant should do:**
1. Load `references/method.md` and `references/heuristics.md`.
2. Classify each assumption: fact (based on observed past behavior), opinion (based on conversations that may have been corrupted), or untested (never verified with actual customers).
3. For each untested or opinion-based assumption, design a Mom-Test-compliant question that would test it.
4. Prioritize: which assumptions are most dangerous if wrong? Start there.
5. Suggest a lightweight plan: who to talk to, how many conversations, what commitment signals to look for.

# Hooked — Heuristics, Do's, Don'ts, Gotchas

> The practical devices that make the difference between applying the Hook Model correctly and doing what Eyal calls a bad version of it. Each item carries attribution. When Eyal has changed his mind or added nuance, we say so.

## Do's

### Start with the internal trigger, not the feature
The most common mistake is starting with "what features should we build?" The Hook Model starts with "what pain is the user trying to escape?" Use the 5 Whys to dig from surface behavior to emotional root cause. If you can't name the internal trigger, you don't have a hook — you have a feature list.

**Source:** *Hooked*, Chapter 2 (Triggers)

### Reduce friction before increasing motivation
When engagement is low, the instinct is to motivate harder — more emails, more incentives, more urgency. Eyal (following Fogg) says this is almost always wrong. First, reduce friction: make the action faster, cheaper, easier, less cognitively demanding, more socially acceptable, more routine. Simplicity beats motivation.

**Source:** *Hooked*, Chapter 3 (Action); BJ Fogg's Behavior Model

### Design the investment to load the next trigger
The investment phase is not just "get users to do more stuff." It has a specific job: improve the product for next use AND load the next trigger. If the investment doesn't create a reason for the user to come back, it's busywork, not a hook component.

**Source:** *Hooked*, Chapter 5 (Investment)

### Check the Manipulation Matrix before you ship
Before launching a habit-forming product, honestly answer: would I use this? Does it materially improve the user's life? If you answer "no" to both, you're a Dealer. This is not a regulatory obligation — it's a personal moral test Eyal considers non-negotiable.

**Source:** *Hooked*, Chapter 8 (Habit Testing and Where to Look for Habit-Forming Opportunities)

### Measure habit formation with the Habit Test
Eyal proposes a three-step diagnostic:
1. **Identify** — who are your habitual users? What percentage of your users are "devotees" (using the product at the frequency you designed for)?
2. **Codify** — what path did habitual users take through the product that non-habitual users didn't? What was their "habit path"?
3. **Modify** — update the product to nudge new users down the habit path.

If fewer than 5% of users are habitual, the hook is broken. Above 5-10% suggests the foundation works.

**Source:** *Hooked*, Chapter 8

### Use the Hook Model as a diagnostic, not just a design tool
The model is as valuable for diagnosing **why** engagement is falling as for designing new features. Walk through each phase: Is the trigger firing? Is the action simple enough? Is the reward variable? Is there an investment that loads the next cycle? The first phase that breaks is usually where the problem lives.

**Source:** Nir Eyal, LeanB2B interview; *Hooked*, Chapter 1

## Don'ts

### Don't confuse hooks with dark patterns
Dark patterns trick users into doing things they didn't intend (hidden charges, confusing opt-outs, bait-and-switch). Hooks form habits by connecting a user's real problem to a genuine solution. The distinction is intent and value: hooks create user value that brings people back; dark patterns extract value by deceiving people. Conflating the two is a category error.

**Author's words:**
> "If used for good, habits can enhance people's lives with entertaining and even healthful routines. If used to exploit, habits can turn into wasteful addictions." — Nir Eyal, *Hooked*, Chapter 1

### Don't use predictable rewards and call them "variable"
Sending the same notification at the same time with the same content is not variable reward — it's a predictable interruption. Variability means the user doesn't know exactly what they'll get. A social feed where every refresh shows different content is variable. A badge system where every action earns the same fixed points is not. Predictable rewards lose potency over time; variable rewards sustain engagement.

**Source:** *Hooked*, Chapter 4 (Variable Reward)

### Don't build hooks for products used infrequently
The Habit Zone requires sufficient frequency. Tax software used once a year, insurance purchased once a decade, or a product used only at quarterly reviews cannot form a habit. Trying to force a hook onto an inherently low-frequency product wastes effort and can annoy users. Different engagement models (excellent service, brand trust, switching cost) are better tools for low-frequency products.

**Source:** *Hooked*, Chapter 1 (The Habit Zone)

### Don't skip the investment phase
Many products nail trigger → action → reward but never close the loop. Without investment, each session is independent — the product doesn't get better for the user over time, and there's no loaded trigger for the next cycle. This is why products with great initial engagement see drop-off: they built 3/4 of the hook.

**Source:** *Hooked*, Chapter 5

### Don't mistake notification spam for triggers
Flooding users with push notifications is not "building triggers." External triggers work when they're well-timed, contextually relevant, and actionable. A push notification that interrupts dinner with irrelevant content trains the user to disable notifications — the opposite of what you want. Quality of triggers matters far more than quantity.

**Source:** *Hooked*, Chapter 2; *Indistractable*, Chapter on hacking back external triggers

## Gotchas (things that go wrong even when you think you're doing it right)

### Variable reward that violates autonomy
You designed a variable reward — great. But if it feels manipulative, coercive, or removes the user's sense of choice, reactance kicks in. People rebel against perceived loss of freedom. Rewards must feel like gifts or discoveries, not traps. The moment users feel "played," the hook breaks permanently and takes trust with it.

**Source:** *Hooked*, Chapter 4; Brehm's Reactance Theory (1966)

### Finite variability masquerading as infinite variability
A puzzle game with 500 levels feels variable — until the user completes them all. A content feed with algorithmic curation has genuinely infinite variability. Products with finite variability eventually become predictable and lose their hook. Diagnose early: is your variability truly open-ended, or is there a ceiling?

> "Experiences with finite variability become increasingly predictable with use and lose their appeal over time. Experiences that maintain user interest by sustaining variability with use exhibit infinite variability." — Nir Eyal, *Hooked*, Chapter 4

### The "vitamin vs. painkiller" trap
Eyal addresses the common VC question "is your product a vitamin or a painkiller?" His answer: habit-forming products start as vitamins (nice to have) and become painkillers (must-have) once the habit is formed. The mistake is dismissing products that look like vitamins early on — the hook is what converts them. But the inverse mistake is also real: assuming any vitamin will become a painkiller if you just hook hard enough. It won't — the underlying value has to be there.

**Source:** *Hooked*, Chapter 1

### Overloading the action phase with features
The action should be the **simplest** behavior in anticipation of reward. When product teams pile features into the action phase (requiring signup, profile creation, preference selection, tutorial completion before the first reward), they're adding friction that kills the loop. The first time through the hook should be nearly frictionless.

## Pro tips (accelerators — small devices that punch above their weight)

### The 5 Whys for trigger discovery
Start with "why would someone use this?" and ask "why?" five times. The surface answer is always functional; the deep answer is always emotional. That emotional root is your internal trigger. Pin your entire hook to it.

**Source:** *Hooked*, Chapter 2

### Map existing behaviors before designing new ones
Before designing your hook, study what the user currently does when the internal trigger fires. They already have a solution (even if it's bad). Your hook has to beat the existing behavior, not just exist alongside it. Eyal: "Instead of relying on expensive marketing or worrying about differentiation, habit-forming companies link their services to the users' daily routines and emotions."

**Source:** *Hooked*, Chapter 2

### Use the Hook Canvas
Eyal provides a one-page canvas that maps all four phases for a single user behavior. Fill it out for your product's core loop. If any quadrant is empty or vague, that's where your hook is weak. Available as a free PDF at nirandfar.com.

**Source:** Nir Eyal, Hooked Model Canvas (nirandfar.com)

### Test the hook with "habit path" analysis
Identify your most engaged users. Work backward from their behavior: what did they do in their first session? Second? Third? The pattern that habitual users share (and that drop-off users don't) is your habit path. Redesign onboarding to accelerate new users down that path.

**Source:** *Hooked*, Chapter 8

## Anti-patterns (the "bad Hooked" the author explicitly names)

### Building hooks without checking the Manipulation Matrix
**What it looks like:** Team builds a highly engaging product but never asks "does this genuinely improve the user's life?"
**Why it fails:** You're building for retention metrics, not user value. Eyal calls this the "Dealer" quadrant — the maker wouldn't use the product and it doesn't help anyone.
**Author's words:**
> "I believe that the trinity of access, data, and speed presents an unprecedented opportunity to create products that improve lives through healthy habits." — Nir Eyal, *Hooked*, Chapter 8

**How to redirect:** Run the Manipulation Matrix honestly. If you land in Dealer, stop and redesign before shipping.

### Treating engagement metrics as proof of value
**What it looks like:** "DAU is up 40%, the hook is working!"
**Why it fails:** Engagement can come from compulsion, not value. A product that triggers anxiety and then briefly relieves it (check email → relief → check again) may have high DAU but be making users' lives worse. Engagement metrics without value metrics are the behavioral design equivalent of vanity metrics.
**How to redirect:** Pair engagement metrics with satisfaction, NPS, time-well-spent, or user-reported value measures. If engagement is high but satisfaction is low, the "hook" may be closer to an addiction loop.

### Copying another product's hook without understanding the internal trigger
**What it looks like:** "Instagram has likes, so we'll add likes to our B2B project management tool."
**Why it fails:** The hook only works when it's connected to a real internal trigger for YOUR users. Instagram likes work because the internal trigger is a desire for social validation around self-expression. A B2B PM tool's internal trigger is uncertainty about project status — likes don't address that.
**How to redirect:** Start from your users' internal trigger, not from another product's solution. Walk the 5 Whys on your own users.

### Gaming variable reward with manipulative mechanics
**What it looks like:** Loot boxes, hidden costs, pay-to-play mechanics disguised as "variable reward."
**Why it fails:** Variable reward is about the anticipation of an uncertain positive outcome that genuinely satisfies a need. Mechanics designed primarily to extract money by exploiting cognitive biases cross from hook to exploitation. Eyal distinguishes between the two — and the Manipulation Matrix is the test.
**How to redirect:** Ask: does this variable reward serve the user's need or the company's revenue? If it's the latter dressed up as the former, it's not a hook — it's a trap.

## Common misapplications (people saying they're doing "Hooked" but aren't)

### "We added gamification, so now we're Hooked"
Points, badges, and leaderboards are not the Hook Model. They can be *part* of variable reward (Rewards of the Self or Tribe), but without a real internal trigger, a simple action, and an investment phase, gamification is decorative. Most gamification layers are bolted on after the product is built — the Hook Model is a design framework that shapes the product from the start.

### "We send push notifications, so we have triggers"
External triggers (including push notifications) are only half the trigger story. The goal is to create internal triggers — emotional associations. Push notifications that are irrelevant, poorly timed, or not connected to a habit loop train users to ignore or disable them. Triggers without the rest of the loop are just interruptions.

### "Our product is addictive, so Hooked worked"
Eyal explicitly separates habits from addictions. Habits are automatic behaviors with little conscious thought that generally benefit the user. Addictions are compulsive behaviors that persist despite harm. If your users report feeling compelled to use the product but don't feel it improves their lives, you haven't built a hook — you've built a trap. Check the Manipulation Matrix.

## Language and vocabulary — say this, not that

- Say **"internal trigger"** not "user motivation" — the trigger is the specific emotional state or situation, not the general concept of being motivated.
- Say **"variable reward"** not "incentive" — the variability is the load-bearing word. Fixed incentives don't create hooks.
- Say **"investment"** not "engagement" — investment is specifically something the user puts in that improves the next cycle. General engagement is too vague.
- Say **"habit"** not "addiction" — Eyal is precise about this distinction. Habits are automatic and generally beneficial; addictions are compulsive and harmful.
- Say **"behavioral design"** not "manipulation" — Eyal uses behavioral design to describe the ethical application of behavioral psychology to product design. Manipulation is what happens without the Manipulation Matrix check.
- Say **"hook"** not "engagement loop" — the hook has four specific phases. "Engagement loop" is vague and misses the structure.

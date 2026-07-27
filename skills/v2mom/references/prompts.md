# V2MOM — Prompt templates

> Copy-paste templates users can adapt. Each starts with a user situation and invokes the skill in a shape Claude or Codex can execute well.

## Draft a company V2MOM from scratch

```
I want to draft a company V2MOM for {{my company}} for the upcoming fiscal year.

Context:
- Company / stage: {{describe — headcount, ARR, stage}}
- Current situation: {{3-5 sentences of where we are right now}}
- Where I'm most stuck: {{one sentence — often Vision or Obstacles}}

Please walk me through V2MOM in Benioff's order (V → V → M → O → M).
Rank the values explicitly. Push me on Obstacles — don't let me skip.
Every method should be an action verb; every obstacle should be paired to a method; every measure should be paired to a method.
Keep the final draft to one page.
```

## Draft an individual V2MOM

```
I want to draft my personal V2MOM for {{my role}} for {{time horizon — usually fiscal year}}.

Context:
- My role: {{describe}}
- My team's V2MOM / OKRs: {{paste if you have them}}
- What my manager expects: {{sentence}}
- Where I'm most stuck: {{sentence}}

Please walk me through V2MOM, making sure my draft:
- Advances my team's methods without cloning them.
- Names 2-3 obstacles that are real for me specifically.
- Ties every measure to a method I control.
- Fits on one page.
```

## Cascade a corporate V2MOM into a team V2MOM

```
Here's our corporate V2MOM:
{{paste corporate V2MOM}}

Help me draft the {{function/team name}} V2MOM that cascades from it.

Push me on:
- Which corporate methods does our team most directly advance?
- What are OUR team-specific values that layer on top of the corporate values (or where we translate them)?
- Our methods should be concrete team actions, not restatements of corporate methods.
- Our obstacles should be team-specific, with countermeasures.
- Our measures should roll up to corporate measures without duplicating them.
```

## Critique an existing V2MOM (or planning doc claiming to be one)

```
Here's a V2MOM (or something claiming to be one) that {{someone}} drafted:

{{paste content}}

Please critique it against Benioff's V2MOM. Specifically:
1. Is the order right (V → V → M → O → M)?
2. Are the values ranked? Do they actually do decision work?
3. Are the methods actions, or are they aspirations / measures in disguise?
4. Are the obstacles real and paired to methods? Or are they environmental commentary / CYA?
5. Are the measures paired to methods, or floating vanity metrics?
6. Does it fit on one page?
7. If this is not a V2MOM, what is it actually — a mission statement, an OKR list, a vision poster? Name it, then offer to convert.
```

## Compare V2MOM to another framework I'm using

```
I'm currently using {{OKRs / VMV / Balanced Scorecard / EOS / other}} for planning.

Help me decide whether V2MOM would serve me better, or whether to stay put.

Push me on:
- What's the actual gap in what I'm using? (OKRs = no values/obstacles context, VMV = no methods/measures, etc.)
- Is switching worth the org's switching cost?
- If I add V2MOM, do I keep my current framework or replace it? Don't let me run two authoritative planning docs in parallel.
```

## Refresh a stale V2MOM (quarterly / mid-year)

```
Here's my V2MOM from the start of the fiscal year:

{{paste original V2MOM}}

Since then:
- {{what has changed — new customers, dropped bets, new obstacles, hires, market events}}

Help me refresh it with beginner's mind (shoshin):
- Which elements are still true? Keep them, but be deliberate.
- Which methods have been overtaken by events?
- Which obstacles have been overcome (celebrate + remove) vs. new ones surfaced?
- Do the measures still make sense given the changed methods?
- Should the Vision or Values shift, or is the plan still under them?
```

## Draft a project-scope V2MOM

```
I'm running {{project — launch / campaign / offsite / integration}} over {{horizon}}.

Help me draft a project V2MOM (same 5 elements, tighter horizon).

Context:
- Goal of the project: {{sentence}}
- Who's involved: {{roles}}
- Known constraints: {{sentence}}

Keep the same load-bearing rules: values ranked, obstacles paired to countermeasures, measures paired to methods, one page.
```

## Reverse-engineer a company's V2MOM from public signals

```
Help me reverse-engineer what {{company name}}'s V2MOM might look like, based on public signals (recent CEO letters, earnings calls, press releases, keynotes).

Follow V2MOM structure:
1. Vision — what better place are they publicly aiming for?
2. Values — what values do they publicly rank, and in what order?
3. Methods — what concrete actions are they taking (product launches, hires, M&A, restructures)?
4. Obstacles — what have they publicly acknowledged as blocking them?
5. Measures — what public numbers are they optimizing for?

Flag which elements are inferable vs. speculative.
Compare to how Benioff writes V2MOM at Salesforce.
```

## Draft the Values section carefully (with ranking)

```
I need to draft the Values section of my V2MOM.

Context:
- Vision I've drafted: {{paste}}
- Culture of the org today: {{sentence}}
- Real conflicts we've had recently where values would have mattered: {{sentence}}

Help me:
1. Draft 3-5 candidate values.
2. Force-rank them.
3. For each pair of top-ranked values, name a specific decision where they'd conflict and confirm which wins.
4. Write one line of description per value that makes it operative (not decorative).
```

## Frame Obstacles without landing badly (post-2023-controversy)

```
I want to name obstacles in my V2MOM but I'm worried about how they'll land publicly.

Draft obstacles for {{context}}, and for each one:
- Frame it as a thing to overcome, not as people/behaviors/values to blame.
- Name a specific countermeasure.
- Sanity-check: if this V2MOM were readable by every employee (as Benioff's is on Chatter), would this obstacle read as fair diagnosis or as accusation?

Reference the 2023 "wellness culture" incident (from `heuristics.md`) as the cautionary tale.
```

## Convert OKRs into a V2MOM

```
Here are our OKRs:

{{paste OKRs}}

Help me convert them into a full V2MOM by:
1. Extracting or drafting the Vision that these OKRs implicitly serve.
2. Naming and ranking the Values that would govern trade-off decisions.
3. Reorganizing the O's into Methods (actions) and the KRs into Measures (paired to methods).
4. Adding the missing Obstacles section — what will make these methods hard?
5. Keeping the whole thing on one page.

If some OKRs shouldn't survive the conversion (e.g., they're vanity metrics), name that and cut them.
```

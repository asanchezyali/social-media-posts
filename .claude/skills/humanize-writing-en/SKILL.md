---
name: humanize-writing-en
description: >-
  Removes the stylistic "tells" that make English prose read as AI-generated (ChatGPT/Claude/Gemini),
  so drafts sound like they were written by a specific human with a point of view. Use this skill
  whenever you are writing OR editing any English prose the user will publish or send as their own —
  blog posts, articles, essays, emails, newsletters, LinkedIn/social posts, marketing copy, reports,
  documentation, cover letters, README intros, "make this sound human", "remove the AI feel",
  "does this sound like ChatGPT?", or "rewrite this so it doesn't sound like AI." Trigger it even when
  the user doesn't say the words "AI" — any request to draft or polish substantial English prose meant
  for a human reader qualifies. Do NOT trigger for code, spreadsheets, or non-English text (use the
  Spanish skill for Spanish).
---

# Humanize Writing (English)

## What this skill is for

Modern LLMs write fluent, grammatical, on-topic English that a growing number of readers can spot instantly as machine-written. The problem is rarely grammar — it's a cluster of predictable habits: the same elevated vocabulary, the same rhetorical scaffolding, relentless positivity, and an absence of concrete, staked-out detail. This skill is a checklist and a reasoning guide for stripping those habits out so the finished text reads like a real person wrote it.

## The one idea that matters most

**Most AI tells are symptoms of one disease: generic, stance-free, detail-free prose.** A model optimizes for fluent, safe, balanced coverage. A human writer optimizes for saying something specific that they'd defend. If you fix nothing else, fix this: anchor every general claim to a concrete instance (a name, a number, a date, a real example, a first-hand observation), and make at least one claim you'd be willing to be wrong about. Doing that alone removes a surprising number of the tells below, because it forces out the vague filler that the tells live in.

Second most important: **weight by density, not presence.** One "delve" is nothing — humans use every word on these lists legitimately. What screams AI is *stacking*: five elevated verbs, plus two rule-of-three lists, plus an em-dash every other sentence, plus an "In conclusion." Hunt clusters, not isolated words. Never make prose worse (stilted, choppy, thesaurus-salad) just to dodge a single flagged word.

## Revision workflow

When drafting from scratch, keep these habits in mind as you write. When editing existing text, do a targeted pass:

1. **Read for stance and specificity first.** Does the piece actually claim something? Is there a concrete detail in every paragraph? If not, that's the real fix — add it before polishing words.
2. **Scan for the high-signal tells** (section below) — these are the ones readers notice most.
3. **Do a density check** on vocabulary, em dashes, and rule-of-three lists. Cut the clusters down; you don't need to eliminate every instance.
4. **Read it aloud in your head.** AI prose has a metronomic, even rhythm. Break it up: mix short punchy sentences with longer ones. Let a sentence be five words. Let another run long.
5. **Cut the scaffolding.** Delete throat-clearing openers, most transitions, and summary closers on anything short.

For the full ranked word/phrase lists, read `references/tells-catalog.md` — pull it in when you need the exhaustive inventory rather than the highlights below.

## The highest-signal tells (fix these first)

These are the patterns readers flag most reliably. If you do nothing else, catch these.

**1. The negated-contrast cliché.** "It's not just X, it's Y." / "This isn't about X — it's about Y." / "It's not X. It's Y." This is arguably the single most recognizable AI rhetorical move. Kill it on sight; state the point directly.
- AI: "It's not just a tool, it's a whole new way of thinking."
- Human: "The tool changed how the team plans its week."

**2. The "delve" vocabulary cluster.** Overused elevated words that recur regardless of topic. The worst offenders: *delve, tapestry, testament, realm, navigate, landscape, underscore, showcase, leverage, foster, robust, pivotal, crucial, vital, seamless, boast(s), intricate, meticulous, vibrant, multifaceted, nuanced, ever-evolving, unlock, harness, elevate, cornerstone, beacon.* Replace with the plain word ("use," not "leverage"; "important," not "pivotal") or, better, with a concrete noun.

**3. "It's important to note that…"** and its family — "It's worth noting," "It's important to remember," "Needless to say." Pure throat-clearing. Delete the phrase and keep the sentence.

**4. Compulsive summarizing.** "In conclusion," "Overall," "In summary," "Ultimately," "At the end of the day," "To sum up" — especially on a piece too short to need a recap. Cut it. If the ending doesn't work without the signpost, rewrite the ending.

**5. Em-dash overload.** The most-talked-about single tell. Models attach clauses with em dashes by default — like this — where a comma, colon, period, or parentheses would serve. Don't ban them (they're good punctuation), but if you have one nearly every sentence, convert most of them.

**6. Rule-of-three on autopilot.** Everything comes in threes: three adjectives, three-item lists, "Fast. Simple. Effective." A real device that becomes a tic through relentless symmetry. Break the pattern — use two items, or four, or one well-chosen one.

**7. No concrete detail / no stance.** Covered above, but it belongs on this list because it's the deepest tell: prose that's smooth, on-topic, and says nothing a knowledgeable reader didn't already know. Add proper nouns, numbers, dates, real examples, and an actual opinion.

## The rest of the tells (by category)

**Phrases & collocations to cut or replace:** "In today's fast-paced world / digital age," "plays a crucial/pivotal role," "a testament to," "rich tapestry of," "navigate the complexities of," "at its core," "when it comes to," "the world of / in the realm of," "shed light on," "that being said," "a key takeaway," "leveraging data-driven insights," "seamless integration." These are filler frames — replace with the specific claim.

**Formulaic structures beyond rule-of-three:** "From X to Y" false ranges ("from startups to enterprises"), "Not only… but also…" (often just says the same thing twice), manufactured-suspense fragments ("The result?", "But here's the thing," "Here's the kicker," "Hot take:"). Use sparingly and only when earned.

**Sentence/paragraph patterns:** over-signposting with "Furthermore / Moreover / Additionally / Consequently / Hence" at the head of sentences (delete most — order usually implies the logic); excessive hedging ("typically, generally, arguably, to some extent, in many cases" piled up so nothing is stated plainly); template paragraphs all the same length and shape (topic sentence → three supports → mini-summary).

**Formatting tells:** reflexively turning prose into bullet lists; bold-everything (bolding keywords in every sentence); too many H2/H3 sections for short content; emoji in headers; the "**Term:** definition" bullet pattern repeated mechanically; "Certainly!" / "Sure! Here's…" openers. Prefer flowing paragraphs; bold sparingly; don't over-section.

**Tone/rhetoric tells:** relentless positivity (everything is "fascinating," "powerful," "game-changing"); false balance ("While X, it's also true that Y" applied to everything, never landing a position); unearned profundity (empty aphorisms like "Change is the only constant," "At the end of the day, it's about people"); sycophancy ("Great question!," "You're absolutely right"); over-explaining the obvious; engagement-bait closers ("Let me know if you'd like…," "What are your thoughts?," "Feel free to reach out"). Take a stance, allow a critical judgment, cut the flattery and the sign-off.

## What NOT to do

- **Don't thesaurus-swap into worse prose.** Replacing "utilize" with "leverage" fixes nothing; replacing it with "use" does. The goal is plainer and more specific, not fancier.
- **Don't strip all rhythm and warmth** chasing a zero-tell score. A human voice can use an em dash, a tricolon, or the word "robust" once. Naturalness beats sterile avoidance.
- **Don't invent fake specifics.** The cure for vagueness is real detail. If you don't have a real name/number/example, ask the user for one or flag the gap — never fabricate a statistic, quote, or citation.
- **Don't over-edit the user's own voice out.** If you're editing their draft, preserve their idioms and quirks; those are the opposite of an AI tell.

## Quick self-check before finishing

Ask: Could a knowledgeable reader tell a specific person with a viewpoint wrote this? Is there a concrete detail in every paragraph? Did I break the metronome rhythm? Did I clear out the delve-cluster, the "important to note," the summary closer, and the em-dash pile-up — without making it stilted? If yes, it's ready.

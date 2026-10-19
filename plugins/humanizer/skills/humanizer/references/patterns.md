# Humanizer Pattern Catalog

Detailed guidance on AI-writing tells and false positives. Consult the relevant numbered section for ambiguous or scanner-flagged passages; use the full checklist for a requested comprehensive audit. The Detection Guidance at the end protects clean human prose from over-editing.

This is reference detail only. Mode routing lives in `SKILL.md`; edit policy, detect behavior, quality checks, and examples live in their dedicated references.

## Contents

- **Content patterns (§1–6):** significance inflation, notability puffery, superficial -ing analyses, promotional language, vague attributions, formulaic "Challenges" sections.
- **Language and grammar patterns (§7–13):** AI vocabulary, copula avoidance, negative parallelisms, rule of three, elegant variation, false ranges, passive voice.
- **Style patterns (§14–19):** em/en dashes, boldface, inline-header lists, title case, emojis, curly quotes.
- **Communication patterns (§20–22):** chatbot artifacts, cutoff disclaimers / speculative gap-filling, sycophantic tone.
- **Filler and hedging (§23–30):** filler phrases, excessive hedging, generic/recap conclusions, hyphenated-pair overuse, persuasive authority tropes, rhetorical signposting, fragmented headers, diff-anchored writing.
- **Structural reflexes (§31–32):** dramatic colon reveals and robotic sentence rhythm.
- **Detection guidance:** what NOT to flag (false positives) and signs of human writing to preserve.

---

## Detection checklist

For a comprehensive audit, walk this list against the actual text. Report meaningful patterns with exact quotes; do not produce `none` rows. **Recording a hit is not a mandate to delete:** clustered tells may need rewriting, while isolated earned choices can stay (see Detection guidance below).

**Fixed-shape tells — `skills/humanizer/scripts/scan.py` finds these mechanically; confirm and resolve each hit.**
- §7 AI vocabulary — delve, underscore, testament, tapestry, showcase, pivotal, leverage, seamless…?
- §14 em/en dashes — clustered or reflexive use that does not match the source voice?
- §15 boldface overuse — bold phrases clustered for mechanical emphasis?
- §16 inline-header lists — bullets starting `**Header:** …`?
- §17 title case headings — headings with every main word Capitalized?
- §18 emojis — decorating headings or bullets?
- §19 curly quotes — typography clustered with pasted chatbot artifacts, not ordinary word-processor output?
- §20 chatbot artifacts — "I hope this helps", "let me know", "here is a…"?
- §21 cutoff / gap-filling — "as of my last", "while specific details are limited", "maintains a low profile"?
- §22 sycophantic tone — "Great question!", "You're absolutely right!"?
- §23 filler phrases — "in order to", "due to the fact that", "it is important to note"?
- §24 excessive hedging — stacked qualifiers like "could potentially possibly"?
- §26 hyphenated word pairs — "cross-functional", "data-driven" (esp. in predicate position)?
- §25 generic / recap conclusions — "the future looks bright", "in conclusion", or a paragraph that only restates the piece?
- §27 authority tropes — "the real question is", "at its core", "what most people get wrong", "the real <noun>"?
- §28 signposting / rhetorical setups — "let's dive in", "what if I told you", "think about it", "plot twist"?

**Partly mechanical now — `skills/humanizer/scripts/scan.py` catches the common shapes; the manual read still owns the variants it can't template.**
- §9 negative parallelism — "isn't X. It's Y", "you don't X. You Y", "Not X, just Y", "not about X, it's about Y", or a clipped tailing negation? scan.py templates the frequent forms and flags the same rhythm repeated across sibling files (set mode). Still walk it manually for forms the regex misses, and remember the clustering rule: one earned contrast stays, the repeated reflex goes.
- §31 colon reveals — "The best part: it learns" or "The detail that makes it work: a separate grader"?
- §32 robotic rhythm — three or more short punchline sentences or repeated sentence/paragraph shapes? The scanner catches one conservative short-sentence shape; the manual read owns the rest.

**Semantic tells — the scan can't see these; this is the read that matters most for recall.**
- §1 significance inflation — sentences puffing up how something "marks a pivotal moment" / "reflects broader trends"?
- §2 notability puffery — listing media coverage / follower counts as proof of importance?
- §3 superficial -ing — trailing "highlighting / reflecting / showcasing…" adding fake depth?
- §4 promotional language — "nestled", "vibrant", "breathtaking", "must-visit", brochure tone?
- §5 vague attributions — "experts argue", "industry reports", "observers have noted" with no source?
- §6 formulaic challenges — a "Challenges and Future Prospects"-style section?
- §8 copula avoidance — "serves as / stands as / boasts / features" where "is / has" would do?
- §10 rule of three — ideas forced into groups of three to sound comprehensive?
- §11 synonym cycling — the same referent renamed each mention (protagonist → main character → hero)?
- §12 false ranges — "from X to Y" where X and Y aren't on one meaningful scale?
- §13 passive voice / subjectless fragments — hidden actor, "No configuration file needed"?
- §29 fragmented headers — a heading restated by a one-line paragraph before the real content?
- §30 diff-anchored writing — narrating a change instead of describing the thing as it is?

Each line points at the full `§N` section below; this checklist is the index, the numbered sections are the detail.

---

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 as part of Spain's decentralization of administrative functions.


### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. This extensive media attention proves her ideas are important. She maintains an active social media presence with over 500,000 followers.

**After:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She has more than 500,000 social media followers.


### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold to reference Texas bluebonnets, the Gulf of Mexico, and the state's landscapes.


### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.


### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> Researchers and conservationists are interested in the Haolai River's role in the regional ecosystem.


### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Korattur faces traffic congestion and water scarcity despite its industrial growth.


## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine includes camel meat and pasta, which became widespread during Italian colonial rule.


### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's contemporary art exhibition space. It has four separate spaces and more than 3,000 square feet.


### 9. Negative Parallelisms and Tailing Negations

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused. So are clipped tailing-negation fragments such as "no guessing" or "no wasted motion" tacked onto the end of a sentence instead of written as a real clause.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item.


### 10. Rule of Three Overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes keynote sessions, panel discussions, and networking opportunities.


### 11. Elegant Variation (Synonym Cycling)

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.


### 12. False Ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The piece discusses the Big Bang, the cosmic web, stars, and dark matter.


### 13. Passive Voice and Subjectless Fragments

**Problem:** LLMs often hide the actor or drop the subject entirely with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite these when active voice makes the sentence clearer and more direct.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> A configuration file is unnecessary. The results are preserved automatically.


## STYLE PATTERNS

### 14. Em and En Dash Clusters

**Problem:** Generated copy often leans on em dashes as a repeated rhythm crutch. The character alone proves nothing; frequency, surrounding template shapes, target surface, and source voice decide whether it belongs.

For short social, sales, and email copy, default to none. In longer prose, keep one or two when the writer already uses them naturally and they work better than a comma, period, or parentheses. Rewrite clusters and decorative interruptions.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.

**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

The scanner reports every dash candidate so the editor cannot overlook a cluster. A justified `KEEP` verdict resolves an isolated use.


### 15. Overuse of Boldface

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.


### 16. Inline-Header Vertical Lists

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface and performance through optimized algorithms, and adds end-to-end encryption.


### 17. Title Case in Headings

**Problem:** AI chatbots capitalize all main words in headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships


### 18. Emojis

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. Users prefer simplicity. Next step: schedule a follow-up meeting.


### 19. Curly Quotation Marks in Chatbot-shaped Copy

**Problem:** Curly quotes can travel with pasted chatbot output, but Word, Google Docs, macOS, and publishing systems also create them automatically. Typography alone is not a writing tell.

**Before:**
> He said “the project is on track” but others disagreed.

**Decision:** Preserve the source typography unless the target format requires straight quotes or curly quotes cluster with other pasted-chat artifacts. Never normalize quotation marks merely to make prose look less AI-written.


## COMMUNICATION PATTERNS

### 20. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> Here is an overview of the French Revolution.


### 21. Knowledge-Cutoff Disclaimers and Speculative Gap-Filling

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that

**Problem:** Two related tells. (a) Older models leave hard knowledge-cutoff disclaimers in the text. (b) When a model can't find a source, it writes a paragraph *about* not finding one and then invents plausible filler to cover the gap. For a private person the guess almost always lands on the same stock phrases ("maintains a low profile," "keeps personal details private"), none of it sourced. Say what isn't known, or cut the sentence; don't dress a guess up as fact.

**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> Available sources suggest the company was founded in the 1990s; the exact year is unconfirmed.

**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

**After:**
> Her early life is not documented in the available sources. (Or omit the section.)


### 22. Sycophantic/Servile Tone

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.


## FILLER AND HEDGING

### 23. Filler Phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"


### 24. Excessive Hedging

**Problem:** Over-qualifying statements.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.


### 25. Generic, Recap, and Fake-profound Conclusions

**Problem:** Generated drafts often finish with vague optimism, repeat the article the reader just read, or add a detachable "deep" line for a mic-drop effect.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> [Omit this paragraph. The source supplies no concrete forecast.]

**Also cut:**

- "In conclusion", "In summary", or a final paragraph that only recaps earlier points.
- A cute metaphor, aphorism, or dramatic fragment that adds no action, evidence, or useful implication.

End on the last concrete point, takeaway, or next action already supported by the draft. Do not replace a fake-profound line with a better fake-profound line.


### 26. Hyphenated Word Pair Overuse

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end

**Problem:** AI hyphenates these uniformly, including in predicate position (`the report is high-quality`). Humans hyphenate inconsistently — typically only when the compound is attributive (`a high-quality report`) and often dropping the hyphen otherwise (`the report is high quality`). Keep attributive-position hyphens; drop them when the compound follows the noun.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.

**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.


### 27. Persuasive Authority and Faux-insight Tropes

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, what most people get wrong, here's what nobody tells you, the part everyone misses

**Problem:** These setups pretend the writer is cutting through noise or revealing hidden expertise. The sentence that follows usually carries the real point without the ceremony.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. Organizational readiness matters.


### 28. Signposting and Rhetorical Setups

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, what if I told you, think about it, plot twist

**Problem:** LLMs announce what they are about to do or ask a theatrical question they immediately answer. This meta-commentary slows the writing down and gives it a tutorial-script feel.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> This section explains how caching works in Next.js.


### 29. Fragmented Headers

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.

**Problem:** LLMs often add a generic sentence after a heading as a rhetorical warm-up. It usually adds nothing and makes the prose feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.


### 30. Diff-Anchored Writing

**Problem:** Documentation or comments written as if narrating a change rather than describing the thing as it is. Unless the document is inherently version-scoped (changelogs, release notes, migration guides), it should read coherently without knowing what changed in the last commit.

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> This function avoids the previous O(n²) iteration.


## STRUCTURAL REFLEXES

### 31. Dramatic Colon Reveals

**Signs to watch:** The best part:, The reason:, The detail that makes it work:, The lesson:

**Problem:** A noun phrase followed by a lowercase reveal creates artificial suspense around an ordinary statement. Colons remain useful for lists, labels, quotations, and real explanations.

**Before:**
> The detail that makes it work: a separate agent grades every draft.

**After:**
> A separate agent grades every draft.

Do not flag ordinary labels such as `Budget: $500`, headings, metadata, or list introductions.


### 32. Robotic Rhythm and Structural Symmetry

**Signs to watch:** Three or more stacked punchline sentences, repeated sentence openings, identical paragraph shapes, or every section following the same point-detail-summary pattern.

**Problem:** Generated prose often repeats one successful beat until the writing feels assembled. Sentence-length variation by itself is not the goal; intentional pacing is.

**Before:**
> It works. It learns. It scales. That's the whole thing.

**After:**
> It works, learns, and scales.

Keep a short sequence when it is an earned rhetorical choice. Rewrite it when the same beat appears repeatedly in the piece or sibling set.


## DETECTION GUIDANCE

### What NOT to flag (false positives)

A clean human writer can hit several of the patterns above without any AI involvement. Before rewriting, sanity-check that you are not gutting legitimate prose. The following are *not* reliable indicators on their own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal registers.** This often signals a person in a technical field, a young writer, or someone with neurodivergent prose habits — not a chatbot.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* fancy words (see §7), not all fancy words. Don't flatten "ostensibly" or "constituent" just because they sound brainy.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them. Judge frequency, target surface, and source voice.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; repeated dashes plus rule-of-three plus *vibrant tapestry* plus a "Conclusion" section is a strong editing signal.


### Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone — they are evidence of a real person writing, and over-editing will destroy what makes the piece sound human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. A weird quote. The phrase "the lawyer who used to work upstairs from my dentist." LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't fully explain why." LLMs default to clean takes.
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or used a particular word, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Known provenance.** Use source history to understand context, never to produce an AI-authorship score or certainty claim.

# Example `/study:quiz photosynthesis` session

This is an example transcript of the adaptive quiz loop on the sample handout (`S1`). Student answers are illustrative. The quiz asks one question at a time; questions are grouped here to keep the example short.

---

**Student:** /study:quiz photosynthesis

**Claude:** Round 1: 5 questions on photosynthesis, mixed types, medium difficulty. One at a time.

### Round 1

**Q1 · multiple choice · light-dependent reactions · difficulty 2**
Chlorophyll loses electrons during the light-dependent reactions. Where do the replacement electrons come from?
A) Carbon dioxide · B) Water · C) NADPH · D) Glucose

> **Student:** B

✓ **Correct.** Water is split (photolysis) to replace the electrons chlorophyll loses, which is also why the released oxygen comes from water. Source: [S1 ¶6]

**Q2 · fill in the blank · Calvin cycle · difficulty 1**
In carbon fixation, the enzyme ________ attaches CO₂ to RuBP.

> **Student:** rubisco

✓ **Correct.** Rubisco catalyzes carbon fixation, joining CO₂ to the five-carbon sugar RuBP. Source: [S1 ¶7]

**Q3 · true/false · Calvin cycle · difficulty 2**
Because the Calvin cycle is called the "light-independent reactions", it can keep running for a long time in the dark.

> **Student:** True

✗ **Not quite: it's false.** The Calvin cycle doesn't use light *directly*, but it needs the ATP and NADPH made by the light-dependent reactions. In the dark those run out, so the cycle stops soon. The name is about what it uses directly, not about whether it works in the dark. Source: [S1 ¶7]

**Q4 · short answer · light-dependent reactions · difficulty 2**
Explain how ATP synthase makes ATP during the light-dependent reactions.

> **Student:** Electrons from the transport chain go through ATP synthase and that makes ATP.

◐ **Partly right.** You have the right enzyme and the right link to the electron transport chain. The missing key point: the electrons don't go through ATP synthase. Their energy is used to **pump protons (H⁺) into the thylakoid space**, and it's the **protons flowing back out** through ATP synthase that drive ATP production. Source: [S1 ¶5]

**Q5 · explain the significance · overview · difficulty 2**
Explain the significance of photosynthesis for food chains.

> **Student:** Producers make their own sugar from light, CO₂ and water, so they're the start of almost every food chain, and other organisms eat them to get that energy.

✓ **Correct.** You covered the key points: producers (autotrophs) make food from inorganic molecules using light energy, and almost every food chain starts with them. Source: [S1 ¶1]

**Round 1: 3.5 / 5.** Logged 5 answers. Added 2 entries to your error log:

```json
{"id":"e-20261023-001","ts":"2026-10-23T16:12:00","topic":"calvin-cycle","type":"tf","question":"The Calvin cycle can keep running for a long time in the dark.","student_answer":"True","correct_answer":"False","why_wrong":"Took 'light-independent' literally; missed that the cycle depends on ATP and NADPH from the light-dependent reactions.","source":"[S1 ¶7]","times_missed":1,"streak":0,"resolved":false,"resolved_ts":null}
{"id":"e-20261023-002","ts":"2026-10-23T16:15:00","topic":"light-reactions","type":"short","question":"Explain how ATP synthase makes ATP.","student_answer":"Electrons go through ATP synthase.","correct_answer":"Electron energy pumps H+ into the thylakoid space; H+ flowing back through ATP synthase drives ATP synthesis.","why_wrong":"Thought electrons flow through ATP synthase instead of protons (missed the proton gradient).","source":"[S1 ¶5]","times_missed":1,"streak":0,"resolved":false,"resolved_ts":null}
```

**Plan for round 2:**
- Calvin cycle: Q2 right → a harder question (apply, difficulty 3); Q3 missed → a **new** question on why it depends on light, from a different angle.
- Light-dependent reactions: Q1 right → harder (difficulty 3); Q4 partial → a **new** question on the proton gradient, in a different format.
- Overview: right → covered by the harder questions above.

### Round 2

**Q6 · short answer · Calvin cycle · difficulty 2** (new angle on Q3's mistake)
Name the two products of the light-dependent reactions that the Calvin cycle needs, and say what happens to the cycle when they run out.

> **Student:** ATP and NADPH. When they run out, for example in the dark, the Calvin cycle stops.

✓ **Correct**, and that's exactly the link Q3 was testing. Source: [S1 ¶7]

**Q7 · multiple choice · light-dependent reactions · difficulty 2** (new format on Q4's mistake)
What flows through ATP synthase to drive the production of ATP?
A) Electrons · B) Protons (H⁺) · C) Water molecules · D) NADPH

> **Student:** B

✓ **Correct.** Protons pumped into the thylakoid space flow back out through ATP synthase. Source: [S1 ¶5]

**Q8 · calculation · Calvin cycle · difficulty 3**
A plant fixes 18 molecules of CO₂ in the Calvin cycle. How many G3P molecules leave the cycle, and how many glucose molecules can be made from them?

> **Student:** 6 G3P, so 3 glucose.

✓ **Correct.** One G3P leaves for every 3 CO₂ fixed (18 ÷ 3 = 6), and each glucose needs 2 G3P (6 ÷ 2 = 3). Source: [S1 ¶8]

**Q9 · short answer · light-dependent reactions · difficulty 3**
A plant is given water labelled with a heavy isotope of oxygen. Where would you expect to find the label after photosynthesis, and why?

> **Student:** In the oxygen gas that's released, because the O₂ comes from splitting water.

✓ **Correct.** That's the classic evidence that released O₂ comes from water, not CO₂. Source: [S1 ¶6]

**Round 2: 4 / 4.** Both mistakes from round 1 were answered correctly with new questions, so each error-log entry now has `streak: 1`. They'll come back once more in a later session (`/study:review-mistakes`) before they count as resolved.

**Summary**
- Solid: overview, carbon fixation and Rubisco, photolysis and where O₂ comes from, G3P arithmetic.
- Revisit: the proton gradient and ATP synthase (new today), and the Calvin cycle's dependence on light.
- Next: want flashcards for the two stages (`/study:flashcards photosynthesis`)? I'd review the two logged mistakes again in 2–3 days.

---

Lines appended to `quizzes/history.jsonl` (first and last shown):

```json
{"ts":"2026-10-23T16:10:00","quiz":"q-20261023-1","mode":"quiz","round":1,"topic":"light-reactions","type":"mcq","difficulty":2,"correct":true,"source":"[S1 ¶6]"}
{"ts":"2026-10-23T16:24:00","quiz":"q-20261023-1","mode":"quiz","round":2,"topic":"light-reactions","type":"short","difficulty":3,"correct":true,"source":"[S1 ¶6]"}
```

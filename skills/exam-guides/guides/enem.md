# ENEM (Exame Nacional do Ensino Médio)

> Starter outline, original summary. Official source: **INEP** (gov.br/inep), the yearly *edital* and the *Cartilha do Participante* for the essay. Last checked: October 2026. Confirm dates and rules in the current edital.

Brazil's national secondary-school exam, used for university entry (SISU, ProUni, FIES) and by many universities directly.

## Format

| Day | Areas | Objective questions | Time |
|---|---|---|---|
| Day 1 | Linguagens, Códigos e suas Tecnologias (incl. 5 foreign-language questions: English or Spanish) + Ciências Humanas e suas Tecnologias + **Redação** | 45 + 45 | 5 h 30 min |
| Day 2 | Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias | 45 + 45 | 5 h |

- 180 multiple-choice questions (five options each) plus one essay.
- Objective areas are scored with **TRI** (Teoria de Resposta ao Item, item response theory): consistency matters, so a pattern of right answers on easy items and wrong answers on hard ones scores better than the reverse. Guessing hard items while missing easy ones is penalized by the model, not by a fixed deduction.
- The essay (**redação**) is a *dissertativo-argumentativo* text on a social, scientific, cultural or political theme given on the day, written by hand, 7 to 30 lines (very short texts, leaving the theme, or ignoring the required text type can score zero).

### Redação: five competencies, 0–200 points each (total 0–1000)

1. Command of the formal written standard of Portuguese.
2. Understanding the prompt and developing the theme within the structure of an argumentative essay, using knowledge from different areas.
3. Selecting, relating, organizing and interpreting information and arguments in defense of a point of view.
4. Using cohesion devices (connectives, reference) to build the argument.
5. Proposing a detailed **intervention** to the problem that respects human rights (agent, action, means, purpose, detail).

## Topic outline

| Area | Starter topics (`id`) |
|---|---|
| Linguagens | text interpretation and genres (`interpretacao-textual`), linguistic variation (`variacao-linguistica`), literature and literary movements (`literatura`), arts and culture (`artes`), body practices and sport (`educacao-fisica`), information technology and media (`tecnologias-comunicacao`), foreign language reading (`lingua-estrangeira`) |
| Ciências Humanas | Brazilian history (`historia-brasil`), world history (`historia-geral`), geography, environment and territory (`geografia`), urbanization and population (`urbanizacao-populacao`), philosophy (`filosofia`), sociology, citizenship and human rights (`sociologia-cidadania`) |
| Ciências da Natureza | ecology and environment (`ecologia`), cell biology and genetics (`biologia-celular-genetica`), human physiology and health (`fisiologia-saude`), mechanics and energy (`mecanica-energia`), electricity and waves (`eletricidade-ondas`), chemical reactions and stoichiometry (`reacoes-estequiometria`), organic chemistry (`quimica-organica`), environmental chemistry (`quimica-ambiental`) |
| Matemática | proportions, percentages and financial math (`proporcao-porcentagem`), functions and graphs (`funcoes`), plane and spatial geometry (`geometria`), statistics and data reading (`estatistica`), probability and combinatorics (`probabilidade-combinatoria`), scales and measurement (`grandezas-medidas`) |
| Redação | essay structure (`redacao-estrutura`), building arguments with repertoire (`redacao-repertorio`), intervention proposal (`redacao-intervencao`) |

ENEM doesn't publish percentage weights by topic; coverage varies by year. Interdisciplinary, context-heavy questions (charts, maps, news excerpts, everyday situations) are typical in every area.

## Skills the exam rewards

- Reading long contexts fast and finding what the question actually asks.
- Interpreting graphs, tables, maps and infographics.
- Applying basic science and math to everyday and environmental situations.
- Managing time over a long day: about 3 minutes per objective question, with time reserved for the essay on day 1.

## Common traps

- Spending too long on a few hard questions; with TRI, securing the easy and medium items matters most.
- Essay: ignoring the motivating texts' theme focus, writing a vague or incomplete intervention proposal, or proposals that disrespect human rights.
- Leaving answers blank at the end: there's no fixed penalty for wrong answers.

## Using the plugin

- `/study:course new ENEM 2026` seeds these topics; `/study:exam-plan` with both exam days.
- `/study:mock-exam` with a half-length area (e.g. 45 Natureza questions in about 2 h 15 min), or `/study:past-paper` with an old ENEM paper from INEP's site.
- Essay practice: write the essay yourself, then use `/study:feynman`-style feedback on each competency. Claude can mark against the five competencies but must not write the essay for you.

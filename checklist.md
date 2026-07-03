# Citation Faithfulness Audit

Auditing all citations in the manuscript against source PDFs in `literature/EnergyBurden/`.

## Status

- ✅ = 100% faithful
- ⚠️ = Partial issue noted
- ❌ = Unfaithful
- ⬜ = Not yet checked

---

### 1. Antunes et al. (2023) — Antunes2023.pdf
✅ All 5 instances faithful. Cited for: energy burden definition [12], fuel poverty terminology in Europe [19], 2M indicator [21], threshold limitations [22], multiple thresholds approach [47]. Paper is about European energy affordability measurement — all uses are appropriate.

### 2. Awan et al. (2022) — Awan2022.pdf
✅ 9 instances faithful: rural burden higher [25][78], low-income → burden [27], demographics [29], agricultural employment ↓ burden [103], renters lower [134], assets ↓ poverty [118].
⚠️ 4 stretched: urban→education mechanism [35], cooking focus [117], cooling exclusion [125], education channel mechanism [141].
❌ 3 unfaithful (contradiction): [119][122][124] cite Awan for asset ownership INCREASING energy burden, but Awan finds durable asset index is NEGATIVELY linked with energy poverty ("more affluent households are less energy poor", line 1263-1268). TV, fan, AC all included in Awan's asset index. Fix: remove Awan from these citations or note contrast.

### 3. Banerjee et al. (2021) — Banerjee2021.pdf
✅ 1 citation [20]: generic support for "energy burden as a critical policy concern." Paper finds energy poverty negatively affects health/education in 50 developing countries. Faithful.

### 4. Bouzarovski (2014) — Bouzarovski2013.pdf
✅ [37] housing/heating path-dependency, retrofitting — all in paper (e.g., line 305: "inefficient homes", 477: "trapped" in housing/heating arrangements, 506-508: retrofitting policy).
✅ [103] farmers in Poland have above-average energy burdens (Table 1, lines 910-912), supporting "contrary findings in Europe" to Awan.
⚠️ [104] Bouzarovski's Table 1 shows self-employed energy burdens (9.6-11.8%) but paper doesn't discuss "energy stability" or identify a "trend" — it's a 2010 cross-section.

### 5. Brown et al. (2020) — Brown2020.pdf
✅ [12] energy burden as measure of affordability — paper's core subject.
✅ [20] health consequences: thermal discomfort, respiratory, mental health (lines 478-482).
⚠️ [25] "inefficient fuels" slightly stretched for US-focused paper, but rural higher burden and limited infrastructure are supported (lines 327-330: rural higher bills, older housing stock).
✅ [137] contrasting finding (temporary housing ↓ burden vs Brown's manufactured homes ↑ burden) — accurate contrast (lines 1423-1426).

### 6. Chan & Delina (2023) — ChanDelina2023.pdf
✅ 2 generic/supporting citations [12][25]. Paper reviews energy poverty studies in Asia, discusses urban-rural dynamics, urbanization, urban energy poverty. Both citations are appropriate general support.

### 7. Colton et al. (2011) — Colton2011.pdf
✅ 1 citation [21]: 6% threshold definition (utility costs ≤20% of shelter ≤30% of income). Paper states exactly this at lines 173-178.

### 8. Cyrek & Cyrek (2022) — Cyrek2022.pdf
✅ 1 citation [103]: agricultural employment ↑ energy poverty in EU (contrary to Awan's Pakistan finding). Abstract line 20-21: "agricultural employment as a factor increasing energy poverty." Accurate.

### 9. Das et al. (2022) — Das2022.pdf
✅ [22] logistic regression with thresholds — correct.
✅ [102] wage employment reduces burden (full-time earners 55% less likely) — correct.
✅ [116] cooking appliances odds ratio 1.0006*** (increases burden) — correct.
✅ [118] refrigerators/freezers odds ratio 0.9992 (insignificant) — correct.
✅ [124] ACs odds ratio 0.9993 (insignificant) — correct.

### 10. Dogan et al. (2022) — Dogan2022.pdf
✅ [12] cited for "equity" — paper examines race and energy poverty, discusses social equity. Appropriate generic reference.
✅ [56] listed in methodology/variable description section — standard practice.

### 11. Dong et al. (2018) — Dong2018.pdf
⚠️ [28] cited for rural heating needs → higher energy burden. Paper studies energy CONSUMPTION in China, not energy burden (expenditure/income ratio). Reasonable inference but Dong doesn't directly study burden. Minor stretch.
Note: Dong et al. (2021) (K. Dong) also cited at [103] but no PDF available.

### 12. Drehobl & Ross (2016) — Drehobl_Ross2016.pdf
✅ [12] equity — ACEEE report on LMI energy burden. Correct.
✅ [25] urban households struggle with electricity prices, poor housing efficiency — US cities focus, correct.
✅ [27] low-income → disproportionately high burdens — report's core subject. Correct.
✅ [28] inefficient dwellings/appliances exacerbate burden — discussed in report. Correct.
✅ [134] renters higher burden — report shows renters have elevated burdens. Correct.

### 13. Drehobl et al. (2020) — Drehobl_etal2020.pdf
✅ [20] policy concern — ACEEE report about US energy burden, correct.
✅ [21] threshold-based approaches — report uses 6%/10% thresholds, correct.
✅ [47] U.S. average energy burden comparisons — report describes this approach, correct.
✅ [78] Low-Income High-Cost phenomenon — report's core topic, correct.
✅ [107] rising income → lower burden — report establishes this relationship, correct.

### 14. Guan et al. (2023) — Guan2023.pdf
✅ [28] Russia-Ukraine conflict raised energy costs 62.6–112.9%, expenditure +2.7–4.8%. Manuscript rounds to 63–113%. Essentially accurate.

### 15. Jones (1991) — Jones1991.pdf
✅ [13] urbanization → transportation energy use — abstract: "largest source of change is personal transportation." Correct.
✅ [34] rural-urban migration → income rise — general development economics framing; reasonable.
✅ [35] motorized transport, commuting, fuel expenditure — paper discusses transport energy use extensively. Correct.
✅ [36] fuel choice, modern displaces traditional — paper: "Urbanization consistently displaces traditional energy with modern energy." Correct.
✅ [103] traditional agriculture consumes no fuel, modern machinery — paper: "energy not used in traditional agriculture" and agricultural mechanization discussed. Correct.
✅ [115] — cited in context of motor vehicles/transport. Correct.

### 16. Liddell & Morris (2010) — LiddelMorris2010.pdf
⚠️ [20] cited for "reduce spending on food, healthcare, and education." Paper discusses food-heating tradeoffs (lines 719-722) but does not mention reducing healthcare or education spending. Education only appears as a covariate. Fix: drop "healthcare, and education" or find a source that supports these.

### 17. Madlener & Sunak (2011) — Madlener_Sunak2011.pdf
✅ [12] urban-rural differences in income, infrastructure, appliances — paper covers these, correct.
✅ [13] urbanization → energy demand, technology, infrastructure — paper's core topic, correct.
✅ [34] rural-urban migration, labor transfer to industry/services, income rise — lines 523-526. Correct.
✅ [35] UHI effect, cooling demand, AC use — lines 592-602, 725-729. Correct.
⚠️ [97] "Engel-curve dynamics" — paper discusses income-energy relationship but not Engel curves specifically. Minor stretch.
✅ [98] incomes increase energy use in urbanized environments — correct (line 838: "urbanization accompanied by increasing incomes").
✅ [124] UHI → AC adoption — correct (lines 592-602, 725-726).
✅ [145] behavioral mechanisms, appliance ownership — correct.

### 18. Mahumane & Mulder (2022) — MahumaneMulder2022.pdf
⚠️ [29] "negligible effects" of demographics — paper finds mixed effects; some demographic variables are significant in some specifications. Slight overstatement.
⚠️ [125] "exclusion of cooling" — paper doesn't discuss cooling. It focuses on energy consumption/expenditure and transport. The claim is an inference from absence, not an explicit finding. Stretch.
✅ [115] transport energy in Mozambique — paper discusses transport energy neglect in surveys, relevant context.

### 19. Mirza & Kemp (2011) — MirzaKemp2011.pdf
✅ [36] fuel choice, traditional biomass (firewood, agricultural waste), low/zero monetary cost — paper studies fuel choices in rural Pakistan, discusses firewood collection vs purchase. Correct.
✅ [103] fuel choice mechanism, biomass self-sufficiency — consistently cited. Correct.
✅ [116] fuel choice context for cooking — appropriate. Correct.

### 20. Oum (2019) — Oum2019.pdf
✅ [25] urban areas associated with higher energy burden — paper finds urban variable significant for energy poverty (2). Correct.
❌ [27] "income elasticity for energy expenditure is below 1" — paper does NOT discuss income elasticity at all. Fix: attribute only to Menyhért.
⚠️ [125] "exclusion of cooling" — paper mentions cooling (line 191,193) but doesn't focus on it. Stretch.
❌ [135] "house size... largely insignificant" — Oum studies household SIZE (number of persons, line 317, 447), not dwelling area/"house size." Different concept.
⚠️ [144] "narrowing gap as seen in Laos" — Oum doesn't discuss urban-rural gap convergence/narrowing over time.

### 21. Pereira & Marques (2022) — Pereira_Marques2023.pdf
✅ [26] energy source choices influence energy burden differently across urbanisation degrees — abstract: "energy forms have differing impacts on energy poverty in areas with different levels of urbanisation." Correct.

### 22. Riva et al. (2021) — Riva_etal2021.pdf
✅ [21] threshold approach — paper uses 10% threshold. Correct.
✅ [22] logistic regression with socio-demographic/geographic factors — paper uses logistic regression. Correct.
✅ [25] rural areas higher odds — abstract: "odds of energy poverty almost twice as high... in rural areas." Correct.
✅ [29] demographic factors predict energy poverty — paper finds one-person, lone-parent, older households higher odds. Correct.
✅ [47] threshold-based classification — expenditure-based indicators. Correct.
✅ [78] rural higher in Canada — same as [25]. Correct.
✅ [134] renters higher burden — "energy poverty is significantly higher for renters in urban centers." Correct.
✅ [140] single-person households contrast — Riva finds one-person households have higher odds; manuscript finds lower. Accurate contrast.
✅ [144] heating costs in advanced economies — Canada's cold climate context discussed. Correct.

### 23. Roberts et al. (2015) — Roberts_etal2015.pdf
✅ [19] fuel poverty in Europe — UK study, correct.
✅ [25] rural higher burden due to housing stock, limited energy sources — paper discusses this. Correct.
✅ [26] urban longer persistence, rural vulnerable to price increases — abstract exactly matches. Perfect.
✅ [30] historical insights from panel data — paper uses panel data 1997-2008. Correct.
✅ [80] UK trajectory 1997-2008 — correct.

### 24. Robinson et al. (2018) — Robinson2018.pdf
✅ [78] LIHC indicator — paper's core focus is "Low Income High Cost (LIHC) indicator." Correct.

### 25. Ross et al. (2018) — Ross2018.pdf
✅ [12] equity — ACEEE report on rural energy burden. Correct.
✅ [19] energy burden definition — report defines energy burden. Correct.
✅ [37] institutional factors, program/subidy access — report extensively discusses energy efficiency programs, bill assistance, policy. Correct.

### 26. Simcock et al. (2021) — Simcock_etal2021.pdf
✅ [29] regional market structures, subsidy policies, economic conditions — review paper covering structural/spatial factors of energy poverty. Generic support, appropriate.

### 27. Sy & Mokaddem (2022) — Sy_Mokaddem2022.pdf
✅ [25] urban-rural energy burden dynamics in developing economies — review paper on energy poverty in developing countries. Appropriate.

### 28. Zhang et al. (2023) — ZhangL_etal2023.pdf
✅ [19] energy poverty definition in developing nations — China study, correct.
✅ [25] "urban areas with higher energy burdens" — paper finds urban 22.8% vs rural 10.7% EP rate (line 459-460). Correct.
✅ [47] threshold-based classification — paper uses 10% threshold. Correct.
✅ [78] "aligns with China's experience" — paper supports urban higher burden pattern. Correct.
✅ [144] "similar to China" — same as above. Correct.

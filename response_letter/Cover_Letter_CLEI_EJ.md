# Cover Letter — Submission of Extended Version

**To:** Editor-in-Chief, CLEI Electronic Journal (CLEI EJ)  
**Date:** November 13, 2026  

**Subject:** Submission of an extended version of CLEI 2026 Submission #37  

Dear Editor-in-Chief,

We are pleased to submit the extended version of our paper entitled **"Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Experimental Investigation"** for consideration for publication in the *CLEI Electronic Journal*.

This manuscript is an extended version of a paper originally presented at CLEI 2026 (Submission #37). The original conference paper reported a preliminary pre/post UTAUT acceptance analysis of a one-group pretest-posttest study in which undergraduate Computer Science students used ChatGPT 3.5 to redesign a browser-based memory game for older adults. The present extended version preserves the original research questions and experimental protocol, but adds substantial new empirical, qualitative, and pedagogical material, as summarized below.

## Summary of Extensions

1. **Objective accessibility audit of AI-generated artifacts (new Section 6.2, Table 8).** We conducted a systematic heuristic evaluation of the 26 submitted executable HTML5/JavaScript game interfaces against WCAG 2.1 Level AA and gerontechnology criteria, quantifying adoption rates across eight accessibility dimensions (font scaling 100%, pacing control 100%, textual color labels 100%, multimodal audio 92.3%, keyboard navigation 69.2%, WAI-ARIA semantics 61.5%, round-state indicators 50.0%, high-contrast toggle 30.8%). This addresses the conference reviewers' primary critique that the original study evaluated only subjective perceptions.

2. **Prompt evolution analysis and the Effort Expectancy Paradox (new Section 6.4, Table 9).** We categorized participants into three interaction-volume tiers (Low: 2–3 prompts, $n = 9$; Moderate: 4 prompts, $n = 11$; High: 5–7 prompts, $n = 6$) and documented a three-layer hierarchical progression in how accessibility features are successfully elicited from the LLM. We further identified a negative association between prompt iteration volume and post-intervention Effort Expectancy, which we designate as the *Effort Expectancy Paradox*.

3. **Expanded inferential statistics (new Sections 5.3–5.6).** The conference version reported only paired $t$-tests as inferential statistics. The extended version adds Wilcoxon signed-rank tests (zero differences excluded, effective sample size $N_{\text{eff}}$ reported), Cohen's $d$ effect sizes, Bonferroni correction for multiple comparisons, granular item-level Wilcoxon tests for all 15 survey statements (Table 5), and non-parametric Mann-Whitney U subgroup comparisons between GenAI novices ($n = 5$) and experienced users ($n = 36$) (Table 6). All subgroup findings are qualified with respect to the small novice sample.

4. **Substantially expanded Discussion (Section 7).** We develop the theoretical interpretation of the baseline ceiling effect, the **Refinement Friction** construct within Effort Expectancy, and the **reality-calibration** effect on Facilitating Conditions that explains the significant post-intervention declines in FC and SI.

5. **New pedagogical framework (new Section 8).** We propose a four-phase framework for integrating GenAI into interaction design and accessibility curricula.

6. **New structured Threats to Validity (Section 9)** covering construct, internal, external, and conclusion validity.

7. **Complete open-science replication package.** De-identified datasets, a data dictionary, an executable Google Colab notebook reproducing all statistical tables and figures, and all analysis scripts are permanently deposited on Zenodo (DOI: [10.5281/zenodo.24198695](https://doi.org/10.5281/zenodo.24198695)) and mirrored in a public GitHub repository ([https://github.com/alkawamo/clei-genai-study](https://github.com/alkawamo/clei-genai-study)).

## Note on Dataset Verification and Analysis Harmonization

The final analyzed cohort consists of $N = 41$ complete paired pre/post observations, matching the sample size reported in the conference version. The raw collection originally contained additional respondents who were excluded due to incomplete pre- or post-test records; this exclusion was applied at the data collection stage, prior to the conference analysis, so that the same set of 41 complete paired records forms the analytical basis of both versions. This continuity is evidenced by the identical baseline pre-intervention construct means across versions (PE: 4.22, EE: 4.30, SI: 3.92, FC: 4.51, BI: 4.24).

Between the conference submission and this extended manuscript, the dataset underwent a full verification and open-science curation process in preparation for FAIR-compliant deposition on Zenodo. This process involved automated re-scoring directly from the raw questionnaire instruments, cross-verification of demographic coding, and systematic re-computation of all post-intervention metrics via reproducible Python scripts, replacing the preliminary spreadsheet tabulations used during the initial conference submission. Some item-level codings were harmonized (reflected, for example, in the revised pre-test reliability coefficient for Behavioral Intention, from $\alpha = 0.810$ to $\alpha = 0.873$), and the post-test means, test statistics, and $p$-values were corrected.

These corrections are substantive rather than cosmetic. Three constructs that were not statistically significant in the preliminary conference analysis (SI, FC, BI) reach significance in the present verified analysis (SI: $p = 0.007$; FC: $p < 0.001$; BI: $p = 0.012$, by paired $t$-test), while PE and EE remain non-significant. The statistical conclusions of the manuscript have therefore been revised accordingly, and the present Discussion section is built around this revised pattern of results. Every value, test statistic, and table reported here is deterministically reproducible from the Zenodo replication package.

## Compliance with the Extended-Paper Requirement

We estimate that the additions above correspond to approximately 45% new content relative to the original conference paper, exceeding the CLEI EJ minimum requirement of 30% substantial, non-trivial additions. A section-by-section comparison is provided below.

## Standard Declarations

- This manuscript is original, has not been published elsewhere, and is not under consideration by any other journal.
- All authors have read and approved the submitted version and agree to its submission to CLEI EJ.
- The study was approved under institutional ethical standards, and all participants provided informed consent prior to data collection. All data have been de-identified.
- The authors declare no conflicts of interest.
- The replication package is publicly available as described above.

## Corresponding Author

**Daniela Marques**  
Federal Institute of São Paulo (IFSP), Hortolândia-SP, Brazil  
marquesdaniela@ifsp.edu.br  

We thank you for considering this manuscript and look forward to your response.

Sincerely,  
Daniela Marques, André Luiz Satoshi Kawamoto, and Valéria Farinazzo Martins  

---

## Appendix to the Cover Letter — Section-by-Section Comparison

| Section in Extended Version | Status relative to Conference Version | Description |
| :--- | :--- | :--- |
| **1. Introduction** | Revised and expanded | Reframed contribution statement; six explicit contributions; open-science statement. |
| **2. Theoretical Background** | Expanded | New Section 2.3 (critique of UTAUT for non-deterministic GenAI) introducing the Refinement Friction construct. |
| **3. Related Work** | Substantially expanded | Conference version cited 3 studies; extended version cites 9 studies (adding 6 new works) and adds a comparative synthesis table (Table 1). |
| **4. Experimental Methodology** | Expanded | New Table 2 (workshop syllabus); new Appendix A (full questionnaire items); ethical safeguards detailed. |
| **5. Empirical and Statistical Results** | **Major revision and expansion** | Recomputed with corrected automated scoring; Wilcoxon tests, Cohen's *d*, Bonferroni correction, item-level tests (Table 5), subgroup Mann-Whitney comparisons (Table 6), prompt iterations by UI experience (Table 7). |
| **6. Prompt Engineering Dynamics and Objective Code Audit** | **Entirely new** | Qualitative patterns of interaction logs; objective accessibility audit (Table 8); thematic analysis; prompt evolution tiers (Table 9). |
| **7. Discussion** | Substantially expanded | Ceiling effect, Refinement Friction, reality calibration; reinterprets the significant FC/SI declines and BI gain. |
| **8. Pedagogical Guidelines** | **Entirely new** | Four-phase framework for HCI education. |
| **9. Threats to Validity** | **Entirely new as a structured section** | Construct, internal, external, and conclusion validity. |
| **10. Conclusion and Future Work** | Revised | Structured theoretical vs. empirical vs. pedagogical contributions; updated future directions. |
| **Appendices A and B** | **Entirely new** | Full survey instrument (Portuguese + English); accessibility heuristics checklist. |

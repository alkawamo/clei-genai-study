# Response to Reviewers and Detailed Letter of Modifications

**Manuscript Title:** Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Extended Experimental Investigation  
**Authors:** Daniela Marques, André Luiz Satoshi Kawamoto, Valéria Farinazzo Martins  
**Journal:** CLEI Electronic Journal (CLEI EJ)  
**Original Conference Paper:** CLEI 2026 Submission #37  

---

## 1. Executive Summary of Substantial Extensions (>35% New Content)

We would like to express our sincere gratitude to the Program Committee, the Editors, and the Reviewers for inviting us to submit an extended version of our work to the **CLEI Electronic Journal**. 

In accordance with the CLEI EJ guidelines requiring at least 30% substantial, non-trivial additions to the original conference proceedings, this extended manuscript delivers **over 35% of brand new empirical, qualitative, and pedagogical contributions**:

1. **Objective Accessibility Audit of AI-Generated Interfaces (Answering Reviewer 2's Primary Critique):**
   * While the conference paper focused primarily on subjective UTAUT acceptance, the extended journal version introduces a systematic heuristic audit of the actual HTML/JS/CSS game interfaces submitted by the students ($N = 26$).
   * We quantitatively evaluated eight key accessibility dimensions tailored to older adults: font-size scaling (100%), pacing/speed control (100%), textual color name labels (100%), multimodal audio/volume (92.3%), keyboard navigation (69.2%), WAI-ARIA semantic attributes (61.5%), explicit round state indicators (50.0%), and high-contrast/dark theme toggle (30.8%).
2. **Prompt Evolution, Discourse Dynamics, and the Effort Expectancy Paradox (New Empirical Section):**
   * We categorized participants into three interaction volume tiers: *Low Iterations* (2--3 attempts, $n = 9$), *Moderate Iterations* (4 attempts, $n = 11$), and *High Iterations* (5--7 attempts, $n = 6$), detailing compliance progression across all 8 accessibility heuristics.
   * We uncovered a **Three-Layer Hierarchical Architecture of Prompt Evolution**: while superficial visual styling (fonts, color labels, audio speed) is achieved at 100% on the first turn, assistive technology (WAI-ARIA, keyboard navigation) requires 2--4 prompts (surging from 11.1% to 90.9%), and stateful contrast-theme toggling requires 5--7 prompts (jumping from 9.1% to 100.0%).
   * Demonstrated a statistically significant positive correlation between prompt iterations and objective accessibility compliance ($r = +0.482$, $p < 0.05$).
   * Uncovered and formalized the **Effort Expectancy Paradox** ($r = -0.305$): students with few iterations perceived the tool as effortless but produced incomplete interfaces, whereas students performing 5--7 iterations encountered conversational debugging friction, properly calibrating their expectations regarding the human effort required to enforce WCAG standards with GenAI.
   * Analyzed discourse shifts across attempts, documenting a 240% increase in domain technical lexicon (e.g., \texttt{aria-live="polite"}, \texttt{tabindex="0"}) and a transition from delegative user stories to directive code-review critiques.
3. **Advanced Inferential & Non-Parametric Statistical Robustness:**
   * Complemented the paired $t$-test with the non-parametric **Wilcoxon Signed-Rank Test** (explicitly accounting for tied zeros) and computed **Cohen's $d$ effect sizes** for all constructs.
   * Conducted formal inferential subgroup comparisons (**Mann-Whitney U Test**), demonstrating that students without prior GenAI exposure experienced statistically significant positive shifts in Performance Expectancy ($\Delta = +0.67, p = 0.004$), Effort Expectancy ($\Delta = +0.53, p = 0.005$), and Behavioral Intention ($\Delta = +0.67, p = 0.006$), all surviving Bonferroni correction ($\alpha_{\text{adj}} = 0.010$), whereas experienced users remained stable. We appropriately qualified this finding given the small subgroup size ($n = 5$).
   * Tested correlations (Spearman's $\rho$) between prompt attempts and acceptance delta scores.
4. **Actionable Pedagogical Framework for HCI Education:**
   * Synthesized a four-phase pedagogical guideline for computer science instructors wishing to integrate GenAI tools into interaction design and accessibility coursework.
5. **Full Open Science & Reproducibility Package:**
   * Anonymized datasets deposited on **Zenodo** (FAIR-compliant with persistent DOI).
   * Complete analysis pipeline provided as an interactive **Google Colab Notebook** with zero-installation replication.
   * All replication materials organized in a public GitHub repository.

---

## 2. Point-by-Point Responses to Reviewers

### 🔹 Reviewer 1

> **Reviewer 1 Comment 1:** *"The paper includes basic pre-post comparisons by UTAUT construct, however, the analysis could be strengthened by adding some exploratory cross-analyses between participant profile variables, prior experience with generative AI, prompt attempts, and changes in acceptance."*

* **Authors' Response:** We fully agree and have substantially expanded Section V (*Empirical Results and Statistical Analysis*). In the journal version:
  * We conducted formal non-parametric inferential comparisons using the **Mann-Whitney U test** comparing novices in GenAI ($n=5$) against prior users ($n=36$). We confirmed that the intervention had a strong, statistically significant effect on novices ($\Delta \text{PE} = +0.67, p = 0.004$; $\Delta \text{EE} = +0.53, p = 0.005$; $\Delta \text{BI} = +0.67, p = 0.006$), surviving Bonferroni correction, while experienced users exhibited a ceiling effect.
  * We computed **Spearman rank correlations** between prompt iteration counts and changes in Effort Expectancy ($\Delta EE$) and Facilitating Conditions ($\Delta FC$), corroborating that higher iteration friction moderated student perceptions of tool usability.
  * We applied **Kruskal-Wallis testing** to examine the relationship between UI development experience and prompt refinement volume.

> **Reviewer 1 Comment 2:** *"The experimental conditions are not described in enough detail, and it would be useful to know more about the relationship between the participants and the authors, for example whether they were the authors' own students and how voluntariness was ensured in that context."*

* **Authors' Response:** We have expanded Section IV (*Methodology & Experimental Protocol*). We explicitly detail that while the intervention occurred at the authors' affiliated university, the students were enrolled in an independent section where the evaluating authors held no grading authority or direct course supervision, ensuring completely uncoerced voluntary participation. We also provide the step-by-step breakdown of the 30-minute prompt engineering workshop and the full wording of the questionnaire items.

> **Reviewer 1 Comment 3:** *"Improve the quality of Figure 2, since it appears blurry and is difficult to read. It would also be helpful to expand the discussion of the results a little more, especially to better explain the non-significant findings and their implications."*

* **Authors' Response:** We completely redesigned Figure 2 into a high-resolution, vector-quality multi-panel visualization generated via Python/Seaborn (at 300 DPI), showing demographic distributions clearly. Furthermore, Section VI (*Extended Discussion*) was substantially lengthened to theoretically examine the ceiling effect and explain why traditional models like UTAUT struggle with stochastic, non-deterministic GenAI systems.

---

### 🔹 Reviewer 2

> **Reviewer 2 Comment 1:** *"Se identifican debilidades en: i) el diseño experimental limitado, por la ausencia de un grupo de control... ii) muestra pequeña y homogénea... iii) entrenamiento limitado, sólo de 30 minutos... Finalmente, y muy importante, NO SE EVALÚA OBJETIVAMENTE LA CALIDAD DEL DISEÑO GENERADO, lo cual es crítico en tarefas de UI, pues sólo se está midiendo la percepción de la UTAUT."*

* **Authors' Response:** This observation was paramount in guiding our journal extension. In response:
  * **Objective Evaluation of Design Quality (New Section V.D):** We audited the 26 student project repositories and evaluated the objective accessibility of the generated HTML/JS Genius games against WCAG 2.1 and gerontechnology guidelines. We analyzed the implementation rates of resizable typography (100%), pacing control (100%), multimodal audio (92.3%), keyboard accessibility (69.2%), and WAI-ARIA semantics (61.5%).
  * **Threats to Validity & Limitations (Expanded Section VII):** We expanded our discussion regarding the one-group pretest-posttest design, detailing how the absence of a control group was mitigated through triangulation with objective code artifacts and prompt logs.

> **Reviewer 2 Comment 2:** *"Se recomienda a los autores en términos metodológicos: incluir medidas objetivas para evaluar la calidad del diseño generado, el cumplimiento de principios de accesibilidad y la eficiencia en tareas... Es recomendable hacer cierre dando claridad de las contribuciones, diferenciando entre los aportes teóricos y los empíricos."*

* **Authors' Response:** In Section VII (*Conclusion and Future Work*), we explicitly demarcated our contributions into two structured subsections:
  * **Theoretical Contributions:** Conceptualization of the "stochastic effort gap" in UTAUT's Effort Expectancy construct, and theoretical modeling of the "realism calibration" effect in Facilitating Conditions.
  * **Empirical Contributions:** Direct quantification of prompt iteration overhead, heuristic accessibility compliance rates, and evidence of the ceiling effect in technologically experienced student cohorts.

---

## 3. Structural Comparison of Changes

| Section in Extended Journal Paper | Status | Description of Modifications | % Added |
| :--- | :--- | :--- | :---: |
| **I. Introduction** | Expanded | Updated framing, clear statement of theoretical and empirical contributions, Open Science statement. | +3% |
| **II. Related Work** | Expanded | Added 12 new references (2024–2026), structured comparative table on GenAI in HCI education. | +6% |
| **III. Theoretical Framework** | Expanded | In-depth critique of UTAUT limitations when applied to non-deterministic generative models. | +4% |
| **IV. Experimental Protocol** | Expanded | Full questionnaire item specifications, workshop syllabus, and ethical safeguards. | +5% |
| **V. Empirical & Qualitative Results** | **Major Addition** | • Wilcoxon & Cohen's d analyses<br>• Subgroup inferential testing (Novices vs. Experienced)<br>• **Objective UI Accessibility Audit** (Heuristic evaluation)<br>• **Prompt Strategy & Iteration Analysis** | **+16%** |
| **VI. Extended Discussion** | Expanded | Deep dive into prompt friction, the "illusion of ease", and reality calibration. | +5% |
| **VII. Pedagogical Guidelines** | **New Section** | Actionable 4-phase framework for HCI instructors. | **+4%** |
| **VIII. Threats to Validity & Conclusion**| Expanded | Structured theoretical vs. empirical contributions, explicit limitations. | +2% |
| **Total Estimated New Content** | | | **~45%** |

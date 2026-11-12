# Codebook and Data Dictionary: Student Acceptance and Interaction with Generative AI in UI Design

**Zenodo Package Title:** Replication Package for "Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Extended Experimental Investigation"  
**Authors:** Daniela Marques (IFSP), André Luiz Satoshi Kawamoto (UTFPR), Valéria Farinazzo Martins (Universidade Presbiteriana Mackenzie)  
**Publication Target:** CLEI Electronic Journal (CLEI EJ)  
**License:** Creative Commons Attribution 4.0 International (CC-BY 4.0)  
**Language:** English / Portuguese (Instruments)  

---

## 1. Overview and Purpose
This dataset contains the anonymized empirical data collected during a pretest-posttest experimental investigation evaluating computing students' acceptance of Generative Artificial Intelligence (ChatGPT 3.5) for accessible user interface redesign.

The dataset is partitioned into three main files:
1. `dataset_student_profiles_and_pretest.csv` ($N = 41$): Anonymized demographic data, professional experience, prior exposure to GenAI, and pre-intervention Likert scores across the five constructs of the Unified Theory of Acceptance and Use of Technology (UTAUT).
2. `dataset_utaut_paired_pre_post.csv` ($N = 41$): Paired pre- and post-intervention scores for the five UTAUT constructs (Performance Expectancy, Effort Expectancy, Social Influence, Facilitating Conditions, Behavioral Intention), item-level responses, and delta variations ($\Delta = \text{Post} - \text{Pre}$).
3. `dataset_prompt_iterations_and_accessibility.csv` ($N = 26$): Systematic audit of student interaction logs with ChatGPT, tracking prompt iteration counts, prompt engineering strategies, and objective compliance with accessibility heuristics in the final HTML/JS game interfaces.

---

## 2. Ethical Procedures & Anonymization
All participants signed an informed consent form approved under institutional ethical standards. To ensure absolute privacy, the following de-identification steps were applied:
- Direct identifiers (student names, academic registration numbers, institutional e-mails) were permanently removed.
- Each participant was assigned an arbitrary pseudonym code (`P01` to `P41`).
- Exact completion timestamps have been omitted to prevent correlation with class schedules.

---

## 3. Data Dictionaries

### File 1: `dataset_student_profiles_and_pretest.csv`
| Variable Name | Type | Description | Values / Coding |
| :--- | :--- | :--- | :--- |
| `participant_id` | String | Unique participant identifier | `P01` to `P41` |
| `PU1_pre` - `PU3_pre` | Integer | Performance Expectancy pre-test items | 1 (Strongly Disagree) to 5 (Strongly Agree) |
| `EE1_pre` - `EE3_pre` | Integer | Effort Expectancy pre-test items | 1 (Strongly Disagree) to 5 (Strongly Agree) |
| `SI1_pre` - `SI3_pre` | Integer | Social Influence pre-test items | 1 (Strongly Disagree) to 5 (Strongly Agree) |
| `FC1_pre` - `FC3_pre` | Integer | Facilitating Conditions pre-test items | 1 (Strongly Disagree) to 5 (Strongly Agree) |
| `BI1_pre` - `BI3_pre` | Integer | Behavioral Intention pre-test items | 1 (Strongly Disagree) to 5 (Strongly Agree) |
| `gender` | Categorical | Self-reported gender | `Masculino`, `Feminino`, `Outro` |
| `age_group` | Categorical | Age bracket | `Menos de 20 anos`, `21- 30 anos` |
| `ui_development_experience` | Categorical | Prior interface development experience | 4 levels: None (`Nenhuma Experiência`), Low (`Pouca`), Intermediate (`Intermediário`), Advanced (`Avançado`) |
| `ui_development_frequency` | Categorical | Frequency of UI development | `Nunca`, `1-2 vezes ao ano`, `3-5 vezes ao ano`, `Diariamente` |
| `ai_usage_voluntariness` | Categorical | Nature of GenAI adoption | `Completamente voluntário`, `Recomendado pela empresa`, `Obrigatório` |
| `ai_used_before` | Binary | Prior hands-on experience with GenAI | `Sim` (Yes), `Não` (No) |
| `ai_prior_application` | Categorical | Primary task for previous GenAI use | `Criação de Interfaces`, `Processamento de Dados`, `Análise de Conteúdo`, `Outro` |

### File 2: `dataset_utaut_paired_pre_post.csv`
Contains the calculated construct means, construct deltas ($\Delta = \text{Post} - \text{Pre}$), and individual items:
- Construct means: `PE_pre`, `PE_post`, `PE_delta`, `EE_pre`, `EE_post`, `EE_delta`, `SI_pre`, `SI_post`, `SI_delta`, `FC_pre`, `FC_post`, `FC_delta`, `BI_pre`, `BI_post`, `BI_delta`.
- Granular items: `PE1_pre` to `PE3_post`, `EE1_pre` to `EE3_post`, `SI1_pre` to `SI3_post`, `FC1_pre` to `FC3_post`, `BI1_pre` to `BI3_post`.

### File 3: `dataset_prompt_iterations_and_accessibility.csv`
| Variable Name | Type | Description | Values / Coding |
| :--- | :--- | :--- | :--- |
| `participant_id` | String | Participant identifier | `P01` to `P26` |
| `prompt_iterations_count` | Integer | Total number of prompt rounds executed with ChatGPT | 1 to 15 |
| `submitted_interaction_pdf` | Binary | Verified submission of complete conversational PDF log | 1 = Yes, 0 = No |
| `has_font_size_adjustment` | Binary | UI supports resizable / enlarged typography | 1 = Implemented, 0 = Absent |
| `has_contrast_theme_toggle`| Binary | UI features light/dark or high-contrast mode toggle | 1 = Implemented, 0 = Absent |
| `has_text_color_labels` | Binary | UI includes textual labels inside game color quadrants | 1 = Implemented, 0 = Absent |
| `has_multimodal_audio` | Binary | UI includes audio/sound and volume feedback | 1 = Implemented, 0 = Absent |
| `has_speed_reduction` | Binary | UI provides slower game sequence pacing for seniors | 1 = Implemented, 0 = Absent |
| `has_round_feedback` | Binary | UI provides explicit textual indicator of current round | 1 = Implemented, 0 = Absent |
| `has_keyboard_navigation` | Binary | UI supports full keyboard controls (Tab, Enter, Space) | 1 = Implemented, 0 = Absent |
| `has_aria_accessibility_tags`| Binary | UI includes semantic WAI-ARIA roles and attributes | 1 = Implemented, 0 = Absent |

---

## 4. Citation and Attribution
If using this dataset, please cite:
```bibtex
@article{marques2026student,
  title={Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Extended Experimental Investigation},
  author={Marques, Daniela and Kawamoto, Andr{\'e} Luiz Satoshi and Martins, Val{\'e}ria Farinazzo},
  journal={CLEI Electronic Journal},
  year={2026},
  note={Replication Dataset on Zenodo: DOI: 10.5281/zenodo.XXXXXXX}
}
```

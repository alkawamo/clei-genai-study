# Replication Package: Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alkawamo/clei-genai-study/blob/main/notebooks/clei_replication_analysis.ipynb)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository is the official Open Science replication package for the extended journal paper:

> **Marques, D., Kawamoto, A. L. S., & Martins, V. F. (2026).** *Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Extended Experimental Investigation.* **CLEI Electronic Journal (CLEI EJ)**.

---

## 📁 Repository Structure

```text
clei-extended-paper/
├── README.md                      # Replication guide and dataset overview
├── notebooks/
│   └── clei_replication_analysis.ipynb  # Interactive Google Colab notebook for all statistics & plots
├── zenodo_dataset/                # De-identified, FAIR-compliant datasets for Zenodo
│   ├── dataset_student_profiles_and_pretest.csv
│   ├── dataset_utaut_paired_pre_post.csv
│   ├── dataset_prompt_iterations_and_accessibility.csv
│   └── codebook_data_dictionary.md
├── manuscript/                    # Official CLEI Electronic Journal LaTeX sources
│   ├── main.tex                   # Extended manuscript (>30% new empirical and qualitative content)
│   ├── cleiej.cls                 # CLEI EJ class file
│   └── references.bib             # Extended bibliography
└── response_letter/
    └── Letter_of_Modifications.md # Point-by-point response to Reviewer 1 & 2
```

---

## 🚀 Quick Start: Running in Google Colab

You can run the complete statistical analysis directly in your browser with zero installation:
1. Click the **[Open In Colab](https://colab.research.google.com/github/alkawamo/clei-genai-study/blob/main/notebooks/clei_replication_analysis.ipynb)** badge above.
2. Select `Runtime` > `Run all` (or press `Ctrl + F9`).
3. The notebook will automatically compute:
   - Sample demographic distributions and generate high-resolution figures.
   - UTAUT construct statistics (Paired $t$-test, Wilcoxon Signed-Rank test, Cohen's $d$ effect sizes).
   - Inferential testing of subgroups (Novices vs. Experienced GenAI users; UI experience levels).
   - Heuristic accessibility audit of student-generated interfaces.

---

## 📊 Datasets & Open Science Compliance

All experimental data is strictly anonymized in compliance with international research ethics:
* Direct identifiers (student names, student IDs, institutional e-mails) have been permanently omitted.
* Arbitrary alphanumeric participant keys (`P01` to `P41`) are used throughout.
* The complete variable definitions and coding schemes are documented in [`zenodo_dataset/codebook_data_dictionary.md`](zenodo_dataset/codebook_data_dictionary.md).

---

## 📖 Citation

```bibtex
@article{marques2026student,
  title={Student Acceptance and Interaction Patterns with Generative AI in Accessible UI Design: An Extended Experimental Investigation},
  author={Marques, Daniela and Kawamoto, Andr{\'e} Luiz Satoshi and Martins, Val{\'e}ria Farinazzo},
  journal={CLEI Electronic Journal},
  volume={29},
  number={1},
  pages={1--22},
  year={2026},
  doi={10.19153/cleiej.29.1.X}
}
```

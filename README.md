````md
# CLARA: A Lightweight Contrastive Embedding Approach for Retail E-Commerce Clustering
*(AI Final Project – Individual Implementation, Week 17)*

This repository contains my **individual implementation** for the AI final project (Week 17).  
The project follows the CLARA idea and improves clustering separability for retail/e-commerce datasets by combining baseline K-Means, LDA projection using pseudo-labels, re-clustering in the embedding space, and evaluation with Elbow and Silhouette scores.

---

## Repository Structure

```text
AI-final-project/
  dataset/                 # dataset download links + feature descriptions + notes
  notebooks/               # runnable Jupyter notebooks (main implementation)
  results/
    figures/               # output plots and visualizations
  requirements.txt         # Python dependencies
  .gitignore
  README.md
  AI-final-project_Instruction-Manual.pdf
````

---

## Environment Setup

```bash
git clone https://github.com/Yourui-droid/AI-final-project.git
cd AI-final-project

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

---

## How to Run (Reproducibility)

1. Prepare datasets:

   * If CSV files are already included under `dataset/`, keep the folder structure unchanged.
   * Otherwise, follow `dataset/README.md` to download datasets and place them in the correct directories.

2. Run notebooks:

   * Open the `notebooks/` folder.
   * Execute notebooks in numeric order (e.g., `01 → 04`) to reproduce:

     * data preprocessing and standardization
     * baseline K-Means clustering
     * LDA projection using pseudo-labels
     * re-clustering, evaluation, and visualization

### Outputs

* Generated plots are saved under: `results/figures/`

---

## Steps to Train Your Own Model

This project is notebook-based. To re-train or re-run the full pipeline, execute the notebooks in order.
Training refers to re-generating K-Means pseudo-labels, fitting the LDA projection, and re-clustering in the LDA embedding space.

---

## Results Summary

The CLARA pipeline improves clustering separability compared to baseline K-Means,
as demonstrated by higher silhouette scores and clearer cluster boundaries
in the LDA embedding space.

---

## Notes / Limitations (Optional)

* If Jupyter is not installed: `pip install jupyter`, then run `jupyter notebook`.
* If datasets are not committed, download links and file placement rules are provided in `dataset/README.md`.

---

## Instruction Manual (PDF)

* `AI-final-project_Instruction-Manual.pdf`

```
```

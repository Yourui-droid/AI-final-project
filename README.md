# AI Final Project – CLARA (K-Means + LDA Embedding)

This repository contains my **individual** implementation for the final project (Week 17).
The goal is to improve retail customer/product clustering by combining:
- Baseline K-Means
- LDA projection using K-Means pseudo-labels
- Re-clustering in the LDA space
- Evaluation using Elbow and Silhouette score
- Visualization using PCA 2D and LDA 2D

---

## Repository Structure

```text
AI-final-project/
  dataset/
    README.md              # dataset download links + features + notes
    raw/                   # (not uploaded) put downloaded csv files here
  notebooks/               # runnable notebooks
  results/
    figures/               # output plots
    metrics/               # (recommended) csv tables for elbow/silhouette
  requirements.txt
  .gitignore
  README.md
## Environment Setup

```bash
pip install -r requirements.txt
python --version
## How to Run (Reproducibility)

### Option 1: Run notebooks (recommended)

1. Download datasets and place them under `dataset/raw/` (see `dataset/README.md`).
2. Open and run notebooks in order:

   1) `notebooks/01_preprocess.ipynb`  
   2) `notebooks/02_kmeans_baseline.ipynb`  
   3) `notebooks/03_lda_projection.ipynb`  
   4) `notebooks/04_kmeans_on_lda_and_eval.ipynb`

### Option 2: Run a single script (if available)

If a pipeline script is provided (e.g., `src/run_pipeline.py`), run:

```bash
python src/run_pipeline.py --dataset all

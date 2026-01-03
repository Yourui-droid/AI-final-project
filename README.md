# AI Final Project – CLARA (K-Means + LDA Embedding)

This repository contains my **individual** implementation for the final project (Week 17).
The goal is to improve retail customer/product clustering by combining:
- Baseline **K-Means**
- **LDA** projection using K-Means pseudo-labels
- Re-clustering in the LDA space
- Evaluation using **Elbow** and **Silhouette score**
- Visualization using **PCA 2D** and **LDA 2D**

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

---

### 2) How to Run（怎麼跑）
你需要把「notebooks 的正確順序」寫出來（用你 repo 真實檔名）。先放模板也行：

```md
## How to Run (Reproducibility)

### Option 1: Run notebooks (recommended)
Run notebooks in order:

1. `notebooks/[YOUR_1ST_NOTEBOOK].ipynb`
2. `notebooks/[YOUR_2ND_NOTEBOOK].ipynb`
3. `notebooks/[YOUR_3RD_NOTEBOOK].ipynb`
4. `notebooks/[YOUR_4TH_NOTEBOOK].ipynb`

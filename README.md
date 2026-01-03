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
  dataset/                 # dataset download links + features + notes
  notebooks/               # runnable notebooks
  results/
    figures/               # output plots
  requirements.txt
  .gitignore
  README.md
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
## Instruction Manual (PDF)
- `AI-final-project_Instruction-Manual_You-Rui-Feng_1137141.pdf`
---
## Instruction Manual (PDF)
- `AI-final-project_Instruction-Manual_You-Rui-Feng_1137141.pdf`

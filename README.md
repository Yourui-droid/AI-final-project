# CLARA: A Lightweight Contrastive Embedding Approach for Retail E-Commerce Clustering

This repository contains my **individual implementation** for the AI final project.  
The project is based on the CLARA framework proposed in our paper and focuses on improving
retail and e-commerce customer/product clustering through a lightweight contrastive
embedding pipeline.

The proposed approach integrates:

- Baseline K-Means clustering  
- LDA projection using K-Means pseudo-labels  
- Re-clustering in the LDA embedding space  
- Evaluation using Elbow and Silhouette scores  
- Visualization using PCA 2D and LDA 2D  

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

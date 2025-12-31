## Author
- Aishwarya Pawar, GMBA, Yuan Ze University, Taiwan :contentReference[oaicite:2]{index=2}
- **Yourui Feng** (Student ID: 1137141), GMBA, Yuan Ze University, Taiwan :contentReference[oaicite:1]{index=1}  
- Qazi Mazhar Ul Haq, Assistant Professor, Yuan Ze University, Taiwan :contentReference[oaicite:3]{index=3}  

---

## Project Description
This project implements **CLARA: A Lightweight Contrastive Embedding Approach for Retail E-Commerce Clustering**, which improves the quality of K-Means clustering on heterogeneous retail datasets using a simple contrastive representation step based on **Linear Discriminant Analysis (LDA)** with **pseudo-labels**. :contentReference[oaicite:4]{index=4}  

### Core Idea (Pipeline)
1. Run **K-Means** on standardized numerical features (baseline clustering).
2. Use the cluster assignments as **pseudo-labels**.
3. Compute an **LDA projection** to increase between-cluster separability.
4. Re-apply **K-Means** in the LDA (contrastive) space and evaluate using **silhouette score**. :contentReference[oaicite:5]{index=5}  

### Datasets
The approach is evaluated on four real-world retail datasets:
- Mall Customers dataset
- Amazon product dataset
- Flipkart laptop dataset
- Walmart weekly sales dataset (45 stores) :contentReference[oaicite:6]{index=6}  

### Key Results (Silhouette Score Improvements)
Re-clustering in the LDA space improves clustering quality across most datasets:
- Amazon: **0.289 → 0.469**
- Flipkart: **0.212 → 0.411**
- Walmart: **0.204 → 0.531**
- Mall Customers: **0.417 → 0.439 (modest improvement)** :contentReference[oaicite:7]{index=7}  

Qualitatively, LDA embeddings generally produce more compact and visually distinct clusters, consistent with the silhouette improvements. :contentReference[oaicite:8]{index=8}  

---

## Repository Contents
This repository contains all materials required to reproduce the project:
- `README.md` : Project documentation and reproducibility instructions
- `data/README.txt` : Dataset information and links (how to obtain the datasets) :contentReference[oaicite:9]{index=9}  
- `AI-IEEE paper Report.pdf` : (Optional) project report describing CLARA and results :contentReference[oaicite:10]{index=10}  
- `notebooks/` or main `.ipynb` / `.py` files : Implementation of K-Means → pseudo-labels → LDA → K-Means pipeline :contentReference[oaicite:11]{index=11}  
- `results/` : Saved outputs such as silhouette scores and summary tables/figures :contentReference[oaicite:12]{index=12}  
- `requirements.txt` : Dependencies for running the code

(If the dataset is large, it is not uploaded; only dataset links and instructions are provided in `data/README.txt`.) :contentReference[oaicite:13]{index=13}  

---

## Environment Setup
### Requirements
- Python 3.8+ (CPU is sufficient; this project uses lightweight and interpretable methods) :contentReference[oaicite:14]{index=14}  

### Recommended Python Packages
- numpy
- pandas
- scikit-learn
- matplotlib

### Installation
```bash
pip install -r requirements.txt

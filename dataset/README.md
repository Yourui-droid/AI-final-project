# Datasets (Download Links & Description)

This project uses 4 retail-related datasets.  
To keep the GitHub repository lightweight, **raw dataset files are NOT uploaded**.  
Please download datasets from the links below and place them into the correct folder.

## Folder Structure
After downloading, put the raw files here:

dataset/raw/
  mall_customers.csv
  amazon.csv
  flipkart.csv
  walmart.csv

(If your filenames are different, either rename them as above or update paths in the notebooks.)

---

## 1) Mall Customers Dataset
- Source: [PASTE YOUR LINK HERE]
- File name (recommended): `mall_customers.csv`
- Main features used:
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)
- Preprocessing notes:
  - Handle missing values (if any)
  - Encode categorical feature(s)
  - Standardize numeric features before clustering

---

## 2) Amazon Dataset
- Source: [PASTE YOUR LINK HERE]
- File name (recommended): `amazon.csv`
- Main features used:
  - [PASTE FEATURES YOU USED]
- Preprocessing notes:
  - Remove/handle missing values
  - Convert price/rating fields to numeric if needed
  - Standardize numeric features before clustering

---

## 3) Flipkart Dataset
- Source: [PASTE YOUR LINK HERE]
- File name (recommended): `flipkart.csv`
- Main features used:
  - [PASTE FEATURES YOU USED]
- Preprocessing notes:
  - Remove/handle missing values
  - Convert price fields to numeric if needed
  - Standardize numeric features before clustering

---

## 4) Walmart Dataset
- Source: [PASTE YOUR LINK HERE]
- File name (recommended): `walmart.csv`
- Main features used:
  - [PASTE FEATURES YOU USED]
- Preprocessing notes:
  - Remove/handle missing values
  - Standardize numeric features before clustering

---

## Expected Output
After running the pipeline/notebooks, results will be saved to:
- `results/figures/` (visualizations)
- (optional) `results/metrics/` (silhouette scores, elbow values)

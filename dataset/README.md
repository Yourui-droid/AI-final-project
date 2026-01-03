# Datasets (Download Links & Description)

This project uses 4 retail-related datasets.  
To keep the GitHub repository lightweight, **raw dataset files are NOT uploaded**.  
Please download datasets from the links below and place them under `dataset/raw/`.

## Folder Structure
dataset/raw/
  mall_customers.csv
  amazon.csv
  flipkart.csv
  walmart.csv

---

## 1) Mall Customers Dataset
- Source: [PUT DOWNLOAD LINK HERE]
- Expected size: (200, 3)
- Features used (numeric):
  - Age
  - Annual Income (k$)
  - Spending Score (1–100)
- Notes:
  - Remove missing values if any
  - Standardize features (zero mean, unit variance) before clustering

---

## 2) Amazon Sales Dataset
- Source: [PUT DOWNLOAD LINK HERE]
- Expected size: (1462, 5)
- Features used (numeric):
  - discounted price
  - actual price
  - discount percentage
  - rating
  - number of ratings
- Notes:
  - Remove/handle missing values
  - Convert price fields to numeric if needed
  - Standardize features before clustering

---

## 3) Flipkart Laptops Dataset
- Source: [PUT DOWNLOAD LINK HERE]
- Expected size: (414, 5)
- Features used (numeric):
  - Selling Price
  - MRP
  - Discount
  - Ratings
  - Number of Ratings
- Notes:
  - Clean monetary format / text if needed
  - Standardize features before clustering

---

## 4) Walmart Sales (45 Stores) Dataset
- Source: [PUT DOWNLOAD LINK HERE]
- Expected size: (6435, 6)
- Features used (numeric):
  - Weekly Sales
  - Holiday Flag
  - Temperature
  - Fuel Price
  - CPI
  - Unemployment rate
- Notes:
  - Remove missing values
  - Standardize features before clustering

---

## Expected Output
After running the pipeline/notebooks, results will be saved to:
- `results/figures/` (visualizations)
- (optional) `results/metrics/` (silhouette / elbow tables)
---
dataset/raw/
  mall_customers.csv
  amazon.csv
  flipkart.csv
  walmart.csv

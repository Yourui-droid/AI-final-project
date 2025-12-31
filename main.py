import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import silhouette_score

# Load dataset
data = load_iris()
X = data.data

# Step 1: KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Step 2: LDA using pseudo-labels
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, labels)

# Step 3: Re-cluster in LDA space
kmeans_lda = KMeans(n_clusters=3, random_state=42)
labels_lda = kmeans_lda.fit_predict(X_lda)

# Evaluation
score = silhouette_score(X_lda, labels_lda)

# Save results
with open("results/output.txt", "w") as f:
    f.write("Clustering with LDA-based embedding\n")
    f.write(f"Silhouette score: {score:.4f}\n")

print("Finished. Silhouette score:", score)

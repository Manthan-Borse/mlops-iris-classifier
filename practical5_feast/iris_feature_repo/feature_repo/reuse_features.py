
from feast import FeatureStore
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Connect to Feast
store = FeatureStore(repo_path=".")

# 2. Load the existing FeatureService
feature_service = store.get_feature_service("iris_feature_service")

# 3. Retrieve features for all Iris samples
entity_rows = [
    {"sample_id": i} for i in range(1, 150)
]

features = store.get_online_features(
    features=feature_service,
    entity_rows=entity_rows,
).to_df()

# 4. Select numerical features for clustering
feature_columns = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = features[feature_columns]

# 5. Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 6. Apply K-Means clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

features["cluster"] = kmeans.fit_predict(X_scaled)

# 7. Display results
print("\nK-Means Clustering Results")
print(features[["sample_id", "cluster"]].head(10))

print("\nCluster Counts:")
print(features["cluster"].value_counts().sort_index())

print("\nTotal samples clustered:", len(features))

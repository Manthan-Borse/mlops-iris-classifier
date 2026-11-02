
import pandas as pd
from feast import FeatureStore

# Connect to the existing Feast feature store
store = FeatureStore(repo_path=".")

# Get the feature service
feature_service = store.get_feature_service("iris_feature_service")

# Test 1: Check online feature retrieval
entity_rows = [
    {"sample_id": 1},
    {"sample_id": 2},
    {"sample_id": 3},
]

online_features = store.get_online_features(
    features=feature_service,
    entity_rows=entity_rows,
).to_df()

expected_features = {
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
    "petal_length_bin",
}

assert len(online_features) == 3, "Online retrieval should return 3 rows."
assert expected_features.issubset(set(online_features.columns)), (
    "Some expected online features are missing."
)

print("PASS: Online feature retrieval")
print("Online rows:", len(online_features))


# Test 2: Check historical feature retrieval
entity_df = pd.read_parquet("data/iris_features.parquet")[
    ["sample_id", "event_timestamp"]
]

historical_features = store.get_historical_features(
    entity_df=entity_df,
    features=feature_service,
).to_df()

assert len(historical_features) == 149, (
    "Historical retrieval should return 149 rows."
)
assert expected_features.issubset(set(historical_features.columns)), (
    "Some expected historical features are missing."
)

print("PASS: Historical feature retrieval")
print("Historical rows:", len(historical_features))

print("\nAll Iris Feast workflow tests passed!")

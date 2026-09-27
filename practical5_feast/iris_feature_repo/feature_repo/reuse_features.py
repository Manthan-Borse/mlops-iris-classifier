from feast import FeatureStore

store = FeatureStore(repo_path=".")

feature_service = store.get_feature_service("iris_feature_service")
entity_rows = [
    {"sample_id": 1},
    {"sample_id": 2},
    {"sample_id": 3},
]

features = store.get_online_features(
    features=feature_service,
    entity_rows=entity_rows,
).to_dict()

print(features)
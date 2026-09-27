from feast import FeatureStore

store = FeatureStore(repo_path=".")

feature_service = "iris_feature_service"

entity_rows = [
    {"sample_id": 1}
]

features = store.get_online_features(
    features=store.get_feature_service(feature_service),
    entity_rows=entity_rows,
).to_dict()

print(features)
import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")

entity_df = pd.read_parquet("data/iris_features.parquet")[
    ["sample_id", "event_timestamp"]
]
historical_features = store.get_historical_features(
    entity_df=entity_df,
    features=store.get_feature_service("iris_feature_service"),
).to_df()

print(historical_features.head())
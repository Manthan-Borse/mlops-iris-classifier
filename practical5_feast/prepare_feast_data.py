import pandas as pd
from datetime import datetime, timezone

df = pd.read_csv("../data/processed/iris_features.csv")
df["sample_id"] = range(1, len(df) + 1)
df["event_timestamp"] = datetime.now(timezone.utc)
df["created_timestamp"] = datetime.now(timezone.utc)

df.to_parquet("iris_feature_repo/feature_repo/data/iris_features.parquet", index=False)
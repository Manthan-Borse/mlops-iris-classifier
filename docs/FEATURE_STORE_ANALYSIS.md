# Feature Store Analysis

## 1. Training-Serving Skew

Training-serving skew occurs when the features used during model training are different from the features available when the model is used for prediction.

A Feature Store helps reduce this problem by using the same registered feature definitions for both historical/offline feature retrieval and online feature retrieval.

In this practical:

- Historical features were retrieved from the Parquet data source using `get_historical_features()`.
- Online features were retrieved from the SQLite online store using `get_online_features()`.
- Both retrieval methods used the same registered `iris_feature_service`.
- The same feature definitions were therefore used across the two retrieval workflows.

This provides consistency between the features used for model training and the features available for online serving.

Point-in-time correctness is also important for historical retrieval because features should correspond to the appropriate event timestamp rather than using information from the future.

## 2. Feature Reusability

Feature reusability means that features can be defined and registered once and then reused by multiple models or tasks.

In this practical:

- The Iris measurement features were registered in the `iris_measurements` FeatureView.
- The engineered features were registered in the `iris_engineered_features` FeatureView.
- Both FeatureViews were included in the `iris_feature_service`.
- The same Feature Service was reused to retrieve features for multiple `sample_id` values.

This avoids repeatedly implementing the same feature definitions for different machine learning tasks. It also provides a common and consistent way to access registered features.

The reuse example successfully retrieved features for `sample_id` values 1, 2, and 3 using the existing `iris_feature_service`.

## 3. Centralized Feature Governance

A Feature Store provides a centralized system for defining, registering, and managing features.

In this practical, the feature definitions were maintained in `feature_definitions.py` and registered in Feast. The feature store contained:

- The `sample_id` entity.
- The `iris_measurements` FeatureView.
- The `iris_engineered_features` FeatureView.
- The `iris_feature_service` Feature Service.

Centralizing these definitions provides a common location for feature definitions and makes the registered features easier to discover and reuse across machine learning workflows.

The Feature Store therefore provides a structured way to manage feature definitions instead of maintaining separate feature definitions for every model or task.

## 4. Conclusion

This practical demonstrated the use of Feast as a Feature Store for managing and retrieving machine learning features.

The practical covered:

- Creation of a Feast feature repository.
- Definition and registration of entities and FeatureViews.
- Preparation of feature data in Parquet format.
- Materialization of features into a SQLite online store.
- Online feature retrieval.
- Historical feature retrieval.
- Reuse of registered features through a Feature Service.

The practical demonstrated how a Feature Store can provide a centralized and reusable approach to feature management while supporting both historical and online feature retrieval.
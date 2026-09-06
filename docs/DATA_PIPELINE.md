 # Data Pipeline Documentation

 ## Overview

 This project uses a modular DVC pipeline to collect, preprocess, feature-engineer, and validate the Iris dataset.

 The pipeline runs through four stages:

 **Collect -> Preprocess -> Feature Engineering -> Validate**

 DVC manages stage dependencies and determines which stages need to run when data or code changes.

 ## Pipeline At A Glance

 | Stage | Purpose | Input | Output |
 | --- | --- | --- | --- |
 | Collect | Obtain the raw Iris dataset | Scikit-learn Iris dataset | `data/raw/iris_raw.csv` |
 | Preprocess | Clean and prepare the raw data | `data/raw/iris_raw.csv` | `data/processed/iris_preprocessed.csv` |
 | Feature Engineering | Create useful derived features | `data/processed/iris_preprocessed.csv` | `data/processed/iris_features.csv` |
 | Validate | Check schema, nulls, and value ranges | `data/processed/iris_features.csv` | Validation result |

 ## Pipeline Stages

 ### 1. Collect

 #### Purpose

 The Collect stage obtains the Iris dataset with Scikit-learn and saves it as a raw CSV file.

 #### Input

 Scikit-learn Iris dataset.

 #### Processing

 - Loads the dataset with `load_iris(as_frame=True)`.
 - Renames the target column to `species`.
 - Converts target values to `setosa`, `versicolor`, and `virginica`.
 - Adds a UTC `collected_at` timestamp.

 #### Output

 `data/raw/iris_raw.csv`

 The collected dataset contains 150 rows.

 ### 2. Preprocess

 #### Purpose

 The Preprocess stage cleans the raw dataset and prepares it for feature engineering.

 #### Input

 `data/raw/iris_raw.csv`

 #### Processing

 - Removes exact duplicate rows.
 - Converts numeric columns to numeric data types.
 - Handles missing numeric values with median imputation.
 - Removes rows with a missing `species` value.
 - Removes the `collected_at` column.

 #### Output

 `data/processed/iris_preprocessed.csv`

 In the current execution, one duplicate row was removed, resulting in 149 processed rows.

 ### 3. Feature Engineering

 #### Purpose

 The Feature Engineering stage creates additional features from the preprocessed measurements.

 #### Input

 `data/processed/iris_preprocessed.csv`

 #### Features Created

 | Feature | Definition |
 | --- | --- |
 | `sepal_area` | `sepal length * sepal width` |
 | `petal_area` | `petal length * petal width` |
 | `sepal_to_petal_length_ratio` | `sepal length / petal length` |
 | Petal length bin | Categorizes petal length as `short`, `medium`, or `long` |

 #### Output

 `data/processed/iris_features.csv`

 The resulting dataset contains 9 columns.

 ### 4. Validate

 #### Purpose

 The Validate stage checks that the feature-engineered dataset satisfies the required schema and value constraints.

 #### Input

 `data/processed/iris_features.csv`

 #### Validation Rules

 The pipeline verifies that:

 - Required measurement columns are present.
 - The `species` column is present.
 - All engineered feature columns are present.
 - Species values are limited to `setosa`, `versicolor`, and `virginica`.
 - Numeric values are within the expected ranges.
 - Required data is valid before the pipeline completes.

 #### Range Checks

 | Column | Minimum | Maximum |
 | --- | ---: | ---: |
 | Sepal length | 3.0 | 9.0 |
 | Sepal width | 1.5 | 5.5 |
 | Petal length | 0.5 | 8.0 |
 | Petal width | 0.05 | 3.0 |

 If validation fails, the pipeline exits with a non-zero status.

 #### Output

 The Validate stage does not create a new data file. It produces a validation result.

 **Current result:** Validation PASSED: 149 rows, 9 columns, all checks satisfied.

 ## DVC Pipeline

 The complete pipeline is defined in `dvc.yaml`.

 **Dependency graph**

 | Order | Stage |
 | ---: | --- |
 | 1 | Collect |
 | 2 | Preprocess |
 | 3 | Feature Engineering |
 | 4 | Validate |

 DVC tracks the dependencies and outputs for each stage in `dvc.yaml` and `dvc.lock`.

 ## Pipeline Execution

 Run the complete pipeline with:

 `dvc repro`

 When nothing has changed, DVC skips stages that are already up to date. A typical result is:

 > Stage `collect` didn't change, skipping  
 > Stage `preprocess` didn't change, skipping  
 > Stage `features` didn't change, skipping  
 > Stage `validate` didn't change, skipping  
 >  
 > Data and pipelines are up to date.

 This avoids unnecessary processing.

 ## DVC Remote Storage

 The project uses a local DVC remote named `myremote`.

 **Remote storage location:** `C:/Users/HP/dvc-remote-storage`

 Upload data objects to the remote with:

 `dvc push`

 ## Versioning And Reproducibility

 DVC uses hashes to track data and pipeline dependencies. The `dvc.lock` file stores the exact versions and hashes required to reproduce the pipeline.

 This enables the project to:

 - Track data changes.
 - Reproduce previous pipeline states.
 - Avoid unnecessary stage execution.
 - Maintain consistency between data and code.

 ## Summary

 The final automated flow is:

 **Raw Iris Dataset -> Collect -> Preprocess -> Feature Engineering -> Validate -> Validated Feature Dataset**

 The pipeline is modular, reproducible, and automatically managed with DVC.

# Practical 7: Hyperparameter Tuning

## 1. Objective
To find the best hyperparameters for a Random Forest Classifier using GridSearchCV and improve model performance.

## 2. Tools and Libraries Used
- Python
- Scikit-learn
- GridSearchCV
- Random Forest Classifier
- Joblib

## 3. Dataset
Iris Dataset – contains flower measurements used to classify three species of Iris flowers.

## 4. Hyperparameters Tested

| Parameter | Values |
|---|---|
| n_estimators | 50, 100, 150 |
| max_depth | 2, 3, 5, None |

A total of 12 parameter combinations were tested.

## 5. Methodology
1. Loaded the Iris dataset.
2. Split the data into training and testing sets (80:20).
3. Created a Random Forest Classifier.
4. Applied GridSearchCV with 5-fold cross-validation.
5. Selected the best hyperparameter combination.
6. Evaluated the best model using test data.
7. Saved the trained model using Joblib.

## 6. Results

**Best Parameters:**
- n_estimators = 50
- max_depth = 3

**Best Cross-Validation Accuracy:** 95%

**Test Accuracy:** 100%

## 7. Conclusion
GridSearchCV successfully identified the best hyperparameter combination for the Random Forest Classifier. The selected model achieved 95% cross-validation accuracy and 100% test accuracy on the Iris dataset.

The trained model was saved as `models/iris_best_model.joblib`.
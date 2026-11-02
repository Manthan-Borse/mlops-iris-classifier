import joblib
import os

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report


# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target


# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 3. Create the model
rf = RandomForestClassifier(random_state=42)


# 4. Define hyperparameters to test
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [2, 3, 5, None]
}


# 5. Apply GridSearchCV
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)


# 6. Train and find the best combination
grid_search.fit(X_train, y_train)


# 7. Get the best model
best_model = grid_search.best_estimator_


# 8. Evaluate on test data
predictions = best_model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Accuracy:", grid_search.best_score_)
print("Test Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# 9. Save the best model
os.makedirs("models", exist_ok=True)

joblib.dump(
    best_model,
    "models/iris_best_model.joblib"
)

print("\nBest model saved successfully!")
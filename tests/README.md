# Practical 8: Unit Testing

## 1. Objective
To test individual parts of the Iris classification project using the `pytest` framework.

## 2. Tools Used
- Python 3.13.1
- pytest 9.2.0
- Scikit-learn

## 3. Test File
`tests/test_train.py`

## 4. Test Cases

1. **test_load_data:** Checks whether the training and testing datasets load correctly and contain 120 and 30 samples respectively.
2. **test_train_model:** Checks whether the Random Forest model is created successfully and uses 100 decision trees.
3. **test_evaluate_model:** Checks whether model evaluation returns a valid accuracy score and a classification report.

## 5. Execution

Run the following command in the terminal:

```bash
python -m pytest tests/ -v
```

## 6. Results

- Total test cases: 3
- Passed: 3
- Failed: 0

All three tests passed successfully.

## 7. Conclusion
Unit testing was performed using pytest. The tests verified that data loading, model training, and model evaluation functions work as expected.
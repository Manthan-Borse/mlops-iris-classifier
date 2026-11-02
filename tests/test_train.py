from src.train import load_data, train_model, evaluate_model


# Test 1: Check whether data loads correctly
def test_load_data():
    X_train, X_test, y_train, y_test = load_data()

    assert len(X_train) == 120
    assert len(X_test) == 30
    assert len(y_train) == 120
    assert len(y_test) == 30


# Test 2: Check whether model trains correctly
def test_train_model():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)

    assert model is not None
    assert model.n_estimators == 100


# Test 3: Check whether model evaluation works
def test_evaluate_model():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)

    accuracy, report = evaluate_model(model, X_test, y_test)

    assert 0 <= accuracy <= 1
    assert isinstance(report, str)
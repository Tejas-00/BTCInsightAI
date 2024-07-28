from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    # Predict the test set results
    y_pred = model.predict(X_test)

    # Calculate Mean Squared Error and R-squared for Open price
    mse_open = mean_squared_error(y_test['Open'], y_pred[:, 0])
    r2_open = r2_score(y_test['Open'], y_pred[:, 0])

    # Calculate Mean Squared Error and R-squared for Close price
    mse_close = mean_squared_error(y_test['Close'], y_pred[:, 1])
    r2_close = r2_score(y_test['Close'], y_pred[:, 1])

    # Print the evaluation metrics
    print(f'Mean Squared Error (Open): {mse_open:.2f}')
    print(f'R-squared (Open): {r2_open:.2f}')
    print(f'Mean Squared Error (Close): {mse_close:.2f}')
    print(f'R-squared (Close): {r2_close:.2f}')

from data_loading import load_data
from feature_engineering import create_features
from model_training import split_data, train_model
from model_evaluation import evaluate_model
from prediction import predict_future_price

if __name__ == "__main__":
    data = load_data()
    data = create_features(data)
    X_train, X_test, y_train, y_test = split_data(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    predict_future_price(model, data)

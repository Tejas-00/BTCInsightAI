from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def split_data(data):
    features = ['Price_Lag1', 'Volume_Lag1', 'FearGreed_Lag1']
    target = 'Close'
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

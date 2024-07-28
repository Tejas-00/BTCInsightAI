from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def split_data(data):
    # Define features and target
    features = ['Open_Lag1', 'Close_Lag1', 'Volume_Lag1', 'FearGreed_Lag1']
    target = ['Open', 'Close']  # Adding Open to the target

    # Split the data into features and target
    X = data[features]
    y = data[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    # Initialize the Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model on the training data
    model.fit(X_train, y_train)
    
    return model

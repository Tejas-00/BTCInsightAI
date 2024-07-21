def create_features(data):
    data['Price_Lag1'] = data['Close'].shift(1)
    data['Volume_Lag1'] = data['Volume'].shift(1)
    data['FearGreed_Lag1'] = data['value'].shift(1)
    data = data.dropna()
    return data

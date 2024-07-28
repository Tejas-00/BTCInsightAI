import pandas as pd
from datetime import date

def predict_future_price(model, data):
    # Returns the current local date
    today = date.today()
    print("Today's date is:", today)

    # Calculate tomorrow's date
    tomorrow_date = today + pd.DateOffset(days=1)

    # Create a new DataFrame with the latest values for prediction
    new_data = pd.DataFrame({
        'Open_Lag1': [data['Open'].iloc[-1]],   # Include lagged Open price
        'Close_Lag1': [data['Close'].iloc[-1]], # Lagged Close price
        'Volume_Lag1': [data['Volume'].iloc[-1]], # Lagged Volume
        'FearGreed_Lag1': [data['value'].iloc[-1]] # Lagged Fear & Greed Index
    })

    # Predict the future price
    future_price = model.predict(new_data)

    # Print the predictions for both Open and Close prices
    print(f'Predicted Open price for {tomorrow_date.strftime("%Y-%m-%d")}: {future_price[0][0]:.2f}')
    print(f'Predicted Close price for {tomorrow_date.strftime("%Y-%m-%d")}: {future_price[0][1]:.2f}')

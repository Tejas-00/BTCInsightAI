import pandas as pd
from datetime import date

def predict_future_price(model, data):

    # Returns the current local date
    today = date.today()
    print("Today date is: ", today)

    
    # Calculate tomorrow's date
    tomorrow_date = today + pd.DateOffset(days=1)
    
    # Create a new DataFrame with the latest values
    new_data = pd.DataFrame({
        'Price_Lag1': [data['Close'].iloc[-1]],
        'Volume_Lag1': [data['Volume'].iloc[-1]],
        'FearGreed_Lag1': [data['value'].iloc[-1]]
    })
    
    # Predict the future price
    future_price = model.predict(new_data)
    
    # Print the prediction with the date
    print(f'Predicted price for {tomorrow_date.strftime("%Y-%m-%d")}: {future_price[0]}')

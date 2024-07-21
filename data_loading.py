import pandas as pd

def load_data():
    bitcoin_data = pd.read_csv('bitcoin_price_history.csv', parse_dates=['Date'], index_col='Date')
    fear_greed_data = pd.read_csv('fear_greed_index.csv', parse_dates=['Date'], index_col='Date')
    volume_data = pd.read_csv('bitcoin_volume_history.csv', parse_dates=['Date'], index_col='Date')
    data = bitcoin_data.merge(fear_greed_data, on='Date').merge(volume_data, on='Date')
    data = data.fillna(method='ffill')
    return data

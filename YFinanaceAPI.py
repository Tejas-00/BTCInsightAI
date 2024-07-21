import yfinance as yf

# Define the ticker symbol
ticker = 'BTC-USD'

# Download historical data
bitcoin_data = yf.download(ticker, start='2018-02-01', end='2023-12-31')

# Extract only the closing prices
bitcoin_prices = bitcoin_data['Close']
bitcoin_volume = bitcoin_data['Volume']

# Display the first few rows
print(bitcoin_prices.head())

# Save the closing prices to a CSV file
bitcoin_prices.to_csv('bitcoin_price_history.csv', header=True)
bitcoin_volume.to_csv('bitcoin_volume_history.csv', header=True)
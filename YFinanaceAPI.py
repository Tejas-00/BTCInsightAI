import yfinance as yf

# Define the ticker symbol
ticker = "BTC-USD"

# Get data on this ticker
btc_data = yf.download(ticker, start="2014-09-17", end="2024-01-01")

# Print the first few rows of the data
print(btc_data.head())

# Save data to CSV file
btc_data.to_csv('BTC_USD.csv')
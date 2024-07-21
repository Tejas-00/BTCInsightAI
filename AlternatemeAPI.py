import requests
import pandas as pd

# Fetch data from the Fear & Greed Index API
url = 'https://api.alternative.me/fng/?limit=0'
response = requests.get(url)
data = response.json()

# Convert to DataFrame
fng_data = pd.DataFrame(data['data'])

# Convert the timestamp to datetime format and set it as the index
fng_data['timestamp'] = pd.to_datetime(fng_data['timestamp'], unit='s')
fng_data.set_index('timestamp', inplace=True)

# Rename the index to 'Date'
fng_data.index.name = 'Date'

# Select only the 'value' column
fng_values = fng_data[['value']]

# Sort the DataFrame by index (Date) in ascending order
fng_values.sort_index(inplace=True)

# Save the DataFrame to a CSV file
fng_values.to_csv('fear_greed_index.csv')

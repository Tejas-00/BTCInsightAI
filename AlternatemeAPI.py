import requests
import pandas as pd

url = 'https://api.alternative.me/fng/?limit=0'
response = requests.get(url)
data = response.json()

# Convert to DataFrame
fng_data = pd.DataFrame(data['data'])
fng_data['timestamp'] = pd.to_datetime(fng_data['timestamp'], unit='s')
fng_data.set_index('timestamp', inplace=True)
fng_data.to_csv('fear_greed_index.csv')
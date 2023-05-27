import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
key = 'https://api.binance.com/api/v3/ticker/price'

data = requests.get(key)

new_data = data.json()

df = pd.DataFrame(new_data)

# Convert 'price' column to numeric type
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Perform aggregation operation
average_price_by_symbol = df.groupby('symbol')['price'].mean()

#average_price_by_symbol = df.groupby('symbol')['price'].mean()

# Example: Plot price distribution
df['price'].plot(kind='hist')

# Show analysis results or visualizations
print(average_price_by_symbol)
plt.show()






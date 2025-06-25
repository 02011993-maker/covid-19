import requests
import pandas as pd
import os

# Create data directory if not exists
os.makedirs("data", exist_ok=True)

# Fetch data from COVID19 API
url = "https://api.covid19api.com/summary"
response = requests.get(url)
data = response.json()

# Normalize and save
df = pd.json_normalize(data['Countries'])
df.to_csv("data/covid_summary.csv", index=False)
print("Downloaded and saved as data/covid_summary.csv")

import requests
import pandas as pd
import os

# Create data directory if not exists
os.makedirs("data", exist_ok=True)

# Fetch data from COVID19 API
url = "https://api.covid19api.com/summary"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data['Countries'])
    df = df[['Country', 'Date', 'TotalConfirmed', 'TotalDeaths']]
    df.rename(columns={'TotalConfirmed': 'Confirmed', 'TotalDeaths': 'Deaths'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.to_csv("data/covid_summary.csv", index=False)
    print("Downloaded and saved as data/covid_summary.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")

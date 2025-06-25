# fetch_data.py
import requests
import pandas as pd

def fetch_and_save():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data['Countries'])
    df.to_csv("data/latest_data.csv", index=False)

if __name__ == "__main__":
    fetch_and_save()

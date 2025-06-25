# process_data.py
import pandas as pd

def process():
    df = pd.read_csv("data/latest_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    df['DailyCases'] = df.groupby('Country')['TotalConfirmed'].diff()
    df['7DayAvg'] = df.groupby('Country')['DailyCases'].rolling(window=7).mean().reset_index(0, drop=True)
    df.to_csv("data/processed_data.csv", index=False)

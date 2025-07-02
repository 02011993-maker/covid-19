import pandas as pd
import os

# Load WHO raw data
df = pd.read_csv("data/covid_summary.csv")

# Select and clean
df = df[['Date_reported', 'Country', 'Cumulative_cases', 'Cumulative_deaths']]
df.rename(columns={
    'Date_reported': 'Date',
    'Cumulative_cases': 'Confirmed',
    'Cumulative_deaths': 'Deaths'
}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Country'].notna()]
df = df.sort_values(by=['Country', 'Date'])
df.to_csv("data/processed_data.csv", index=False)

print("✅ Processed WHO data saved as processed_data.csv")

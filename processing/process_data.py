import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/covid_summary.csv")

# Select and clean relevant fields
df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'Date']]
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=["Country", "Date"], inplace=True)

# Save processed data
df.to_csv("data/processed_data.csv", index=False)
print("Processed data saved as data/processed_data.csv")

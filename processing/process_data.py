import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/covid_summary.csv")

# Select and clean relevant fields
df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'Date']]
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Country'].notna()]

# Clean numeric data
df['TotalConfirmed'] = pd.to_numeric(df['TotalConfirmed'], errors='coerce').fillna(0).astype(int)
df['TotalDeaths'] = pd.to_numeric(df['TotalDeaths'], errors='coerce').fillna(0).astype(int)

# Sort and save
df.sort_values(by=["Country", "Date"], inplace=True)
df.to_csv("data/processed_data.csv", index=False)

print("Processed data saved as data/processed_data.csv")

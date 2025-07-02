import pandas as pd
import os

# WHO COVID-19 dataset
URL = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

try:
    df = pd.read_csv(URL)
    df.to_csv(os.path.join(DATA_DIR, "covid_summary.csv"), index=False)
    print("✅ Downloaded WHO data and saved as covid_summary.csv")
except Exception as e:
    print(f"❌ Failed to fetch WHO data: {e}")
    exit(1)

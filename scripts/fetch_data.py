import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve the API key from .env
API_KEY = os.getenv("VELIB_API_KEY")

# Check if the API key is properly loaded
if not API_KEY:
    raise ValueError("❌ Error: VELIB API key not found. Check your .env file!")

# Create the folder "data" if it doesn't exist
os.makedirs("data", exist_ok=True)

# Vélib API URL
API_URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-emplacement-des-stations/exports/json"

# Make the API request
print("📡 Fetching Vélib data...")
response = requests.get(API_URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # Display available columns for verification
    print("✅ Available columns:", df.columns.tolist())

    # Select relevant columns (adjusted based on actual columns)
    columns_to_keep = ["stationcode", "name", "capacity", "station_opening_hours"]
    df = df[columns_to_keep]
    # print(df[df["capacity"] >= 0])  # Display stations with capacity >= 0

    # Add a "panne" column (if capacity is 0)
    df["panne"] = df["capacity"] == 0

    # Save to CSV
    df.to_csv("data/velib_data.csv", index=False, encoding="utf-8")

    print("✅ Vélib data retrieved and saved in 'data/velib_data.csv'!")

else:
    print(f"❌ Error retrieving data (Code {response.status_code})")

    #print(f"Stations with capacity greater than 0: {df['capacity'] >= 0}")

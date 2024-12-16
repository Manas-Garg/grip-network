import json
import os
import pandas as pd

DATA_DIR = "data/"
PROCESSED_DIR = "processed/"

def preprocess_carbon_data(file_path):
    """Preprocess carbon levels data."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data['results'])
    df = df[['date', 'co2', 'ch4']]
    df['date'] = pd.to_datetime(df['date'])
    return df

def save_processed_data(df, filename):
    """Save preprocessed data to CSV."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    file_path = os.path.join(PROCESSED_DIR, filename)
    df.to_csv(file_path, index=False)
    print(f"Processed data saved to {file_path}.")

if __name__ == "__main__":
    for file in os.listdir(DATA_DIR):
        if file.startswith("carbon_levels"):
            raw_path = os.path.join(DATA_DIR, file)
            processed_df = preprocess_carbon_data(raw_path)
            save_processed_data(processed_df, f"processed_{file.split('_')[0]}.csv")

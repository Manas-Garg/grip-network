import requests
import json
from datetime import datetime

# Configuration for Data Sources
DATA_SOURCES = {
    "carbon_levels": "https://api.carbontracker.org/v1/data",
    "temperature": "https://www.ncdc.noaa.gov/cdo-web/api/v2/data",
    "ocean_acidity": "https://api.copernicus.eu/ocean/acidity",
}

HEADERS = {
    "noaa": {"token": "<YOUR_NOAA_API_TOKEN>"},
    "copernicus": {"Authorization": "Bearer <YOUR_COPERNICUS_TOKEN>"},
}

def fetch_data(source_name, url, headers=None):
    """Fetch data from a given URL with optional headers."""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Successfully fetched data for {source_name}.")
        return response.json()
    else:
        print(f"Failed to fetch data for {source_name}: {response.status_code}")
        return None

def save_data_to_file(data, filename):
    """Save the fetched data to a local JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)
        print(f"Data saved to {filename}.")

if __name__ == "__main__":
    for source, url in DATA_SOURCES.items():
        headers = HEADERS.get(source.split("_")[0], None)
        data = fetch_data(source, url, headers)
        if data:
            save_data_to_file(data, f"data/{source}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json")

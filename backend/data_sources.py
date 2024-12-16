import requests

NOAA_API_URL = "https://www.ncei.noaa.gov/access/services/data/v1"
NOAA_TOKEN = "fbFiNXdMFdKefPnFAzwbmsWgSyZhlzSQ"

def test_noaa_connection():
    headers = {"token": NOAA_TOKEN}
    response = requests.get(f"{NOAA_API_URL}datasets", headers=headers)
    if response.status_code == 200:
        print("NOAA API connection successful.")
        print(response.json())
    else:
        print(f"Failed to connect to NOAA API: {response.status_code}")

if __name__ == "__main__":
    test_noaa_connection()

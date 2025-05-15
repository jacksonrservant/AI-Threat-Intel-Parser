import requests

def fetch_otx_iocs(api_key, limit=1000):
    url = f"https://otx.alienvault.com/api/v1/indicators/export?limit={limit}&format=json"
    headers = {"X-OTX-API-KEY": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()  # List of IOCs
    except requests.exceptions.RequestException as e:
        print(f" OTX export failed: {e}")
        return []

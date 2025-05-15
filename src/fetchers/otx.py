import requests

def fetch_otx_pulses(api_key, limit=5):
    url = "https://otx.alienvault.com/api/v1/pulses/subscribed?page=1"
    headers = {"X-OTX-API-KEY": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])[:limit]
    except requests.exceptions.HTTPError as e:
        print(f"❌ OTX fetch failed: {e}")
        return []


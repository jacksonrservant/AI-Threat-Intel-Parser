import requests

def fetch_cisa_kev():
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("vulnerabilities", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch CISA KEV: {e}")
        return []


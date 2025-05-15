from src.fetchers.cisa import fetch_cisa_kev
from src.fetchers.otx import fetch_otx_pulses
from src.fetchers.talos import fetch_talos_latest_blog_text
from src.parser import extract_iocs

print("🔎 Fetching CISA KEV...")
cisa_vulns = fetch_cisa_kev()
print(f"✅ Retrieved {len(cisa_vulns)} vulnerabilities from CISA")

print("\n🔎 Fetching OTX Pulses...")
api_key = "YOUR_OTX_API_KEY_HERE"  # Store securely
otx_data = fetch_otx_pulses(api_key)
print(f"✅ Retrieved {len(otx_data)} OTX pulses")

print("\n🔎 Fetching Cisco Talos blog...")
talos_text = fetch_talos_latest_blog_text()
if talos_text:
    print("✅ Got Talos blog content. Extracting IOCs...\n")
    iocs = extract_iocs(talos_text)
    for k, v in iocs.items():
        print(f"\n{k} ({len(v)} found):")
        for val in set(v):
            print(f"  - {val}")
else:
    print("❌ Failed to extract Talos content")


print("🧠 Real main.py is working")


from dotenv import load_dotenv
import os
from src.parser import extract_iocs
from src.fetchers.cisa import fetch_cisa_kev
from src.fetchers.otx import fetch_otx_pulses
from src.fetchers.talos import fetch_talos_article_text

# Load OTX API key from .env
load_dotenv()
api_key = os.getenv("OTX_API_KEY")

# === CISA KEV ===
print("🔎 Fetching CISA KEV...")
cisa_vulns = fetch_cisa_kev()
print(f"✅ Retrieved {len(cisa_vulns)} vulnerabilities from CISA")

# Optionally extract CVEs
cisa_text = "\n".join(vuln.get("cveID", "") for vuln in cisa_vulns if vuln.get("cveID"))
cisa_iocs = extract_iocs(cisa_text)
print("\n🧪 Extracted CVEs from CISA:")
for val in cisa_iocs.get("CVE", []):
    print(f"  - {val}")

# === OTX Pulses ===
print("\n🔎 Fetching OTX Pulses...")
otx_data = fetch_otx_pulses(api_key)

if not otx_data:
    print("❌ No pulses returned.")
else:
    for pulse in otx_data:
        print(f"\n📦 Pulse: {pulse.get('name')}")
        indicators = pulse.get("indicators", [])
        text = "\n".join(ind.get("indicator", "") for ind in indicators)
        results = extract_iocs(text)

        for ioc_type, values in results.items():
            print(f"\n{ioc_type} ({len(values)} found):")
            for val in set(values):
                print(f"  - {val}")

# === Cisco Talos Blog ===
print("\n🔎 Fetching Cisco Talos Blog...")
talos_text = fetch_talos_article_text("https://blog.talosintelligence.com/threat-hunting-discord-infrastructure/")

if talos_text:
    print("✅ Extracting IOCs from Talos article...\n")
    talos_iocs = extract_iocs(talos_text)
    for ioc_type, values in talos_iocs.items():
        print(f"\n{ioc_type} ({len(values)} found):")
        for val in set(values):
            print(f"  - {val}")
else:
    print("❌ Failed to extract Talos content")

print("\n✅ Finished parsing all sources.")

from src.utils import export_iocs_to_excel

# Collect all IOCs into one dict
all_iocs = {}

# Merge results (simple union)
for result_set in [cisa_iocs, talos_iocs, results]:  # results = OTX
    for ioc_type, values in result_set.items():
        all_iocs.setdefault(ioc_type, []).extend(values)

# Export to Excel
export_iocs_to_excel(all_iocs, filename="threat_iocs.xlsx")




from src.fetchers.cisa import fetch_cisa_kev
from src.parser import extract_iocs
from src.utils import export_iocs_to_excel, export_cves_with_metadata

print("\n Fetching CISA KEV...")
vulns = fetch_cisa_kev()

if not vulns:
    print(" No vulnerabilities retrieved.")
    exit()

print(f" Retrieved {len(vulns)} vulnerabilities from CISA")

#  Export raw CVE metadata with timestamped name
export_cves_with_metadata(vulns, base_name="cisa_detailed_cves")

# Extract all CVEs into a string
cve_text = "\n".join(v.get("cveID", "") for v in vulns if "cveID" in v)

# Parse the CVEs
results = extract_iocs(cve_text)

# Prepare CVEs list (but do not print them)
cves = sorted(set(results.get("CVE", [])))  # Deduplicate + sort

#  Export structured IOCs with timestamped name
export_iocs_to_excel(results, base_name="cisa_kev_iocs")

import pandas as pd
import os
from datetime import datetime

def _generate_timestamped_filename(base_name: str, folder: str = "output") -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, f"{base_name}_{timestamp}.xlsx")

def export_iocs_to_excel(iocs_dict, base_name="cisa_kev_iocs"):
    """
    Export IOCs (Indicators of Compromise) to a timestamped Excel file.
    """
    rows = []
    for ioc_type, values in iocs_dict.items():
        for val in sorted(set(values)):
            rows.append({"Type": ioc_type, "Value": val})

    df = pd.DataFrame(rows)
    filename = _generate_timestamped_filename(base_name)
    df.to_excel(filename, index=False)
    print(f"✅ Exported IOCs to {filename}")

def export_cves_with_metadata(cve_data, base_name="cisa_detailed_cves"):
    """
    Export CVEs with metadata (description, vendor, etc.) to a timestamped Excel file.
    """
    if not cve_data:
        print("❌ No CVE data to export.")
        return

    df = pd.DataFrame(cve_data)
    filename = _generate_timestamped_filename(base_name)
    df.to_excel(filename, index=False)
    print(f"✅ Exported CVE data to {filename}")


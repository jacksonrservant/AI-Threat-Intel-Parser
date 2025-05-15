import re

# Regular expressions for basic IOCs
IOC_PATTERNS = {
    "IPv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "MD5": r"\b[a-fA-F\d]{32}\b",
    "SHA1": r"\b[a-fA-F\d]{40}\b",
    "SHA256": r"\b[a-fA-F\d]{64}\b",
    "Domain": r"\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b",
    "CVE": r"\bCVE-\d{4}-\d{4,7}\b"
}

def extract_iocs(text):
    matches = {}
    for ioc_type, pattern in IOC_PATTERNS.items():
        matches[ioc_type] = re.findall(pattern, text)
    return matches
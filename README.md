# CISA KEV IOC Analyzer

## Overview
This project retrieves vulnerability data from the [CISA Known Exploited Vulnerabilities (KEV) Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), parses it, and outputs detailed vulnerability information into structured Excel (.xlsx) files.

## Features
- Downloads the latest CISA KEV JSON feed
- Parses CVE metadata including ID, description, vendor, product, and required remediation dates
- Outputs clean, filterable Excel spreadsheets for reporting or threat analysis

## Usage
```bash
python main.py

# AI-Threat-Intel-Parser

An AI-powered tool (in-progress) for extracting and structuring threat intelligence indicators (IOCs, TTPs) from open-source cyber threat data.

## Overview

**AI-Threat-Intel-Parser** is an open-source cybersecurity utility designed to collect and organize threat intelligence from publicly available sources. Its current implementation focuses on structured parsing and data export — laying the groundwork for future AI enhancements.

### Current Capabilities

- Fetches threat data from:
  - [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
  ```
  - [AlienVault OTX API](https://otx.alienvault.com/)
  - [Cisco Talos Blog](https://blog.talosintelligence.com/)
  ```
- Parses structured threat intelligence (CVEs, IOCs, dates, vendors, etc.)
- Outputs clean, filterable spreadsheets (`.xlsx`) for threat research and incident response use
- Modular and script-driven for easy extension and experimentation

### Project Vision

The long-term goal is to evolve this parser into a truly **AI-driven threat intel extractor**, capable of:

- Performing **natural language processing** (NLP) on unstructured threat reports and blogs
- Automatically identifying and classifying:
  - Indicators of Compromise (IOCs)
  - MITRE ATT&CK TTPs
  - Threat actor behaviors
- Summarizing threat campaigns with **AI-generated reports**
- Correlating multi-source data to support SOC teams and blue teams

## Project Structure

AI-Threat-Intel-Parser/
├── output/ # Exported threat intel data (.xlsx)
├── parser.py # Script for parsing and generating reports
├── utils.py # Helper functions and data handling logic
├── src/ # (Planned) directory for AI/NLP modules
├── .env # API keys and environment configs
├── README.md # Project overview and goals

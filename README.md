# 🍲 GoFood Competitor Price Intelligence Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📋 Overview
**GoFood Price Intelligence Tool** is a Python-based automation pipeline designed to scrape, clean, and analyze menu data from food delivery platforms (Case Study: *GoFood Indonesia*). 

This tool helps F&B business owners and suppliers perform **Market Research** and **Competitor Price Analysis** in seconds, replacing hours of manual data entry.

## 🚀 Key Features
* **Automated Extraction:** Scrapes restaurant name, menu items, prices, and descriptions from raw HTML.
* **Smart Parsing:** Utilizes `BeautifulSoup4` with precise CSS selectors to handle complex nested HTML structures.
* **ETL Pipeline:**
    * **Extract:** Pulls raw data from offline/online sources.
    * **Transform:** Cleans currency formatting (e.g., converts "24.000" string to `24000` integer), handles missing values, and standardizes text.
    * **Load:** Exports analysis-ready data to CSV and Excel (`.xlsx`) formats.
* **Regional Support:** specifically tuned for Indonesian Currency (IDR) formatting.

## 🛠️ Tech Stack
* **Python 3.10+**
* **BeautifulSoup4** (HTML Parsing)
* **Pandas** (Data Manipulation & Export)
* **OpenPyXL** (Excel Writer Engine)

## 📂 Project Structure
```bash
├── scraper.py          # The Mining Engine (Extracts data from HTML)
├── cleaner.py          # The Refinery (Cleans data & fixes currency types)
├── data_mentah.html    # Raw Source (Target Website)
├── .gitignore          # Git configuration
└── Laporan_Burjo_Final.xlsx  # Final Output (The "Gold")

**`KizunaK15/Scraping-Data-Burjo-Gojek`**
**`[Prima Aji Setyawan]`**
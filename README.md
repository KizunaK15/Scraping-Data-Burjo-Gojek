# GoFood Competitor Price Intelligence Tool 🍲

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License">
</p>

**GoFood Price Intelligence Tool** is a Python-based automation pipeline designed to scrape, clean, and analyze menu data from food delivery platforms (Case Study: *GoFood Indonesia*).

This tool helps F&B business owners and suppliers perform **Market Research** and **Competitor Price Analysis** in seconds, replacing hours of manual data entry.

<!-- Add a GIF of your project in action here -->
<!-- <p align="center"> <img src="link_to_your_gif.gif" width="700"> </p> -->

## Table of Contents
- [Key Features](#key-features-)
- [Tech Stack](#tech-stack-)
- [Installation](#installation-️)
- [Usage](#usage-)
- [Project Structure](#project-structure-)
- [Author](#author-️)
- [License](#license-)


## Key Features 🚀
* **Automated Extraction:** Scrapes restaurant name, menu items, prices, and descriptions from raw HTML.
* **Smart Parsing:** Utilizes `BeautifulSoup4` with precise CSS selectors to handle complex nested HTML structures.
* **ETL Pipeline:**
    * **Extract:** Pulls raw data from offline/online sources.
    * **Transform:** Cleans currency formatting (e.g., converts "24.000" string to `24000` integer), handles missing values, and standardizes text.
    * **Load:** Exports analysis-ready data to CSV and Excel (`.xlsx`) formats.
* **Regional Support:** Specifically tuned for Indonesian Currency (IDR) formatting.

## Tech Stack 🛠️
* **Python 3.10+**
* **BeautifulSoup4** (HTML Parsing)
* **Pandas** (Data Manipulation & Export)
* **OpenPyXL** (Excel Writer Engine)

## Installation ⚙️

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/GoFood-Price-Intelligence.git
   cd GoFood-Price-Intelligence
   ```

2. **Install dependencies**
   Ensure you have Python 3.10+ installed. Then run:
   ```bash
   pip install beautifulsoup4 pandas openpyxl
   ```

## Usage 💻

1. **Prepare Data:** Save the target GoFood menu page as `data_mentah.html` in the root directory.
2. **Run Scraper:** Execute the mining engine to extract raw data.
   ```bash
   python scraper.py
   ```
3. **Run Cleaner:** Process and refine the data into an Excel file.
   ```bash
   python cleaner.py
   ```
4. **Result:** Find the generated report `Laporan_Burjo_Final.xlsx` in the project folder.


## Project Structure 📂
```bash
├── scraper.py                # ⛏️ The Mining Engine (Extracts data from HTML)
├── cleaner.py                # 🏭 The Refinery (Cleans data & fixes currency types)
├── data_mentah.html          # 📄 Raw Source (Target Website HTML)
├── .gitignore                # 🚫 Git configuration
└── Laporan_Burjo_Final.xlsx  # 📊 Final Output (Analysis Ready)
```

---

## Author ✍️

**Prima Aji Setyawan**

*Engineer & IoT Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=social&logo=github)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://linkedin.com/in/yourprofilename)

> **Disclaimer:** This project is for educational and research purposes only. The data used in this repository is a snapshot sample for learning Data Engineering concepts. Please respect the robots.txt and Terms of Service of any website you scrape.

## License 📄

This project is licensed under the MIT License.
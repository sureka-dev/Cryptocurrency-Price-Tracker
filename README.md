# Cryptocurrency Price Tracker

A Python-based Cryptocurrency Price Tracker that automates the extraction and organization of cryptocurrency market information using Selenium, BeautifulSoup, and Pandas.

## 📌 Project Overview

The Cryptocurrency Price Tracker collects important cryptocurrency market information such as:

* Cryptocurrency rank
* Cryptocurrency name
* Symbol
* Current price
* 24-hour percentage change
* Market capitalization
* Timestamp

The extracted data is processed and stored in CSV files for easy viewing and further analysis.

## 🎯 Objectives

* Automate cryptocurrency data extraction.
* Collect information for the top 10 cryptocurrencies.
* Process the extracted data using Pandas.
* Store current cryptocurrency data in CSV format.
* Maintain timestamped historical records.
* Reduce manual effort in collecting cryptocurrency information.

## 🛠️ Technologies Used

* **Python** – Core programming language
* **Selenium** – Browser automation
* **BeautifulSoup** – HTML parsing
* **Pandas** – Data processing and CSV handling
* **ChromeDriver** – WebDriver for browser automation
* **CSV** – Data storage

## ⚙️ How It Works

```text
CoinMarketCap Webpage
        ↓
     Selenium
        ↓
    Page Source
        ↓
   BeautifulSoup
        ↓
   Data Extraction
        ↓
      Pandas
        ↓
 ┌───────────────┬──────────────────┐
 ↓               ↓
crypto_data.csv  crypto_history.csv
```

1. Selenium starts the browser.
2. The CoinMarketCap webpage is loaded.
3. Selenium collects the webpage source.
4. BeautifulSoup parses the HTML.
5. The top 10 cryptocurrency records are extracted.
6. Pandas organizes the extracted information.
7. The current data is saved to `crypto_data.csv`.
8. Timestamped records are stored in `crypto_history.csv`.

## 📊 Data Collected

The project extracts the following fields:

| Field          | Description                     |
| -------------- | ------------------------------- |
| Rank           | Cryptocurrency ranking          |
| Cryptocurrency | Name of the cryptocurrency      |
| Symbol         | Cryptocurrency symbol           |
| Price          | Current displayed price         |
| 24h Change     | Percentage change over 24 hours |
| Market Cap     | Market capitalization           |
| Timestamp      | Date and time of extraction     |

## 📁 Project Structure

```text
Cryptocurrency-Price-Tracker/
│
├── crypto_tracker.py
├── coinmarketcap.html
├── crypto_data.csv
├── crypto_history.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Cryptocurrency-Price-Tracker.git
```

### 2. Open the project folder

```bash
cd Cryptocurrency-Price-Tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

Run the following command:

```bash
python crypto_tracker.py
```

The program will extract the cryptocurrency information and generate the CSV output files.

## 📄 Output Files

### `crypto_data.csv`

Contains the latest extracted cryptocurrency information.

### `crypto_history.csv`

Stores timestamped records for maintaining historical data.

## 🧪 Testing

The project was tested for:

* Selenium browser initialization
* Webpage loading
* Cryptocurrency table detection
* Data extraction
* Top 10 cryptocurrency collection
* Pandas DataFrame creation
* CSV file generation
* Historical data logging

The final execution completed successfully without errors.

## ⚠️ Limitations

* The current implementation collects the top 10 cryptocurrencies.
* The working version uses a saved CoinMarketCap webpage because direct network access to the website was unavailable in the development environment.
* The extracted market values therefore depend on the saved webpage.
* Data is stored in CSV files instead of a database.
* A graphical dashboard is not currently included.

## 🔮 Future Scope

The project can be extended with:

* Live cryptocurrency API integration
* Real-time price updates
* Interactive dashboards
* Price and market-cap charts
* Database integration
* Automated scheduled data collection
* Cryptocurrency filtering
* Price-change notifications
* Support for more cryptocurrencies

## 👩‍💻 Author

**Sureka M S**

B.Tech Artificial Intelligence and Data Science
SKP Engineering College

## 📌 Project Type

**Individual Internship Project**

---

⭐ This project demonstrates practical applications of **Python automation, web scraping, HTML parsing, and data processing** for cryptocurrency market data collection.

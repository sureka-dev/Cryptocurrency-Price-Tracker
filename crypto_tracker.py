from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# =====================================================
# CRYPTOCURRENCY PRICE TRACKER
# =====================================================

TOP_COINS = 10

DRIVER_PATH = r"C:\Users\DELL\.wdm\drivers\chromedriver\win64\152.0.7977.82\chromedriver-win64\chromedriver.exe"

HTML_FILE = os.path.abspath("coinmarketcap.html")
DATA_FILE = "crypto_data.csv"
HISTORY_FILE = "crypto_history.csv"

print("=" * 60)
print("CRYPTOCURRENCY PRICE TRACKER")
print("=" * 60)

# -----------------------------------------------------
# Selenium setup
# -----------------------------------------------------

options = Options()
options.binary_location = r"C:\Users\DELL\AppData\Local\Programs\Opera\opera.exe"
options.add_argument("--start-maximized")

service = Service(DRIVER_PATH)

driver = webdriver.Chrome(
    service=service,
    options=options
)

print("\nSelenium browser started.")
print("Opening saved CoinMarketCap page...")

driver.get("file:///" + HTML_FILE.replace("\\", "/"))

print("Saved page loaded.")

# -----------------------------------------------------
# Get page source using Selenium
# -----------------------------------------------------

html = driver.page_source

print("Page source collected.")

driver.quit()

# -----------------------------------------------------
# Parse HTML
# -----------------------------------------------------

soup = BeautifulSoup(html, "html.parser")

rows = soup.select("table tbody tr")

print("Rows found:", len(rows))

data = []

for row in rows:

    text = row.get_text(" | ", strip=True)

    parts = [
        x.strip()
        for x in text.split("|")
        if x.strip()
    ]

    # Need at least the required fields
    if len(parts) < 9:
        continue

    # First row is CMC20, so only accept numbered rows
    if not parts[0].isdigit():
        continue

    rank = parts[0]
    name = parts[1]
    symbol = parts[2]
    price = parts[4]
    change_24h = parts[5]
    market_cap = parts[8]

    data.append({
        "Rank": rank,
        "Cryptocurrency": name,
        "Symbol": symbol,
        "Price": price,
        "24h Change": change_24h,
        "Market Cap": market_cap,
        "Timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    })

    if len(data) == TOP_COINS:
        break

# -----------------------------------------------------
# Save data
# -----------------------------------------------------

if data:

    df = pd.DataFrame(data)

    print("\n")
    print("=" * 70)
    print("TOP 10 CRYPTOCURRENCIES")
    print("=" * 70)

    print(df.to_string(index=False))

    # Current data
    df.to_csv(
        DATA_FILE,
        index=False
    )

    # Historical logging
    if os.path.exists(HISTORY_FILE):

        df.to_csv(
            HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            HISTORY_FILE,
            index=False
        )

    print("\nData saved successfully!")
    print("Current data    :", DATA_FILE)
    print("Historical data :", HISTORY_FILE)

else:

    print("\nNo cryptocurrency data found.")

print("\nTracker completed.")
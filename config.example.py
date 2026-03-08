# API Configuration
API_BASE_URL = "https://v6.exchangerate-api.com/v6"
API_KEY = "your_api_key_here"

# Currencies to track
BASE_CURRENCY = "USD"
TARGET_CURRENCIES = [
    "EUR", "GBP", "JPY", "CAD",
    "AUD", "CHF", "CNY", "SAR"
]

# Output
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "currency_report.xlsx"
LOG_FILE = BASE_DIR / "automation.log"
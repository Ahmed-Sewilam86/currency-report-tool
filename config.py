# API Configuration
API_BASE_URL = "https://v6.exchangerate-api.com/v6"
API_KEY = "870d415513a7ad3cb68d2068"

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
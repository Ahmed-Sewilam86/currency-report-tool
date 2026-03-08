# Currency Exchange Rate Report Tool

A Python automation tool that fetches real-time currency exchange rates
and generates a formatted Excel report automatically.

---

## The Problem It Solves

Businesses and traders who deal with multiple currencies need
up-to-date exchange rates in a clean, readable format.
This tool fetches live rates and delivers a professional Excel
report in seconds.

---

## What It Does

- Fetches real-time exchange rates via API
- Supports multiple currencies simultaneously
- Generates a formatted Excel report
- Logs all operations for traceability

---

## Supported Currencies

USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, SAR

---

## Project Structure
```
currency-report-tool/
│
├── main.py               # Main execution pipeline
├── config.py             # API and file configuration
├── api_client.py         # API connection handler
├── data_processor.py     # Data processing and structuring
├── report_generator.py   # Excel report generation
└── requirements.txt      # Project dependencies
```

---

## Technologies Used

- Python 3.10+
- requests
- pandas
- openpyxl

---

## Installation
```bash
git clone https://github.com/your-username/currency-report-tool.git
cd currency-report-tool
pip install -r requirements.txt
```

---

## How to Run
```bash
python main.py
```

The file `currency_report.xlsx` will be created in the project folder.

---

## Use Cases

- Daily currency tracking for traders
- Financial reporting automation
- Import/export business rate monitoring
- Multi-currency business dashboards

---

## License

MIT License — free to use and modify.
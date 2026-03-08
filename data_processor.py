import pandas as pd
import logging
from datetime import datetime
from config import TARGET_CURRENCIES, BASE_CURRENCY


def process_exchange_rates(data: dict) -> pd.DataFrame:
    """
    Process raw API data into a structured DataFrame.

    Args:
        data (dict): Raw API response.

    Returns:
        pd.DataFrame: Processed exchange rates.
    """
    try:
        rates = data["conversion_rates"]
        last_update = data["time_last_update_utc"]

        records = []

        for currency in TARGET_CURRENCIES:
            if currency in rates:
                records.append({
                    "Base Currency": BASE_CURRENCY,
                    "Target Currency": currency,
                    "Exchange Rate": rates[currency],
                    "Last Updated": last_update,
                    "Report Date": datetime.today().strftime("%Y-%m-%d"),
                })

        df = pd.DataFrame(records)

        logging.info("Exchange rates processed successfully.")
        return df

    except Exception as e:
        logging.error(f"Error processing exchange rates: {e}")
        raise
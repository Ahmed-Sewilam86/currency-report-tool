import httpx
import logging
from config import API_BASE_URL, API_KEY, BASE_CURRENCY


def get_exchange_rates() -> dict:
    """
    Fetch latest exchange rates from API.

    Returns:
        dict: Exchange rates data.
    """
    try:
        url = f"{API_BASE_URL}/{API_KEY}/latest/{BASE_CURRENCY}"
        response = httpx.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["result"] != "success":
            raise ValueError(f"API returned error: {data}")

        logging.info("Exchange rates fetched successfully.")
        return data

    except httpx.ConnectError:
        logging.error("No internet connection.")
        raise

    except httpx.TimeoutException:
        logging.error("API request timed out.")
        raise

    except Exception as e:
        logging.error(f"Error fetching exchange rates: {e}")
        raise
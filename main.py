import logging
from config import OUTPUT_FILE, LOG_FILE
from api_client import get_exchange_rates
from data_processor import process_exchange_rates
from report_generator import generate_excel_report


def setup_logging():
    """
    Configure logging settings.
    """
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main():
    """
    Main execution pipeline for currency report automation.
    """
    try:
        logging.info("Currency report process started.")

        # Step 1: Fetch exchange rates
        raw_data = get_exchange_rates()

        # Step 2: Process data
        df = process_exchange_rates(raw_data)

        # Step 3: Generate report
        generate_excel_report(str(OUTPUT_FILE), df)

        logging.info("Currency report process completed successfully.")
        print("Currency report generated successfully.")
        print(f"Report saved to: {OUTPUT_FILE}")

    except Exception as e:
        logging.error(f"Currency report process failed: {e}")
        print("An error occurred. Check the log file for details.")


if __name__ == "__main__":
    setup_logging()
    main()
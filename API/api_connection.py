import pandas as pd
import requests
import smtplib
from typing import Dict, Any


# =========================
# Configuration
# =========================

CSV_PATH = "/complete/path/"

CSV_PRODUCTION = "production.csv"
CSV_MACHINES = "alarms.csv"
CSV_ERRORS = "errors.csv"

BASE_URL = "https://.../"

API_PRODUCTION = BASE_URL + "api1/api"
API_MACHINES = BASE_URL + "api2"
API_ERRORS = BASE_URL + "api3"

EMAIL_HOST = "host.email.com"
EMAIL_PORT = 587
EMAIL_USER = "myemail@email.com"
EMAIL_PASSWORD = "mypassword"
EMAIL_FROM = "emailfrom@email.com"
EMAIL_TO = "toemail@email.com"

ERROR_GENERAL = "GENERAL ERROR: CSV files could not be generated."
ERROR_EMPTY_FILE = "EMPTY DATA ERROR: The file was not generated because the API returned no data."


# =========================
# Core Functions
# =========================

def fetch_api_data(url: str) -> Dict[str, Any]:
    """
    Fetch data from an API endpoint.
    """
    response = requests.get(url, verify=False, timeout=60)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"API connection failed: {url}")


def save_to_csv(data: Dict[str, Any], filename: str) -> None:
    """
    Convert API response data into a CSV file.
    """
    df = pd.DataFrame(data.get("data", []))
    df.to_csv(CSV_PATH + filename, index=False)


def send_error_email(message: str) -> None:
    """
    Send an error notification email.
    """
    email_message = f"Subject: API Processing Error\n\n{message}"

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout=120)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, email_message)
    server.quit()


# =========================
# Main Execution
# =========================

def main() -> None:
    try:
        production_data = fetch_api_data(API_PRODUCTION)

        if not production_data.get("data"):
            send_error_email(ERROR_EMPTY_FILE)
            return

        save_to_csv(production_data, CSV_PRODUCTION)

        machines_data = fetch_api_data(API_MACHINES)
        save_to_csv(machines_data, CSV_MACHINES)

        errors_data = fetch_api_data(API_ERRORS)
        save_to_csv(errors_data, CSV_ERRORS)

    except Exception as error:
        send_error_email(f"{ERROR_GENERAL}\n\nDetails: {error}")


if __name__ == "__main__":
    main()



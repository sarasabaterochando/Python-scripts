import pandas as pd
import requests
import smtplib

csv_production = 'production_data.csv'
csv_machines = 'machines_data.csv'
csv_errors = 'errors_data.csv'

URL_PRODUCTION = API_URL + "machines/data"
URL_MACHINES = API_URL + "alarms"
URL_ERRORS = API_URL + "errors"

# Email error messages
ERROR_GENERAL = 'GENERAL ERROR: Failed to generate the files'
ERROR_EMPTY_FILE = 'EMPTY FILE ERROR: The file was not generated because it contains no data'


def connect_to_api(url):
    """Call the provided API URL and return the JSON response."""
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return send_email(url)


def convert_to_dataframe(data, csv_file):
    """Convert API JSON response into a CSV file."""
    df = pd.DataFrame(data['data'])
    df.to_csv(path + csv_file, index=False)


def send_email(error_message):
    """Send an error notification via email."""
    message = f'API connection error.\n\nError connecting to API: {error_message}\n\n'
    mailserver = smtplib.SMTP(MAIL_HOST, 587, timeout=120)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(MAIL_ADDRESS, MAIL_PASSWORD)
    mailserver.sendmail(MAIL_ADDRESS, MAIL_ADDRESS, message)
    mailserver.quit()


if __name__ == '__main__':
    try:
        production_data = connect_to_api(URL_PRODUCTION)

        if len(production_data) != 0:
            convert_to_dataframe(production_data, csv_production)
            machines_data = connect_to_api(URL_MACHINES)
            convert_to_dataframe(machines_data, csv_machines)
            errors_data = connect_to_api(URL_ERRORS)
            convert_to_dataframe(errors_data, csv_errors)
        else:
            send_email(ERROR_EMPTY_FILE)

    except Exception:
        send_email(ERROR_GENERAL)

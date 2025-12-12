# Data Pipeline Automation

This Python script automates the process of fetching data from multiple API endpoints, converting the responses into CSV files, and handling errors by sending email notifications.  

## 📦 Features

- Connects to 3 API endpoints:
  - Machine production history
  - Machine alarms
  - Error logs
- Converts JSON responses into clean CSV files.
- Sends automatic email alerts in case of API or data issues.

## ⚙️ Environment Setup

Create a secure method to keep the following variables:
```
path = "path/to/output/folder/"
API_URL = "https://example.com/api/"
MAIL_HOST = "smtp.yourprovider.com"
MAIL_ADDRESS = "youremail@example.com"
MAIL_PASSWORD = "your_password"
```

### 🔐 Security Notes

-   Avoid storing passwords in the script\
-   Prefer environment variables or `.env` files\
-   Use SSH key-based authentication whenever possible

Install dependencies: 

`pip install pandas requests`


## 🚀 Usage

Run the script manually or schedule it:

python api_connection.py


The script will:
1. Fetch API data.
2. Save it into CSV files in the specified path.
3. Send an email if something goes wrong (no data or connection errors).

## 🧠 Notes

- The script disables SSL verification (`verify=False`) for convenience — enable it in production for security.
- Do **not** commit your real credentials or company URLs to public repositories.
- Replace the API endpoints and email configuration with generic/demo data before publishing.

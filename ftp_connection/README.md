# 📄 SSH CSV Downloader & Appender (Python Script)

## 📌 Overview

This Python script automates the process of **connecting to a remote
server via SSH**, **downloading a CSV file**, and **appending its
contents to a local CSV file**.

It is designed for tasks such as scheduled data ingestion, daily CSV
updates, or consolidating remote datasets.

Technologies used: - **Paramiko** -- SSH & SFTP connection\
- **Pandas** -- Data processing\
- **OS** -- File handling

------------------------------------------------------------------------

## 🚀 Features

-   SSH connection to remote server\
-   CSV download via SFTP\
-   Appends data into a local "complete" CSV\
-   Adds header only when needed\
-   Skips malformed CSV lines with `on_bad_lines='skip'`

------------------------------------------------------------------------

## 📁 Project Structure

    .
    ├── connection.py
    └── README.md

------------------------------------------------------------------------

## ⚙️ Requirements

Install dependencies:

    pip install pandas paramiko

------------------------------------------------------------------------

## 🔧 Configuration

Update the following variables inside the script before running:

    host = "host address"
    username = "username"
    password = "password"
    port = 22

    path_download = "local download path"
    path_remote = "remote file path"
    full_file = "full.csv"
    file_download = "download.csv"

### Variable Description

  Variable                  Description
  ------------------------- -----------------------------------
  `host`                    Remote server IP or hostname
  `username` / `password`   SSH credentials
  `port`                    SSH port (default: 22)
  `path_remote`             File path in the remote server
  `path_download`           Local folder for downloads
  `file_download`           Name of the downloaded file
  `full_file`               Destination CSV for appended data

------------------------------------------------------------------------

## ▶️ How It Works

### **1. Download the CSV file (`download_file`)**

-   Connects to the server via SSH\
-   Opens an SFTP session\
-   Downloads the remote CSV\
-   Closes all connections

### **2. Append data (`copy_file`)**

-   Reads the downloaded CSV with Pandas\
-   Appends it to `full.csv`\
-   Adds header only if the file does not yet exist\
-   Skips invalid CSV rows

------------------------------------------------------------------------

## ▶️ Running the Script

Simply execute:

    python connection.py

The script will: 1. Download the CSV from the remote server\
2. Append its contents to `full.csv`

------------------------------------------------------------------------

## 🔐 Security Notes

-   Avoid storing passwords in the script\
-   Prefer environment variables or `.env` files\
-   Use SSH key-based authentication whenever possible

------------------------------------------------------------------------

## 📌 Possible Improvements

-   Add exceptions and error handling\
-   Add logging for monitoring executions\
-   Parameterize file names and paths\
-   Switch to SSH keys instead of password authentication
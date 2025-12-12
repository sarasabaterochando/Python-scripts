# 📄 Document Processing Application (Streamlit)

This project is a Streamlit application that automates the generation of DOCX and PDF documents from an Excel file using predefined templates. It is designed as a practical example of document automation, error handling, and a simple web UI for non-technical users.

## Features

- Loads data from an Excel file and iterates through each row.
- Fills Word (`.docx`) templates by replacing placeholder tags (e.g. `{{NAME}}`, `{{ID_NUMBER}}`, `{{ROLE}}`, `{{DATE}}`).
- Fills a base PDF template by overlaying text (name, ID number, date, etc.) at specific coordinates.
- Generates one DOCX or PDF per record, with meaningful output filenames.
- Provides a Streamlit UI with options to select:
  - Document type (template group).
  - Output file type: Word or PDF.
- Implements a logging decorator to capture and log errors to a file.
- Includes a cleaning function to clear previous output before generating new files.

## How It Works

1. The app reads an Excel file that contains columns such as `Name`, `IdNumber`, `Role`, and `Date`.
2. For each row:
   - If the selected file type is **Word**, it:
     - Opens each `.docx` template in the selected document type folder.
     - Replaces placeholders in both paragraphs and tables.
     - Saves a new `.docx` file in the output folder.
   - If the selected file type is **PDF**, it:
     - Loads a base PDF template.
     - Creates an overlay PDF with the text positioned at predefined coordinates.
     - Merges the overlay with the base template.
     - Saves the final PDF in the output folder.
3. Logging is applied through a decorator that wraps key functions, logging errors with stack traces and showing user-friendly messages in the Streamlit interface.
4. The user interacts with the app via a simple Streamlit UI:
   - Selects the document type (`type_1`, `type_2`, `type_3`).
   - Chooses whether to generate PDF or Word files.
   - Clicks **Run** to start the process.

## Project Structure (Conceptual)

Although paths and configuration are injected externally, the core components are:

- **Excel input**: `file_xlsx` (path to the Excel file).
- **Word template folder**: `path_doc_files` (base path where template subfolders reside).
- **Base PDF template**: `path_pdf_file` (path to the PDF used as a background).
- **Output folder**: `path_final` (where generated DOCX/PDF files are stored).
- **Log folder**: `path_log` (directory to store the log file `transformation_log.log`).

These paths are expected to be defined before running the application (for example via environment variables, configuration file, or another initialization script).

## Main Components

### 1. Error Logging Decorator

A `log_function` decorator wraps critical functions. It:

- Catches exceptions.
- Logs detailed error information (including arguments and full traceback) to `transformation_log.log`.
- Displays a concise error message in the Streamlit UI, keeping the interface user-friendly.

### 2. Word Document Processing

`process_word_files(name, id_number, role, date, document_type)`:

- Iterates over all `.docx` files in a given document type folder.
- Replaces the placeholders:
  - `{{NAME}}`
  - `{{ID_NUMBER}}`
  - `{{ROLE}}`
  - `{{DATE}}`
- Handles replacements in both paragraphs and tables.
- Uses `save_docx(...)` to write the final document into the output folder.

### 3. PDF Filling

`fill_pdf_files(name, id_number, date)`:

- Loads the base PDF template.
- Creates an overlay using `reportlab` and writes the text fields at specified coordinates.
- Merges the overlay with the original PDF page.
- Saves the result as `<Name>_<IdNumber>.pdf` in the output folder.

The coordinates are manually tuned and can be adjusted to fit different PDF templates.

### 4. Excel Processing

`process_excel(document_type, file_type)`:

- Iterates through each row of the loaded Excel data.
- Extracts `name`, `id_number`, `role`, and `date`.
- Dispatches processing to:
  - `process_word_files(...)` when `file_type == "word"`.
  - `fill_pdf_files(...)` when `file_type == "pdf"`.

### 5. Output Folder Cleanup

`clear_output_folder()`:

- Removes all files and subdirectories inside the output directory.
- Logs and displays errors in case any file cannot be deleted.
- Ensures each run starts with a clean set of outputs.

### 6. Streamlit UI

`render_ui()`:

- Sets the main title and subtitle.
- Displays a short instruction for the user.
- Renders controls:
  - `st.radio` for document type (`type_1`, `type_2`, `type_3`).
  - `st.radio` for file type (`pdf`, `word`).
  - `st.button('Run')` to trigger the process.

When the user presses **Run**:

1. The output folder is cleared.
2. The Excel is processed.
3. A success message is shown on completion, or an error message if something fails.

## Requirements

The project uses:

- `pandas`
- `python-docx` (`docx`)
- `pypdf`
- `reportlab`
- `streamlit`

Example installation (using `pip`):

`pip install pandas python-docx pypdf reportlab streamlit`

## Running the Application

1. Ensure all required libraries are installed.
2. Make sure the following variables are defined before running the script:
   - `file_xlsx`
   - `path_doc_files`
   - `path_pdf_file`
   - `path_final`
   - `path_log`
3. From the project directory, run:

`streamlit run fill_word_pdf.py`


4. Open the URL shown in the terminal (usually `http://localhost:8501`) in a browser.
5. Select the document type and output format (PDF or Word).
6. Click **Run** to generate the documents.


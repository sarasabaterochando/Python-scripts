# Sales Data Processing with PySpark

## Overview
This project demonstrates a **data engineering workflow** using **PySpark**.  
The goal is to read raw transaction data from a text file, transform it into a structured **Spark DataFrame**, cast the data to appropriate types, and save the final output as a **CSV file**.  

This notebook is suitable for portfolio demonstration as it shows **end-to-end data processing** steps commonly used in ETL pipelines.

---

## Technologies Used
- **Python 3.12**  
- **PySpark** for distributed data processing  
- **Regular Expressions (`re`)** for parsing raw text  
- **Jupyter Notebook** for step-by-step workflow and visualization  

---

## Project Workflow

### 1. Read Raw Text File
The raw data contains sales transactions in the following format:

TRANSACTION_ID: 1001 | DATE: 2026-01-15 | CUSTOMER: Ana_Martinez | PRODUCT: Laptop_Pro_15 | TOTAL: 1250.50 | STATUS: Completed
TRANSACTION_ID: 1002 | DATE: 2026-01-15 | CUSTOMER: Luis_Gomez | PRODUCT: Monitor_4K | TOTAL: 340.00 | STATUS: Pending
...


### 2. Parse Text Lines
Each line is parsed using **regular expressions** to extract fields:  
- `transaction_id`  
- `date`  
- `customer`  
- `product`  
- `total`  
- `status`  

The parsed data is stored as a **list of dictionaries**.

### 3. Create Spark DataFrame
The list of dictionaries is converted into a **PySpark DataFrame**.  
The schema is inferred initially, and the data types are printed using `printSchema()`.

### 4. Transform Data Types
Columns are cast to appropriate types:
- `transaction_id` → Integer  
- `date` → Date  
- `total` → Double  

This ensures consistent and structured data for analysis.

### 5. Save DataFrame as CSV
The transformed DataFrame is saved as a **single CSV file** using:

```python
df.coalesce(1).write.csv("files/sales_final.csv", header=True, mode="overwrite")
```
* coalesce(1) merges all partitions into one file

* header=True includes column names

### 6. Read and Verify CSV
Finally, the CSV is read back into a Spark DataFrame to verify the output.
```python
df2 = spark.read.csv("files/sales_final.csv", header=True, inferSchema=True)
df2.show()
df2.printSchema()
```

## How to Run
1. Install dependencies:
```bash
pip install pyspark jupyter
```
2. Open the notebook in Jupyter:
```
jupyter notebook Sales_ETL.ipynb
```
3. Run cells sequentially.

**Note:** Paths in the notebook use relative paths (`files/sales_raw.txt` and `files/sales_final.csv`). Make sure the `files` folder exists.

## Expected Output
* A structured Spark DataFrame with columns:
```
transaction_id	date	customer	product	total	status
1001	2026-01-15	Ana_Martinez	Laptop_Pro_15	1250.50	Completed
1002	2026-01-15	Luis_Gomez	Monitor_4K	340.00	Pending
…	…	…	…	…	…
```
* CSV file saved as `sales_final.csv` with the same structure.
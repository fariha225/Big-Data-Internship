Task 1 – Big Data Cleaning (Using PySpark)

This task focuses on loading a large dataset using Apache Spark and performing essential data cleaning operations such as handling missing values, removing invalid records, converting data types, and generating a cleaned output file.

✅ 1. Objective of This Task

The goal of Task 1 was to:
⦁	Load a large retail dataset using Apache Spark
⦁	Perform manual data handling & cleaning
⦁	Remove duplicates
⦁	Filter invalid/negative records
⦁	Clean text columns
⦁	Add new calculated fields
⦁	Save the cleaned output as a new file

This task demonstrates basic data engineering skills using Spark for big-data processing.


📂 2. Dataset Used

Dataset Name: Online Retail Dataset (UCI Repository)
File: OnlineRetail.csv


Contains customer transactions from a UK-based retailer

Rows: 541,909
Columns: 8


Includes details like:

Invoice number
Product code
Description
Quantity
Invoice date
Price
Customer ID
Country


⚙️ 3. Tools & Technologies

Python 3.11
Apache PySpark
VS Code for running scripts


🔍 4. Data Cleaning Steps Performed

Below is the exact cleaning pipeline implemented in PySpark.

⦁	Step 1 — Start Spark Session

   Initialize Spark engine with required memory.

⦁	Step 2 — Load Raw CSV

   Read file with header
   Infer schema automatically
   Print row/column count + schema

⦁	Step 3 — Remove Cancellation Invoices

   Invoices starting with “C” indicate returns.
   These were removed.

⦁	Step 4 — Remove Duplicate Rows

   Ensures cleaner and more accurate analysis.

⦁	Step 5 — Handle Missing Customer IDs

   Rows where CustomerID was null were removed.

⦁	Step 6 — Remove Invalid Quantity & Unit Price

   Removed rows where:

   Quantity ≤ 0
   Unit price ≤ 0

⦁	Step 7 — Clean Product Description

   Converted to lowercase

   Trimmed extra spaces

⦁	Step 9 — Add TotalPrice Column

   TotalPrice = Quantity × UnitPrice

⦁	Step 10 — Save Cleaned Data

   Output saved as:
   cleaned_retail.csv


📊 5. Before vs After Cleaning
Metric	                 Before Cleaning     After Cleaning
Rows	                   541,909   	         392,692
Columns	                 8	                 10 (added InvoiceDateTS & TotalPrice)
Missing Customer IDs	   135,080	           Removed
Negative/Zero Quantity	 10,624	             Removed
Negative/Zero UnitPrice	 2,517	             Removed
Cancellation Invoices	   9,288	             Removed


🧾 6. Final Output

The cleaned dataset is exported as:

✔ cleaned_retail.csv

This file is used in Task 2 (Distributed Processing).




🧪 7. How to Run the Script

Open terminal and run:

py task1_cleaning.py


Make sure the following files are in the same folder:

task1_cleaning.py
OnlineRetail.csv



📘 8. Learning Outcomes

⦁	How to process large datasets using Spark
⦁	How to apply filtering, deduplication, and missing-value handling
⦁	How to clean text fields
⦁	How to add calculated columns
⦁	How to export cleaned output

This task is foundational for the upcoming analysis and visualizations.

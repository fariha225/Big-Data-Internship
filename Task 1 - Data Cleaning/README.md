# ⭐ Task 1 – Big Data Cleaning (Using PySpark)

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : Syeda Fariha Fatima 

*INTERN ID* : CT04DR818

*DOMAIN* : Big Data

*DURATION*: 4 weeks

*MENTOR* : Neela Santhosh Kumar

This task focuses on cleaning a **large retail dataset** using **Apache Spark**, performing operations such as handling missing values, removing invalid records, converting data types, and generating a cleaned dataset for further analysis.

---

## ✅ 1. Objective of This Task

The goal of Task 1 was to:

- Load a large dataset using **Apache Spark**
- Perform **manual data handling & cleaning**
- Remove **duplicates**
- Filter invalid or negative records
- Clean text fields
- Add **new calculated columns**
- Save the **final cleaned dataset**

This task demonstrates core **data engineering skills** for Big Data processing.

---

## 📂 2. Dataset Used

**Dataset:** Online Retail Dataset (UCI Repository)  
**File:** `OnlineRetail.csv`

Contains customer transaction records from a UK-based retailer.

| Property | Value |
|---------|--------|
| **Rows** | 541,909 |
| **Columns** | 8 |
| **Includes** | InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country |

---

## ⚙️ 3. Tools & Technologies

- **Python 3.11**
- **Apache PySpark**
- **VS Code** (to run scripts)

---

## 🔍 4. Data Cleaning Steps Performed

Below is the complete cleaning pipeline implemented in PySpark:

### **Step 1 — Start Spark Session**
- Initialize Spark engine with memory configs.

### **Step 2 — Load Raw CSV**
- Load CSV with header  
- Infer schema  
- Print dataset size + schema  

### **Step 3 — Remove Cancellation Invoices**
- Invoices starting with **“C”** indicate returns → removed.

### **Step 4 — Remove Duplicate Rows**
- Ensures correctness of further analysis.

### **Step 5 — Handle Missing Customer IDs**
- All rows with **CustomerID = NULL** removed.

### **Step 6 — Remove Invalid Quantity & UnitPrice**
Removed rows where:
- Quantity **≤ 0**
- UnitPrice **≤ 0**

### **Step 7 — Clean Description Field**
- Lowercased text  
- Trimmed whitespace

### **Step 8 — Convert Invoice Date to Timestamp**
- Added new column: `InvoiceDateTS`

### **Step 9 — Add TotalPrice Column**
- TotalPrice = Quantity × UnitPrice

### **Step 10 — Save Final Cleaned Output**
- Output saved as: **cleaned_retail.csv**

---

## 📊 5. Before vs After Cleaning

| Metric | Before Cleaning | After Cleaning |
|--------|------------------|----------------|
| **Rows** | 541,909 | 392,692 |
| **Columns** | 8 | 10 (added InvoiceDateTS & TotalPrice) |
| **Missing Customer IDs** | 135,080 | Removed |
| **Negative/Zero Quantity** | 10,624 | Removed |
| **Negative/Zero UnitPrice** | 2,517 | Removed |
| **Cancellation Invoices** | 9,288 | Removed |

---

## 🧾 6. Final Output

The cleaned dataset generated:

✔ `cleaned_retail.csv`  
(used in Task 2 – Distributed Data Processing)

---

## 🧪 7. How to Run the Script

To run the cleaning script:

```py task1_cleaning.py ```

Make sure the following files are in the same folder:

task1_cleaning.py
OnlineRetail.csv

## 📘 8. Learning Outcomes

This task helped in understanding:

- Loading & processing large datasets using PySpark

- Handling missing values & invalid records

- Filtering, deduplication, and text cleaning

- Adding calculated columns

- Exporting cleaned datasets for further analysis


---

## OUTPUT ## 
- Cleaned Dataset
<img width="900" height="799" alt="Image" src="https://github.com/user-attachments/assets/a2b9dbeb-70a5-44ed-b4e4-4555c7a71323" />




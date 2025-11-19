# **Big Data Internship – Project Repository**

This repository contains all four tasks completed during the **CodTech Big Data Internship**, covering data cleaning, distributed processing, visualization, and data security.

## 📌 **Task Summary**

### ✅ **Task 1: Data Cleaning (PySpark)**
- Loaded & cleaned **500K+ retail records** using PySpark  
- Removed duplicates, invalid data, missing CustomerID  
- Cleaned text columns & added derived fields  
- Output generated: **`cleaned_retail.csv`**

---

### ✅ **Task 2: Distributed Processing (PySpark)**
- Performed distributed group-by aggregations  
- Generated KPIs:
  - Total Revenue  
  - Average Order Value (AOV)  
  - Total Customers  
  - Total Transactions  
- Created:
  - Revenue by Country  
  - Top Products / Customers  
  - Invoice-level summaries  
- Extracted **Monthly Revenue Trend**  
- Output CSVs used for visualization in Task 3

---

### ✅ **Task 3: Data Visualization (Power BI)**  
Created a complete BI dashboard with:
- Executive Summary (KPI cards)
- Revenue by Country (Map + Bar)
- Product Analysis
- Customer Analysis
- Monthly Revenue Trend

Final file: **`Data Visualization.pbix`**

---

### ✅ **Task 4: Data Security & Compliance**
Implemented two security mechanisms:
- **Role-Based Access Control**
  - Analyst → Masked CustomerID  
  - Manager → Full access  
- **Data Masking**
- **Audit Logging System** for all access events

Generated outputs:
- `demo_masked.csv`
- `demo_manager.csv`
- `task4_audit_log.txt`
- `terminal_output.txt`

Screenshots stored in: **`Task 4 - Data Security/Screenshots/`**

---

## ⭐ **Final Notes**

This repository demonstrates complete **end-to-end Big Data workflow** including:

- Data Engineering  
- Big Data Processing with PySpark  
- Business Intelligence using Power BI  
- Data Security & Compliance Implementation  

---



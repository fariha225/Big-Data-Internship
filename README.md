# **Big Data Internship – Project Repository**

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : 

*INTERN ID* : 

*DOMAIN* : 

*DURATION*: 

*MENTOR* : 

This repository contains all four major tasks completed during the **CodTech Big Data Internship**, covering the entire lifecycle of a modern Big Data project. The work includes *data cleaning, distributed data processing, business intelligence visualization, and data security implementation*. Each task has been structured, documented, and executed using industry-standard tools such as **PySpark** and **Power BI**, ensuring that the workflow resembles real-world big data engineering and analytics pipelines.

The goal of this internship project is to demonstrate practical knowledge in managing, processing, analyzing, visualizing, and securing large datasets while following best practices and maintaining clean, reproducible code. This repository can serve as a reference for future projects and showcases hands-on skills required in data engineering, big data analytics, and BI development roles.

---

## 📌 **Task Summary**

### ✅ **Task 1: Data Cleaning (PySpark)**  
Task 1 focuses on performing large-scale data cleaning using **Apache Spark**, a distributed processing engine widely used in real-world big data environments.  
Key operations performed:

- Loaded and processed **500K+ retail transaction records** using PySpark  
- Removed duplicate rows and invalid entries  
- Filtered out negative quantities and incorrect prices  
- Dropped rows with missing or null CustomerID  
- Cleaned the product description fields  
- Added derived columns such as **TotalPrice**  
- Exported the cleaned dataset as: **`cleaned_retail.csv`**

This task demonstrates the ability to perform scalable data preprocessing using Spark’s distributed dataframes, which is essential for handling enterprise-level datasets.

---

### ✅ **Task 2: Distributed Processing (PySpark)**  
Task 2 expands upon the cleaned dataset to perform **distributed aggregations and analytical queries**.

Key achievements:

- Implemented **group-by aggregations** across millions of data points  
- Generated business KPIs including:  
  - Total Revenue  
  - Number of Unique Customers  
  - Total Transactions  
  - Average Order Value (AOV)  
- Created analytical datasets such as:  
  - Revenue by Country  
  - Top Products by Revenue and Sales Volume  
  - Top Customers  
  - Revenue per Invoice  
- Computed **Monthly Revenue Trend** using a combination of Spark + Pandas  

All generated CSV files were then used as the primary input for Power BI visualizations in Task 3.

---

### ✅ **Task 3: Data Visualization (Power BI)**  
In this task, a fully designed **Business Intelligence Dashboard** was created using Power BI. The dashboard includes:

- Executive Summary view with four KPI cards  
- Revenue by Country using a world map + bar chart  
- Product Analysis table and visuals  
- Customer Analysis charts  
- Monthly Revenue Trend line graph  

These dashboards transform raw processed data into clear, visual insights that allow stakeholders to interpret performance and trends effectively.  
Final BI report: **`Data Visualization.pbix`**

---

### ✅ **Task 4: Data Security & Compliance**  
This task implements a practical security demonstration focused on data protection and compliance (GDPR/HIPAA).

Security mechanisms implemented:

- **Role-Based Access Control (RBAC)**  
  - Analyst → receives masked CustomerID  
  - Manager → receives full CustomerID  
- **Data Masking** to protect sensitive information  
- **Audit Logging System** that logs every access event and action  

Generated outputs include:

- `demo_masked.csv`
- `demo_manager.csv`
- `task4_audit_log.txt`
- `terminal_output.txt`

These outputs validate the implemented security controls.

---

## ⭐ **Final Notes**

This project demonstrates a complete, end-to-end **Big Data workflow**, including:

- Data Engineering (Cleaning & Preprocessing)  
- Distributed Data Processing with PySpark  
- Business Intelligence Dashboarding  
- Data Security & Compliance Controls  

The repository reflects real-world practices in modern big data systems and provides a strong foundation for advanced data engineering and analytics work.





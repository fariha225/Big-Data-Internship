# ⭐ Task 3 – Data Visualization (Using Microsoft Power BI)

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : Syeda Fariha Fatima 

*INTERN ID* : CT04DR818

*DOMAIN* : Big Data

*DURATION*: 4 weeks

*MENTOR* : Neela Santhosh Kumar

This task focuses on creating an **interactive BI dashboard** using the processed outputs from Task 2.  
The goal was to transform distributed Spark metrics into **business-ready visual insights**.

---

## 🎯 1. Objective of This Task

The objective of Task 3 was to:

- Import the analyzed CSV files from Task 2  
- Build visually appealing dashboards using **Power BI**  
- Create KPIs, charts, maps, and tables  
- Allow interactive filtering using slicers  
- Present clear insights for business decision-making  

This task demonstrates basic **Business Intelligence (BI)** and **Data Visualization** skills.

---

## 📂 2. Dataset Files Used (from Task 2)

The following CSV files generated in Task 2 were used:

| File Name | Purpose |
|-----------|---------|
| summary_total_revenue.csv | KPIs for Executive Summary |
| revenue_by_country.csv | Map + Bar Chart |
| top_10_products.csv | Product performance |
| top_10_customers.csv | Customer analysis |
| transactions_by_invoice.csv | Invoice-level details |
| monthly_revenue.csv | Monthly revenue trend |

All these were imported into Power BI as individual tables.

---

## 💡 3. Power BI Visualizations Created

The dashboard was built across **5 pages**, as described below:

---

## 🟦 Page 1 – Executive Summary (KPIs)

Created **four KPI Cards** using `summary_total_revenue.csv`:

- **Total Revenue**
- **Total Transactions**
- **Unique Customers**
- **Average Order Value**

**Visual Type:** Card  
**Formatting Applied:** Title enabled, bold headings, centered values.

---

## 🟦 Page 2 – Country-wise Sales Overview

This page displays geographic and country-level revenue.

### Visuals Created:

### ✓ 1. Map Visualization  
- Used **Country** (Location)  
- Used **Revenue** (Size)  
- Displays total revenue by country.

### ✓ 2. Bar Chart  
Shows top countries by revenue.

- X-axis → Revenue  
- Y-axis → Country  

### ✓ 3. Country Slicer  
Allows filtering map + bar chart together.

---

## 🟦 Page 3 – Product Performance

This page shows top-selling products.

### Visuals Created:

### ✓ 1. Bar Chart  
- X-axis → Revenue  
- Y-axis → Description  

### ✓ 2. Product Table  
Includes:  
- Description  
- TotalQuantity  
- Revenue  

Formatted with alternating row colors & right-aligned number columns.

---

## 🟦 Page 4 – Customer Analysis

Highlights the highest-value customers.

### Visuals Created:

### ✓ 1. Bar Chart  
- X-axis → Revenue  
- Y-axis → CustomerID  

### ✓ 2. Customer Table  
Columns:  
- CustomerID  
- TotalQuantity  
- Revenue  

Helps identify the most profitable customers.

---

## 🟦 Page 5 – Monthly Revenue Trend

A time-series analysis of monthly revenue.

### ✓ Line Chart  
- X-axis → MonthName (Jan–Dec)  
- Y-axis → Monthly Revenue  

### Transformation Performed in Power BI
A custom **MonthName** column was created using:
```MonthName = FORMAT([InvoiceDate_parsed], "MMM")```

Then sorted using:
```Sort by Column → MonthNumber```

This ensures the correct chronological order.

---

## 📊 4. Final Dashboard Deliverables

The final BI report includes:

✔ 5 interactive pages  
✔ KPIs  
✔ Bar charts  
✔ Tables  
✔ Slicer filters  
✔ Global sales map  
✔ Monthly trend line chart  

These visuals convert the Spark analysis into **clear and actionable insights**.

---

## 🧪 5. How to Open the Dashboard

1. Install **Microsoft Power BI Desktop**  
2. Open the file:  
```Data Visualization.pbix```
3. Ensure all CSV files are present in the same directory (for refresh).

---

## 📘 6. Learning Outcomes

This task provided experience with:

- Importing multiple datasets in Power BI  
- Creating KPI cards  
- Building maps, tables, and charts  
- Applying formatting & design best practices  
- Adding slicers for interactive filtering  
- Designing a complete analytical dashboard  

Task 3 transforms the technical Spark outputs into **business-level insights**.

---

## OUTPUT ## 

<img width="1003" height="573" alt="Image" src="https://github.com/user-attachments/assets/31f24d9e-ea88-4260-92c3-fca05e94b0ca" />

<img width="1014" height="572" alt="Image" src="https://github.com/user-attachments/assets/3f631e4e-9abd-4312-accd-d14665f3ddb1" />

<img width="1020" height="568" alt="Image" src="https://github.com/user-attachments/assets/72a986cb-bd9d-4079-a6f3-edae50841df0" />

<img width="1017" height="570" alt="Image" src="https://github.com/user-attachments/assets/8ecbf1c6-b55e-4fac-ba09-15b9b86fb258" />

<img width="1013" height="570" alt="Image" src="https://github.com/user-attachments/assets/165f977d-147e-48b6-b74a-26ebe16d8af4" />







#Spark analysis: filtering, grouping, aggregations.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, countDistinct, count, round as spark_round
import pandas as pd
import os

# ---------- Setup Spark ----------
spark = SparkSession.builder \
    .appName("RetailTask2_Analysis") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

print("Spark session created for Task 2")

# ---------- Load cleaned CSV ----------
CSV = "cleaned_retail.csv"
if not os.path.exists(CSV):
    raise FileNotFoundError(f"{CSV} not found in working dir: {os.getcwd()}")

df = spark.read.csv(CSV, header=True, inferSchema=True)
print("Loaded cleaned_retail.csv -> rows:", df.count())

# ---------- Quick preview (first 5 rows) ----------
print("\nSample rows:")
df.show(5, truncate=80)

# ============================
# FILTERING examples (useful to demonstrate)
# ============================
# Example: filter sales for United Kingdom only
uk_df = df.filter(col("Country") == "United Kingdom")
print("\nFiltering example: rows for United Kingdom:", uk_df.count())

# Example: filter high-value transactions (> 100)
high_value_df = df.filter(col("TotalPrice") > 100)
print("Filtering example: transactions with TotalPrice > 100:", high_value_df.count())

# ============================
# GROUPING & AGGREGATIONS examples
# ============================

# 1) Revenue by country (groupBy + sum)
rev_by_country = df.groupBy("Country") \
                   .agg(spark_round(spark_sum("TotalPrice"), 2).alias("Revenue")) \
                   .orderBy(col("Revenue").desc())

print("\nTop 5 countries by revenue:")
rev_by_country.show(5, truncate=50)

# Save to CSV for dashboards
rev_by_country.toPandas().to_csv("revenue_by_country.csv", index=False)
print("Saved: revenue_by_country.csv")

# 2) Top 10 products by revenue (groupBy StockCode + Description)
top_products = df.groupBy("StockCode", "Description") \
                 .agg(spark_round(spark_sum("TotalPrice"), 2).alias("Revenue"),
                      spark_sum("Quantity").alias("TotalQuantity")) \
                 .orderBy(col("Revenue").desc()) \
                 .limit(10)

print("\nTop 10 products by revenue:")
top_products.show(truncate=80)

top_products.toPandas().to_csv("top_10_products.csv", index=False)
print("Saved: top_10_products.csv")

# 3) Top 10 customers by revenue
top_customers = df.groupBy("CustomerID") \
                  .agg(spark_round(spark_sum("TotalPrice"),2).alias("Revenue"),
                       spark_sum("Quantity").alias("TotalQuantity")) \
                  .orderBy(col("Revenue").desc()) \
                  .limit(10)

print("\nTop 10 customers by revenue:")
top_customers.show(truncate=50)

top_customers.toPandas().to_csv("top_10_customers.csv", index=False)
print("Saved: top_10_customers.csv")

# 4) KPI summary: TotalRevenue, TotalTransactions, UniqueCustomers, AvgOrderValue
total_revenue = df.select(spark_sum("TotalPrice").alias("TotalRevenue")).collect()[0]["TotalRevenue"]
total_transactions = df.select(countDistinct("InvoiceNo").alias("Transactions")).collect()[0]["Transactions"]
unique_customers = df.select(countDistinct("CustomerID").alias("UniqueCustomers")).collect()[0]["UniqueCustomers"]
avg_order_value = total_revenue / total_transactions if total_transactions else 0.0

import pandas as pd
kpi_df = pd.DataFrame([{
    "TotalRevenue": round(total_revenue,2),
    "TotalTransactions": int(total_transactions),
    "UniqueCustomers": int(unique_customers),
    "AvgOrderValue": round(avg_order_value,2)
}])
kpi_df.to_csv("summary_total_revenue.csv", index=False)
print("\nSaved: summary_total_revenue.csv")
print(kpi_df.to_string(index=False))

# 5) Transactions by invoice (useful distribution)
tx_by_invoice = df.groupBy("InvoiceNo") \
                  .agg(spark_round(spark_sum("TotalPrice"),2).alias("InvoiceRevenue"),
                       spark_sum("Quantity").alias("InvoiceQuantity"))
tx_by_invoice.orderBy(col("InvoiceRevenue").desc()).limit(10).show()
tx_by_invoice.toPandas().to_csv("transactions_by_invoice.csv", index=False)
print("Saved: transactions_by_invoice.csv")

# 6) Monthly revenue - use pandas for robust date parsing (mixed formats possible)
print("\nPreparing monthly revenue (pandas handling dates) ...")
pdf = pd.read_csv(CSV)
pdf['InvoiceDate_parsed'] = pd.to_datetime(pdf['InvoiceDate'], infer_datetime_format=True, errors='coerce')
# fallback parse trial if many nulls
if pdf['InvoiceDate_parsed'].isna().sum() > 0:
    pdf['InvoiceDate_parsed'] = pd.to_datetime(pdf['InvoiceDate'], dayfirst=False, errors='coerce', infer_datetime_format=True)
pdf['YearMonth'] = pdf['InvoiceDate_parsed'].dt.to_period('M').astype(str)
monthly = pdf.groupby('YearMonth', as_index=False).agg({'TotalPrice':'sum','InvoiceNo':'nunique'})
monthly = monthly.rename(columns={'TotalPrice':'Revenue', 'InvoiceNo':'UniqueInvoices'})
monthly['Revenue'] = monthly['Revenue'].round(2)
monthly = monthly.sort_values('YearMonth')
monthly.to_csv("monthly_revenue.csv", index=False)
print("Saved: monthly_revenue.csv")

# ---------- finish ----------
spark.stop()
print("\nTask 2 complete. Summary CSVs saved. Use them in Power BI / Tableau.")

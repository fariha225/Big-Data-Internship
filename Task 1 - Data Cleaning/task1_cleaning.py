from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower, to_timestamp

# ------------------------
# 1. Create Spark Session
# ------------------------
spark = SparkSession.builder \
    .appName("RetailCleaning") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

print("Spark session created!")

# ------------------------
# 2. Load the dataset
# ------------------------
df = spark.read.csv("OnlineRetail.csv", header=True, inferSchema=True)

# Show dataset size (intern-friendly)
print("\n==== RAW DATA INFO ====")
print("Number of rows (raw):", df.count())
print("Number of columns:", len(df.columns))
print("Columns:", df.columns)
df.printSchema()

# ------------------------
# 3. Show basic problems before cleaning
# ------------------------
print("\n==== DATA QUALITY CHECKS BEFORE CLEANING ====")
print("Missing CustomerID:", df.filter(df.CustomerID.isNull()).count())
print("Negative or zero Quantity:", df.filter(df.Quantity <= 0).count())
print("Negative or zero UnitPrice:", df.filter(df.UnitPrice <= 0).count())
print("Cancellation invoices (InvoiceNo starting with 'C'):", 
      df.filter(col("InvoiceNo").startswith("C")).count())

# ------------------------
# 4. Remove cancellations
# ------------------------
df = df.filter(~col("InvoiceNo").startswith("C"))

# ------------------------
# 5. Drop duplicates
# ------------------------
df = df.dropDuplicates()

# ------------------------
# 6. Handle missing CustomerID
# ------------------------
df = df.dropna(subset=["CustomerID"])

# ------------------------
# 7. Remove invalid Quantity & UnitPrice
# ------------------------
df = df.filter(col("Quantity") > 0)
df = df.filter(col("UnitPrice") > 0)

# ------------------------
# 8. Clean Description column
# ------------------------
df = df.withColumn("Description", trim(lower(col("Description"))))


# ------------------------
# 9. Add TotalPrice
# ------------------------
df = df.withColumn("TotalPrice", col("Quantity") * col("UnitPrice"))

# ------------------------
# 10. Final dataset summary
# ------------------------
print("\n==== CLEANED DATA INFO ====")
print("Number of rows (cleaned):", df.count())
print("Number of columns:", len(df.columns))
df.printSchema()

# ------------------------
# 11. Save cleaned data
# ------------------------
print("Converting Spark DF to Pandas DF...")
pdf = df.toPandas()

print("DATAFRAME CONVERTED TO PANDAS, ROWS:", len(pdf))
print("CURRENT WORKING DIRECTORY:", __import__("os").getcwd())
print("FILES IN DIR BEFORE SAVING:", __import__("os").listdir())

print("Saving cleaned CSV using pandas...")
pdf.to_csv("cleaned_retail.csv", index=False)

print("FILES IN DIR AFTER SAVING:", __import__("os").listdir())
print("Done! Saved cleaned_retail.csv")



spark.stop()

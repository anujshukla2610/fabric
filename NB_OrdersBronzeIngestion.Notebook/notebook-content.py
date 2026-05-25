# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "88414f66-4801-4d95-ab29-2f77013cb0e9",
# META       "default_lakehouse_name": "FabricTraining_LH",
# META       "default_lakehouse_workspace_id": "dc024af1-86c0-4c27-a198-8311368df95f",
# META       "known_lakehouses": [
# META         {
# META           "id": "88414f66-4801-4d95-ab29-2f77013cb0e9"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/raw/orders.csv")

from pyspark.sql.functions import col, to_date

df = df.withColumn(
    "order_date",
    to_date(col("order_date"), "yyyy-MM-dd")
)

from pyspark.sql.functions import date_format

df = df.withColumn(
    "year_month",
    date_format(col("order_date"), "yyyy-MM")
)

df.printSchema()

df.write.mode("overwrite").format("delta").saveAsTable("orders_bronze")

display(df.limit(10))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE DETAIL orders_bronze

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC OPTIMIZE orders_bronze
# MAGIC ZORDER BY (order_date)

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC VACUUM orders_bronze RETAIN 168 HOURS

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY orders_bronze

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC ANALYZE TABLE orders_bronze COMPUTE STATISTICS

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

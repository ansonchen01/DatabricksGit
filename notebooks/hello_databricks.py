# Databricks Notebook: Hello World
print("Hello from GitHub → Databricks!")

# Test Spark (Databricks built-in)
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("HelloSpark").getOrCreate()
df = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])
df.show()

from pyspark.sql.types import StructType,StructField, StringType

customSchema = StructType().add("col1", StringType(), True).add("col2", StringType(), True).add("col3", StringType(), True)

df = spark.read.format("csv").option("header", "true").schema(customSchema).load("path_to_files")
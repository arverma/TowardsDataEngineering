# PySpark

### Create Dataframe
```
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["letter","number"]
data = [(l, n) for l, n in zip("abcdefghijklmnopqrstuvwxyz", "12345678912345678912345678")]
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(columns)
```

### Get number of partitions
```
if dataframe:
  df.rdd.getNumPartitions()
if RDD
  rdd.getNumPartitions()
```

### Repartition dataframe into "n" partitions
* Partitions has unequal distribution of data(Fast since less suffeling, cann't increase number of partitions) = `df.coalesce(n)`
* Partitoins has euqal distribution of data(Slow since more suffeling) = `df.repartition(n)`

### Drop Columns from Spark DataFrame

`df = df.drop("query_type").drop("_c0").drop("_c01")`

### Write data to S3

`df.write.mode("overwrite").format("csv").option("compression", ".gzip").save(output_s3_path_in_string, header=True)`

### Validation Steps
```python
>>> df_new = spark.read.csv("s3://leadid-sandbox/aranjan/mysql_leads_new")

>>> df_old = spark.read.option("delimiter", "\x01").csv("s3://..")

>>> df_new.count()

>>> df_intersect = df_old.intersect(df_new)

>>> df_subtract = df_old.subtract(df_intersect)

>>> df_new.filter(df_new._c0 == "").filter(df_new._c1 == "").head()
```

### Select records with specific string in columns

`df.filter(lower(col("_c0")).contains('%string_to_find%')).head()`

### Get max/min/mean value for a column

`max_value = df.agg({"_c0": “max”}).collect()[0]`

### Spark Configuration
In a cluster with 10 nodes with each node(16 cores and 64GB RAM)
* Assign 5 core per executors => --executor-cores = 5 (for good HDFS throughput)
* Leave 1 core per node for Hadoop/Yarn daemons => Num cores available per node = 16-1 = 15
  So, Total available of cores in cluster = 15 x 10 = 150
* Number of available executors = (total cores/num-cores-per-executor) = 150/5 = 30
* Leaving 1 executor for ApplicationManager => --num-executors = 29
* Number of executors per node = 30/10 = 3
* Memory per executor = 64GB/3 = 21GB
* Counting off heap overhead = 7% of 21GB = 3GB. So, actual --executor-memory = 21 - 3 = 18GB

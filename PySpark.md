# PySpark

### Create Dataframe
```
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["letter","number"]
data = [(l, n) for l, n in zip("abcdefghijklmnopqrstuvwxyz", "12345678912345678912345678")]
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(columns)
```

### Run SQL Query on Spark DF
```
df.createOrReplaceTempView("table_name")
df_new = spark.sql("Select * from table_name")
df_new.show()
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
* Partitoins has equal distribution of data(Slow since more suffeling) = `df.repartition(n)`

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

### Setup Colab to run PySpark
1. As a first step, Let's setup Spark on your Colab environment. Run the cell below!
```[Python]
  !pip install pyspark
  !pip install -U -q PyDrive
  !apt install openjdk-8-jdk-headless -qq
  import os
  os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
```
2. Import some of the libraries usually needed by our workload.
```[Python]
  import pyspark
  from pyspark.sql import *
  from pyspark.sql.types import *
  from pyspark.sql.functions import *
  from pyspark import SparkContext, SparkConf
```
3. Initialize the Spark context, 
```[Python]
  # Create the session
  conf = SparkConf().set("spark.ui.port", "4050")

  # Create the context
  sc = pyspark.SparkContext(conf=conf)
  spark = SparkSession.builder.getOrCreate()

  spark
```
4. If you are running this Colab on the Google hosted runtime, the cell below will create a ngrok tunnel which will allow you to still check the Spark UI.
```[Python]
  !wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
  ! rm -rf ngrok
  !unzip ngrok-stable-linux-amd64.zip
  get_ipython().system_raw('./ngrok http 4050 &')
  !curl -s http://localhost:4040/api/tunnels | python3 -c \
      "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
```
5. Test Spark installation
```[Python]
  import pyspark
  print(pyspark.__version__)
  spark = SparkSession.builder.master("local[*]").getOrCreate()
  # Test the spark 
  df = spark.createDataFrame([{"hello": "world"} for x in range(1000)])

  df.show(3, False)
```

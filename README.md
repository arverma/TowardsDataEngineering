### Rename files in S3

`for f in $(aws s3api list-objects --bucket bucket_name --prefix "key/" --delimiter "/" | grep 097 | cut -d : -f 2 | cut -d \" -f 2);  do aws s3 mv s3://bucket_name/$f s3://bucket_name/${f/%/.csv.gz}; done `

### Sync files at two S3 locations

`aws s3 sync s3_source s3_target --recursive`

### Drop Columns from Spark DataFrame

`df = df.drop("query_type").drop("_c0").drop("_c01")`

### Write data to S3

`df.write.mode("overwrite").format("csv").option("compression", ".gzip").save(output_s3_path_in_string, header=True)`

### Validation Steps
`df_new = spark.read.csv("s3://leadid-sandbox/aranjan/mysql_leads_new")`

`df_old = spark.read.option("delimiter", "\x01").csv("s3://..")`

`df_new.count()`

`df_intersect = df_old.intersect(df_new)`

`df_subtract = df_old.subtract(df_intersect)`

`df_new.filter(df_new._c0 == "").filter(df_new._c1 == "").head()`

### Select records with specific string in columns

`df.filter(lower(col("_c0")).contains('%string_to_find%')).head()`

### Run a job in background on Linux

`nohup command > my.log 2>&1 &`

### Get max/min/mean value for a column

`max_value = df.agg({"_c0": “max”}).collect()[0]`

### Connect to EMR Cluster from CLI

`ssh -i jornaya.pem hadoop@ip.ip.ip.ip`

### Screen

* Create a new screen: `screen -S aranjan`
* Go into specific screen: `screen -rd aranjan`
* Nested screen: `screen -t aman`

### Secure copy a file from local to hadoop

`scp -i jornaya.pem file_path hadoop@ip.ip.ip.ip:/home/hadoop/`

### extract .gz file

`gunzip *`

### Download bucket object from s3
`aws s3 cp s3://.. . --recursive`

### Add extension to file
`for f in *; do mv "$f" "$f.gz"; done`

### Find a file in Linux
`$ sudo find . -name <file_name>`

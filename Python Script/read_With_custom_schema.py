# from pyspark.sql.types import StructType,StructField, StringType
#
# customSchema = StructType().add("account_id", StringType(), True).add("tag", StringType(), True).add("hashed_mobile_no", StringType(), True)
#
# df = spark.read.format("csv").option("header", "true").schema(customSchema).load("/dre/axis/202111/outputfile.csv")
#
# df_join = df.join(df_p,["hashed_mobile_no"],"inner")
#
# >>> df.drop_duplicates(subset=["hashed_mobile_no"])
# DataFrame[tag: string, hashed_mobile_no: string]
# >>>
# >>> df_join = df.join(df_p,["hashed_mobile_no"],"inner")
# >>> df.count()
# 22295582
# >>> df_join.count()
# 23856457
# >>> df_p.select("hashed_mobile_no").distinct().count()
# 402747727
# >>> df_p.count()
# 453680898
# >>> df_p.drop_duplicates(subset=["hashed_mobile_no"])
# DataFrame[account_id: string, hashed_mobile_no: string]
# >>> df_join = df.join(df_p,["hashed_mobile_no"],"inner")
# >>> df_join.count()
#
# df_join.write.save('hdfs:///tmp/aman.rv/vidya', format='csv', header=True)
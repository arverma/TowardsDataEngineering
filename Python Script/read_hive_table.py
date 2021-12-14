from pyspark.sql import HiveContext
hive_context = HiveContext(sc)
df2=hive_context.table("database_name.table_name1")
df2=df2.drop(*["list_of_columns"])
df3=hive_context.table("database_name.table_name2")
df3=df3.drop(*["list_of_columns"])
df=df2.join(df3,None,"outer")
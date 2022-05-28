from pyspark.sql import SparkSession
from pyspark.sql import functions as F

if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()
    data = [('James', 'Smith', 'M', 30),
            ('Anna', 'Rose', 'F', 41),
            ('Robert', 'Williams', 'O', 62),
            ]

    columns = ["firstname", "lastname", "gender", "salary"]
    df = spark.createDataFrame(data=data, schema=columns)
    df = df.withColumn("Sex", F.when(df.gender == "M", "Male").when(df.gender == "F", "Female").otherwise(None))
    df.show()

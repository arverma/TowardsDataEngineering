"""
spark-submit --master local --py-files foo.zip main.py
"""

from pyspark.sql import functions as F
from foo.foo import Foo


def do_transform(df):
    df.groupBy("department").sum("salary").show(truncate=False)

    df.groupBy("department").count().show(truncate=False)

    df.groupBy("department", "state") \
        .sum("salary", "bonus") \
        .show(truncate=False)

    df.groupBy("department") \
        .agg(F.sum("salary").alias("sum_salary"),
             F.avg("salary").alias("avg_salary"),
             F.sum("bonus").alias("sum_bonus"),
             F.max("bonus").alias("max_bonus")
             ) \
        .show(truncate=False)

    df.groupBy("department") \
        .agg(F.sum("salary").alias("sum_salary"),
             F.avg("salary").alias("avg_salary"),
             F.sum("bonus").alias("sum_bonus"),
             F.max("bonus").alias("max_bonus")).\
        where(F.col("sum_bonus") >= 50000) \
        .show(truncate=False)


if __name__ == '__main__':
    foo = Foo("PySparkPackagingTest")
    df = foo.get_source_df()
    do_transform(df)

count = 0
for i in range(162):
    file = "0"*(5-len(str(i)))+str(i)
    print("path/*/part-{}".format(file))
    rdd = spark.sparkContext.textFile("path/part-{}".format(file))
    temp = rdd.count()
    print(temp)
    count += temp
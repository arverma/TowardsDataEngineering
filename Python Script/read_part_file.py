count = 0
for i in range(162):
    file = "0"*(5-len(str(i)))+str(i)
    print("/tmp/fdp_payload/Oct2021CBCScores/*/part-{}".format(file))
    rdd = spark.sparkContext.textFile("/tmp/fdp_payload/Oct2021CBCScores/*/part-{}".format(file))
    temp = rdd.count()
    print(temp)
    count += temp
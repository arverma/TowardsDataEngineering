from pyspark.sql.functions import lit, udf
from cryptography.fernet import Fernet
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession, Row


def encrypt_val(clear_text, MASTER_KEY):
    f = Fernet(MASTER_KEY)
    clear_text_b = bytes(clear_text, 'utf-8')
    cipher_text = f.encrypt(clear_text_b)
    cipher_text = str(cipher_text.decode('ascii'))
    return cipher_text


def decrypt_val(cipher_text, MASTER_KEY):
    f = Fernet(MASTER_KEY)
    clear_val = f.decrypt(cipher_text.encode()).decode()
    return clear_val


if __name__ == '__main__':
    spark = SparkSession.builder.appName("Test Job").getOrCreate()

    #     df = spark.read.csv("sample_file.csv", header=True)
    # create a list of rows with the data
    data = [
        Row("John Doe", "IT", "201901", 50000),
        Row("Jane Doe", "HR", "202001", 60000),
        Row("Bob Smith", "IT", "201905", 70000),
        Row("Alice Smith", "HR", "202011", 80000),
        Row("James Johnson", "IT", "202002", 90000),
        Row("Emily Johnson", "HR", "201310", 100000),
        Row("David Williams", "IT", "201511", 110000),
        Row("Samantha Williams", "HR", "202207", 120000),
        Row("Charles Brown", "IT", "202101", 130000),
        Row("Ashley Brown", "HR", "202111", 140000)
    ]

    # create the DataFrame
    df = spark.createDataFrame(data, schema)

    encrypt = udf(encrypt_val, StringType())
    decrypt = udf(decrypt_val, StringType())

    encryptionKey = Fernet.generate_key()

    df = df.withColumn("first_name_encrypted", encrypt(df.employee_name, lit(encryptionKey)))
    df = df.withColumn("first_name_decrypted", decrypt(df.employee_name, lit(encryptionKey)))

    df.show()
#     df.coalesce(1).write.mode("overwrite").csv("output", header=True)

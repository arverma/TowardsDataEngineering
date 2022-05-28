from pyspark.sql.functions import lit, udf
from cryptography.fernet import Fernet
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession


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

    df = spark.read.csv("sample_file.csv", header=True)

    encrypt = udf(encrypt_val, StringType())
    decrypt = udf(decrypt_val, StringType())

    encryptionKey = Fernet.generate_key()

    df = df.withColumn("first_name_encrypted", encrypt(df.first_name, lit(encryptionKey)))
    df = df.withColumn("first_name_decrypted", decrypt(df.first_name_encrypted, lit(encryptionKey)))
    df.coalesce(1).write.mode("overwrite").csv("output", header=True)

# preprocessing.py
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataPreprocessing") \
    .getOrCreate()

kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9093") \
    .option("subscribe", "transactions-topic") \
    .load()

processed_df = kafka_df \
    .selectExpr("CAST(value AS STRING)") \
    .select("value")

processed_df \
    .writeStream \
    .format("console") \
    .start() \
    .awaitTermination()

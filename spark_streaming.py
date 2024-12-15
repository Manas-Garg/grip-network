from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("RealTimeClimateAnalytics") \
    .getOrCreate()

# Define Schema for Incoming Data
schema = StructType([
    StructField("timestamp", TimestampType(), True),
    StructField("metric", StringType(), True),
    StructField("value", FloatType(), True)
])

# Read Data from Kafka
climate_data = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "climate_data") \
    .load()

# Process the Data
parsed_data = climate_data.selectExpr("CAST(value AS STRING)")
parsed_data = parsed_data.withColumn("value", from_json(col("value"), schema))

# Analytics: Calculate Average Value per Metric
aggregated_data = parsed_data.groupBy("metric") \
    .agg({"value": "avg"})

# Write to Console in Real-Time
query = aggregated_data.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

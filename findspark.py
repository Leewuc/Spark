import findspark
findspark.init("/home/ubuntu/app/spark/spark-3.5.1-bin-hadoop3")
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
df = spark.read.parquet("/home/ubuntu/work/spark01/data/iris.parquet")
df.show(3)

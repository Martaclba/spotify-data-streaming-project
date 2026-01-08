from pyspark.sql import SparkSession
from pathlib import Path
from pyspark.sql.window import Window
import pyspark.sql.functions as F
from pyspark.sql.functions import desc, count, col, sum as Fsum, when
import json, pprint
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType, BooleanType, LongType
from requests.exceptions import ReadTimeout, ConnectionError
import pprint
import time
import math
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import sys


# spark = SparkSession.builder.appName("SpotifyStreamingHistory").getOrCreate()
# print(spark)


# # Lista todos os volumes dentro do schema 'default' do catálogo 'workspace'
# display(spark.sql("SHOW VOLUMES IN workspace.default"))


# folder_path = "/Volumes/workspace/default/spotify-data/streaming_history/raw/streaming_history/*Audio*.json"
# df_streamingHistory = spark.read.option("multiline", "true").json(folder_path)
# print("Total values across all files: ", df_streamingHistory.count())
# display(df_streamingHistory.limit(10))


# df_streamingHistory.printSchema()


# windowSpec = Window.partitionBy("ts").orderBy("spotify_track_uri")
# df_with_duplicatesNum = df_streamingHistory.withColumn("ts_count", count("*").over(windowSpec))
# # este dataframe é apenas para visualizar e analisar os valores duplicados
# df_with_duplicates = df_with_duplicatesNum.filter(col("ts_count") > 1)
# duplicates_num = df_with_duplicates.count()
# df_with_duplicates.orderBy("ts_count", "ts").show(truncate=False)


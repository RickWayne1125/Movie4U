import os
from pyspark.sql.functions import lit, col
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RecommendationEngine:
    """A movie recommendation engine
    """

    def recommend(self, movieList):
        tableSimilarities = self.spark.read.format("mongo").load()
        tableMovies = self.spark.read.format("mongo").option("uri", "mongodb://127.0.0.1/MovieLens.movies").load()
        result = tableMovies.drop("_id", "genres", "title")
        result = result.withColumn("interest", lit(0))
        for movieId in movieList:
            print("start %d" % movieId)
            tableSimilaritiesFiltered = tableSimilarities.filter(tableSimilarities.movieId_1 == movieId)
            tmp = result 
            # tmp.show()
            tableSimilaritiesFiltered = tableSimilaritiesFiltered.drop("_id")
            # tableSimilaritiesFiltered.show()
            tmp = tmp.join(tableSimilaritiesFiltered, tableSimilaritiesFiltered.movieId_2 == tmp.movieId, "left_outer").fillna(0)
            tmp.show()
            tmp = tmp.drop("movieId_1", "_id", "title", "genres", "movieId_2")
            tmp = tmp.withColumnRenamed("value", "y")
            result = result.withColumnRenamed("interest", "x")
            # tmp.show()
            result = result.join(tmp, result.movieId == tmp.movieId, "left_outer").select(result.movieId, result.x, tmp.y).fillna(0)
            result = result.withColumn("interest", col("x") + col("y")).drop("x", "y", "value")
            result = result.dropDuplicates()
            result.show()

        result = result.orderBy(result.interest.desc())
        top10 = [int(row.movieId) for row in result.limit(10).select("movieId").collect()]
        return top10

    
    def __init__(self, spark):
        """Init the recommendation engine given a Spark session and a dataset path
        """

        logger.info("Starting up the Recommendation Engine: ")

        self.spark = spark

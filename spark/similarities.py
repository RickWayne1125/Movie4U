import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RecommendationEngine:
    """A movie recommendation engine
    """

    def recommend(thisUserId):
        logger.info("Loading Rating and Similarity data: ")

        tableSimilarities = spark.read.format("mongo").load()
        tableRatings = spark.read.format("mongo").option("uri", "mongodb://127.0.0.1/MovieLens.ratings").load()
        userRatings = tableRatings.filter(tableRatings.userId == thisUserId)
        userRatingsJoined = userRatings.join(tableSimilarities, tableSimilarities["movieId_1"] == userRatings["movieId"])
        userRatingsInterests = userRatingsJoined.withColumn("interests", (userRatings.movieId-3)*userRatingsJoined.value)
        results = userRatingsInterests.orderBy(userRatingsInterests.interests.desc())
        # results.write.format("mongo").mode("append").option("database", "MovieLens").option("collection", "interests").save()
        top10 = [int(row.movieId) for row in results.limit(10).select("movieId").collect()]
        return top10

    
    def __init__(self, spark):
        """Init the recommendation engine given a Spark session and a dataset path
        """

        logger.info("Starting up the Recommendation Engine: ")

        self.spark = spark

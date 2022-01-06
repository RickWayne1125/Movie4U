import os
from pyspark.mllib.recommendation import ALS
from pyspark.sql.DataFrame import columns

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ALS

def get_counts_and_averages(ID_and_ratings_tuple):
    """Given a tuple (movieID, ratings_iterable) 
    returns (movieID, (ratings_count, ratings_avg))
    """
    nratings = len(ID_and_ratings_tuple[1])
    return ID_and_ratings_tuple[0], (nratings, float(sum(x for x in ID_and_ratings_tuple[1]))/nratings)


class RecommendationEngine:
    """A movie recommendation engine
    """

    def __count_and_average_ratings(self):
        """Updates the movies ratings counts from 
        the current data self.ratings_RDD
        """
        logger.info("Counting movie ratings...")
        self.ratingsCount = self.ratingsDF.count()
        self.moviesCount = self.moviesDF.count()
        print('There are {0} ratings and {1} movies in the datasets.'.format(self.ratingsCount, self.moviesCount))


    def __train_model(self):
        """Train the ALS model with the current dataset
        """
        logger.info("Training the ALS model...")
        self.spark.conf.set("spark.sql.shuffle.partitions", "16")
        als = (ALS()
            .setUserCol("userId")
            .setItemCol("movieId")
            .setRatingCol("rating")
            .setPredictionCol("predictions")
            .setMaxIter(2)
            .setSeed(self.seed)
            .setRegParam(0.1)
            .setColdStartStrategy("drop")
            .setRank(12))
        self.alsModel = als.fit(self.trainingDF)
        logger.info("ALS model built!")


    def __predict_ratings(self, user_and_movieDF):
        """Gets predictions for a given (userID, movieID) formatted RDD
        Returns: an RDD with format (movieTitle, movieRating, numRatings)
        """
        predictedDF = self.model.predictAll(user_and_movieDF)
        predicted_ratingDF = predicted_RDD.map(lambda x: (x.product, x.rating))
        
        return predicted_rating_title_and_count_RDD
    
    def add_ratings(self, ratings):
        """Add additional movie ratings in the format (user_id, movie_id, rating)
        """
        # Convert ratings to an dataframe
        new_ratings = self.spark.createDataFrame(ratings, columns)
        # Add new ratings to the existing ones
        self.ratingsDF = self.ratingsDF.union(new_ratings)
        # Re-compute movie ratings count
        self.__count_and_average_ratings()
        # Re-train the ALS model with the new ratings
        self.__train_model()
        
        return ratings

    def get_ratings_for_movie_ids(self, user_id, movie_ids):
        """Given a user_id and a list of movie_ids, predict ratings for them 
        """
        requested_movies_RDD = self.sc.parallelize(movie_ids).map(lambda x: (user_id, x))
        # Get predicted ratings
        ratings = self.__predict_ratings(requested_movies_RDD).collect()

        return ratings
    
    def get_top_ratings(self, user_id, movies_count):
        """Recommends up to movies_count top unrated movies to user_id
        """
        # Get pairs of (userID, movieID) for user_id unrated movies
        user_unrated_movies_RDD = self.ratings_RDD.filter(lambda rating: not rating[0] == user_id)\
                                                 .map(lambda x: (user_id, x[1])).distinct()
        # Get predicted ratings
        ratings = self.__predict_ratings(user_unrated_movies_RDD).filter(lambda r: r[2]>=25).takeOrdered(movies_count, key=lambda x: -x[1])

        return ratings

    def __init__(self, spark, dataset_path):
        """Init the recommendation engine given a Spark context and a dataset path
        """

        logger.info("Starting up the Recommendation Engine: ")

        self.spark = spark

        # Load ratings data for later use
        logger.info("Loading Ratings data...")
        ratings_df_schema = "userId integer, movieId integer, rating float"
        self.ratingsDF = spark.read.csv("../datasets/ml-latest/ratings.csv", header=True, schema=ratings_df_schema).cache()
        # Load movies data for later use
        logger.info("Loading Movies data...")
        movies_df_schema = "ID integer, title string"
        self.moviesDF = spark.read.csv("../datasets/ml-latest/movies.csv", header=True, schema=movies_df_schema)
        # Pre-calculate movies ratings counts
        self.__count_and_average_ratings()

        # Train the model
        self.rank = 12
        self.seed = 42
        self.iterations = 2
        self.regularization_parameter = 0.1
        (self.trainingDF, self.testDF) = self.ratingsDF.randomSplit([0.8, 0.2], seed=self.seed)
        print('Training: {0}, test: {1}'.format(self.trainingDF.count(), self.testDF.count()))
        self.__train_model() 

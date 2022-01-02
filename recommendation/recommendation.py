import pymongo

# 输入为当前用户userId
# 返回为该用户推荐的10个电影的movieId
def recommendationForUser(thisUserId):
    myClient = pymongo.MongoClient("mongodb://mongodb.chufanchen.com:27017/")
    myDb = myClient["MovieLens"]
    tableRatings = myDb["ratings"]
    tableSimilarities = myDb["similarities"]
    userRatings = dict()
    for recordRating in tableRatings.find({'userId': thisUserId}):
        userRatings[recordRating['movieId']] = recordRating['rating']
    interests = dict()
    for userMovieId in userRatings.keys():
        for recordSimilarity in tableSimilarities.find({'movieId_1': userMovieId}):
            movieId_2 = recordSimilarity['movieId_2']
            interests.setdefault(movieId_2, 0)
            interests[movieId_2] += (userRatings[userMovieId]-3) * recordSimilarity['value']

    recommendationResult = []
    for i in range(10):
        thisMovieId = max(interests, key=interests.get)
        recommendationResult.append(thisMovieId)
        del interests[thisMovieId]

    return recommendationResult







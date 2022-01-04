import pymongo

# 输入为当前用户userId
# 返回为该用户推荐的10个电影的movieId
def recommendationForUser(thisUserId):
    myClient = pymongo.MongoClient("MongoDB_uri")
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


# 输入为用户选择的感兴趣电影的movieId列表
# 返回为该用户推荐的10个电影的movieId
def recommendationForUser_2(moviesList):
    myClient = pymongo.MongoClient("MongoDB_uri")
    myDb = myClient["MovieLens"]
    tableSimilarities = myDb["similarities"]
    interests = dict()

    for movieID in moviesList:
        for recordSimilarity in tableSimilarities.find({'movieId_1': movieID}):
            movieId_2 = recordSimilarity['movieId_2']
            interests.setdefault(movieId_2, 0)
            interests[movieId_2] += recordSimilarity['value']

    recommendationResult = []
    for i in range(10):
        thisMovieId = max(interests, key=interests.get)
        recommendationResult.append(thisMovieId)
        del interests[thisMovieId]

    return recommendationResult






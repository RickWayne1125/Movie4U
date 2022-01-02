import math

# 输入为ratings表信息
# 生成所有电影之间的相似度（相似度信息已存入数据库）
def BuildSimilarity(ratings):
    alone = dict()
    dual = dict()
    for userId, rating in ratings.items():
        for movieId, score in rating.items():
            alone.setdefault(movieId, 0)
            alone[movieId] += 1
            dual.setdefault(movieId, {})
            for otherMovieId in rating.keys():
                if otherMovieId == movieId:
                    continue
                dual[movieId].setdefault(otherMovieId, 0)
                dual[movieId][otherMovieId] += 1
    f = open("similarities.txt", "w")
    for firstMovieId, secondMovies in dual.items():
        for secondMovieId, dualCount in secondMovies.items():
            similarityValue = dualCount / (math.sqrt(alone[firstMovieId] * alone[secondMovieId]))
            f.write("{} {} {}\n".format(firstMovieId, secondMovieId, similarityValue))
    f.close()

import pymongo

db_uri = "localhost"
movie_info_db_name = "test"  # 本地:test，远程:MovieLens
movie_info_col_name = "movies"
tag_movie_array_col_name = "tagId-movieIdArray"
client = pymongo.MongoClient(db_uri)
root_db = client[movie_info_db_name]


# 根据movieId返回title
def get_movie_info(movie_id):
    movie_col = root_db[movie_info_col_name]
    try:
        movie_info = movie_col.find_one({"movieId": movie_id})
        return movie_info['title']
    except:
        print("error")


# 根据tag_id返回高分电影title集合, count为需求电影id数量
def get_movie_array_on_tag(tag_id, count):
    tag2movie_col = root_db[tag_movie_array_col_name]
    try:
        tag_info = tag2movie_col.find_one({"_id": tag_id})
        movie_id_array = tag_info['movieIdArray']
        movie_title_array = []
        for movie_id in movie_id_array:
            movie_title_array.append(get_movie_info(movie_id))
        return movie_title_array
    except:
        print("error")


if __name__ == '__main__':
    t1 = get_movie_info(1)
    t2 = get_movie_array_on_tag(5)
    print(t1)
    print(t2)

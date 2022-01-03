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
def get_movie_array_on_tag(tag_id, count=2):
    tag2movie_col = root_db[tag_movie_array_col_name]
    try:
        tag_info = tag2movie_col.find_one({"_id": tag_id})
        if tag_info is None:  # 查到空tag
            return [], 0
        movie_id_array = tag_info['movieIdArray']
        return movie_id_array[0:count], min(count, len(movie_id_array))
    except:
        print("error")


if __name__ == '__main__':
    tag_zero_array = get_movie_array_on_tag(tag_id=2, count=2)
    tag_one_array = get_movie_array_on_tag(tag_id=6, count=2)
    tag_multi_array = get_movie_array_on_tag(tag_id=3, count=2)
    print(tag_zero_array)
    print(tag_one_array)
    print(tag_multi_array)

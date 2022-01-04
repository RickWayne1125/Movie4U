from random import randrange
import pymongo

tag_num_max = 1126
db_uri = "mongodb://mongodb.chufanchen.com:27017"
movie_info_db_name = "MovieLens"  # 本地:test，远程:MovieLens
movie_info_col_name = "movies"
tag_info_col_name = "genome-tags"
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


# 根据tagId返回tag名称
def get_tag_info(tag_id):
    tag_col = root_db[tag_info_col_name]
    try:
        tag_info = tag_col.find_one({"tagId": tag_id})
        return tag_info['tag']
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


# 从tag对应电影集合初始取8个movie，每个tag最多对应两个
def get_check_list():
    check_list = []
    max_len = 8
    movie_cnt = 2
    tag_id = randrange(tag_num_max)
    while len(check_list) != max_len:
        tag_name = get_tag_info(tag_id)
        tmp_array, tmp_cnt = get_movie_array_on_tag(tag_id, movie_cnt)
        for m_id in tmp_array:
            m_name = get_movie_info(m_id)
            list_item = dict()
            list_item.update({'id': m_id})
            list_item.update({'name': m_name})
            list_item.update({'tag': tag_name})
            check_list.append(list_item)
        movie_cnt = min(max_len - len(check_list), 2)
        tag_id = (tag_id + 1) % tag_num_max
    return check_list


if __name__ == '__main__':
    # movie信息获取 测试
    print(get_movie_info(1))
    # tag信息获取 测试
    print(get_tag_info(760))

    # 取tag对应movieId 测试
    tag_zero_array = get_movie_array_on_tag(tag_id=2, count=2)
    tag_one_array = get_movie_array_on_tag(tag_id=6, count=2)
    tag_multi_array = get_movie_array_on_tag(tag_id=3, count=2)
    print(tag_zero_array)
    print(tag_one_array)
    print(tag_multi_array)

    # get_check_list 测试
    for item in get_check_list():
        print(item)

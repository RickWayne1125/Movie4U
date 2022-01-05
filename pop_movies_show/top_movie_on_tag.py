import time
import pprint
import pymongo

from config import database

tag_num_max = 1126
movie_info_db_name = "MovieLens"
movie_info_col_name = "movies"
tag_info_col_name = "genome-tags"
tag_movie_array_col_name = "tagId-movieIdArray"
hot_movie_on_single_tag_col_name = "hot_movie_on_single_tag"
client = pymongo.MongoClient(database['url'])  # TODO:加用户，密码
root_db = client[movie_info_db_name]
skip_len = 0
LIMIT_LEN = 8


# 根据movie_id返回， 格式{'id': 电影id, 'name': 电影名, 'tag': 电影表中genre列, 'url'：图片地址}
def get_movie_info(movie_id):
    movie_col = root_db[movie_info_col_name]
    try:
        movie_info = movie_col.find_one({"movieId": movie_id})
        return movie_info['title']
    except:
        print("error")


# 根据movie_id_list 返回需求格式的数组
def get_movie_info_by_list(movie_id_list):
    movie_col = root_db[movie_info_col_name]
    try:
        # in操作符一次获取所有满足条件cursor
        cursor = movie_col.find({"movieId": {"$in": movie_id_list}})
        res = []
        for item in cursor:
            tmp = dict()
            tmp.update({"id": item['movieId']})
            tmp.update({"name": item['title']})
            tmp.update({"tag": item['genres']})
            tmp.update({"url": item['url']})
            res.append(tmp)
        return res
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


# 选取8部热门电影，{'_id': 电影id, 'tag_id': 标签id, 'tag_name': '标签名', 'title': '电影名'}
def get_check_list():
    col = root_db[hot_movie_on_single_tag_col_name]
    second = time.localtime().tm_sec % 46  # 数据集369，最多46组
    hot_movie_list = col.find().skip(second * LIMIT_LEN).limit(LIMIT_LEN)
    check_list = [i for i in hot_movie_list]
    return check_list


if __name__ == '__main__':
    # # movie信息获取 测试
    # print(get_movie_info(1))

    # # tag信息获取 测试
    # print(get_tag_info(760))

    # # 取tag对应movieId 测试
    # tag_zero_array = get_movie_array_on_tag(tag_id=2, count=2)
    # tag_one_array = get_movie_array_on_tag(tag_id=6, count=2)
    # tag_multi_array = get_movie_array_on_tag(tag_id=3, count=2)
    # print(tag_zero_array)
    # print(tag_one_array)
    # print(tag_multi_array)

    # get_check_list 测试
    # for i in range(5):
    #     time.sleep(1)
    #     for item in get_check_list():
    #         print(item)

    # 获取一个电影列表中所有电影对应信息
    movie_info_list = get_movie_info_by_list([12, 456, 78])
    for i in movie_info_list:
        print(i)

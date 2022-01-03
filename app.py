from random import randrange
from flask import Flask
from pop_movies_show.top_movie_on_tag import get_movie_array_on_tag

app = Flask(__name__)
tag_num_max = 1126

# 返回电影信息，title，poster，tag
@app.route('/movie')
def movie_show():
    pass


@app.route('/')
def init_pop_movies():
    # 从tag对应电影集合初始取8个movie，每个tag最多对应两个
    movie_id_set = set()
    max_len = 8
    movie_cnt = 2
    tag_id = randrange(tag_num_max)
    while len(movie_id_set) != max_len:
        tmp_array, tmp_cnt = get_movie_array_on_tag(tag_id, movie_cnt)
        for mid in tmp_array:
            movie_id_set.add(mid)
        movie_cnt = min(max_len - len(movie_id_set), 2)
        tag_id = (tag_id + 1) % tag_num_max
    print(tag_id)
    print(movie_id_set)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

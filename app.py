from flask import Flask, jsonify, render_template, redirect, request
from flask import make_response
from flask_cors import CORS

from pop_movies_show.top_movie_on_tag import get_check_list, get_movie_info_by_list
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)


# 返回电影信息，title，poster，tag
@app.route('/movie')
def movie_show():
    pass


@app.route('/init')
def init_pop_movies():
    init_list = get_check_list()
    resp = make_response('Test')
    resp.set_cookie('same-site-cookie', 'strict', samesite='Lax')
    return jsonify(init_list)


#  movieId list  ->  url -> item requests  数量: 前端：24  spark返回：无穷
#  请求spark格式 localhost:5432/data?movie=12&movie=1&movie=180
@app.route('/recommend', methods=['POST'])
def recommend():
    # 前端提供偏好电影list中，取前24个
    # pre_movie_list = [1, 2, 3] # 测试，数组内容为int
    print(request.get_json())
    pre_movie_list = request.get_json()['pre_movies'][:24]
    new_list = ["movie=" + str(i) for i in pre_movie_list]
    param = '&'.join(new_list)
    url = "http://localhost:5432/data?" + param
    # 认为response为推荐电影id列表
    rec_movie_list = requests.get(url).json()
    print(rec_movie_list)
    # 前端在此取得data数据
    data = get_movie_info_by_list(rec_movie_list)
    print(data)
    return jsonify(data)


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask import Flask, jsonify
from flask import make_response
from flask_cors import CORS

from pop_movies_show.top_movie_on_tag import get_check_list

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
    # return resp
    return jsonify(init_list)


if __name__ == '__main__':
    app.run()

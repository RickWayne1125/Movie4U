from flask import Flask, render_template, request,jsonify

from pop_movies_show.top_movie_on_tag import get_check_list

app = Flask(__name__)


# 返回电影信息，title，poster，tag
@app.route('/movie')
def movie_show():
    pass


@app.route('/')
def init_pop_movies():
    init_list = get_check_list()
    return jsonify(init_list)
    # return render_template('index.html')


if __name__ == '__main__':
    app.run()

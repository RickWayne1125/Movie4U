from flask import Blueprint
main = Blueprint('main', __name__)
 
import json
from similarities import RecommendationEngine
 
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from flask import Flask, request

@app.route('/data', methods=['GET', 'POST'])
def recommend():
    movieList = request.args.getlist('movie', type=int)
    print(movieList)
    return json.dumps(recommendation_engine.recommend(movieList))


def create_app(spark):
    global recommendation_engine 

    recommendation_engine = RecommendationEngine(spark)    
    
    app = Flask(__name__)
    app.register_blueprint(main)
    return app 

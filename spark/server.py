import time, sys, cherrypy, os
from paste.translogger import TransLogger
from app import create_app
from pyspark.sql import SparkSession

def init_spark_context():
    # load spark context
    spark = SparkSession \
    .builder \
    .appName("Movie4U") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/MovieLens.similarities") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/MovieLens.similarities") \
    .config("spark.executor.memory", "8g") \
    .config("spark.driver.memory", "8g") \
    .getOrCreate()
    # IMPORTANT: pass aditional Python modules to each worker
    spark.sparkContext.addPyFile("similarities.py")
    spark.sparkContext.addPyFile("app.py")
 
    return spark
 
 
def run_server(app):
 
    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)
 
    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')
 
    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload.on': True,
        'log.screen': True,
        'server.socket_port': 5432,
        'server.socket_host': '0.0.0.0'
    })
 
    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()
 
 
if __name__ == "__main__":
    # Init spark context and load libraries
    spark = init_spark_context()
    app = create_app(spark)
 
    # start web server
    run_server(app)
1. Import data from Movilens Dataset to MongoDB
```
mongoimport -d MovieLens  --type csv --file similarities.csv --headerline
mongoimport -d MovieLens  --type csv --file movies.csv --headerline
```
2. engine.py
Recommendation engine using Collaborative Filtering-Alternating Least Square
3. sparkfm.py
Recommendation engine using Factorization Machines
4. recommendation.ipynb
Adoption of `../recommendation/recommendation.py` for Spark
5. Submuit to Spark Cluster
spark-submit --master spark://chufanchen.com:7077 --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 --total-executor-cores 14 --executor-memory 6g server.py 

curl 'localhost:5432/data?movie=12&movie=1&movie=180'
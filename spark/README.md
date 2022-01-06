1. Import data from Movilens Dataset to MongoDB
```
mongoimport -d MovieLens  --type csv --file similarities.csv --headerline
mongoimport -d MovieLens  --type csv --file movies.csv --headerline
mongoimport -d MovieLens  --type csv --file ratings.csv --headerline
```
2. engine.py
Recommendation engine using Collaborative Filtering-Alternating Least Square
3. sparkfm.py
Recommendation engine using Factorization Machines
4. recommendation.ipynb

Adoption of `../recommendation/recommendation.py` for Spark

5. Submuit to Spark Cluster
`spark-submit --master spark://chufanchen.com:7077 --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 --total-executor-cores 14 --executor-memory 6g server.py `
6. Test API
`curl 'localhost:5432/data?movie=12&movie=1&movie=180'`
7. movielens.py
To download the dataset, please install Pandas package first. Then issue the following command:
```
python ncf/movielens.py
```
Arguments:
- `--data_dir`: Directory where to download and save the preprocessed data. By default, it is /tmp/movielens-data/.
- `--dataset`: The dataset name to be downloaded and preprocessed. By default, it is ml-1m.
Use the `--help` or `-h` flag to get a full list of possible arguments.
8. Scalable Movie Recommendations.ipynb

A  highly scalable and accurate neural network using Spark and Horovod




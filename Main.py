from pyspark.sql import SparkSession
import pandas 
from pyspark.ml.recommendation import ALS

spark = SparkSession \
    .builder \
    .appName("Suggestioner") \
    .getOrCreate()

rating_df = spark.read.csv('ratings.csv', header = True)
game_df = pandas.read_csv('games.csv')

uid = int(input('Enter user id: '))

rating_df = rating_df.select(rating_df.user_id.cast('int'), rating_df.game_id.cast('int'), rating_df.rating.cast('int'))

(training, test) = rating_df.randomSplit([0.8, 0.2])

als=ALS(maxIter = 5, regParam = 0.01 , userCol = "user_id" , ratingCol = "rating" , itemCol = "game_id" , coldStartStrategy = "drop")

model = als.fit(training)

predictions = model.transform(test)

gid = predictions.orderBy('prediction', ascending = False).select('game_id').collect()
score = predictions.orderBy('prediction', ascending = False).select('prediction').collect()

for i in range(5):
     game_data = game_df.loc[game_df['game_id'] == gid[i][0]]
     print(game_data['name'].values[0], '---->', score[i][0])

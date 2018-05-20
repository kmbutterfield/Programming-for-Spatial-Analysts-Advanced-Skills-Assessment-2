## Python Files

#### TweetStream_RoyalWedding.py
Requires Tweepy and PyMongo

Script to create a stream listener which scrapes live Tweets on the Royal wedding, storing the data into a MONGODB collection. If the collection does not exist, it will be created. For an easy method of viewing the collection, I recommend downloading MongoDB Compass to check your data is being saved.

#### MongoDB_to_CSV.py
Requires PyMongo and CSV

Script to create and write a CSV file from the MongoDB. Ensure your code is in Python 3, otherwise syntax will be altered for creating the CSV columns. Also ensure that the encoding is in utf-8 for data to be understood and avoidance of misunderstanding characters or emojis.

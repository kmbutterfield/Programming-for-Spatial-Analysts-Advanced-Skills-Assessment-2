## Python Files

#### TweetStream_RoyalWedding.py
Requires Tweepy and PyMongo

Script using <a href="http://tweepy.readthedocs.io/en/v3.5.0/">Tweepy</a> to create a stream listener which scrapes live Tweets on the Royal wedding, storing the data into a <a href="https://www.mongodb.com/">MongoDB</a> collection. If the collection does not exist, it will be created. For an easy method of viewing the collection, I recommend downloading <a href="https://www.mongodb.com/products/compass?_bt=229925058879&_bk=mongo%20compass&_bm=e&_bn=g&utm_source=google&utm_campaign=EMEA_UK-IE_CorpEntOnly_Brand_Alpha_FM&utm_keyword=mongo%20compass&utm_device=c&utm_network=g&utm_medium=cpc&utm_creative=229925058879&utm_matchtype=e&_bt=229925058879&_bk=mongo%20compass&_bm=e&_bn=g&jmp=search&gclid=EAIaIQobChMI9eTowt2U2wIVB7XtCh2Y3g8KEAAYASABEgJyZfD_BwE">MongoDB Compass</a> to check your data is being saved.

Please ensure you have API Keys and Token for Twitter in order to stream their live Tweets. Visit https://apps.twitter.com/ to get started.

If you want to learn how to setup Twitter API and Tweepy, I read up on documentation, and followed <a href="https://www.youtube.com/watch?v=pVmCI9zIMbc&list=PLmcBskOCOOFW1SNrz6_yzCEKGvh65wYb9">Sukhvinder Singh's</a> tutorials on Youtube whenever I encountered issues. 

If you want to learn more about using MongoDB, and have a paid subscription for SkillShare, I recommend enrolling onto <a href="https://www.skillshare.com/classes/MongoDB-Essentials-Understand-the-Basics-of-MongoDB/543813362?via=search-layout-grid">this</a> class to get a basic understanding, this is what I followed for my own work. 



#### MongoDB_to_CSV.py
Requires PyMongo and CSV

Script to create and write a CSV file from the MongoDB. Ensure your code is in Python 3, otherwise syntax will be altered for creating the CSV columns. Also ensure that the encoding is in utf-8 for data to be understood and avoidance of misunderstanding characters or emojis.

## Python Files

### CreateTimeSeries.py
<b>Requires Pandas and Vincent</b>

Using <a href="http://vincent.readthedocs.io/en/latest/">Vincent</a>, a time-series area chart is created based on the CSV Tweet data's "created_at" column. As shown below, the output is not very visually effective due to the constant abundance of tweets.

<img src="https://github.com/kmbutterfield/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2/blob/master/0.%20Images/TimeSeriesOutput.png" width="700">

Tweets during the live Royal wedding streamed in consantaly at around 2,700 Tweets per minute. This is not surpring as it is such a large event. To improve this code, an alternative graphing method could be utilised with a larger y-axis miniumum value.

If you are struggling to use Vincent, I can recommend reading <a href="http://wrobstory.github.io/2013/04/pandas-vincent-timeseries.html">these</a> examples on creating your own time series chart. It helped me when I struggled to workout displaying data over minutes.

### CommonTimeZones.py
<b>Requires Pandas </b>

Using <a href="https://pandas.pydata.org/">Pandas</a> in Jupyter Notebooks, you can create a table of the top 15 most common time zones from the Tweet data.

<img src="https://github.com/kmbutterfield/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2/blob/master/0.%20Images/TimeZoneOutput.png" width="300">

This script is simple yet useful, providing you an idea of where Tweeters are from using their bio location. As you can see, most Tweets on the Royal wedding came from those in the US and Canada, and the UK. Despite the time difference, users around the world tuned in and watched the wedding, or Tweeted about it. To improve this, you could combine the US and Canadas timezones to make a complete Nort America Time Zone.

## MapTweets.py
<b>Requires Pandas and Folium </b>

Using <a href="https://github.com/python-visualization/folium">Folium</a> and Pandas, a HTML file is created containing a map of the geolocations of Tweets.

<img src="https://github.com/kmbutterfield/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2/blob/master/0.%20Images/TeetMapOutput.png">

Not all Twitter users have their geolocation turn on, for good reason too, but those that do allow us to create maps of Titter data. For all Tweets that had their geolocations on, have been mapped. To improve this code, further Folium tools can be added such as a hover tool containing further information such as the user's Tweet.. but not their username, that would be too much info!

As seen above, most Tweets about the Royal wedding with geolocation turned on were from the US and the UK. Other Tweeters around the world also Tweeted in areas such as the Phillipines, Egypt, and Dubai. 

For help with using Folium, I can reccomend following <a href="https://www.kaggle.com/daveianhickey/how-to-folium-for-maps-heatmaps-time-data">this</a> tutorial which I found helpful when learning to use the library.

## TweetPlatformPieChart.py
<b>Requires Pandas, CSV, and Matplotlib </b>

Using Pandas and Maplotlib, a pie chart can be created displaying the percentage of what platform Tweeters used to Tweet in, such as Twitter for Andorid, iPhone, Twitter Web Client and other sources.

<img src="https://github.com/kmbutterfield/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2/blob/master/0.%20Images/TweetPlatformOutput.png" width="500">

As shown above, most Tweets came from users using an iPhone, which is not surprising considering how many people own an Apple phone. The second largest client used was Twitter for Android, whilst the least used was the Twitter Web Client. 'Other' sources were common too, as people sent Tweets via other websites, Facebook, and adverts.

## WordFrequencyAnalysis.py
<b>Requires NLTK and Pandas and NLTK stopwords </b>

Using NLTK, stopwords, and Pandas, you can create a graph to show the frequency of the top 25 most common words in Tweets from the database. Stopwords was used to filter out common words used in everyday language such as 'the', 'and', 'I' as most Tweets include these words. Punctuation was also removed from the Tweets as they would definitely make up the most common pieces of text.

<img src="https://github.com/kmbutterfield/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2/blob/master/0.%20Images/FreqDistBefore.png">

The image above displays the 25 most common words during just before the wedding started. As you can see, Tweeters seemed focused on David Beckham's presence, George Clooney, and Meghan's dress. Celebrity appearances seems to catch viewers attention! To improve this code, more filters should be appplied to remove the 'b"rt' (retweet) text and the search terms used during the Tweet stream. Also an alternative graphing library as I struggled to make it look aesthetically pleasing!



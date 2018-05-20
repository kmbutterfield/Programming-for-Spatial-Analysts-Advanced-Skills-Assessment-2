## Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-2
This repository contains assessment work for the module GEOG5790M. The purpose of this module was to create an independent project using a coding language on any topic of choice. Therefore, I decided to learn how to stream live-Tweets and the visualise the output to analyse them using, using Python. The Tweets scraped are on the topic of Prince Harry and Megan Markle's Royal wedding which took place Saturday the 19th of May 2018. 

Please note all code has been written in Python 3.

### Libraries Required:
* Tweepy for streaming via Twitter's API
* PyMongo to save the Tweets, and convert to CSV
* Vincent to create a time series graph of the Tweets during the stream
* Pandas to visualise the data
* Folium to create an aesthetically  pleasing map of tweets
* NLTK for language processing of Tweet text

### Folder Structure:
Folder 1. Stream-Convert-Tweets contains scripts to run the Tweet streamer, tracking words on the Royal wedding, and script to convert to CSV from MongoDB.

Folder 2. Analyse-Tweets contains scripts to visualise and analyse the Tweet data with examples of output.

For more information, please read the information files provided within each folder.

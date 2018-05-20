'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: CreateTweetTimeSeries.py
    Description: Converts CSV tweet data into a time series area chart.
'''

import pandas as p
import vincent
from pandas.tseries.offsets import DateOffset

# read in CSV containing tweets with their date and time using pandas
tweets = p.read_csv('./RoyalWedding.csv')
tweets['created_at'] = p.to_datetime(p.Series(tweets['created_at']))

# use 'created_at' (contains date/time) to index
tweets.set_index('created_at', drop=False, inplace=True)
# convert to GMT due to streaming being off by one hour
tweets.index = tweets.index.tz_localize('GMT').tz_convert('GMT')
tweets.index = tweets.index - DateOffset(hours = 24)

# use tweets per minute to index
tweets_pm = tweets['created_at'].resample('1t').count()

# use Vincent library to create a time series of tweets
vincent.core.initialize_notebook()
area = vincent.Area(tweets_pm)
area.colors(brew='Set3')
area.axis_titles(x='Time', y='Tweets')
area.display()
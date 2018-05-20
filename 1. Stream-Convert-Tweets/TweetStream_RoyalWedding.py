'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: TweetStream_RoyalWedding.py
    Description: Stream real-time tweets using tweepy, store into MongoDB.
'''

import sys
import pymongo
import tweepy

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

''' Setup and connenct to Mongo client '''

client = pymongo.MongoClient('localhost', 27017)
db = client.test

''' Insert Twitter API information and Authorise '''

consumer_key="<insert your consumer key>"
consumer_secret="<insert your consumer secret>"

access_token="<insert your access token>"
access_token_secret="<insert your access token secret>"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

''' Create Tweepy Stream Listener and setup new MongoDB '''

class CustomListener(StreamListener):
  def __init__(self, api):
    self.api = api
    super(tweepy.StreamListener, self).__init__()
    # if the database doesn't exist, it will be created
    self.db = pymongo.MongoClient().RoyalWedding

  def on_status(self, status):
    data = {}
    data['created_at'] = status.created_at
    data['user'] = status.user.screen_name
    data['text'] = status.text
    data['userTimeZone'] = status.user.time_zone
    data['userLocation'] = status.user.location
    data['geo'] = status.geo
    data['source'] = status.source
        
    print (data, '\n')
    self.db.Tweets.insert(data) # save data to database

  def on_error(self, status):
    print ('Error: ', status, file=sys.stderr)
    return True

  def on_timeout(self):
    print ('Stream timeout', file=sys.stderr)
    return True

''' Start Streaming, tracking the keywords '''

listen = Stream(auth, CustomListener(api))
listen.filter(track=['#RoyalWedding','Prince Harry','Meghan'])
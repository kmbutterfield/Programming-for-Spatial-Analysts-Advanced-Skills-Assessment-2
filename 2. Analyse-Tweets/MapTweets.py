'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: MapTweets.py
    Description: If geolocation is available, map tweets.
'''

import folium
import pandas

# derive geolocation data from CSV rows that contain coordinates
locations = pandas.read_csv('./RoyalWedding.csv', usecols=[6]).dropna()

# create list of geos (coordinates)
geos = []

for location in locations.values:
  geos.append(ast.literal_eval(location[0])['coordinates'])

# create a map of the world using Mapbox styling
tweet_map = folium.Map(location=[52.8, -2], tiles='Mapbox Bright', 
                       zoom_start=3)

# creates dots using folium
for geo in geos:
  folium.CircleMarker(location=geo, radius=2).add_to(tweet_map)
  
tweet_map.save('TweetMap.html')

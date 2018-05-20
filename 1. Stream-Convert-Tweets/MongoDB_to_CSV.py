'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: MongoDB_to_CSV.py
    Description: Write the MongoDB collection to a CSV file..
'''

from pymongo import MongoClient
import csv

db = MongoClient().RoyalWedding # connect to the database

''' Write to CSV '''
field_names = ["created_at", "user", "text", "userTimeZone", "userLocation", 
               "geo", "source"]

with open('RoyalWedding.csv', 'w', encoding="utf-8", newline='') as f_output:
    csv_output = csv.writer(f_output, delimiter=",")
    csv_output.writerow(field_names)
        
    for data in db.Tweets.find():
        csv_output.writerow([ 
                data['created_at'],   # tweet creation time
                data['user'],         # tweet user's name
                data['text'],         # tweet text
                data['userTimeZone'], # user's time zone
                data['userLocation'], # user's profile location
                data['geo'],          # coordinates of the tweet
                data['source']        # the app used to send the tweet
        ])

f_output.close()
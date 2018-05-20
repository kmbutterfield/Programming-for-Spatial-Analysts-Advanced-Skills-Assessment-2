'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: TweetPlatformPieChart.py
    Description: Creates a pie chart of tweet sources (iPhone, Android, Web)
'''

import pandas as pd
import csv
import matplotlib.pyplot as plt

# read into CSV file, seelct column 8 containing tweet source info
df = pandas.read_csv('./RoyalWeddingAll.csv', usecols=[8]).dropna()

# group tweets by source such as iPhone, Android, others
a = df.groupby('source').size()

# set custom pie chart colours
color_set = ('crimson', 'darkorange', 'c', 'yellow', 'darkcyan')
# display the pie chart and counts
print (a)
a.plot.pie(colors = color_set, figsize=(5,5))
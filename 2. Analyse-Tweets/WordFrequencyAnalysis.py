'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: WordFrequencyAnalysis.py
    Description: Filters and plots frequency distribution of common words.
'''

import nltk
nltk.download('stopwords')
import pandas

from nltk.corpus import stopwords

# only identify words written in English
stop = stopwords.words('English')
texts = pandas.read_csv('./RoyalWedding.csv')['text'] # read text part of tweet

tokens = []

# remove punctuation from the tweet text
for text in texts.values:
  tokens.extend([word.lower().strip(':,."-') for word in text.split()])

freq_dist = nltk.FreqDist()
# create frequency distribution plot of 25 most common words in the tweets
print (freq_dist.plot(25))
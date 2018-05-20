'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Assessment: Personal Project
    Author: kmbutterfield
    File name: CommonTimeZones.py
    Description: Creates a table of user time zones using pandas.
'''

import pandas as pd

df = pd.read_csv('RoyalWedding.csv')
# print 15 most common timezones as percentage
timezone = df.userTimeZone.value_counts(normalize=True)
print (timezone.nlargest(15))

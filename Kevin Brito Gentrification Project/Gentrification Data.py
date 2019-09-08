#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import urllib.request
import json

# In[22]:


permit = pd.read_csv('Permits.csv')

# In[23]:


# Extracted the year from every permit from the permit type column
permit['YEAR'] = pd.DatetimeIndex(permit['ISSUED']).year

# Dropped any rows that did not contain BOTH latitude and longitude info
permit.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
permit.head(100)

# In[24]:


# This block of code is necessary to obtain data from API because it times out periodically
# It allows the program to continue running by pausing or "sleeping" for five seconds after a time out
# Takes 4 hours and 33 minutes to run completely
# Try and except provided by KJ

from tqdm import tqdm
from urllib.error import URLError
from time import sleep

# Used census block column to isolate geoID from API
geoID = []
for index, row in tqdm(permit.iterrows()):
    lat = row['LATITUDE']
    lon = row['LONGITUDE']
    url = 'https://geo.fcc.gov/api/census/block/find?latitude=' + str(lat) + '&longitude=' + str(lon) + '&format=json'

    try:
        response = urllib.request.urlopen(url)
        content_string = response.read().decode()
        location_info = json.loads(content_string)
        geoID.append(location_info['Block']['FIPS'])
    except URLError:
        print("Exception - time out")
        sleep(5)

permit['geo.id2'] = geoID

# In[2]:


# grouped = permit.groupby(['PERMIT TYPE', 'YEAR', 'CENSUS BLOCK'])
# grouped_size = grouped.size().reset_index()
# multi_index = grouped_size.set_index(['YEAR', 'CENSUS BLOCK'])
# multi_index.head(10)


# In[1]:


# perm_by_year = multi_index.pivot(columns = 'PERMIT TYPE')
# perm_by_year.fillna(0)


# In[35]:


grouped2 = permit.groupby(['PERMIT TYPE', 'YEAR', 'geo.id2'])
grouped_count2 = grouped2.size().reset_index()
multi_index2 = grouped_count1.set_index(['YEAR', 'geo.id2'])
multi_index2.head(10)

# In[38]:


# Pivots DF on Permit Type to isolate num of permits per block for each year
perm_by_year2 = multi_index2.pivot(columns='PERMIT TYPE').fillna(0)
perm_by_year2.head(50)

# In[39]:


perm_by_year2.to_csv('Permits By Geoid2.csv')

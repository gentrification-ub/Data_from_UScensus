#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Voltaire Vergara
# Created Date: 7/6/2019
# =============================================================================
'''
The aim of this file is to reproduce the population data that is indicated in the document, Buffalo Turning the corner,
for the neighborhood, Elicott Neighborhood.
Once reproduced, all the data will be turned into csv files for visualization
'''
import json
import requests




api_key = '3fad1f7c603dfb341edd045495a58a7c0e77f15c' #My API key
parameters = {"key": api_key}
api_base_url = lambda year :'https://api.census.gov/data/' + year + '/acs/acs5?' #API call link
response =requests.get(api_base_url("2016"), params = parameters)

parameters.update( {"get": "B02001_003E,NAME"} )

#ELICOTT NEIGHBORHOOD ACCORDING TO BUFFALO TURNING THE CORNER
parameters.update( {"for":"block group:1,2,4", "in": "state:36+county:029+tract:001402"} )

response = requests.get(api_base_url('2016'), params = parameters)
json = response.content
print(api_base_url('2019'))
'''
print( "Population of African American: \n" + response.content.decode("utf-8"))
print("Total of black: 1461")
parameters.update( {"get": "B02001_001E,NAME"} )
print( "Total Population: \n" + response.content.decode("utf-8"))
print("Total of population: 1644\n" + "Percent of black in these places: " +  str((1461/1644) * 100))
#["19798228","New York","36"], '''
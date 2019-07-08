#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Voltaire Vergara
# Created Date: 7/6/2019
# =============================================================================
'''
The aim of this file is to reproduce the population data that is indicated in the document, Buffalo Turning the corner,
for the neighborhood, Ellicott Neighborhood.
Once reproduced, all the data will be turned into csv files for visualization
'''
import json
import requests

# =============================================================================
api_key = '3fad1f7c603dfb341edd045495a58a7c0e77f15c' # API key
# The parameters are set to have my API key and the geography level down to the block level of Ellicott neighborhood
parameters = {"key": api_key, "for":"block group:1,2,4", "in": "state:36+county:029+tract:001402"}
api_base_url = lambda acs_year: 'https://api.census.gov/data/' + acs_year + '/acs/acs5?' # API call link
# ==============================================================================
'''
def ACScalculate_percent(variable_sample, variable_total,year, num_blockGrp = 3):
    
    @assumes that 
    :param variable_sample: 
    :param variable_total: 
    :return: 
    if isinstance(variable_sample, list): 
        for var in variable_sample: 
            parameters.update( {"get": var +  ","  + variable_total})
            response = requests.get(api_base_url(str(year)), params = parameters) 
            json = response.json()
            for i in range(1,num_blockGrp):
                total_var_count =+ json[i][0]
        return total_var 
    parameters.update( {"get": variable_sample +  ","  + variable_total})
    response = requests.get(api_base_url(str(year)), params = parameters) # edit these parameters later need to put a if NONe
 '''

variables = {"Total population": "B01003_001E",
             # race
             "Total number of person(only White)": "B02001_002E",
             "Total number of person(only Hisapnic": "B01001I_001E",
             # household type
             "Total Number of Housing Units": "B25001_001E",
             "Total Number of Renter per housing unit": "B25003_003E",
             "Total Number of Vacant Housing Units": "B25002_003E",
             # poverty
             "Total ratio of income to poverty (population whose poverty level is determined)": "C17002_001E",
             "Total below povery line (population whose poverty level is determined)": ["C17002_002E", "C17002_003E"],
             # gross rent as income
             "Total Median Gross Rent As A Percentage Of Household Income In The Past 12 Months (Dollars)":
                                                                                                    "B25071_001E",
             # educational attainment
             "Total Population over 25 years and over that have less than a college education":
                                                                    ["B15003_00" + str(i) + "E" for i in range(2, 19)]}





parameters.update( {"get": "B25071_001E"} ) # till 18



response = requests.get(api_base_url('2016'), params = parameters)
json = response.content.decode("utf-8")
print(json)

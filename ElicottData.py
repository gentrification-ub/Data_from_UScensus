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
import csv
import json
import requests

# =============================================================================
api_key = '3fad1f7c603dfb341edd045495a58a7c0e77f15c' # API key
# The parameters are set to have my API key and the geography level down to the block level of Ellicott neighborhood
parameters = {"key": api_key, "for":"block group:1,2,4", "in": "state:36+county:029+tract:001402"}
api_base_url = lambda acs_year: 'https://api.census.gov/data/' + acs_year + '/acs/acs5?' # API call link
# ==============================================================================

'''
THIS IS TO CALCULATE ON A NEIGHBORHOOD LEVEL 

def ACScalculate_percent(variable_sample, variable_total,year, num_block = 3):
    
    assumes that 
    :param variable_sample: 
    :param variable_total: 
    :param year 
    :param num_block
    :return:
    
    parameters.update( {"get": variable_sample + "," + variable_total})
    response = requests.get(api_base_url(str(year)), params=parameters)
    json = response.json()
    for i in range(1, num_block):
        var_count =+ json[i][1] 
        total_var_count =+ json[i][1] 
    if isinstance(variable_sample, list): 
        var_count = 0
        for var in variable_sample: 
            parameters.update( {"get": var })
            response = requests.get(api_base_url(str(year)), params = parameters) 
            json = response.json()
            for i in range(1,num_block):
                var_count =+ json[i][0]
       
    else:

    return (var_count / total_var_count) * 100
'''

# these are the variables needed for the gentrification early warning system

variables = {"Total population": "B01003_001E",
             # race
             "Total number of person(only White)": "B02001_002E",
             "Total number of person(only Hisapnic)": "B03002_012E",
             # household type
             "Total Number of Housing Units": "B25001_001E",
             "Total Number of Renter per housing unit": "B25003_003E",
             "Total Number of Vacant Housing Units": "B25002_003E",
             # poverty
             "Total Population for whom poverty status is determined" : "C17002_001E",
             "Total below povery line (population whose poverty level is determined)": ["C17002_002E", "C17002_003E"],
             # gross rent as income
             "Total Median Gross Rent As A Percentage Of Household Income In The Past 12 Months (Dollars)":
                                                                                                    "B25071_001E",
             # educational attainment
             "Total Population over 25 years and over that have less than a college education":
                    ["B15003_0" + str(i).zfill(2) + "E" for i in range(2, 19)]}


# This calculates the percentages on a block level , then puts them into a csv file

with open('UBgentrification_data.csv', mode='w') as data:
    data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    data_writer.writerow(["Percent compared to the total", "Variable Title", "data", "tract", "block group", "year"])
    for year in range(2013,2018):
        for var_title, var_code in variables.items():
            data_list = []  # initializing empty list
            if isinstance(var_code, list):
                data_list = [0] * 3
                for codes in var_code:
                    parameters.update({"get": codes})
                    response = requests.get(api_base_url(str(year)), params=parameters)
                    json = response.json()
                    for block_count in range(1, len(json)):
                        data_list[block_count-1] += int(json[block_count][0])

            else:
                parameters.update({"get": var_code})
                response = requests.get(api_base_url(str(year)), params=parameters)
                json = response.json()
            print(data_list)
            for block in range(1,len(json)):
                var_data = json[block][0] if len(data_list) == 0 else data_list[block-1]
                data_tract = json[block][3]
                data_blockGrp = json[block][4]
                data_writer.writerow(["blank", var_title, var_data, data_tract, data_blockGrp, year])

parameters.update( {"get": "C17002_001E"} ) # till 18



response = requests.get(api_base_url('2016'), params = parameters)
json = response.content.decode("utf-8")
print(json)

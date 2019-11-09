#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Voltaire Vergara
# Created Date: 11/8/2019
# =============================================================================
"""
The aim of this file is to reproduce a beautiful soup object that contains
the tax history data of an individual through the erie county tax parcel website. Here we use an individiuals
unique SBL to query information
"""

import requests
from bs4 import BeautifulSoup

def grab_source_SBL(sbl):
    """
    Queries the Real Property Parcer of erie county(Specifically only SBL values), which can be found on this link:
                            http://www2.erie.gov/ecrpts/index.php?q=real-property-parcel-search
    This function will return a beautiful soup object of the source code of a SBL's tax History.
    :param sbl: SBL value that we are searching for
    :return: a Beautiful soup object of the tax extry history of that SBL
    """
    body = {'txtsbl': sbl,  # WE CAN CHANGE THIS TO SBL BUT THIS IS OWNER NAME
            'showHistory': 'y'}
    url2 = 'https://paytax.erie.gov/webprop/'  # url we needed adding to since this is the root link
    url = 'https://paytax.erie.gov/webprop/property_info_results.asp'  # search website
    link = requests.post(url, data=body)
    source_soup = BeautifulSoup(link.content, 'lxml')
    details_link = []
    for a in source_soup.find_all('a', href=True):
        details_link.append(a['href'])

    # if there's only one element then that means that an SBL does not exist
    if len(details_link) > 1:
        # we can assure that SBL's are unique and always at the head of the list
        con2 = requests.post(url2+details_link[0])
        details_soup = BeautifulSoup(con2.content, 'lxml')
        for a in details_soup.find_all('a', href=True):
            details_link.append(a['href'])
        TAXLINK = url2 + details_link[3]
        return BeautifulSoup(requests.post(TAXLINK).content, 'lxml')

    else:
        raise Exception("SBL does not exist")



print(grab_source_SBL('100.23-2-12./S'))
import requests
from bs4 import BeautifulSoup
body = {'txtowner':'wyse',  # WE CAN CHANGE THIS TO SBL BUT THIS IS OWNER NAME
        'showHistory': 'y'} # <-- use 'query' not `Search'
url2 = 'https://paytax.erie.gov/webprop/' #url we needed adding to
url = 'https://paytax.erie.gov/webprop/property_info_results.asp' # search website
con = requests.post(url, data=body)
soup = BeautifulSoup(con.content, 'lxml')
details_link = []
for a in soup.find_all('a', href=True):
    details_link.append(a['href'])
    #print ("Found the URL:", a['href'])  # what we found here we need to add to url + "FOUND URL'

con2 = requests.post(url2+details_link[0])
soup2 = BeautifulSoup(con2.content, 'lxml')
for a in soup2.find_all('a', href=True):
    #details_link.append(a['href'])
    print ("Found the URL:", a['href'])  # what we found here we need to add to url + "FOUND URL'

#print(con2.url) # Taxpayment history starts iwth ecgov_pgl.asp <- use this by url2 + the found url
# https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
import requests
from bs4 import BeautifulSoup
''' url = 'http://services.runescape.com/m=itemdb_rs/'
body = {'Search':'rune'}
s = requests.Session()
log = s.get(url)
with requests.Session() as s:
    con = s.post('http://services.runescape.com/m=itemdb_rs/results#main-search', data=body)
    print (con.text)
print (con.content) '''

import requests
from bs4 import BeautifulSoup
body = {'txtowner':'wyse',  # WE CAN CHANGE THIS TO SBL BUT THIS IS OWNER NAME
        'showHistory': 'y'} # <-- use 'query' not `Search'
url2 = 'https://paytax.erie.gov/webprop/'
url = 'https://paytax.erie.gov/webprop/property_info_results.asp'
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

#print(con2.url)
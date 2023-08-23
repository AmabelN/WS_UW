# Amabel_Nabila
# 455854

from urllib import request
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
html = request.urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
links = bs.find('span', {'id': 'A'}).find_next('ul').find_all('li')

# Extract links to web page containing information about musicians specialising in music genre beginning with ”A”
Alinks = []
for link in links:
    a = link.find('a')
    if a:
        href = a.get('href')
        if href and href.startswith('/wiki/'):
            Alinks.append('https://en.wikipedia.org' + href)

print(Alinks)

# Extract the links to artists’ web pages for the first of the links from the previous step
response = requests.get(Alinks[0])
soup = BeautifulSoup(response.content, 'html.parser')
artists = soup.find_all('div', {'class': 'div-col'})

artist_links = []
for artist in artists:
    for link in artist.find_all('a'):
        artist_links.append('https://en.wikipedia.org'+link['href'])

print(artist_links)

# From artist’s pages extract: name of the band, years active
artist_data = []
for artist_link in artist_links:
    response = requests.get(artist_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    info_box = soup.find('table', {'class': 'infobox'})
    if info_box:
        name = soup.find('h1', {'class': 'firstHeading'}).text
        rows = info_box.find_all('tr')
        for row in rows:
            if row.th and 'Years active' in row.th.text:
                years_active = row.td.text.strip()
                artist_data.append({'Name': name, 'Years Active': years_active})

# As an output use default print function on pandas data frame
data = pd.DataFrame(artist_data)
print(data)
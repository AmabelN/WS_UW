# Amabel_Nabila
# 455854

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Queen_(band)'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the name of the band
band_name = soup.find('h1', {'class': 'firstHeading'}).text.strip().replace('(band)', '')
print('The name of the band:', band_name)

# Extracting the genre of the band
band_genre = soup.find('a', {'title': 'Rock music'}).text.strip()
print('The genre of the band:', band_genre)

# Extracting the number of years active of the band
band_active = soup.find('th', string='Years active').find_next_sibling('td').text.strip()
print('The number of years active of the band:', band_active)

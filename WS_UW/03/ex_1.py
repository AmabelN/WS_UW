# Amabel Nabila
# 455854

import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# Using lambda expressions print out how many times a tag consisting of a string "Anna Pavlovna" appears in the text."
Anna_Pavlovna = soup.findAll(lambda tag: 'Anna Pavlovna' in tag.get_text())

# Print the number of names appears
print(f'The name "Anna Pavlovna" occurs {len(Anna_Pavlovna)} times in the web.')

# Using lambda expressions enlist tags with exactly one attribute. Also, print out the length of this list.
tags = soup.find_all(lambda tag: len(tag.attrs) == 1)

# Print tags with only one attribute and the length
print(tags)
print(len(tags))
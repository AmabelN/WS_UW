# Amabel Nabila
# 455854

import requests
import re

url = "https://en.wikipedia.org/wiki/United_Nations"
response = requests.get(url)

# Use regex to retrieve all of the flags' image paths
regex = r'<img[^>]*src="([^"]*Flag_of_[^"]*)"[^>]*>'
flags = re.findall(regex, response.text)

# Print the image paths
for flag in flags:
    print(flag)
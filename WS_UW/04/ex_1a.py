# Amabel_Nabila
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z)"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract links to web pages containing information about musicians whose name begin with ”Q”
Qmusicians = soup.find_all("a", href=lambda href: href and href.startswith("/wiki/") and href[6:].startswith("Q"))

# Including Suzi Quatro
Qmusicians.append(soup.find("a", href="/wiki/Suzi_Quatro"))

# Print the output as links
for link in Qmusicians:
    href = link.get("href")
    text = link.get_text()
    print(f'<a href="https://en.wikipedia.org{href}" target="_blank">{text}</a>')

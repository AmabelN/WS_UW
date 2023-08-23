# Amabel_Nabila

import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/page3.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract bolded text 1
first_heading = soup.find('h1')
bolded1 = [elem.text for elem in first_heading.select('span.excitingNote')]
bolded1.append(first_heading.text.replace(''.join(bolded1), '').strip())

# Print extract bolded text 1
print(bolded1)

# Extract bolded text 2
table_headers = soup.find('table', {'id': 'giftList'}).find_all('th')
bolded2 = [header.find('b').get_text(strip=True) if header.find('b') else header.get_text(strip=True) for header in table_headers]

# Print extract bolded text 2
print(bolded2)

# Extract bolded text 3
exciting_notes = soup.find_all('span', {'class': 'excitingNote'})
bolded3 = [note.text.strip() for note in exciting_notes]

# Print extract bolded text 3
print(bolded3)

# Extract the last item title from the table
last_item_title = soup.select('#giftList tr.gift')[-1].select('td')[0].text

# Print the last item title
print(last_item_title)

# Extract the footer of the webpage
footer = soup.find('div', {'id': 'footer'}).text

# Print the footer
print(footer)

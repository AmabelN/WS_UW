# Amabel_Nabila
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the infobox on the right side of the page
infobox = soup.find('table', {'class': 'infobox'})

# Find the born in the infobox
born = infobox.find('th', string='Born')

# Extract the date of birth from the corresponding table cell
date_of_birth = born.find_next_sibling('td').find('span', {'class': 'bday'}).text.strip()

# Change the format of the date
date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').strftime('%d %B %Y')

# Print the born
print(date_of_birth)

# Find the occupations in the infobox
occupations = infobox.find('th', string='Occupations')
occupations = occupations.find_next_sibling('td').get_text(separator=' ').strip().replace('\n', '')

# Print the occupations
print(occupations)

# Find the references section
references_section = soup.find('div', {'class': 'reflist'})

# Extract the reference items if the references section exists
reference_items = references_section.find_all('li') if references_section else []

# Print the reference
for item in reference_items:
    print(item.text)

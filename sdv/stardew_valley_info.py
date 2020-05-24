import requests
import pprint
from bs4 import BeautifulSoup

url = 'https://stardewvalleywiki.com/List_of_All_Gifts'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='roundedborder')
# Why doesn't this work?
# table = results.find_all('tbody')
rows = results.find_all('tr')
for row in rows:
    villager_elem = row.find_all('td')
    if villager_elem:

        villager_name = villager_elem[0]
        villager_birthday = villager_elem[1]
        villager_loves = villager_elem[2]
        villager_likes = villager_elem[3]

        print(villager_name.text.strip())



from bs4 import BeautifulSoup
import requests

url = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(url)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())
box = soup.find('article', class_='main-article')
title = soup.find('h1').get_text()
# print(title)
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
print(transcript)
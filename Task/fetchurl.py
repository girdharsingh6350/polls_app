from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

urls = 'https://www.gmail.com/'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')


f = open("test1.txt", "w")

for link in soup.find_all("a"):
  data = link.get('href')
  f.write(data)
  f.write("\n")

f.close()

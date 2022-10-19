import csv
from requests import HTMLSession
from bs4 import BeautifulSoup
import requests



with open('list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        url = " ".join(row)
        headers = requests.head(url.get('href'))
        print(url, (headers.status_code))




        resp = requests.head(url)
print('%s %d' % (url, resp.status_code))
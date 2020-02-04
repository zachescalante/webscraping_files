import re

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

webpage = 'https://www.insidearbitrage.com/2020/02/merger-arbitrage-mondays-comtech-telecommunications-acquires-gilat-satellite-networks-in-a-cash-plus-stock-deal/'

with urllib.request.urlopen(webpage) as response:
   html = response.read()

soup = BeautifulSoup(html, features='lxml')

deals = soup.find_all('ol')[0].find_all('li')

for deal in deals:
    print(deal.text)
    [print(tag['href'], tag.text) for tag in deal.find_all('a', href=True, text=True)]


import re

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

webpage = 'https://www.insidearbitrage.com/2020/02/merger-arbitrage-mondays-introducing-weekly-spread-changes/'

with urllib.request.urlopen(webpage) as response:
   html = response.read()

soup = BeautifulSoup(html, features='lxml')

deals = soup.find_all('ol')[0].find_all('li')

deal_type = []
deal_link = []
of_ticker = []
by_ticker = []
of_price = []
by_price = []
deal_text = []
for deal in deals:
	print(deal.text)
	details= deal.find_all('a', href=True)
	deal_type.append(re.findall(r'^The(.*?)of', details[0].text)[0].strip())
	deal_link.append(details[0]['href'])
	of_ticker.append(details[1].text)
	of_price.append(details[1]['href'])
	by_ticker.append(details[2].text)
	by_price.append(details[2]['href'])
	deal_text.append(deal.text)
#print(deal_link)
#print(deal_type)
#print(of_ticker)
#rint(of_price)
#print(by_ticker)
#print(by_price)
#print(deal_text)

df = pd.DataFrame({'SEC_Link': deal_link, 'Deal_Type': deal_type, 'Target': of_ticker,
	'Target_Price': of_price, 'Acquirer': by_ticker, 'Acquirer_Price': by_price, 
	'Details': deal_text})

df.to_csv('deal_details.csv')



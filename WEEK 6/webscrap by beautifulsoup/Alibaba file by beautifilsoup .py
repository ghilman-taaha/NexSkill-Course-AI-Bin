#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = r'E:\neskill\NexSkill course AI bin\WEEK 6\beautiful soap and selenium files\Alibaba.com.html'
with open(URL, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'class':'organic-list'}) 
 
for row in table.find_all('div',
                         attrs = {'class':'fy26-product-card-wrapper'}):
    quote = {}
    quote['theme'] = row.h2.text
    quote['url'] = row.h2.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.h2.text
    quote['author'] = row.find('div', attrs={'class':'searchx-product-price-price-main'}).text
    quotes.append(quote)
 
filename = r'E:\neskill\NexSkill course AI bin\Alibaba_products_bs4.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
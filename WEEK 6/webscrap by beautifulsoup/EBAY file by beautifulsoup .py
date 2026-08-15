import requests
from bs4 import BeautifulSoup
import pandas as pd

with open(r'E:\neskill\NexSkill course AI bin\WEEK 6\beautiful soap and selenium files\Cell Phones & Smartphones _ eBay.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

products = soup.find_all('div', class_='brwrvr__item-card__wrapper')

product_price = []
product_name = []
product_link = []

for product in products:
    try:
        name = product.find('h3', class_='bsig__title__text').get_text(strip=True)
    except:
        name = ''
    try:
        price = product.find(string=lambda s: s and '$' in s)
        price = price.strip() if price else ''
    except:
        price = ''
    try:
        link = product.find('a', class_='bsig__title__wrapper')['href']
    except:
        link = ''
    product_price.append(price)
    product_name.append(name)
    product_link.append(link)

EbayProducts = pd.DataFrame({
    'Product_Name': product_name,
    'Product_Price': product_price,
    'Product_Link': product_link
})
EbayProducts.to_csv('Ebay_mobiles_bs4.csv', index=False)
print('Data Saved')
print('Products found:', len(products))
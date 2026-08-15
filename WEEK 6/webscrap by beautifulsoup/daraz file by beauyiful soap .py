import requests
from bs4 import BeautifulSoup
import pandas as pd

with open(r'E:\neskill\NexSkill course AI bin\WEEK 6\beautiful soap and selenium files\Buy Smart Phones Online at Best Price in Pakistan - Daraz.pk.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

products = soup.find_all('div', class_='Bm3ON')

product_price = []
product_name = []
product_reviews = []

for product in products:
    try:
        name = product.find('div', class_='RfADt').get_text(strip=True)
    except:
        name = ''
    try:
        price = product.find('span', class_='ooOxS').get_text(strip=True).replace('Rs.', '').strip()
    except:
        price = ''
    try:
        reviews = product.find('span', class_='qzqFw').get_text(strip=True)
    except:
        reviews = ''
    product_price.append(price)
    product_name.append(name)
    product_reviews.append(reviews)

DarazProducts = pd.DataFrame({
    'Product_Name': product_name,
    'Product_Price': product_price,
    'Product_Reviews': product_reviews
})
DarazProducts.to_csv('Daraz_mobiles_bs4.csv', index=False)
print('Data Saved')
print('Products found:', len(products))
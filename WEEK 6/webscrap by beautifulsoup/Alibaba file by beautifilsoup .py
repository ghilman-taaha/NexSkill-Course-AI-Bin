import requests
from bs4 import BeautifulSoup
import pandas as pd

with open(r'E:\neskill\NexSkill course AI bin\WEEK 6\beautiful soap and selenium files\Alibaba.com.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

products = soup.find_all('div', class_='fy26-product-card-wrapper')

product_price = []
product_name = []
product_link = []

for product in products:
    try:
        title = product.find('h2', class_='searchx-product-e-title')
        name = title.get_text(strip=True)
    except:
        name = ''
    try:
        price = product.find('div', class_='searchx-product-price-price-main').get_text(strip=True)
    except:
        price = ''
    try:
        link = title.find('a')['href']
    except:
        link = ''
    product_price.append(price)
    product_name.append(name)
    product_link.append(link)

AlibabaProducts = pd.DataFrame({
    'Product_Name': product_name,
    'Product_Price': product_price,
    'Product_Link': product_link
})
AlibabaProducts.to_csv('Alibaba_products_bs4.csv', index=False)
print('Data Saved')
print('Products found:', len(products))
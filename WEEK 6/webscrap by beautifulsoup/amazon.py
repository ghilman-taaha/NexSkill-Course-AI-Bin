#Python program to scrape website 
#and save products from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

r = requests.get(URL, headers=headers)
print("Status code:", r.status_code)

soup = BeautifulSoup(r.content, 'html5lib')

products=[]  # a list to store products

table = soup.find('div', attrs = {'class':'s-main-slot'})

if table is None:
    print("Amazon blocked the request or changed the page structure — no products found.")
    with open('amazon_debug.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print("Saved the raw response to amazon_debug.html — open it to see what Amazon actually sent back.")
    exit()

for row in table.find_all('div',
                         attrs = {'data-component-type':'s-search-result'}):
    product = {}
    product['title'] = row.h2.text
    product['url'] = "https://www.amazon.com" + row.a['href']
    product['img'] = row.img['src']
    product['price'] = row.find('span', attrs={'class':'a-offscreen'}).text
    products.append(product)

filename = 'amazon_products.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','url','img','price'])
    w.writeheader()
    for product in products:
        w.writerow(product)
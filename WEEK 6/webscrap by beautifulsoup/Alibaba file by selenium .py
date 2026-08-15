from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&keywords=Auto+Accessories"

driver = webdriver.Chrome()

driver.get(url)

productList=[]
productDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'fy26-product-card-wrapper')]")
for p in range(len(productDiv) - 1):
    product = {}
    try:
        titleEl = productDiv[p+1].find_element(By.XPATH, ".//h2[contains(@class,'searchx-product-e-title')]")
        product["title"] = titleEl.text
    except:
        product["title"] = ''
    try:
        priceEl = productDiv[p+1].find_element(By.XPATH, ".//div[contains(@class,'searchx-product-price-price-main')]")
        product["price"] = priceEl.text
    except:
        product["price"] = ''
    try:
        innera = productDiv[p+1].find_element(By.TAG_NAME, "a")
        product['url'] = innera.get_attribute('href')
    except:
        product['url'] = ''
    productList.append(product)

filename = 'Alibaba_productsMethod2.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['title', 'price', 'url'])
    w.writeheader()
    for product in productList:
        w.writerow(product)

driver.close()
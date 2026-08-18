from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://armasclothing.com/collections/new-arrivals"

driver = webdriver.Chrome()

driver.get(url)

qouestList = []
qoutesDiv = driver.find_elements(By.XPATH, "//li[contains(@class, 'product a')]")
for p in range(len(qoutesDiv)):
    quote = {}
    innerImg = qoutesDiv[p].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p].find_element(By.TAG_NAME, "a")
    inners = qoutesDiv[p].find_element(By.XPATH, ".//span[@class='price-item price-item--regular']")
    quote["img"] = innerImg.get_attribute('src')
    quote["lines"] = innerImg.get_attribute('alt')
    quote['url'] = innera.get_attribute('href')
    quote['price'] = inners.get_attribute("textContent")

    qouestList.append(quote)

filename = 'Week6/armasclothingV3.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['url', 'img', 'lines', 'price'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = r"file:///E:/neskill/NexSkill course AI bin/WEEK 6/beautiful soap and selenium files/Smart Home Devices & Systems.html"

driver = webdriver.Chrome()

driver.get(url)

qouestList=[]
qoutesDiv = driver.find_elements(By.CSS_SELECTOR, "div.ucw-widget-product-card")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = r'E:\neskill\NexSkill course AI bin\Amazon_mobiles_Method2.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

print("Saved", len(qouestList), "products to", filename)

input("Data save ho chuka hai. Website dekh lein, phir yahan Enter dabayein browser band karne ke liye...")

try:
    driver.close()
except:
    
    pass
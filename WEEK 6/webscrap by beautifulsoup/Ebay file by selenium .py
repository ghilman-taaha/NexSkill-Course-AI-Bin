from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = r"file:///E:/neskill/NexSkill course AI bin/WEEK 6/beautiful soap and selenium files/Cell Phones & Smartphones _ eBay.html"

driver = webdriver.Chrome()

driver.get(url)

qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'brwrvr__item-card__wrapper')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = r'E:\neskill\NexSkill course AI bin\Ebay_mobiles_Method2.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()
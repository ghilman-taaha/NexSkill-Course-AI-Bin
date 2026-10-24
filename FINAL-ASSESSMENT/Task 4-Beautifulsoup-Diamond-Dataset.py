#Python program to scrape website 
#and save diamond clarity grades from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://en.wikipedia.org/wiki/Diamond_clarity"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
clarities=[]  # a list to store clarity grades
 
table = soup.find('div', attrs = {'id':'mw-content-text'}) 
 
for row in table.find_all('li'):
    if 'category (' in row.text:
        clarity = {}
        clarity['category'] = row.text.split(' category')[0]
        clarity['grade'] = row.text.split('(')[1].split(')')[0]
        clarity['description'] = row.text.split(') ', 1)[1].split('[')[0].strip()
        clarities.append(clarity)
        print(clarity)
 
filename = r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\diamond_clarity.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['category','grade','description'])
    w.writeheader()
    for clarity in clarities:
        w.writerow(clarity)
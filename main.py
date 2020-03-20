def open_html(path):
    with open(path,'rb') as f:
        return f.read

def save_html(html, path):
    with open(path,'wb') as f:
        f.write(html)

import requests
from bs4 import BeautifulSoup

f = open('Report.xls','rb')
content = f.read()
soup = BeautifulSoup(content,'html.parser')
rows = soup.select_one("table tr")

print(rows)
elements = rows.select('td')

for x in range(len(elements)):
    print(rows.select('td')[x].text.strip())

print(rows.select('td')[0].text.strip())

f.close()

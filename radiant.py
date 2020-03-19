def open_html(path):
    with open(path,'rb') as f:
        return f.read

def save_html(html, path):
    with open(path,'wb') as f:
        f.write(html)

import requests
from bs4 import BeautifulSoup

f = open('Report.xls','r')
content = f.read()
soup = BeautifulSoup(content,'html.parser')
print(soup)
f.close()

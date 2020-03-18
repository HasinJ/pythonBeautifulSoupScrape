def save_html(html, path): #local save
    with open(path,'wb') as f: #wb 'write bytes', avoid encoding issues #same as file opening and closing + exception handling
        f.write(html)

#save_html(r.content, google_com)

def open_html(path): #open/read HTML from local file
    with open(path,'rb') as f:
        return f.read

#open_html(google_com)

import requests
from bs4 import BeautifulSoup #module

#saving, so that there is a need for only one request
url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser') #soup becomes an object with MANY methods

#News Source
rows = soup.select('tbody tr')
row = rows[0]
name = row.select_one('.source-title').text.strip()
print(name)

#reference page for News Source
allsides_page = row.select_one('.source-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page
print('reference: ' + allsides_page)

#bias
bias = row.select_one('.views-field-field-bias-image a')['href']
bias = bias.split('/')[-1] #string operation, like javascript
print(bias)

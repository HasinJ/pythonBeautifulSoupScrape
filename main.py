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

mainHeaderText = soup.div.text.strip()
beginBusiness = mainHeaderText.find("Business Unit")
endBusiness = mainHeaderText.find("VA")+2
businessUnit = mainHeaderText[beginBusiness:endBusiness]
print(businessUnit)

#should grab last id of the table
lastID = soup.tfoot.find('tr')['id']

#find first header row
rows = soup.find(class_="RowStyleHead")
elements = rows.select('.CellStyle')
for x in range(len(elements)):
    print(elements[x].text.strip())



f.close()

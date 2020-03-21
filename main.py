def open_html(path):
    with open(path,'rb') as f:
        return f.read

def save_html(html, path):
    with open(path,'wb') as f:
        f.write(html)

def sliceString(string,beginStr,endStr):
    startIndex = string.find(beginStr)+len(beginStr) #doesnt include beginStr
    stopIndex = string.find(endStr,startIndex) #to counteract against space
    output = string[startIndex:stopIndex]
    return output

import requests
from bs4 import BeautifulSoup

f = open('Report.xls','rb')
content = f.read()
soup = BeautifulSoup(content,'html.parser')
mainHeaderText = soup.find(id='MainReportDiv').text.strip().split('Report Time')[0]

#grabs business unit and then PC#
businessUnit = sliceString(mainHeaderText,'Business Unit','-')
PCnumber = sliceString(businessUnit,' ',' ')
print(PCnumber)

#should grab last id of the table
lastID = soup.tfoot.find('tr')['id']


#find first header row
rows = soup.find(class_="RowStyleHead")
elements = rows.select('.CellStyle')
for x in range(len(elements)):
    print(elements[x].text.strip())



f.close()

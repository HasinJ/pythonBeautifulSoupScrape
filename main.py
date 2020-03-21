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

data = []
template = dict()

#grabs business unit and then PC#
businessUnit = sliceString(mainHeaderText,'Business Unit','-')
PCnumber = sliceString(businessUnit,' ',' ')
print(PCnumber)

#should grab count of the table, including total ROWS
lastID = soup.tfoot.find('tr')['id']

#should grab count of the table without total rows
dataCount = soup.select('.RowStyleData')
dataCount.append(soup.select('.RowStyleDataEven'))
dataCount = len(dataCount)

#find first header row
rows = soup.find(class_="RowStyleHead")
elements = rows.select('.CellStyle')
for index in range(len(elements)):
    template[elements[index].text.strip()] = 0

dataCell = template
data.append(dataCell)

print(dataCount)
print(dataCell)
print(data[0]['Item'])

f.close()

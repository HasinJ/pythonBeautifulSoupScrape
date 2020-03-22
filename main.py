def open_html(path):
    with open(path,'rb') as f:
        return f.read

def save_html(html, path):
    with open(path,'wb') as f:
        f.write(html)

def sliceString(string,beginStr,endStr='nothing'):
    startIndex = string.find(beginStr)+len(beginStr) #doesnt include beginStr
    if endStr=='nothing':
        return string[startIndex:]
    stopIndex = string.find(endStr,startIndex) #so it doesn't take beginStr into consideration
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

#grabs first table since there are two tables and CSS
table = soup.find(class_='TableStyle')

#grabs business unit and then PC#
businessUnit = sliceString(mainHeaderText,'Business Unit','-')
PCnumber = sliceString(businessUnit,' ',' ')
print(PCnumber)

#grabs date
businessDate = sliceString(mainHeaderText,'Date','End')
date = sliceString(businessDate,' ')
print(date)

#should grab count of the table, including total ROWS
lastID = table.tfoot.find('tr')['id']

#grabs count of the table without total rows
dataCount = table.findAll(True, {'class':['RowStyleData', 'RowStyleDataEven']})



#find first header row/column names
rows = table.find(class_="RowStyleHead")
elements = rows.select('.CellStyle')


for count in range(len(dataCount)):
    dataCell = dict()
    for index in range(len(elements)):
        try:
            dataCell[elements[index].text.strip()] = dataCount[count].select('.CellStyle')[index]['dval']
        except:
            dataCell[elements[index].text.strip()] = dataCount[count].select('.CellStyle')[index].text.strip()
    data.append(dataCell)

#These are some checks to have (there are a lot to check, but these are the crucial ones):

#this one should show the last row:
#print(dataCell)

#these should match:
#print(len(dataCount))
#print(len(data))
#end

#proper sibling navigation:
#print(dataCount[0].select('.CellStyle')[0].next_sibling.next_sibling['dval'])

f.close()

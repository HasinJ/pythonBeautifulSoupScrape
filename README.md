pythonWebscrapeRadiant

BeautifulSoup Doc:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

Files:

Report.xls - xls file with data to parse

courseProj.py - allsides.com example - SERVES AS THE BEST EXPLANATION TO MOST THE FUNDAMENTALS IN MAIN.PY

output - html example of xls file and webpage

{date}Output.json - outputs the data list

RDSconfig.py - should make its own __pycache__ when DB connects properly, has DB credentials

HTML analysis:
- differentiated with CSS
- differentiated with class
- 'Data' and 'DataEven' are the same but different colors
- 'break' breaks down with no values, but 'breaktotal' breaks the opposite way AND has values
- grabbing last child from 'tbody' shows us the amount of loops to go through

Python MySQLdb download:
https://stackoverflow.com/questions/51062920/pip-install-mysqlclient-error/58931018#58931018

Notes:
- date and PC number needs to be associated with each row (data frame-wise)
- not using object oriented/more than a couple of functions
- delete .json and .csv file to check if script works
- anything and everything is either on w3schools and the BeautifulSoup doc
- to test, maybe a "whitespace" checker
- to test, maybe something with the fact that PC numbers are getting scraped once the HTML report is being recorded

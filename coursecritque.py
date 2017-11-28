####################################################################
# CREATOR: DS GROUP 13
# DATE: 11/27/17
# DESCRIPTION: A PYTHON WEBSCRAPER UTILIZING THE BeautifulSoup
# LIBRARY TO SCRAPE AND FORMAT HTML FOR DATA TO BE USED IN MACHINE
# LEARNING APPLICATIONS.
####################################################################

# LIBRARIES: requests, bs4
import requests
from bs4 import BeautifulSoup

# DEFINING BROWSER HEADER SPECIFIC TO GOOGLE CHROME
headers = {'User-Agent': 'Chrome/62.0.3202.94'}

# TARGET URL TO SCRAPE
url = 'https://critique.gatech.edu/course.php?id=MATH1512'

# CHECKING TO SEE IF CONNECTION HAS BEEN ESTABLISHED
# SUCCESSFUL CONNECTION OCCURS WHEN STATUS.CODE == 200
website_connection = requests.get(url, headers = headers)
if website_connection.status_code == 200:
    print('--------------------------------------------------------------')
    print('           Connection established successfully.')
    print('--------------------------------------------------------------\n')

else:
    print('--------------------------------------------------------------')
    print('Error: Bad Connection. Please check internet connection or URL')
    print('--------------------------------------------------------------')

# PARSING HTML INFORMATION FROM WEB PAGE AND FINDING
# DESIRED TABLE
website_data = BeautifulSoup(website_connection.content, 'html.parser')
website_table = website_data.find_all('table')

# LOOKS FOR THE SECOND TABLE NAMELY GPA TABLE
website_table = website_table[1];
counter = 0;
count = 0;

for row in website_table.find_all('tr'):
    for cell in row.find_all('th'):
        print(cell.text, end = ' ')
        counter = counter + 1
        if (counter%9 == 0):
            print()

    for cell in row.find_all('td'):
        print(cell.text, end = ' ')
        count = count + 1
        if (count%9 == 0):
            print()

with open ('Math_1512.txt', 'w') as data:
    for row in website_table.find_all('tr'):
        for cell in row.find_all('th'):
            data.write(cell.text)
            data.write(' ')
            counter = counter + 1
            if (counter%9 == 0):
                data.write('\n')

        for cell in row.find_all('td'):
            data.write(cell.text)
            data.write(' ')
            count = count + 1
            if (count%9 == 0):
                data.write('\n')

# Tutorial followed: 
# https://www.youtube.com/watch?v=XVv6mJpFOb0

# In terminal, pip install beautifulsoup4
# In terminal, pip install lxml

from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    # print(content)
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)

    tags = soup.find("h5")
    # print(tags)

    tags = soup.find_all("h5")
    # print (tags)
    courses_html_tags = tags

    for course in courses_html_tags:
        #print(course.text)
import requests
import os.path
import filecmp
from bs4 import BeautifulSoup

# only grabs the text of the article, since other data can be arbitrary
def get():
    url = 'https://uconn.edu/public-notification/coronavirus/'
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, features="lxml")

    output = soup.body.find('div', attrs={'class':'fl-rich-text'}).text
    
    if os.path.isfile('stored.txt'):
        pass
    else:
        file = open('stored.txt', 'w')
        file.write(output)
        file.close()

    file = open('new.txt', 'w')
    file.write(output)
    file.close()

def verify():
    return filecmp.cmp('stored.txt', 'new.txt')

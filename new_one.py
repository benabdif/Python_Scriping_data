import requests
from bs4 import BeautifulSoup
import csv

# date = input('Enter data: ')
page = requests.get('https://www.yallakora.com/match-center/?date=5/29/2023#days')

def mysorce(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    champioships = soup.find_all("div", {'class':'matchCard'})

    def get_match_info(champioships):
        champioships_title = champioships.contents[1].find('h2').text.strip()
        print(champioships_title)
    get_match_info(champioships[0])
    
mysorce(page)







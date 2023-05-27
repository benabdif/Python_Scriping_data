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
        


    
    
# new_python scriping 

page_analys = requests.get('https://www.yallakora.com/europa-league/2790/stats/#Tour-Menu')

def myana(page_analys):
    src = page_analys.content
    soup = BeautifulSoup(src, 'lxml')
    myanaltys_is = soup.find_all("section", {'class':'stats'})
    myanaltys_is_1 = soup.find_all("div", {'class':'scorer'})
    
    
    
    
    def get_myanals_of(myanaltys_is,myanaltys_is_1):
        box = []
        get_info = myanaltys_is.contents[1].find('h2').text.strip()
        print(get_info)       
        golas_title = myanaltys_is_1.contents[1].find('h3').text.strip()
        # nam = myanaltys_is_1.contents[3].find('li').find_all('div',{'class':'name'})
        nam = myanaltys_is_1.contents[3].find('li').find_all('a')
        
    
        
        # go = myanaltys_is_1.contents[3].find_all('a')[10].text.strip()
        # print('=' * 40)
        # print (go)
        
       
        
     
    get_myanals_of(myanaltys_is[0], myanaltys_is_1[0])
    
            
myana(page_analys)





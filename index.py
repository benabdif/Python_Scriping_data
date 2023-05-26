import os
import platform
import requests
from bs4 import BeautifulSoup
import csv

date = input('Enter numner of date: (DD/MM/YY)')

page = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}#days")


def myso(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    box = []
    new_find = soup.find_all("div", {'class':'matchCard'})
    print(new_find)
    

myso(page)



        



        
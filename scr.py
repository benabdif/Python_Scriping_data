import requests
from bs4 import BeautifulSoup
import csv


# link of code
page_analys = requests.get('https://www.yallakora.com/europa-league/2790/stats/#Tour-Menu')

def myana(page_analys):
    src = page_analys.content
    soup = BeautifulSoup(src, 'lxml')
    myanaltys_is_1 = soup.find_all("div", {'class':'scorer'})
    myanaltys_is = soup.find_all("section", {'class':'stats'})
   
    
    last_info = []
    
    def get_all_info(myanaltys_is_1,myanaltys_is):
        
        all_goals_name = myanaltys_is_1.contents[3].find_all('li')
        title_goals = myanaltys_is.contents[1].find('h2').text.strip()


        num_of_goals = len(all_goals_name)
        num_gols_in = []
        
        for x in range(num_of_goals):
            name_of_players = all_goals_name[x].find('div', {'class':'name'}).find('p').text.strip()
            name_of_cluop = all_goals_name[x].find('div', {'class':'name'}).find('a').text.strip()
            number_goals_me = all_goals_name[x].find('div', {'class':'num'}).find('p').text.strip()
            num_gols_in.append(number_goals_me)
            
            last_info.append({'Name of Players': name_of_cluop, 'Clup': name_of_players, 'Golse': number_goals_me})
        
      
            kesy = last_info[x].values()
           
            
            
        # get the totals of goals
        int_of_number = [int(num) for num in num_gols_in]
        total_of_goals = sum(int_of_number)
        
        
               
    get_all_info(myanaltys_is_1[0], myanaltys_is[0])
    
    
    keys = last_info[0].keys()
    
    with open('/Users/benabdi/info.csv', 'w') as outpute_file:
        myfines_info = csv.DictWriter(outpute_file, keys)
        myfines_info.writeheader()
        myfines_info.writerows(last_info)
        
        print('file created')

   
myana(page_analys)



    

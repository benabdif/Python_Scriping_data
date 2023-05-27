import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from openpyxl import workbook, load_workbook

# web = load_workbook('')


mydata = {
    'cars': ['BMW', 'marced', 'shaver'],
    'name': ['Fadhel', 'Mohammed', 'Ali']
}

new_1 = pd.DataFrame(mydata)
# print(new_1)

number = ['A','B','C','E']

x = pd.Series(number)
# print(x[0])


new_1 = pd.DataFrame(
    
    {'cars': ['BMW', 'marced', 'shaver','d'],
    'name': ['Fadhel', 'Ali', 'Mohammed','v'],
    'product': ['Allpe', 'Orainge', 'grape','s'],
    'friend': ['Sam', 'Kora', 'Salem','r'],
    'calss': ['AB222', 'BA321', 'Salem32','a'],
    },index=pd.RangeIndex(start=1, stop=5)
    )

# print(new_1[['name','cars']])

num_1 = {
    'day1': 222,
    'day2': 322,
    'day3': 522,
}

myav = pd.Series(num_1)
# print(myav)


class fadhel:
    def __init__(self, num1, num2):
        self.num_1 = num1
        self.num_2 = num2
    
    def myinfo(self):
        d = self.num_1 * self.num_2
        return d
    
    def mylis(self):
        list_of = [1,3,5,2]
        for x in list_of:
            print(x * 12 + self.myinfo())     
    
# x = fadhel(100,100)


# print(x.myinfo())
# x.mylis()



# sns.distplot([9, 1, 2, 3, 4, 5])

# plt.show()

lis_num = [1,2,3,4,87,2]

print(min(lis_num))

def myfun(lis_num):
    num_1 = 0
    for x in lis_num:
        if x > num_1:
            num_1 = x
    return num_1

# x = myfun(lis_num)

# print(x)
        
lis_num = [1,1,1,1,2,1,1,1,1]

total_num = sum(lis_num)
num_have = len(lis_num) // 2

avarge = total_num/num_have

print(f'this is {num_have}')

from openpyxl import Workbook, load_workbook


# create new excel


wb = Workbook()

ws = wb.active

wb.save('myexcel.xlsx')





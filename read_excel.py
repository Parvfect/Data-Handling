# Reading an excel file using Python
import xlrd
 
# Give the location of the file
loc = ("lab.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0, 2))

fil = open('db6', 'w')
fil.write("mass\n")
fil.write("t x y\n")

for i in range(760):

    fil.write(str(sheet.cell_value(i,61))+","+str(sheet.cell_value(i,62))+","+str(sheet.cell_value(i,63))+"\n")
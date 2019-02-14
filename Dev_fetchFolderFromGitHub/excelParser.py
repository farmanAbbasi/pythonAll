# Reading an excel file using Python 
import xlrd 

# Give the location of the file 
loc = ("sqlAccessor.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)


# For row 0 and column 0
#print(sheet.cell_value(0, 0))

# For number of rows and columns
print(sheet.nrows,'rows')
print(sheet.ncols,'columns')

'''
#extracting all column names
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i),end=" ")
print(end='')
#extracting first column
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))

#print a particular row
print(sheet.row_values(2))
'''

#printing all row values
for i in range(sheet.nrows):
    #way 1 of printing all rows
    #print(sheet.row_values(i))

    
    #way 2 of printing whole rows
    for j in range(sheet.ncols):
        print(sheet.cell_value(i, j), end=',')
    print()
    
    #the above for loop for two columns is same as below    
    #print(sheet.cell_value(i, 0))
    #print(sheet.cell_value(i, 1))
    

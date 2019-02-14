# Reading an excel file using Python 
import xlrd 

# Give the location of the file 
loc = ("sqlAccessor.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

#printing all row values
for i in range(sheet.nrows):
        #if id is in first column use 0 in cols place
        if sheet.cell_value(i,0)==2016:

            #to print the all column name
            for z in range(sheet.ncols):
                print(sheet.cell_value(0,z),end=',')
            print()   
                       
            
            for j in range(sheet.ncols):
                print(sheet.cell_value(i, j), end=',')
            print() 
           
        
  

    
   
       
   

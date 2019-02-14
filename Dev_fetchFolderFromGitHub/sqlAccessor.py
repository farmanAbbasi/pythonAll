import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=HSC-HVSLXP1;"
                      "Database=Movies;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM tblActor')

'''
cnxn = pyodbc.connect(< db details here >)
cursor = cnxn.cursor()
script = """
SELECT * FROM my_table
"""

'''

for row in cursor:
    print('row = %r' % (row,))
    


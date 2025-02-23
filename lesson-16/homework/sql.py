import pyodbc
connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=MSL-DESKTOP;'
                               'Database=TSQL2012;'
                               'trusted_Connection=yes;'
                               )
print('Connected to database')

cursor=connection.cursor()
#use_qy='use TSQL2012'

#cursor.execute(use_qy)

select_qy='select*from  TSQL2012.[Sales].[OrderDetails]'
result=cursor.execute(select_qy)
data=result.fetchall()

connection.commit()


with open('orders.csv','w') as f:
    columns=[i[0] for i in result.description]
    columns=','.join(columns)+'\n'
    f.write(columns)
    for obj in data:
        values=','.join(map(str,obj))+'\n'
        f.write(values)
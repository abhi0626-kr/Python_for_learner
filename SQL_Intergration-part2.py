# Part-2 (Update the data in the table)# Python (Exceute the Query)

# MySQL With Python is the Base of Data Engineering,Data Pipeline, Backend database connection in Softwares

# pip install mysql.connector
    
import mysql.connector as msc

# MYSQL -> 
# C- Create Table, database, views 
# R-> Select * from 
# U -> Update Table
# D -> Delte Rows, Drop Tables  Truncate


connection = msc.connect(
    host="localhost",
    user="root",
    password="@Abhishek2006",
    auth_plugin='mysql_native_password'
)

if connection.is_connected():
    print("Connection Established Successfully")

cur = connection.cursor()

cur.execute('Select * from Stud_Data')
cur.fetchall()
cur.execute('Truncate Stud_Data')

file = open("students.csv",'r')

content = file.readlines()

file.close()
InserQuery ='insert into stud_data values(%s, %s, %s, %s, %s , %s)'

from datetime import datetime

start = datetime.now()
print(start)

content.pop(0)

for i in content:
    Val = i.split(',')
    Val[5] = Val[5].replace('\n','')
    Val = tuple(Val)
    
    cur.execute(InserQuery, Val)
    connection.commit()
    
end = datetime.now()
print(end,'\n')
print("Total Duration:-",end - start)


# ------------------------------------------------------------------
import pandas as pd

df= pd.read_csv("students.csv")
cur.execute("Truncate Stud_Data")

start = datetime.now()
print(start)

for idx, val in df.iterrows():
    Values =(val['StuId'],val['StudentName'], val['Course'],val['Fees'],val['Location'],val['EmailId'])
    cur.execute(InserQuery, Values)
    connection.commit()
    
end = datetime.now()
print(end,'\n')
print("Total Duration:-",end - start)
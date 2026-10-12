# Python (Exceute the Query)

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

query = connection.cursor()

query.execute('Show Databases')
output = query.fetchall()
print(output)
DatabaseList = output

DBName = "Python_9_AM"
# To create a database.
if (DBName.lower(),) in DatabaseList:
    print("Database already Exists")
else:
    print("Database not Exists")
    DB_Creation = f'Create database {DBName};'
    query.execute(DB_Creation)
# Create a table to store account details.
Table_Creation_Query = """
CREATE TABLE IF NOT EXISTS Python_9_AM.AccountDetails(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)"""
query.execute(Table_Creation_Query)
print("Table Created Successfully")

# Insert data into the table.
Insert_Query = """
INSERT INTO Python_9_AM.AccountDetails(id, name, email) VALUES (%s, %s, %s)
"""
values = (1, "Max Verstappen", "max.verstappen@F1.com")

query.execute(Insert_Query, values)
connection.commit()
print("Inserting data into the table...")

query.execute("SELECT * FROM Python_9_AM.AccountDetails")
output = query.fetchall()
print(output)

# Adding a new column to the table.
Add_Column_Query = """
ALTER TABLE Python_9_AM.AccountDetails ADD COLUMN age INT
"""
query.execute(Add_Column_Query)
print("Column Added Successfully")

Insert_Query = """ 
INSERT INTO Python_9_AM.AccountDetails(id, name, email, age) VALUES (%s, %s, %s, %s)
"""




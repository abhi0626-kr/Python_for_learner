# It just for Testing purpose.............# Insert data into the table.

import mysql.connector as msc


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

# To create a database.
query.execute("CREATE DATABASE IF NOT EXISTS Python_9_AM")
# Use the database.
query.execute("USE Python_9_AM")
print("Database Used Successfully")

# Create a table to store account details.
Table_Creation_Query = """
CREATE TABLE IF NOT EXISTS Python_9_AM.AccountDetails(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)"""
query.execute(Table_Creation_Query)
print("Table Created Successfully")

# ----------------------------------------------------------------


Insert_Query = """
INSERT INTO Python_9_AM.AccountDetails(id, name, email) VALUES (%s, %s, %s)
"""
values = (1, "Max Verstappen", "max.verstappen@F1.com")

query.execute(Insert_Query, values)
connection.commit()
print("Inserting data into the table...")
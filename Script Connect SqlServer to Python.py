
# import python driver (open database connectivity)
# first download the driver then import

import pyodbc

#todo)   Connecting From Sql Server To Python
#todo)   Pyodbc Driver using Connecting (SQL SERVER NATIVE CLIENT 11.0)

# connecting Script todo) Script ↴
connection=pyodbc.connect(
    "Driver= {SQL Server Native Client 11.0};"
    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
    "Database=Hotel;"
    "Trusted_Connection=yes;"
)

# Terminology

# 1. Driver keyword: Enter The  driver name to connect sql-server and python
# Driver name is (SQL SERVER NATIVE CLIENT 11.0)

# 2. Server Keyword: Enter  The server name of your pc to know ur server
# open SSMS (Sql server management studio)
# then in Object explorer Search Your Server Name

# 3: Database keyword: Enter the database name that you want to access or connect
# your application

# Trusted_Connection Keyword: Is The Permissions That The User Can Access Your
# Database If You Have Sql-Server Authentication
# Enter The Authentic Username & Password if You Don't
# The Trusted Pass yes

# todo) Testing The Database NOTE: Change The Database I Used into your Database

#Selecting Making Cursor
cursor=connection.cursor()
# execute
cursor.execute('SELECT *FROM <Your_Table_Name>')
connection.close()

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "debian-sys-maint",
    password = "kaJamZZifVt8CBoo",
    database = "Lab3db"
)

mycursor = mydb.cursor()

#Creating the Table for the Database

mycursor.execute("CREATE TABLE Question2 (Fname VARCHAR(255), Lname VARCHAR(255),  Age INT)")

#Showing the Tables for the Databasee

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)



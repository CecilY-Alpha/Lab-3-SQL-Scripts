import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "debian-sys-maint",
    password = "kaJamZZifVt8CBoo"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE DATABASE Lab3db")
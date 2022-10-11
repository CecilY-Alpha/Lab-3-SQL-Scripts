import mysql.connector

import pyodbc, csv

mydb = mysql.connector.connect(
    host = "localhost",
    user= "debian-sys-maint",
    password = "kaJamZZifVt8CBoo",
    database = "Lab3db"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM Question2"

mycursor.execute(sql)

res = mycursor.fetchall()

with open("Lab3-Question2-Exported.csv","w") as file:
    for row in res:
        csv.writer(file).writerow(row)


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user= "debian-sys-maint",
    password = "kaJamZZifVt8CBoo",
    database = "Lab3db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Question2 (Fname, Lname, Age) VALUES (%s, %s, %s)"

val = [
    ("James", "Johnson", 32),
    ("Phillip", "King", 25),
    ("John", "Michaels", 45)
]

mycursor.executemany(sql, val)


mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM Question2")

myresult = mycursor.fetchall()

for x in myresult:
    print (x)

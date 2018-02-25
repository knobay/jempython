import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()

cursor.execute("SELECT * FROM CUSTOMERS")

user1 = cursor.fetchone()
print(user1[0])

all_rows = cursor.fetchall()
for row in all_rows:
    print(row) #see if you can print out only the title either by row[?] or amending the SQL
db.close()




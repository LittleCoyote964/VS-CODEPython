import mysql.connector as mc

db = mc.connect(
    host = "35.238.120.192", # copy and paste from the google cloud console.
    user = "root",
    passwd = "1qaz2wsx!QAZ@WSX",
    database = "carmax"
)

print(db)

cursor = db.cursor()

sql = "insert into cars values(%s, %s, %s, %s, %s, %s, %s)"
values = [('KUK32', "Ford", "F250", 2024, 23, 65000, "silver"), 
          ("USE44", "Toyota", "Rav4", 2023, 55, 25000, "blue"),
          ("BCV49", "Honda", "Civic", 2023, 10435, 23150, "red"),
          ("HTP40", "Toyota", "Corolla", 2020, 50654, 17000, "black"),
          ("KLPT0", "Honda", "Ridgeline", 2024, 4, 31650, "red")]

query = "DELETE FROM cars WHERE model in (F250, Rav4, civic, Corolla, Ridgeline)"
cursor.execute(query)

cursor.executemany(sql, values)



db.commit()

print(cursor.rowcount, "records inserted")
cursor.execute("select * from cars")

records = cursor.fetchall()

for record in records:
    print(record)
import mysql.connector
mydb = mysql.connector.connect( #establishing connection
    host="localhost",
    user="root",
    password="8179"
)
cur = mydb.cursor() #creates new cursor object for executing SQL statements
cur.execute("CREATE DATABASE mydb") #creating new database

cur.execute("SHOW DATABASES") # executes sql query to check all databases
print("Printing all databases")
for x in cur:
    print(x) #prints all databases

myconn = mysql.connector.connect( #establishing connection
    host="localhost",
    user="root",
    password="8179",
    database="mydb"
)
mycur = myconn.cursor()
#creating a new table in database 
mycur.execute("CREATE TABLE students (sname VARCHAR(255), domain VARCHAR(255))")
mycur.execute("SHOW TABLES")
print("Printing all tables in mydb")
for x in mycur:
    print(x)

#creating primary key in students table using alter
mycur.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#inserting record
sql = "INSERT INTO students (sname,domain) VALUES (%s, %s)"
val = ("Khushboo","Data Science")
mycur.execute(sql,val)

myconn.commit() #commits the transactions in table
print("1 record inserted, ID: ", mycur.lastrowid)

sql ="INSERT INTO students (sname,domain) VALUES (%s, %s)"
val = [
    ('Priyanka','Graphic Designing'),
    ('Ishika','Cyber Security'),
]
mycur.executemany(sql, val)
mydb.commit()
print(mycur.rowcount, "was inserted.")

mycur.execute("SELECT * FROM students")
res = mycur.fetchall()

for x in res:
    print(x)

#select where
sql = "SELECT * FROM students WHERE sname='Khushboo'"
mycur.execute(sql)
myres = mycur.fetchall()
for x in myres:
    print(x)

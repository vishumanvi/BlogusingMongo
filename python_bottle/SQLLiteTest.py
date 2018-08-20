import sqlite3

connection = sqlite3.connect("test_database.db")

c = connection.cursor()

#c.execute("create table employee (empNo INT, empName TEXT, empDesignation TEXT)")

c.execute("insert into employee values (100,'vishu','project manager')")

c.execute(("select * from employee"))

for row in c.fetchall():
	print(row)

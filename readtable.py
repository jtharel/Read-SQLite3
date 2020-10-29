import sqlite3

conn = sqlite3.connect('DBName.sqlite')

c = conn.cursor()
d = conn.cursor()

sql = "SELECT name FROM sqlite_master WHERE type='table';"
for row in c.execute(sql):
	print("Table: " + str(row)[3:-3])
	table_name = str(row)[3:-3]

	newsql = "SELECT * FROM " + table_name + ";"
	print("SQL Statement = " + newsql)
	for row in d.execute(newsql):
		print(str(row))
	conn.commit()
	print("   ")
	print("**********")
	print("   ")

		
conn.commit()


conn.close()


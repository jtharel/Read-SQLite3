import sqlite3
import sys

def Help():
	print("Usage:")
	print("  python ./readtable.py [tablename]")
	print(" ")
	print("  python ./readtable.py users")


def dumptables(dbname):

	conn = sqlite3.connect(dbname)

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


if len(sys.argv) == 1:
	Help()
	sys.exit
else:
	dbname = sys.argv[1]
	dumptables(dbname)


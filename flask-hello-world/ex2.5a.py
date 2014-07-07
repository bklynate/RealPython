import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	c.execute("UPDATE population SET population = 2500000 where city='Brooklyn' ")

	c.execute("DELETE FROM population WHERE city='Boston'")
	
	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]
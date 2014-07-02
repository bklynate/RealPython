import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	cities = [
		('Phoenix', 'AZ', 1500000),
		('Houston', 'TX', 2100000),
		('Brooklyn', 'NY', 2400000)
	]

	c.executemany('INSERT INTO population VALUES(?,?,?)', cities)
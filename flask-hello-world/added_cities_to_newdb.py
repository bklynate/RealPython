import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	cities = [
		('Brooklyn','NY', 2500000),
		('Queens','NY', 2200000),
		('Staten Island', 'NY', 420000),
		('Bronx', 'NY', 1500000)
		]

	c.executemany("INSERT INTO population VALUES(?,?,?)", cities)

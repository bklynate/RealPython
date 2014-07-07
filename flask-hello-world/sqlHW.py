import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	cars = [
		('Focus', 'Ford', 8),
		('F-150', 'Ford', 3),
		('Explorer', 'Ford', 4),
		('M3', 'BMW', 2),
		('Evolution MR', 'Mitsubishi', 1)
		]
	
	#c.executemany("INSERT INTO inventory VALUES(?,?,?)",cars)

	#c.execute("UPDATE inventory SET quantity= 4 WHERE Model= 'BMW'")

	c.execute("SELECT * from inventory WHERE Model='Ford'")

	r = c.fetchall()

	for data in r:
		print data[0]


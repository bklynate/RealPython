import sqlite3 
 
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	c.execute("""INSERT INTO population VALUES("Chicago", "IL", 2700000)""")
	c.execute("""INSERT INTO population VALUES("Boston", "MA", 600000)""")

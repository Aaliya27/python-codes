import sqlite3

con=sqlite3.connect("books_db.sqlite3")
cur=con.cursor()

try:
	cur.execute("CREATE TABLE booklist(id INTEGER PRIMARY KEY,name TEXT,rating INTEGER)")
except sqlite3.OperationalError:
	print("Table Already exists...")

cur.execute("""INSERT INTO booklist VALUES(1,"book1",4)""")
cur.execute("""INSERT INTO booklist VALUES(2,"book2",3)""")
cur.execute("""INSERT INTO booklist VALUES(3,"book3",5)""")

con.commit()
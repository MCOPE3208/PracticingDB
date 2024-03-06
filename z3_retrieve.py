import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE  type='table';")
tables = cr.fetchall()
print(tables)

#pulls data from table movies
cr.execute("SELECT * FROM movies")
print(cr.fetchall())
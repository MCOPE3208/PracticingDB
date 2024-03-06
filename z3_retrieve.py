import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

#uses the database file specified with cr
#pulls the list of all the tables in that database
cr.execute("SELECT name FROM sqlite_master WHERE  type='table';")
tables = cr.fetchall()
print(tables)

#this will pull all the column from that table
cr.execute("PRAGMA table_info({});".format("movies"))
columns = cr.fetchall()

if columns:
    column_names = [column[1] for column in columns]
    print(f"Column Names: {', '.join(column_names)}")
else:
    print(f"No columns found in the table {"movies"}.")

#pulls data from table movies
cr.execute("SELECT * FROM movies")
print(cr.fetchall())
import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

def add_movie(title,director,year,genre):
    cr.execute("""
        INSERT INTO movies(title,director,year,genre) 
        VALUES (?,?,?,?)""",(title,director,year,genre))
    conn.commit()
    print("Movie added :)")

#template fr adding new movies:
#add_movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
#do not run the above inception has already been added
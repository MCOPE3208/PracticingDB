import sqlite3
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

def add_movie(title,director,year,genre):
    cr.execute("""
        INSERT INTO movies(title,director,year,genre) 
        VALUES (?,?,?,?)""",(title,director,year,genre))
    conn.commit()
    print("Movie added :)")

#add_movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
add_movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
add_movie("The Dark Knight", "Christopher Nolan", 2008, "Action")
add_movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime")
add_movie("Forrest Gump", "Robert Zemeckis", 1994, "Drama")
add_movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999, "Action")
add_movie("Titanic", "James Cameron", 1997, "Romance")
add_movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
add_movie("Avatar", "James Cameron", 2009, "Action")
add_movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi")
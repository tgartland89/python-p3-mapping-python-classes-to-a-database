from config import CONN, CURSOR

class Song:
  
    def __init__ (self, name, album):
        self.name = name
        self.album = album

# adding the init with self, name, album will clear this FAIL:
# FAILED Class Song in song.py takes a name and album as __init__ arguments and saves them as instance attributes. 
# - TypeError: Song() takes no arguments

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

# adding the above @classmethod with a def for create_table that passes class (cls) and uses SQL to create a table with PRIMARY KEY, name, and album
# FAILED Class Song in song.py has classmethod "create_table()" that creates a table "songs" if table does not exist. 
# - AttributeError: type object 'Song' has no attribute 'create_table'

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

# added the following def save passing self and using sql to INSERT INTO songs (name, album) and VALUES (?, ?)
# FAILED Class Song in song.py has instancemethod "save()" that saves a song to music.db. 
# - AttributeError: 'Song' object has no attribute 'save'


    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    
    # Adding this @classmethod of def create passing cls, name, and album clears the final error: 
    # song = Song(name, ablum)
    # song.save()
    # return song 
    # FAILED Class Song in song.py has classmethod "create()" that creates a Song instance, saves it, and returns it.
    #  - AttributeError: type object 'Song' has no attribute 'create'

# NOTES for Me: 

# this code is creating a class to represent songs. 
# It has methods to create a table in a database, save a song to the database, and create new songs.

# This code is defining a class called "Song" that represents a song in a music library. The class has several methods to interact with a database.

# The code starts by importing the "CONN" and "CURSOR" objects from a module called "config". 
# These objects are used to establish a connection to a database and execute SQL queries.

# The class "Song" has an initializer method called "init" which is called when a new instance of the class is created. 
# It takes two parameters: "name" and "album". Inside this method, some attributes of the object are set, 
# such as "id" (initialized as None), "name", and "album".

# Next, there is a class method called "create_table". 
# This method is used to create a table in the database if it doesn't already exist. 
# It executes an SQL query that creates a table named "songs" with three columns: "id" (an integer primary key), 
# "name" (a text column), and "album" (a text column).

# The class also has another method called "save". 
# This method is used to save the current song object to the database. 
# It executes an SQL query that inserts the values of "name" and "album" into the "songs" table. 
# After executing the query, the changes are committed to the database using the "CONN.commit()" statement. 
# Then, it retrieves the ID of the newly inserted row using the "last_insert_rowid()" function in SQL and 
# assigns it to the "id" attribute of the current song object.

# Finally, there is another class method called "create" which is a convenient way to create a new song object, 
# save it to the database, and return the created song object.

# from config import CONN, CURSOR

# class Song:

#     def __init__(self, name, album):
#         self.id = None
#         self.name = name
#         self.album = album

#     @classmethod
#     def create_table(cls):
#         sql = """
#             CREATE TABLE IF NOT EXISTS songs (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 album TEXT
#             )
#         """

#         CURSOR.execute(sql)

#     def save(self):
#         sql = """
#             INSERT INTO songs (name, album)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.album))
#         CONN.commit()

#         self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

#     @classmethod
#     def create(cls, name, album):
#         song = Song(name, album)
#         song.save()
#         return song
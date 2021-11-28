import dbconfig as conf
import mysql.connector
import queries

class Moviedao:
    '''
        class for interacting with movie database objects,
        initializes using connection to mysql server with details stored in dbconfig conf variable
        function:
            get_all_movies() - queries database movies table and returns all column names and rows
            add_movie() - inserts new row to movies table, if ID doesn't already exist, returns rows added
            update_movie() - updates an existing row in movies table, returns rows affected
            __repr__ - prints summary of the class and it's connection string except password
    '''
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=conf.mysql['host'],
            user=conf.mysql['user'],
            password=conf.mysql['password'],
            database=conf.mysql['database']
        )
        self.cursor = self.conn.cursor()

    #Gets all movies from movies table
    def get_all_movies(self):
        self.cursor.execute(queries.select_all_movie)
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]
        return column_names, results

    #Adds single movie to movies table
    def add_movie(self, values):
        self.cursor.execute(queries.insert_movie, values)
        self.conn.commit()
        rowcount = self.cursor.rowcount
        return rowcount

    #Update existing movie in Movies table
    def update_movie(self, values):
        try:
            self.cursor.execute(queries.update_movie, values)
            self.conn.commit() #save result back to database
            rowcount = self.cursor.rowcount
            return rowcount
        except mysql.connector.Error as e:
            print(f"Hit the follow mysql error: {e}")
            print(self.cursor.statement)
            return str(e)
        except Exception as e:
            print(f"Hit some non-specific error: {e}")
            return str(e)

    #__repr__ displays connection information without exposing password
    def __repr__(self):
        repr_str = "Database access object for querying, inserting, updating and deleting tables relating to movies"
        repr_str += f"\nConnecting to Host: {conf.mysql['host']}\nWith user: {conf.mysql['user']}\n To Database: {conf.mysql['database']}"
        return repr_str

#movie_dao = Moviedao()
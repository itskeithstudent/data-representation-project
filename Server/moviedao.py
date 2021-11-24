import dbconfig as conf
import mysql.connector
import queries

class Moviedao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=conf.mysql['host'],
            user=conf.mysql['user'],
            password=conf.mysql['password'],
            database=conf.mysql['database']
        )
        self.cursor = self.conn.cursor()

    def get_all_movies(self):
        self.cursor.execute(queries.select_all_movie)
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]
        return column_names, results

    def add_movie(self, values):
        self.cursor.execute(queries.insert_movie, values)
        rowcount = self.cursor.rowcount
        return rowcount

    def update_movie(self, values):
        try:
            self.cursor.execute(queries.update_movie, values)
            rowcount = self.cursor.rowcount
            return rowcount
        except mysql.connector.Error as e:
            print("Hit some issue")
            print(e)
            print(self.cursor.statement)
            return str(e)
        except Exception as e:
            print("Hit some other weirder issue")
            print(e)
            return str(e)

    def __repr__(self):
        return "Database access object for querying, inserting, updating and deleting tables relating to movies"

#movie_dao = Moviedao()
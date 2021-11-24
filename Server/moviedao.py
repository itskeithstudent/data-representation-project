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

    def __repr__(self):
        return "Database access object for querying, inserting, updating and deleting tables relating to movies"

#movie_dao = Moviedao()
import dbconfig as conf
import mysql.connector

class Moviedao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=conf.mysql['host'],
            user=conf.mysql['user'],
            password=conf.mysql['password'],
            database=conf.mysql['database']
        )
        self.cursor = self.conn.cursor()

    def __repr__(self):
        return "Database access object for querying, inserting, updating and deleting tables relating to movies"

#movie_dao = Moviedao()
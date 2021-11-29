import dbconfig as conf
import mysql.connector
import queries

class Moviedao:
    '''
        class for interacting with movie database objects,
        initializes using connection to mysql server with details stored in dbconfig conf variable
        function:
            __initialize_connect_db() - function immediately called by __init__ to set up to database with pooling (name mangled as should only be called within class)
            get_connect_db - function called in each, function for interacting with database, leverages connection pool, returns connection object
            get_all_movies() - queries database movies table and returns all column names and rows
            add_movie() - inserts new row to movies table, if ID doesn't already exist, returns rows added
            update_movie() - updates an existing row in movies table, returns rows affected
            __repr__ - prints summary of the class and it's connection string except password
    '''

    def __initialize_connect_db(self):
        conn = mysql.connector.connect(
            host=conf.mysql['host'],
            user=conf.mysql['user'],
            password=conf.mysql['password'],
            database=conf.mysql['database'],
            pool_name=conf.mysql['default_pool_name'],
            pool_size=conf.mysql['default_pool_size']
        )
        return conn

    def get_connect_db(self):
        conn = mysql.connector.connect(
            pool_name=conf.mysql['default_pool_name'],
            pool_size=conf.mysql['default_pool_size']
        )
        return conn

    def __init__(self):
        #create connection and immediately close, connection pool will re-reference this later
        conn = self.__initialize_connect_db()
        conn.close()

    #Gets all movies from movies table
    def get_all_movies(self):
        conn = self.get_connect_db()
        cursor = conn.cursor()
        cursor.execute(queries.select_all_movie)
        results = cursor.fetchall()
        #print(cursor.statement)
        column_names = [i[0] for i in cursor.description]
        row_results = []
        for row in results:
            row_dict = dict(zip(column_names,row))
            row_results.append(row_dict)
        conn.close()
        #print(row_results)
        return row_results

    #Adds single movie to movies table
    def add_movie(self, values):
        conn = self.get_connect_db()
        cursor = conn.cursor()

        cursor.execute(queries.insert_movie, values)
        #print(cursor.statement)
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount

    #Update existing movie in Movies table
    def update_movie(self, values):
        try:
            conn = self.get_connect_db()
            cursor = conn.cursor()
            cursor.execute(queries.update_movie, values)
            conn.commit() #save result back to database
            rowcount = cursor.rowcount
            #print(cursor.statement)
            conn.close()
            return rowcount
        except mysql.connector.Error as e:
            print(f"Hit the follow mysql error: {e}")
            print(cursor.statement)
            conn.close()
            return str(e)
        except Exception as e:
            conn.close()
            print(f"Hit some non-specific error: {e}")
            return str(e)

    #Update existing movie in Movies table
    def delete_movie(self, movie_id):
        try:
            conn = self.get_connect_db()
            cursor = conn.cursor()
            cursor.execute(queries.delete_movie, [movie_id])
            conn.commit() #save result back to database
            rowcount = cursor.rowcount
            conn.close()
            return rowcount
        except mysql.connector.Error as e:
            print(f"Hit the follow mysql error: {e}")
            print(cursor.statement)
            conn.close()
            return str(e)
        except Exception as e:
            conn.close()
            print(f"Hit some non-specific error: {e}")
            return str(e)

    #__repr__ displays connection information without exposing password
    def __repr__(self):
        repr_str = "Database access object for querying, inserting, updating and deleting tables relating to movies"
        repr_str += f"\nConnecting to Host: {conf.mysql['host']}\nWith user: {conf.mysql['user']}\n To Database: {conf.mysql['database']}"
        return repr_str

#movie_dao = Moviedao()
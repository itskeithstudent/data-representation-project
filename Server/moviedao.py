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
        with self.get_connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(queries.select_all_movie_plus_rating)
            results = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            row_results = []
            for row in results:
                row_dict = dict(zip(column_names,row))
                row_results.append(row_dict)
            return row_results

    #Adds single movie to movies table
    def add_movie(self, values):
        with self.get_connect_db() as conn:
            try:
                cursor = conn.cursor()

                cursor.execute(queries.insert_movie, values)
                #print(cursor.statement)
                conn.commit()
                rowcount = cursor.rowcount
                return rowcount
            except mysql.connector.IntegrityError as e:
                print("Hit an integrity error, meaning a movieID was trying to be used more than once")
                print(f"Detailed Error Message:\n{e}")
                return "IntegrityError"
            except mysql.connector.Error as e:
                print(f"Hit the follow mysql error: {e}")
                #print(cursor.statement)
                return str(e)
            except Exception as e:
                print(f"Hit some non-specific error: {e}")
                return str(e)

    #Update existing movie in Movies table
    def update_movie(self, values):
        with self.get_connect_db() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(queries.update_movie, values)
                conn.commit() #save result back to database
                rowcount = cursor.rowcount
                #print(cursor.statement)
                return rowcount
            except mysql.connector.Error as e:
                print(f"Hit the follow mysql error: {e}")
                return str(e)
            except Exception as e:
                print(f"Hit some non-specific error: {e}")
                return str(e)

    #Update existing movie in Movies table
    def delete_movie(self, movie_id):
        with self.get_connect_db() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(queries.delete_movie, [movie_id])
                conn.commit() #save result back to database
                rowcount = cursor.rowcount
                return rowcount
            except mysql.connector.Error as e:
                print(f"Hit the follow mysql error: {e}")
                #print(cursor.statement)
                return str(e)
            except Exception as e:
                print(f"Hit some non-specific error: {e}")
                return str(e)

    def get_ratings(self):
        with self.get_connect_db() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(queries.select_all_ratings)
                results = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                row_results = []
                for row in results:
                    row_dict = dict(zip(column_names,row))
                    row_results.append(row_dict)
                return row_results
            except mysql.connector.Error as e:
                print(f"Hit the follow mysql error: {e}")
                #print(cursor.statement)
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
#!flask/bin/python
from os import error
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template
from flask_cors import CORS

#import pymysql
import mysql.connector

import queries
import moviedao
#import dbconfig as conf

app = Flask(__name__)

#initialise connection
'''conn = mysql.connector.connect(
    host=conf.mysql['host'],
    user=conf.mysql['user'],
    password=conf.mysql['password'],
    database=conf.mysql['database']
)'''
#create cursor object
test_dao = moviedao.Moviedao()

'''
    TODO - Add html to GET data and populate a table with response
'''
@app.route('/', methods=['GET'])
def test():
    cursor = test_dao.cursor # test the cursor object
    cursor.execute(queries.select_all_movie)
    query_result = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    # print(column_names)
    # for row in query_result:
    #     print(row)
    return jsonify(columns=column_names,data=query_result)

'''
    TODO - Add html form to add a new film, like done in labs
'''
@app.route('/', methods=['POST'])
def add_film():
    if not request.json:
        abort(400)
    if "MovieID" in request.json:
        movie_id = request.json['MovieID']
    else:
        #movie_id = None
        abort(403) #movie must have an identifier
    if "Title" in request.json:
        movie_title = request.json['Title']
    else:
        movie_title = None #strangely I've decided a movie does not necessarily need a name
    if "RatingID" in request.json:
        rating_id = request.json['RatingID']
    else:
        abort(403) #movie must have a rating
    cursor.execute(queries.insert_movie, (movie_id, movie_title, rating_id))
    return request.json

'''
    TODO - Add POST and DELETE methods for different functions and add html functionality
'''
@app.route('/', methods=['PUT'])
def update_film():
    if not request.json:
        abort(400)
    if "MovieID" in request.json:
        movie_id = request.json['MovieID']
    else:
        abort(403) #movie must have an identifier
    if "Title" in request.json:
        movie_title = request.json['Title']
    else:
        movie_title = None #strangely I've decided a movie does not necessarily need a name
    if "RatingID" in request.json:
        rating_id = request.json['RatingID']
    else:
        abort(403) #movie must have a rating
    try:
        cursor.execute(queries.update_movie, ( movie_title, rating_id, movie_id))
    except mysql.connector.Error as e:
        print("Hit some issue")
        print(e)
        print(cursor.statement)
    except Exception as e:
        print("Hit some other weirder issue")
        print(e)
    return request.json



if __name__ == '__main__':
    app.run(debug=True)
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

app = Flask(__name__,
            static_url_path='',
            static_folder='./templates/',
            template_folder='./templates/')

#create cursor object
movie_dao = moviedao.Moviedao()

@app.route('/', methods=['GET'])
def default_page():
    return render_template('movieform.html')

'''
    TODO - Add html to GET data and populate a table with response
'''
@app.route('/movies', methods=['GET'])
def get_movie():
    query_results = movie_dao.get_all_movies()
    return jsonify(data=query_results)

'''
    TODO - Add html form to add a new film, like done in labs
'''
@app.route('/movies', methods=['POST'])
def add_movie():
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
    row_added = movie_dao.add_movie((movie_id, movie_title, rating_id))
    return str(row_added)

'''
    TODO - Add POST and DELETE methods for different functions and add html functionality
'''
@app.route('/movies', methods=['PUT'])
def update_movie():
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

    response = movie_dao.update_movie(( movie_title, rating_id, movie_id))

    return str(response)

@app.route('/movies', methods=['DELETE'])
def delete_movie():
    if not request.json:
        abort(400)
    if "MovieID" in request.json:
        movie_id = request.json['MovieID']
    else:
        abort(400)
    response = movie_dao.delete_movie(movie_id)
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
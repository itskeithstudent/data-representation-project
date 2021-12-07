#!flask/bin/python
from os import error
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template
from flask_cors import CORS

import requests
import apiconfig

import moviedao
#import dbconfig as conf

app = Flask(__name__,
            static_url_path='',
            static_folder='./templates/',
            template_folder='./templates/')

movie_dao = moviedao.Moviedao()

@app.route('/', methods=['GET'])
def default_page():
    return render_template('movieform.html')

@app.route('/movies', methods=['GET'])
def get_movie():
    query_results = movie_dao.get_all_movies()
    return jsonify(data=query_results)

@app.route('/movies', methods=['POST'])
def add_movie():
    print(request.json)
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

@app.route('/ratings', methods=['GET'])
def get_ratings():
    query_results = movie_dao.get_ratings()
    return jsonify(data=query_results)

@app.route('/imdbdetails', methods=['GET'])
def get_film_details():
    if not request.json:
        abort(400)
    if "Title" in request.json:
        title = request.json['Title']
        params = [title, apiconfig.omdb_api_key]
        request.get(apiconfig.omdb_url,params)
        print(request.text)
        return jsonify(data=request.text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

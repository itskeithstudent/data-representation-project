#!flask/bin/python
from os import error
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template, render_template_string
from flask_cors import CORS

import requests
import apiconfig #api details

import moviedao #used for interacting with DB

app = Flask(__name__,
            static_url_path='',
            static_folder='./templates/',
            template_folder='./templates/')

movie_dao = moviedao.Moviedao() #initialise connection object at start

#base url, simply returns movieform.html
@app.route('/', methods=['GET'])
def default_page():
    return render_template('movieform.html')

#GET - retrieves movies to populate table
@app.route('/movies', methods=['GET'])
def get_movie():
    query_results = movie_dao.get_all_movies()
    return jsonify(data=query_results)

#POST - adds new movie to database
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

#PUT - update existing movie in database
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

#DELETE - removes movie from table based on movieID
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

#GET - retrieves data from rating table, used in dropdown
@app.route('/ratings', methods=['GET'])
def get_ratings():
    query_results = movie_dao.get_ratings()
    return jsonify(data=query_results)

#POST - gets sent a request with json containing movie title, this title is used to send GET to omdb api
@app.route('/imdbdetails', methods=['POST'])
def get_film_details():
    if not request.json:
        abort(400)
    if "Title" in request.json:
        title = request.json['Title']
        params = {"t":title, "apikey":apiconfig.omdb_api['omdb_api_key']}
        response = requests.get(url=apiconfig.omdb_api['omdb_url'],params=params)
        print(response.json())
        return jsonify(data=response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

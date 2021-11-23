#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template
from flask_cors import CORS

#import pymysql
import mysql.connector


import queries

app = Flask(__name__)

#initialise connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="G00387816_DataRepProject"
)
#create cursor object
cursor = conn.cursor()

'''
    TODO - Add html to GET data and populate a table with response
'''
@app.route('/', methods=['GET'])
def test():
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

    return request.json

'''
    TODO - Add POST and DELETE methods for different functions and add html functionality
'''


if __name__ == '__main__':
    app.run(debug=True)
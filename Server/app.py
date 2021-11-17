#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template
from flask_cors import CORS

#import pymysql
import mysql.connector

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

@app.route('/', methods=['GET'])
def test():
    print("Hello Terminal")
    cursor.execute("SELECT * FROM MOVIES;")
    query_result = cursor.fetchall()
    for row in query_result:
        print(row)
    return jsonify(data=query_result)

if __name__ == '__main__':
    app.run(debug=True)
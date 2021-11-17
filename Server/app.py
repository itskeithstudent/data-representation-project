#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
from flask.templating import render_template
from flask_cors import CORS
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    print("Hello Terminal")
    return "Hello Curl or Browser"

if __name__ == '__main__':
    app.run(debug=True)
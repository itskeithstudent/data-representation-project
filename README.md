# data-representation-project
REST API server using Flask and with a backend Database to access

This project demonstrates a web front-end which sends API requests to a flask server, which in turn retrieves data from a MySQL database.

## Project Content

* ./Database/ - This folder contains .sql script for creating the required database along with creating tables and adding some data to these tables.
* ./Server/ - Contains Python code for the flask server, includes a sub directory ./templates/ which contains html page to be returned by the flask server.
* ./ - The base folder contains non technical parts of the project; this Readme, a .txt document for some example cURL commands, a requirements.txt for installing any required python packages.


## Installing required Python packages
All required packages are listed in the requirements.txt, these can be simply installed by running the following command in your base python environment or a virtual environment:
 ```
 pip install -r requirements.txt
 ```
 
## Running the project
The flask REST server can be started by navigating to the ./Server/ directory and running either of the following commands:
````
python app.py
````
Alternatively it can be launched using the following (note this will only work as app.py is an expected name for flask, and this will only work if running the command from command line while in this directory):
````
flask run
````
After starting the server you can navigate to http://127.0.0.1:5000/ using a web browser (Tested using Google Chrome and Firefox, other browsers such as IE may experience errors).
Once navigated to the webpage, you will be able to retrieve data from the mysql database using GET requests, update existing rows using PUT requests, add new rows with POST requests and delete rows using DELETE requests.

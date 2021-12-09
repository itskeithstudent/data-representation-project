# data-representation-project

A 'live' version of this project can is hosted at this link on [Python Anywhere](http://g00387816.pythonanywhere.com/).

The aim of this project is to create a REST API server using Flask with a html frontend and a backend mysql Database which has CRUD operations performed against it based off the type of API request sent to the flask server via the webpage - This was achieved by creating a simple movie rating website, which also retrieves data from IMDB.

## Project Highlights
This project can be ran/interacted with in three ways:
1. Running via pythonanywhere
2. Running via the terminal to spin locally
3. Running via docker containers, to make the project agnostic of where it could be deployed

It presents a user with a webpage for loading in details about movies and allows the end user, to create, update, delete and read this information, further to this, the user can search IMDB for details about a particular movie presented to them.
Providing content for this webpage is a backend mysql database with two tables which are retrieved via ajax API call's from the webpage, the full range of CRUD operations can be performed on the html page that flask renders, which interacts with the Movies table (the Ratings table is supposed to be a hardcoded set of textual ratings, so it shouldn't be modifiable).
For the IMDB search functionality, this is achieved with a third party api called omdb, upon getting a POST request from a user which contains the title of the movie they would like to retrieve it takes the movie title from the request.json and sends that using a GET request to omdb (this is authenticated using an api key, which is hardcoded), what is returned from this api then populates a text section on the webpage. 

Efforts were put in to make sure the webpage was visually consistent and nice looking (subjectively!).

Packaging up this project in a set of docker containers was a personal aim of mine, I have previously dabbled with docker, but never spun up dependent containers e.g. a flask container which retrieves data on a mysql container across the same network but can also reach external sites.


## Project Content

* ./Database/ - This folder contains .sql script for creating the required database along with creating tables and adding some data to these tables.
* ./Server/ - Contains Python code for the flask server, includes a sub directory ./templates/ which contains html page to be returned by the flask server.
* ./ - The base folder contains non moving parts of the project; this Readme, a .txt document for some example cURL commands, a requirements.txt for installing any required python packages, a set of docker related files for spinning up flask and mysql containers.


## Installing required Python packages
All required packages are listed in the requirements.txt, these can be simply installed by running the following command in your base python environment or a virtual environment:
 ```
 pip install -r requirements.txt
 ```

## Setting up the mysql database
In order for the project to work it requires a mysql database called G00387816_DataRepProject to exist.
A script for creating the necessary Database can be found in the Database folder. The database can be created by first navigating to the bin folder of your mysql server and entering the following in your command line terminal
````
mysql -u root -p < "C:\path\to\directory\data-representation-project\Database\G00387816_DataRepProject.sql"
````
Alternatively a similar command can be ran when in a mysql terminal
````
source "C:\path\to\directory\data-representation-project\Database\G00387816_DataRepProject.sql"
````

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


## Third party API - OMDB (Open Movie Database) API
The external API used is (OMDB)[http://www.omdbapi.com/], which is itself retrieving data from IMDB based on a film title or IMDB ID, though for the purposes of this project simply retrieves based on title as it would not make sense to expect a user to enter an IMDB ID.
Getting a key for this API you must first sign up, however this is free to do so and the API key used in this project could be used by others.


## Python Anywhere hosting
The project itself is hosted over on Python Anywhere, and can be accessed at this url: http://g00387816.pythonanywhere.com/
It is kept up to date by performing a git pull command within a bash terminal after making any changes to this repository.

For reproducing this with this project in your own Python Anywhere account, the following are a short set of steps that were followed:
1. In the bash console clone in the repository.
2. Also in the bash console, create a virtual environment and install required packages.
3. Under Databases add a new database, giving it a name consistent with what is used as the host in the projects dbconfig.py file, however do note that pythonanywhere will add the username as a prefix for this database so in my case G00387816_DataRepProject became G00387816$G00387816_DataRepProject, and this is the hostname that should be used for connecting in python anywhere context.
4. Under Web, click to add a new webapp, select to add a flask web application and go with the default folder it gives for flask_app.py as we will change the wsgi this doesn't matter.
5. Configure Web Application settings to use the early created virtual environment.
6. Change the wsgi configuration file to point it at your projects app.py, instead of the flask_app.py file created in the last step in my case this was /home/G00387816/data-representation-project/Server.
7. Reload and start the webapp. It should now work as you've set up a virtual environment which can run your projects code, set up a database to connect to and configured you webapplication to correctly use the correct code.


## Running the project in Docker containers
The project can also be ran using the docker-compose.yml file, this spins up two containers, one for hosting the flask REST server and the other hosting the mysql database.
To run this, first make sure you have docker desktop or the docker daemon started.
Then in your terminal navigate to the projects base directory (same one which contains docker-compose.yml) and enter the following:
````
docker-compose up
````
When this launches you may be unlucky and note several (or quite a few) error messages for the flask container, this is due to the mysql container not having it's database ready yet, and so when the flask container trys to connect on port 3306 it can't connect. To handle this issue, the flask container restarts on hitting an error, unfortunately there is no simple solution to this, containers can wait for the other to be ready, however that does not mean they wait for the services within to be ready e.g. in this case the mysql database being created and ready.

Screenshot showing running containers after "docker-compose up" command.
![image](https://user-images.githubusercontent.com/60199302/144525963-bd9f72ac-6e7b-42d4-ae09-0663a6c2c39f.png)

Once the containers have both sucessfully spun up, you can access the webpage in exactly the same manner as before; by entering https://127.0.0.1:5000/ into your browser.

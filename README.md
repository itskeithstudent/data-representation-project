# data-representation-project
REST API server using Flask and with a backend Database to access

This project demonstrates a web front-end which sends API requests to a flask server, which in turn retrieves data from a MySQL database.

## Project Content

* ./Database/ - This folder contains .sql script for creating the required database along with creating tables and adding some data to these tables.
* ./Server/ - Contains Python code for the flask server, includes a sub directory ./templates/ which contains html page to be returned by the flask server.
* ./ - The base folder contains non technical parts of the project; this Readme, a .txt document for some example cURL commands, a requirements.txt for installing any required python packages, a set of docker related files for spinning up flask and mysql containers.


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

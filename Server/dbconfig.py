import os

#Check for environment variable 'DOCKER_ENV' - this is set as part of docker-compose.yml
environment_check_docker = os.environ.get('DOCKER_ENV', False)
#Check for environment variable 'PYTHONANYWHERE_SITE' - this is standard env variable on python anywhere
environment_check_pythonanywhere = os.environ.get('PYTHONANYWHERE_SITE', False)
#whichever env variable returns true, determines what connection details to use
if environment_check_docker:
    mysql = {
        'host':'db', #host is db due to container name in docker-compose.yml
        'user':'root',
        'password':'root', #can't provide blank password
        'database':'G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':10,
        'port':3306
    }
elif environment_check_pythonanywhere:
    mysql = {
        'host':'G00387816.mysql.pythonanywhere-services.com', #db on pythonanywhere
        'user':'G00387816',
        'password':'rootroot',
        'database':'G00387816$G00387816_DataRepProject', #pythonanywhere has strange convention for database name
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':3, #pythonanywhere has limit on pool size
        'port':3306
    }
else: #base-case where ran from
    mysql = {
        'host':'localhost',
        'user':'root',
        'password':'',
        'database':'G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':10,
        'port':3306
    }
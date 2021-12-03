import os

environment_check = os.environ.get('DOCKER_ENV', False)

if environment_check:
    mysql = {
        'host':'db',
        'user':'root',
        'password':'root',
        'database':'G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':10,
        'port':3306
    }
else:
    mysql = {
        'host':'localhost',
        'user':'root',
        'password':'',
        'database':'G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':10,
        'port':3306
    }
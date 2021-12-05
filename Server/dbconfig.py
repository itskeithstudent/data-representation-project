import os

environment_check_docker = os.environ.get('DOCKER_ENV', False)
environment_check_pythonanywhere = os.environ.get('PYTHONANYWHERE_SITE', False)

if environment_check_docker:
    mysql = {
        'host':'db',
        'user':'root',
        'password':'root',
        'database':'G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':10,
        'port':3306
    }
elif environment_check_pythonanywhere:
    mysql = {
        'host':'G00387816.mysql.pythonanywhere-services.com',
        'user':'G00387816',
        'password':'rootroot',
        'database':'G00387816$G00387816_DataRepProject',
        'default_pool_name':'movie_conn_pool',
        'default_pool_size':3,
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
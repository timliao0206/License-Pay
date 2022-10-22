import psycopg2
import json


DEFAULT_PATH = './config.json'

'''
establish connection to database server

param:
file_path: path to config file which contains the connecting information.

return:
psycopg2 connection object
'''
def get_connection(file_path = DEFAULT_PATH):
    param_name = ['host','user','dbname','password']
    
    try:
        f = open(file_path)
        config = json.load(f)
    except FileNotFoundError:
        print('{1} json file not found'.format(file_path))
        return None
    
    connection_string = ""
    
    for name in param_name:
        connection_string += name + "=" + config[name] + " "
    
    try:    
        conn = psycopg2.connect(connection_string)
        return conn
    except Exception as e:
        print("Database connection error.\n",e)
        return None


from flask import Flask,render_template,request
from transaction import *
import connection
import json

conn = connection.get_connection()
app = Flask(__name__)


@app.route('/payer',method=['GET'])
def get_payer():
    username = request.args.get('username')
    payer = Payer(username)
    payer.findByName(conn)
    
    return payer.jsonify()

@app.route('/receiver',method=['GET'])
def get_receiver():
    username = request.args.get('username')
    receiver = Receiver(username)
    receiver.findByName(conn)
    
    return receiver.jsonify()


'''
Need unit test
'''
@app.route('/transaction',method=['GET'])
def get_transaction():
    param = request.args
    ls = get_all_with_constraint(**param)
    json_ls = [item.jsonify() for item in ls]
    
    return json.dumps(json_ls)
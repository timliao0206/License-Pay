from flask import Flask,render_template,request
from transaction import *
import connection
import json

conn = connection.get_connection()
app = Flask(__name__)


@app.route('/payer',methods=['GET'])
def get_payer():
    username = request.args.get('username')
    payer = Payer(username)
    payer.findByName(conn)
    
    return payer.jsonify()

@app.route('/payer',methods=['POST'])
def post_payer():
    param = request.args
    payer = Payer(**param)
    payer.commit(conn)
    
    return payer.jsonify()

@app.route('/receiver',methods=['GET'])
def get_receiver():
    username = request.args.get('username')
    receiver = Receiver(username)
    receiver.findByName(conn)
    
    return receiver.jsonify()

@app.route('/receiver',methods=['POST'])
def post_receiver():
    param = request.args
    receiver = Receiver(**param)
    receiver.commit(conn)
    
    return receiver.jsonify()


'''
Need unit test
'''
@app.route('/transaction',methods=['GET'])
def get_transaction():
    param = request.args
    ls = get_all_with_constraint(conn,**param)
    json_ls = [item.jsonify() for item in ls]
    
    return json.dumps(json_ls)

@app.route('/transaction',methods=['POST'])
def post_transaction():
    param = request.args
    
    trans = Transaction(**param)
    trans.commit(conn)
    
    
    return trans.jsonify()

app.run(host="0.0.0.0",port=3000)
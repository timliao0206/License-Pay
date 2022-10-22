from symbol import stmt
from sql_object import SQL_object
from utils import strify

class Payer(SQL_object):
    def __init__(self,
                 username:str,
                 psw = "",
                 license_plate = "",
                 phone_number = "",
                 balance = 0):
        
        self.col = {}
        self.col['username'] = username
        self.col['psw'] = psw
        self.col['phone_number'] = phone_number
        self.col['license_plate'] = license_plate
        self.col['balance'] = balance
    
    entries = ['username','psw','license_plate','phone_number','balance']
    
    '''
    Find user infomation by their username.
    
    param:
        conn: psycopg2.connection object
    return:
        None
    '''
    def findByName(self,conn):
        stmt = 'SELECT * FROM public."Payer" WHERE username=' + strify(self.col['username'])
        
        cursor = conn.cursor()
        cursor.execute(stmt)
        record = cursor.fetchone()
        
        for i,name in enumerate(Payer.entries):
            self.col[name] = record[i]
        return
    
    '''
    Update money and commit
    
    param:
        delta: money difference = new money - old money
    return:
        None
    '''
    def updateMoney(self,delta):
        self.col['balance'] = self.col['balance'] + delta
        return
    
    def insert_stmt(self):
        stmt = 'INSERT INTO public."Payer"'
        
        column = "(" + ','.join(Payer.entries) + ")"
        
        stmt += column
        stmt += " VALUES "
        stmt += "(" + ",".join([strify(self.col[name]) for name in Payer.entries]) + ")"
        
        return stmt
    
    def update_stmt(self):
        stmt = 'UPDATE public."Payer" SET balance=' + strify(self.col['balance']) + " "
        stmt += "WHERE username=" + strify(self.col['username'])
        return stmt
    
    def __str__(self):
        return "'" + self.col['username'] + "'"
    
        
    
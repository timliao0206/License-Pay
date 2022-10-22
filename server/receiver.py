from sql_object import SQL_object
from utils import strify

class Receiver(SQL_object):
    def __init__(self,username,psw="",contact = ""):
        self.col = {}
        self.col['username'] = username
        self.col['psw'] = psw
        self.col['contact_info'] = contact
        return
    
    entries = ["username","psw","contact_info"]
    
    
    
    def insert_stmt(self):
        stmt = 'INSERT INTO public."Receiver"'
        
        column = "(" + ','.join(Receiver.entries) + ")"
        
        stmt += column
        stmt += " VALUES "
        stmt += "(" + ",".join([strify(self.col[name]) for name in Receiver.entries]) + ")"
        
        return stmt
    
    # Unneed for now
    def update_stmt(self):
        raise NotImplementedError
    
    '''
    Find user infomation by their username.
    
    param:
        conn: psycopg2.connection object
    return:
        None
    '''
    def findByName(self,conn):
        stmt = 'SELECT * FROM public."Receiver" WHERE username=' + strify(self.col['username'])
        
        cursor = conn.cursor()
        cursor.execute(stmt)
        record = cursor.fetchone()
        
        for i,name in enumerate(Receiver.entries):
            self.col[name] = record[i]
        return
    
    
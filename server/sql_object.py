import json

class SQL_object:
    def __init__(self):
        self.col = {}
        return
    
    
    def insert_stmt(self) -> str:
        raise NotImplementedError
    
    def update_stmt(self) -> str:
        raise NotImplementedError
    
    def insert(self,conn):
        stmt = self.insert_stmt()
        
        cursor = conn.cursor()
        cursor.execute(stmt)
        conn.commit()
        
        return
    
    def update(self,conn):
        stmt = self.update_stmt()
        
        cursor = conn.cursor()
        cursor.execute(stmt)
        conn.commit()
        
        return
    
    '''
    commit changes to database
    

    params:
        conn: psycopg2.connection object
        type: in ['insert','update']
    return:
        None
    '''
    def commit(self,conn,type = "insert"):
        types = ['insert','update']
        if type not in types:
            print("type",type,"not in",types)
            return
        
        if type is 'insert':
            self.insert(conn)
            
        if type is 'update':
            self.update(conn)
            
        return
    
    def jsonify(self):
        return json.dump(self.col)
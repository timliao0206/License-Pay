from payer import Payer
from receiver import Receiver
from sql_object import SQL_object
from utils import strify
from datetime import datetime
from typing import List, Union

permission_code = {
    "SENDED" : 0,
    "ALLOWED" : 1,
    "DENIED" : 2
}

class Transaction(SQL_object):
    def __init__(self,
                 payer: Payer,
                 receiver: Receiver,
                 time="",
                 money_diff=0,
                 permission = 0,
                 description = ""):
        
        self.col = {}
        
        self.col['payer_username'] = payer
        self.col['receiver_username'] = receiver
        self.col['time'] = time
        self.col['money_diff'] = money_diff
        self.col['permission'] = permission
        self.col['description'] = description
        return
    
    def insert_stmt(self):
        
        if self.col['time'] is "":
            self.col['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        stmt = 'INSERT INTO public."Transaction"' + "(" + ','.join(Transaction.entries) + ") VALUES "
        stmt += '(' + ','.join( [ strify( self.col[name] ) for name in Transaction.entries ] ) + ')'

        return stmt
    
    '''
    Set permission
    
    param:
        permission: int or str
            int should be in [0,2]
            str should be in permission_code's key
    return
        None
    '''
    def set_permission(self,permission: Union[int,str]):
        if type(permission) is int and permission in permission_code.values():
            self.col['permission'] = permission
        elif type(permission) is str and permission in permission_code.keys():
            self.col['permission'] = permission_code[permission]
            
            
    '''
    Allowed this permission
    
    param:
        None
    return:
        None
    '''
    def allow(self):
        self.set_permission("ALLOWED")
    
    def update_stmt(self):
        stmt = 'UPDATE public."Transaction" SET permission=' + self.col['permission']
        stmt += " WHERE payer_username=" + strify(self.col['payer_username'])
        stmt += " AND receiver_username=" + strify(self.col['receiver_username'])
        stmt += " AND time=" + strify(self.col['time'])
        
        return stmt
    
    entries = ["payer_username","receiver_username","time","money_diff","permission","description"]
    
    def __str__(self):
        return strify(self.col['payer_username']) + "," + strify(self.col['receiver_username']) + " on " + strify(self.col['time']) 
    
'''
return a list of Transaction object which satisfies all the requirement.

params:
    conn: psycopg2 connection object
        connection to database
        
    payer: Payer object
        select Transaction with this user as payer
        
    receiver: Receiver object
        select Transaction with this user as receiver
        
    permission: str or int
        select Transaction with this permission. -1 implies all kind of transaction.
        
    time_before: str
        select Transaction before or exactly this given time
        
    time_after: str
        select Transaction after or exactly this given time
        
    money_diff_greater: int
        select Transaction greater or equal to this given amount
        
    money_diff_lesser: int
        select Transaction lesser or equal to this given amount

return:
    a list of Transaction which satisfies all the requirement
'''
def get_all_with_constraint(conn,payer: Payer = None,
                            receiver: Receiver = None,
                            permission: Union[str,int] = -1,
                            time_before: str = None,
                            time_after: str = None,
                            money_diff_greater: int = None,
                            money_diff_lesser: int = None):
    stmt = 'SELECT * FROM public."Transaction" WHERE '
    
    # building condition
    using = {}
    
    using['payer'] = payer is not None
    using['receiver'] = receiver is not None
    using['permission'] = permission is not -1
    if type(permission) is str:
        permission = permission_code[permission]
    using['time_before'] = time_before is not None
    using['time_after'] = time_after is not None
    using['money_diff_greater'] = money_diff_greater is not None
    using['money_diff_lesser'] = money_diff_lesser is not None
    
    
    not_first = False
    
    if using['payer']:
        stmt += "payer_username=" + strify(payer)
        not_first = True
    
    if using['receiver']:
        if not_first:
            stmt += " AND "
        stmt += "receiver_username=" + strify(receiver)
        not_first = True
        
    if using['permission']:
        if not_first:
            stmt += " AND "
        stmt += "permission=" + strify(permission)
        not_first = True
    
    if using['time_before']:
        if not_first:
            stmt += " AND "
        stmt += "time<=" + strify(time_before)
        not_first = True
    
    if using['time_after']:
        if not_first:
            stmt += " AND "
        stmt += "time>=" + strify(time_after)
        not_first = True
    
    if using['money_diff_greater']:
        if not_first:
            stmt += " AND "
        stmt += "money_diff>=" + strify(money_diff_greater)
        not_first = True
    
    if using['money_diff_lesser']:
        if not_first:
            stmt += " AND "
        stmt += "money_diff<=" + strify(money_diff_lesser)
        not_first = True
    
    
    
    cursor = conn.cursor()
    cursor.execute(stmt)
    
    fetched = cursor.fetchall()
    
    transactions = [Transaction(*args) for args in fetched]
    
    return transactions

'''
return a list of Transaction which has not yet been determined.

param:
    conn: psycopg2 connection Object
        connection to database
    user: Payer or Receiver
        the person from whom the transactions needed to be listed. 
return:
    a list of Transaction object
'''
def get_all_undetermined_transaction(conn,user: Union[Payer,Receiver]) -> List[Transaction]:
    
    if type(user) is Payer:
        return get_all_with_constraint(conn,payer = user,permission="SENDED")
    elif type(user) is Receiver:
        return get_all_with_constraint(conn,receiver=user,permission="SENDED")
    
    return []
    
    
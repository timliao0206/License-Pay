from connection import get_connection
from payer import Payer
from receiver import Receiver
from transaction import *

def main():
    conn = get_connection()
    #p = Transaction("Crson","Fetty",description="test",money_diff=120,permission=2)
    #p.commit(conn)
    p = Payer("Crson")
    r = Receiver("Detty")
    p.findByName(conn)
    r.findByName(conn)
    ls = get_all_with_constraint(conn,payer=p,receiver=r,time_after=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print([strify(item) for item in ls])
    
    conn.close()


if __name__ == '__main__':
    main()
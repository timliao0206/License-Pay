from connection import get_connection
from payer import Payer
from receiver import Receiver

def main():
    conn = get_connection()
    p = Receiver("Betty","betty","betty@gmail.com")
    p.commit(conn)
    print(p.insert_stmt())
    conn.close()


if __name__ == '__main__':
    main()
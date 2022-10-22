from connection import get_connection



def main():
    conn = get_connection()
    print(conn)


if __name__ == '__main__':
    main()
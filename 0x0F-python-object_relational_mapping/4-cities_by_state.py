#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import sys
import MySQLdb


def main():
    '''Dirver function'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, database=database_name)

    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c\
                INNER JOIN states AS s ON c.state_id = s.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()

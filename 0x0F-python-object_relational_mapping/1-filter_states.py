#!/usr/bin/python3
'''script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa'''
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
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
'''script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument'''
import sys
import MySQLdb


def main():
    '''Dirver function'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, database=database_name)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC""".format(search_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()

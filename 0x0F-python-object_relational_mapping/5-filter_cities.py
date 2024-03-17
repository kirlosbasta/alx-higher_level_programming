#!/usr/bin/python3
'''script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa'''
import sys
import MySQLdb


def main():
    '''Dirver function'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, database=database_name)

    cur = db.cursor()
    cur.execute("""SELECT sub.city FROM (SELECT c.id, c.name city, s.name\
                state FROM cities AS c INNER JOIN states AS s ON\
                c.state_id = s.id) AS sub WHERE sub.state = %s""",
                (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))


if __name__ == '__main__':
    main()

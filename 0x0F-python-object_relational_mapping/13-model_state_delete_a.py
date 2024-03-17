#!/usr/bin/python3
'''script that deletes all State objects with a name
containing the letter a from the database
hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def main():
    '''Driver function'''
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    main()

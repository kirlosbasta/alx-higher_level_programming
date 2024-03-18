#!/usr/bin/python3
'''script that prints all City objects from the database hbtn_0e_14_usa'''
from model_state import Base, State
from model_city import City
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
    cities = session.query(City, State).\
        join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()


if __name__ == '__main__':
    main()

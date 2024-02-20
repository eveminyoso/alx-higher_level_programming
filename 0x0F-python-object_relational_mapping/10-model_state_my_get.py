#!/usr/bin/python3
"""
"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # connecting database and macthes arguments
    # with existing data in db
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    condition = [sys.argv[4]]
    result = session.query(State.id) \
            .filter(State.name.in_(condition)) \
            .all()

    if result:
        for i in result:
            print(i[0])
    else:
        print("Not found")

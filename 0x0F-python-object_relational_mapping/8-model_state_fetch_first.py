#!/usr/bin/python3
"""
Selecting the first object
"""
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Pass in arguments
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id.asc()).first()

    if result:
        print(f"{result.id}: {result.name}")
    else:
        print("Nothing")

    session.close()

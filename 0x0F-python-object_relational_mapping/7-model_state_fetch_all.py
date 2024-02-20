#!/usr/bin/python3
"""
fetch query
"""
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # connecting to the database
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id.asc()).all()

    for i in result:
        print(f"{i.id}: {i.name}")

    session.close()

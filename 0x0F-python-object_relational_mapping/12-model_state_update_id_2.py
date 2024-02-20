#!/usr/bin/python3
"""
updating record
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # connect to db and manipulate
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    condition = 2
    new = {'name': 'New Mexico'}
    result = session.query(State) \
        .filter_by(id=condition) \
        .update(new)
    session.commit()
    session.close()

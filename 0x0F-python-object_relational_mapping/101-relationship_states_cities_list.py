#!/usr/bin/python3
"""

"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import select


if __name__ == '__main__':
    # connect to db and list all state
    # objects corr to City
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State) \
            .join(City, City.state_id == State.id) \
            .order_by(State.id.asc(), City.id.asc()) \
            .all()
    for city, state in result:
        print(f"{city.id}: {city.name} -> {state.name} {state.id}")
    session.close()

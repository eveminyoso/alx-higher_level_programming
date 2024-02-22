#!/usr/bin/python3
"""
create a new model
and list everything in that model
"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # connect to database and list
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State) \
            .join(State, City.state_id == State.id) \
            .order_by(City.id.asc()) \
            .all()

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

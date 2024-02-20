#!/usr/bin/python3
"""
City relationship
"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert


if __name__ == '__main__':
    # connect to db and create state n city
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='California')
    city = City(name="San Francisco")

    session.add(new)
    session.commit()

    stmt2 = insert(City).values(name=city.name, state_id=new.id)
    session.execute(stmt2)

    session.commit()

    # Closing the connection

    session.close()

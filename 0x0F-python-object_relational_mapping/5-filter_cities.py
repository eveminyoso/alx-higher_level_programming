#!/usr/bin/python3
"""
lists all cities of a given state
"""
import MySQLdb
import sys


def from_state_list(user, pwd, db, state):
    """
    from_state_list takes the passed argument state and
    list all cities associated with it
    """

    db = MySQLdb.connect(
            user=user,
            password=pwd,
            database=db,
            host="localhost",
            port=3306
            )
    query = db.cursor()
    query.execute(
            "SELECT cities.name FROM cities "
            "JOIN states WHERE cities.state_id = states.id "
            "AND states.name = %s",
            (state,)
            )
    result = query.fetchall()

    if result:
        cities = ", ".join([city[0] for city in result])
        print(cities)
    else:
        print()

        db.close()


        if __name__ == '__main__':
            # Parse in the arguments
            if len(sys.argv) != 5:
                print("Usage: executable.py <user> <passwd> <db> <state>")
                sys.exit(1)
                user, pwd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
                from_state_list(user, pwd, db, state)

#!/usr/bin/python3
"""
listing all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(user, pwd, db):
    """
    list_cities list everything in our cities db
    params:
    -> user: this is the root user
    -> pwd: root password
    -> db: database to connect to
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
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states WHERE cities.state_id = states.id "
            "ORDER BY cities.id"
            )
    result = query.fetchall()

    for i in result:
        print(i)


if __name__ == '__main__':
    # parsing arguments
    if len(sys.argv) != 4:
        print("Usage: executable.py <user> <passwd> <db>")
        sys.exit(1)
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(user, pwd, db)

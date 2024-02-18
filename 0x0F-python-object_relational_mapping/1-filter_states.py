#!/usr/bin/python3
"""
listing according to science
"""
import MySQLdb
import sys


def list_cases(username, password, database):
    """"list view wothout restrications"""
    db = MySQLdb.connect(
            user=username,
            password=password,
            database=database,
            host="localhost",
            port=3306
            )
    query = db.cursor()
    query.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' "
            "ORDER BY states.id ASC"
            )
    result = query.fetchall()
    for i in result:
        print(i)


if __name__ == '__main__':
    # Check if arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./executable.py <username> <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cases(username, password, database)

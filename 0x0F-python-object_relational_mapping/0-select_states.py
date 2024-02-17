#!/usr/bin/python3
"""
Lets list everything in our new database
"""
import MySQLdb
import sys


def list_states(username, password, database):
    db = MySQLdb.connect(user=username, password=password, database=database)
    all_items = db.cursor()
    all_items.execute(
            "SELECT * FROM states "
            "ORDER BY states.id ASC"

            result = all_items.fetchall()
            for i in result:
            print(i)

            db.close()


            if __name__ == '__main__':
            # Check if all arguments are provided
            if len(sys.argv) != 4:
            print("Usage: python_script file <username> <passwd> <database>")
            sys.exit(1)
            username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
            list_states(username, password, database)

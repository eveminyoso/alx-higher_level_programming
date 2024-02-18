#!/usr/bin/python3
import MySQLdb
import sys


def list_states_with_n(username, password, database):
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database)
        cursor = db.cursor()
        cursor.execute(
                "SELECT * FROM states "
                "WHERE name LIKE 'N%' ORDER BY states.id ASC")

        results = cursor.fetchall()
        for row in results:
            print(row)
        db.close()

    except Exception as e:
        print("error")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>")
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states_with_n(user, pwd, db)

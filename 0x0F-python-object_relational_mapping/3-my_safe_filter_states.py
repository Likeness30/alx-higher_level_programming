#!/usr/bin/python3

"""This script takes in an argument and displays all values in the `states`
table of the database `hbtn_0e_0_usa` where the `name` matches the argument."""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id;",
                (sys.argv[4], ))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()

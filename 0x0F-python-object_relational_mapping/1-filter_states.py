#!/usr/bin/python3

"""This script lists all states with a name starting with 'N' from
the database `hbtn_0e_0_usa`"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    result = cur.fetchall()
    for row in result:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    db.close()

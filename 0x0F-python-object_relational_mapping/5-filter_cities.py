#!/usr/bin/python3

"""This script lists all cities from the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name LIKE BINARY %s ORDER BY\
                cities.id;", (sys.argv[4], ))
    result = cur.fetchall()
    result = []
    for row in result:
        result.append(row[0])
    print(", ".join(result))

    cur.close()
    db.close()

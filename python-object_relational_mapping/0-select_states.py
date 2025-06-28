#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    # Execute the query to get all states ordered by id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    # Print each row as a tuple
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

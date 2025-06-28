#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    
    # Format the SQL query with user input for state name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Print the results as tuples
    for row in rows:
        print(row)

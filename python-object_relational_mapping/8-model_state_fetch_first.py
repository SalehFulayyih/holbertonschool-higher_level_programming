#!/usr/bin/python3
"""
This script lists the first State object from the database hbtn_0e_6_usa.

It connects to a MySQL database using SQLAlchemy and prints the State
with the lowest id. If the table is empty, it prints 'Nothing'.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    """
    Connects to the MySQL database and prints the first State object.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    session.close()


if __name__ == "__main__":
    main()

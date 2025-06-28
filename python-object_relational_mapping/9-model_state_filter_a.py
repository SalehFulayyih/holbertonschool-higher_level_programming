#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa.

Connects to a MySQL database using SQLAlchemy and prints states whose names
contain the letter 'a', sorted by id in ascending order.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    """
    Connects to the database and prints all State objects containing 'a'.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    session = Session(engine)
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Contains a script to list all State objects with the letter 'a' in their name
from the database hbtn_0e_6_usa.

Connects to a MySQL database using SQLAlchemy, fetches matching states ordered
by id ascending, and prints their id and name.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_states_with_a(username, password, db_name):
    """
    Connects to the MySQL database and lists State objects whose name contains 'a'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )
    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    list_states_with_a(argv[1], argv[2], argv[3])

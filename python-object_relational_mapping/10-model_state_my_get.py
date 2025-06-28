#!/usr/bin/python3
"""
Prints the State id from the database hbtn_0e_6_usa
based on the state name passed as argument.

Connects to a MySQL database using SQLAlchemy and
searches for a State matching the given name safely.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_state_id_by_name(username, password, db_name, state_name):
    """
    Searches for the State object by name and prints its id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.
    """
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    session = Session(engine)
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    get_state_id_by_name(argv[1], argv[2], argv[3], argv[4])

#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa
and prints its id after insertion.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    # Create engine connection to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    # Create session
    session = Session(engine)

    # Create new State object
    new_state = State(name="Louisiana")

    # Add and commit new state to the session
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()

#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    # Set up database connection
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    # Create session
    session = Session(engine)

    # Query states with 'a' in the name
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    # Delete each matching state
    for state in states_to_delete:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()

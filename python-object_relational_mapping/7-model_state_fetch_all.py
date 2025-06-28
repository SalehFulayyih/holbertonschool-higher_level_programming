#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get arguments: username, password, database
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}", pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects ordered by id ascending
    states = session.query(State).order_by(State.id).all()

    # Print results as "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

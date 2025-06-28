#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Format: <state name>: (<city id>) <city name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True
    )

    session = Session(engine)

    # Join State and City and sort by City.id
    results = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

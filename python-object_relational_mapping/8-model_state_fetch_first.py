#!/usr/bin/python3
"""Print first State object from database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    session = Session(engine)
    first = session.query(State).order_by(State.id).first()

    if first is not None:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")

    session.close()

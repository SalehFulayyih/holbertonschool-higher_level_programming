#!/usr/bin/python3
"""
Defines a State class with a relationship to City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from model_state import Base


class State(Base):
    """Represents a state with a one-to-many relationship to cities."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete",
        backref="state"
    )

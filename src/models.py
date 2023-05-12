import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(16))
    email = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    favorites = relationship("Favorites", back_populates="user")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    haircolor = Column(String)
    eyecolor = Column(String)
    favorites = relationship("Favorites", back_populates="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    favorites = relationship("Favorites", back_populates="planet")

class Favorites(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

    def validate(self):
        if self.planet_id is None and self.character_id is None:
            return False
        return True

def main():
    # Create the database engine or perform other operations
    pass

if __name__ == '__main__':
    main()

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

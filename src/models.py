import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)



# Define the User class
class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    favorites = relationship('Favorite')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

# Define the Character class     
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Numeric (4,2))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    species = Column(String(250))
    mass = Column(Numeric (4,2))
    favorites = relationship('Favorite')
 


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'species': self.species,
            'mass': self.mass,
        }
    
# Define the Vehicles class    
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250))
    length = Column(Numeric (4,2))
    passengers = Column(Integer)
    favorites = relationship('Favorite')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'passengers': self.passengers,
        }
# Define the Planets class
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Numeric (4,2))
    orbital_period = Column(Numeric (4,2))
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(Numeric (4,2))
    favorites = relationship('Favorite')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
        }



      

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#These column serves as a flag to indicate whether marked as a favorite by the user.
user_vehicle_association_table = Table(
    'user_vehicle_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id')),
    Column('is_favorite', Integer, default=0)  # Additional column for favorite flag
)

user_character_association_table = Table(
    'user_character_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('character_id', Integer, ForeignKey('characters.id')),
    Column('is_favorite', Integer, default=0)  # Additional column for favorite flag
)

user_planet_association_table = Table(
    'user_planet_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id')),
    Column('is_favorite', Integer, default=0)  # Additional column for favorite flag
)


# Define the User class
class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    


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

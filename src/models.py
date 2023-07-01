import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import  declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    skin_color = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    created = Column(Integer)
    edited = Column(Integer)
    homeworld = Column(Integer, ForeignKey('planets.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    person_id = Column(Integer, ForeignKey('person.id'))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    username = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

def to_dict(self):
        return {
            'id': self.id,
            'favorites_id': self.favorites_id,
            'username': self.username,
            'email': self.email
       }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
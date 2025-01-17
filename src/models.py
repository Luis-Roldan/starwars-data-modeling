import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'    
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base): #parent
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(12), nullable= False, unique=True)
    password = Column(String (20), nullable= False)
    favorite_list = relationship("Favorite_list", back_populates="user")

class Favorite_list(Base): #child   
    __tablename__ = 'favorite_list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    user = relationship("User", back_populates="favorite_list")
    planet = relationship("Planet", back_populates="favorite_list")
    character = relationship("Character", back_populates="favorite_list")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    dimension = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    #favorite_list_id = Column(Integer, ForeignKey("favorite_list.id"), nullable= False)
    favorite_list = relationship("Favorite_list", back_populates="planet")
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    #favorite_list_id = Column(Integer, ForeignKey("favorite_list.id"), nullable= False)
    favorite_list = relationship("Favorite_list", back_populates="character")



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

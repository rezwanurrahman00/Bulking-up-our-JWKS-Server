"""
Author: Rezwanur Rahman
Course: CSCE 3550 - Foundations of Cybersecurity
Date: December 6, 2024
Description: Database models for User and AuthLog to support user management
and authentication logging in the JWKS Server.
"""

from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True)
    date_registered = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP)

class AuthLog(Base):
    __tablename__ = 'auth_logs'
    id = Column(Integer, primary_key=True)
    request_ip = Column(String, nullable=False)
    request_timestamp = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey('users.id'))

# Database setup
engine = create_engine('sqlite:///database.db')

# Drop and recreate tables (use only during testing/development)
Base.metadata.drop_all(engine)  # Drop all tables
Base.metadata.create_all(engine)  # Create tables

Session = sessionmaker(bind=engine)
session = Session()

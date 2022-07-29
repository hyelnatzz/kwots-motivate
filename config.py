import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quote.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(8).hex()
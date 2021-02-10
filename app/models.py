from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    quotes = db.relationship('Quote', backref = 'user')

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f'<User {self.username}>'

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.Column(db.String, nullable = False)
    quote = db.Column(db.String, nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.now())
    favorite = db.Column(db.Boolean, nullable = False)

    def delete_quote(self, id):
        db.session.delete(Quote.query.get(id))

    def __repr__(self) -> str:
        return f'<Quote {self.quote[:10]}>'

db.create_all()
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    quotes = db.relationship('Quote', backref = 'user')
    categories = db.relationship('Category', backref = 'user')

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)

    def __repr__(self) -> str:
        return f'<User {self.username}>'

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.Column(db.String, nullable = False)
    quote = db.Column(db.String, nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.now())
    favorite = db.Column(db.Boolean, nullable = False)
    note = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    period = db.Column(db.String)

    def delete_quote(self, id):
        db.session.delete(Quote.query.get(id))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)

    def __repr__(self) -> str:
        return f'<Quote {self.quote[:10]}>'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, default = False)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    quotes = db.relationship('Quote', backref = 'category')
    icon = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String, nullable = True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        general_category = db.session.query(Category).filter_by(name = "General").first()
        quotes = self.quotes
        for i in quotes:
            i.category = general_category
        self.color.delete()
        db.session.delete(self)

    def __repr__(self) -> str:
        return f'<Category {self.name}>'


class Color(db.Model):
    __tablename__ = 'colors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    category = db.relationship('Category', backref = 'color', uselist = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)

    def __repr__(self) -> str:
        return f'<Color {self.name}>'

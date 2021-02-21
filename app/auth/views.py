from flask import  render_template
from . import auth_bp
from .. import db
from ..models import User


u = {'username':'hyelnatz', 'password':'password', 'email':'hndzarma@gmail.com'}

@auth_bp.route('/login')
def login():
    return render_template('signin.html')

@auth_bp.route('/register')
def register():
    """user = User()
    user.username = u['username']
    user.email = u['email']
    user.set_password(u['password'])
    db.session.add(user)
    db.session.commit()"""
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    return 'logout Page'
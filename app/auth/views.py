from flask import  render_template, jsonify, redirect, flash
from flask.helpers import url_for
from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required
from . import auth_bp
from .. import db
from ..models import User, Color, Category
from ..forms import RegisterForm, LoginForm


def add_initial_data(user):
    color = Color()
    color.name = '#F723FB'
    color.save()
    category = Category()
    category.name = 'General'
    category.color = color
    category.user = user
    category.save()

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.username.data.strip()).first() or \
            User.query.filter_by(username = form.username.data.strip()).first() or None
        if user:
            if user.check_password(form.password.data.strip()):
                login_user(user, remember=form.remember_me)
                return redirect(url_for('user_bp.dashboard'))
            else: 
                flash("Username or password is incorrect")
                return redirect(url_for('auth_bp.login'))
        else:
            flash("Username or password is incorrect")
            return redirect(url_for('auth_bp.login'))
    return render_template('signin.html', form = form)


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #return jsonify({'message':'success', 'username':form.username.data, 'email':form.email.data, 'password':form.password.data})
        user = User()
        user.username = form.username.data.strip()
        user.email = form.email.data.strip()
        user.set_password(form.password.data.strip())
        user.save()
        add_initial_data(user)
        return redirect(url_for('auth_bp.login'))
    return render_template('register.html', form = form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('auth_bp.login'))

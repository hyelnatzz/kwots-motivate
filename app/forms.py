from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Length



class LoginForm(FlaskForm):
    username = StringField('', validators=[InputRequired(message='username is required')])
    password = PasswordField('', validators=[InputRequired(message='password is required')])
    remember_me = BooleanField('Remember me?')
    login = SubmitField('Login')


class AddCategoryForm(FlaskForm):
    name = StringField('', validators=[InputRequired(message='title is required')])
    color = StringField('')
    description = TextAreaField('')
    add_category = SubmitField('')


class RegisterForm(FlaskForm):
    username = StringField('', validators=[InputRequired(message='username is required')])
    email = EmailField('', validators=[InputRequired(message='email field cannot be empty')])
    password = PasswordField('', validators=[InputRequired(message='password is required'), Length(min=8, message='password cannot be less than 8 characters long')])
    confirm_password = PasswordField('', validators=[EqualTo('password', message='password does not match')])
    register = SubmitField('Register')


class QuoteForm(FlaskForm):
    author = StringField('', validators=[InputRequired(message='author name is required')])
    quote = TextAreaField('', validators=[InputRequired('quote body is required')])
    note = TextAreaField('')
    category = SelectField('', choices=['select a category'] )
    add_quote = SubmitField('')



from flask import Blueprint, render_template
from . import db
from .models import User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    user = User.query.filter_by(id = 1).first()
    color = 'red'
    style = 'h1 {color:%s}' % color
    return render_template('index.html', user = user, style = style)
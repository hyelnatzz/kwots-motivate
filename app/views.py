from flask import Blueprint, render_template, current_app
from . import db
from .models import User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')
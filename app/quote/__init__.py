from flask import Blueprint

quote_bp = Blueprint('quote_bp', __name__, url_prefix='/quote')

from .views import *
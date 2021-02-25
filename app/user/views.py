from datetime import datetime
from flask import  render_template, redirect, flash
from flask.helpers import url_for
from flask_login import login_required, current_user
from . import user_bp
from ..forms import RegisterForm
from ..models import db, Category, Color
from ..utils import hex_to_dec


@user_bp.route('/dashboard')
@login_required
def dashboard():
    if datetime.now().hour < 12:
        period = 'morning'
    elif datetime.now().hour > 12 and datetime.now().hour < 4 or 16:
        period = 'afternoon'
    else:
        period = 'evening'
    categories = current_user.categories
    favorites = [i for i in current_user.quotes if i.favorite == 1]
    color = {i.color.name: hex_to_dec(i.color.name) for i in categories}
    print(color)
    return render_template('dashboard.html', categories = categories, favorites = favorites, color = color, period = period)


@user_bp.route('/edit-profile')
@login_required
def edit_profile():
    form = RegisterForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        current_user.username = form.username.data.strip()
        current_user.email = form.email.data.strip()
        current_user.save()
        flash('Details Edited')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('edit-user.html', form = form)

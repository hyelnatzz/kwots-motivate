from flask import  render_template
from flask_login import login_required
from . import user_bp


@user_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@user_bp.route('/edit_profile')
@login_required
def edit_profile():
    return 'edit user profile'

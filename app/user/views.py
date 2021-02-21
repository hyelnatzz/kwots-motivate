from flask import  render_template
from . import user_bp


@user_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@user_bp.route('/edit_profile')
def edit_profile():
    return 'edit user profile'

from . import user_bp


@user_bp.route('/dashboard')
def dashboard():
    return 'user dashboard'


@user_bp.route('/edit_profile')
def edit_profile():
    return 'edit user profile'

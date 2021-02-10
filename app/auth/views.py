from . import auth_bp

@auth_bp.route('/login')
def login():
    return 'login Page'

@auth_bp.route('/register')
def register():
    return 'registration Page'

@auth_bp.route('/logout')
def logout():
    return 'logout Page'
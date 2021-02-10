from . import quote_bp 

@quote_bp.route('/add')
def add_quote():
    return 'add quote view'

@quote_bp.route('/edit/<int:quote_id>/')
def edit_quote(quote_id):
    return f'edit quote {quote_id} view'


@quote_bp.route('/delete/<int:quote_id>/')
def delete_quote(quote_id):
    return f'delete quote {quote_id} view'


@quote_bp.route('/fav/<int:quote_id>/')
def make_favorite(quote_id):
    return f'make favorite {quote_id} view'

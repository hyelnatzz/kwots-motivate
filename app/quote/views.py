from flask import render_template, request, jsonify
from ..models import db, Category, Color
from . import quote_bp 


@quote_bp.route('/add')
def add_quote():
    return render_template('add-quote.html')

@quote_bp.route('/edit/<int:quote_id>/')
def edit_quote(quote_id):
    return f'edit quote {quote_id} view'


@quote_bp.route('/delete/<int:quote_id>/')
def delete_quote(quote_id):
    return f'delete quote {quote_id} view'


@quote_bp.route('/fav/<int:quote_id>/')
def make_favorite(quote_id):
    return f'make favorite {quote_id} view'


@quote_bp.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        color = Color()
        color.name = request.form['color']
        color.save()
        category = Category()
        category.name = request.form['title']
        category.color = color
        category.save()
        return jsonify({'message': 'success', 'name': request.form['title'], 'color':request.form['color']})
    return render_template('add-category.html')


@quote_bp.route('/edit-category/<int:category_id>/')
def edit_category(category_id):
    return f'edit quote {category_id} view'


@quote_bp.route('/delete-category/<int:category_id>/')
def delete_category(category_id):
    return f'delete quote {category_id} view'

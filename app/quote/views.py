from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Category, Color, Quote
from ..forms import QuoteForm, AddCategoryForm
from . import quote_bp 


@quote_bp.route('/add', methods=['POST', 'GET'])
@login_required
def add_quote():
    form = QuoteForm()
    form.category.choices.extend([(i.name) for i in Category.query.all()])
    if form.validate_on_submit():
        category = Category.query.filter_by(name = form.category.data)
        quote = Quote()
        quote.author = form.author.data.strip()
        quote.user = current_user
        quote.category= category
        quote.note = form.note.data.strip()
        quote.save()
        print(request.form['author'], request.form['quote'], request.form['category'] )
        flash('Quote Added')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('add-quote.html', form = form)


@quote_bp.route('/edit/<int:quote_id>/', methods=['POST', 'GET'])
@login_required
def edit_quote(quote_id):
    quote = Quote.query.filter_by(id = quote_id).first()
    form = QuoteForm()
    form.note.data = quote.note
    form.author.data = quote.author
    form.quote.data = quote.quote
    form.category.data = quote.category.name
    if form.validate_on_submit():
        quote.quote = form.quote.data.strip()
        quote.author = form.author.data.stip()
        quote.category = Category.query.filter_by(name = form.category.data).first()
        quote.note = form.note.data.strip()
        quote.save()
        flash('Quote edited')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('edit-category.html', form = form)


@quote_bp.route('/delete/<int:quote_id>/')
@login_required
def delete_quote(quote_id):
    quote = Quote.query.filetr_by(id = quote_id).first()
    quote.delete()
    flash('Quote deleted successfully')
    return redirect(url_for('user_bp.dashboard'))


@quote_bp.route('/fav/<int:quote_id>/', methods=['GET'])
@login_required
def make_favorite(quote_id):
    quote = Quote.query.filter_by(id = quote_id).first()
    quote.favorite = True
    quote.save()
    return redirect(url_for('user_bp.dashboard'))


@quote_bp.route('/add-category', methods=['GET', 'POST'])
@login_required
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        color = Color()
        color.name = form.color.data
        color.save()
        category = Category()
        category.name = form.name.data.strip()
        category.color = color
        category.user = current_user
        category.save()
        flash('Quote deleted successfully')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('add-category.html', form = form)


@quote_bp.route('/edit-category/<int:category_id>/')
@login_required
def edit_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    color = Color.query.filter_by(id = category.color.id).first()
    form = AddCategoryForm()
    form.color.data = color.name
    form.name.data = category.name
    form.description.data = category.description
    if form.validate_on_submit():
        color.name = form.color.data
        color.save()
        category.color = color
        category.name = form.name.data.strip()
        category.description = form.description.data.strip()
        category.save()
        flash('Category edited')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('edit-category.html', form = form)


@quote_bp.route('/delete-category/<int:category_id>/')
@login_required
def delete_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    category.delete()
    flash('Category deleted')
    return redirect(url_for('user_bp.dashboard'))

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Category, Color, Quote
from ..forms import QuoteForm, AddCategoryForm
from . import quote_bp 


@quote_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_quote():
    form = QuoteForm()
    if request.method == 'POST':
        print('post')
        category = Category.query.filter_by(name = form.category.data, user_id = current_user.id).first()
        quote = Quote()
        quote.author = form.author.data.strip()
        quote.user = current_user
        quote.category= category
        quote.note = form.note.data.strip()
        quote.quote = form.quote.data.strip()
        quote.save()
        flash('Quote Added')
        return redirect(url_for('user_bp.dashboard'))
    print('this place')
    form.category.choices.extend([(i.name) for i in Category.query.filter_by(user_id = current_user.id).all()])
    return render_template('add-quote.html', form = form)


@quote_bp.route('/add-to-category/<int:category_id>/', methods=['GET', 'POST'])
@login_required
def add_quote_to_category(category_id):
    form = QuoteForm()
    category = Category.query.filter_by(id=category_id).first()
    if request.method == 'POST':
        quote = Quote()
        quote.author = form.author.data.strip()
        quote.user = current_user
        quote.category = category
        quote.note = form.note.data.strip()
        quote.quote = form.quote.data.strip()
        quote.save()
        flash('Quote Added')
        return redirect(url_for('user_bp.dashboard'))
    form.category.choices = [ Category.query.filter_by(id = category_id).first().name ]
    return render_template('add-quote-cat.html', form=form, category = category)


@quote_bp.route('/edit/<int:quote_id>/', methods=['GET', 'POST'])
@login_required
def edit_quote(quote_id):
    quote = Quote.query.filter_by(id = quote_id).first()
    form = QuoteForm()
    if request.method == "POST":
        quote = Quote.query.filter_by(id=quote_id).first()
        print(quote)
        quote.quote = form.quote.data.strip()
        quote.author = form.author.data.strip()
        if form.category.data == "select a category":
            quote.category = Category.query.filter_by(name = "General", user_id = current_user.id).first()
        else:
            quote.category = Category.query.filter_by(name = form.category.data, user_id = current_user.id).first()
        quote.note = form.note.data.strip()
        db.session.commit()
        print(quote.author)
        print(form.author.data.strip())
        flash('Quote edited')
        return redirect(url_for('user_bp.dashboard'))
    form.category.choices.extend([(i.name) for i in Category.query.filter_by(user_id = current_user.id).all()])
    form.author.data = quote.author
    return render_template('edit-quote.html', form = form, quote = quote)


@quote_bp.route('/delete/<int:quote_id>/')
@login_required
def delete_quote(quote_id):
    quote = Quote.query.filter_by(id = quote_id).first()
    db.session.delete(quote)
    db.session.commit()
    flash('Quote deleted successfully')
    return redirect(url_for('user_bp.dashboard'))


@quote_bp.route('/fav/<int:quote_id>/', methods=['GET'])
@login_required
def make_favorite(quote_id):
    quote = Quote.query.filter_by(id = quote_id).first()
    quote.favorite = True
    quote.save()
    return redirect(url_for('user_bp.dashboard'))


@quote_bp.route('/un-fav/<int:quote_id>/', methods=['GET'])
@login_required
def remove_favorite(quote_id):
    quote = Quote.query.filter_by(id=quote_id).first()
    quote.favorite = False
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
        category.description = form.description.data.strip()
        category.color = color
        category.user = current_user
        category.save()
        flash('Quote deleted successfully')
        return redirect(url_for('user_bp.dashboard'))
    return render_template('add-category.html', form = form)


@quote_bp.route('/edit-category/<int:category_id>/', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    color = Color.query.filter_by(id = category.color.id).first()
    form = AddCategoryForm()
    if form.validate_on_submit():
        color.name = form.color.data
        color.save()
        category.color = color
        category.name = form.name.data.strip()
        category.description = form.description.data.strip()
        category.save()
        print(category.id)
        db.session.commit()
        flash('Category edited')
        return redirect(url_for('user_bp.dashboard'))
    form.color.data = color.name
    color = color.name
    form.name.data = category.name
    description = category.description
    return render_template('edit-category.html', form = form, description=description, color=color, category = category)


@quote_bp.route('/delete-category/<int:category_id>/')
@login_required
def delete_category(category_id):
    general_category = Category.query.filter_by(name = "General", user_id = current_user.id).first()
    category = Category.query.filter_by(id = category_id, user_id = current_user.id).first()
    color = category.color
    quotes = category.quotes
    if quotes:
        for i in quotes:
            i.category = general_category
            i.save()
    db.session.delete(color)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted')
    return redirect(url_for('user_bp.dashboard'))

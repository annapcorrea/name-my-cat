from flask import render_template, request, redirect, url_for, flash
import sqlalchemy as sa
from app import db
from app.forms import NameForm
from app.models import CatName
from flask import current_app as app

# Add new vote route
@app.route('/vote/<int:name_id>', methods=['POST'])
def vote(name_id):
    cat_name = CatName.query.get_or_404(name_id)
    cat_name.votes = cat_name.votes + 1 if cat_name.votes else 1
    db.session.commit()
    flash('Thanks for voting!', 'success')
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    
    if form.validate_on_submit():
        existing_name = CatName.query.filter_by(name=form.cat_name.data).first()
        if existing_name:
            flash('That name already exists! Please choose another.', 'danger')
        else:
            new_name = CatName( name=form.cat_name.data, user_name=form.user_name.data)
            db.session.add(new_name)
            db.session.commit()
            flash('Name submitted successfully!', 'success')
            return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    query = sa.select(CatName)
    
    # Apply sorting
    query = query.order_by(CatName.votes.desc(), CatName.id.desc())
    
    pagination = db.paginate(
        query,
        page=page,
        per_page=5,
        error_out=False
    )

    return render_template(
        "index.html",
        title='Name my Cat',
        form=form,
        cat_names=pagination.items,
        pagination=pagination
    )
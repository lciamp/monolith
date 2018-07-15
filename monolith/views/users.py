from flask import Blueprint, redirect, render_template, request
from ..database import db, User
#from monolith.auth import admin_required
from ..forms import UserForm


users = Blueprint('users', __name__)


@users.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if request.methos == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    return render_template('create_user.html', form=form)


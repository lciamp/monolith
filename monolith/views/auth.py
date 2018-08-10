from flask import Blueprint
from flask_login import LoginManager, logout_user, logout_user
from monolith.forms import LoginForm
from monolith.database import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.data['email'], form.data['password']
        q = db.session.query(User).filter(User.email==email).first()

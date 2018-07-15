from flask import Blueprint, render_template, request, redirect
from stravalib import Client

from monolith.database import db, Run
from monolith.auth import current_user
from monolith.app import app

home = Blueprint('home', __name__)

def get_strava_auth_url():
    client = Client()
    client_id = app.config['STRAVA_CLIENT_ID']
    redirect = 'http://127:0.0.1:5000/strava_auth'
    url = client.authorization_url(client_id=client_id,
                                   redirect=redirect)
    return url

@app.route('/strava_auth')
@login_required
def _strava_auth():
    client = Client()
    code = request.args.get('code')
    xc = client.exchange_code_for_token
    access_token = xc(client_id=app.config['STRAVA_CLIENT_ID'],
                      client_secret=app.config['STRAVA_CLIENT_SECRET'],
                      code=code)
    current_user.strava_token = access_token
    db.session.add(current_user)
    db.session.commit()
    return redirect('/')


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





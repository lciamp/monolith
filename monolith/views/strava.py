from flask import jsonify, Blueprint
from monolith.background import fetch_all_runs

strava = Blueprint('strava', __name__)


@strava.route('/fetch')
def fetch_runs():
    res = fetch_all_runs.delay()
    res.wait()
    return jsonify(res.result)


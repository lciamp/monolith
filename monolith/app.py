from flask import Flask, render_template
from .database import db, User
app = Flask(__name__)
app.config['STRAVA_CLIENT_ID'] = 'runnerly-strava-id'
app.config['STRAVA_CLIENT_SECRET'] = 'runnerly-strava-secret'

@app.route('/users')
def users():
    users = db.session.query(User)
    return render_template('users.html', users=users)


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run()
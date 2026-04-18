import os
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from flask_session import Session

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=False,
    SESSION_TYPE='filesystem',
    SESSION_PERMANENT=False
)
Session(app)
csrf = CSRFProtect(app)
app.permanent_session_lifetime = timedelta(minutes=30)

@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def not_found(e):
    return render_template('errors/500.html'), 500
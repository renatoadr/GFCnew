from functools import wraps
from flask import session, request, redirect, url_for


def login_required(fn):
    @wraps(fn)
    def validate_login(*args, **kwargs):
        if 'logged_in' not in session or session['logged_in'] == False:
            return redirect(url_for('inicio.login', next=request.url))
        return fn(*args, **kwargs)
    return validate_login

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>Login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/signup')
def signup():
    return "<h1>signup</h1>"

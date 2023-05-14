from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('Enter a valid email', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('Account Created Successfully', category='success')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('Enter a valid email', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('Account Created Successfully', category='success')
    return render_template('signup.html')

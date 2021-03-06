from flask import render_template, redirect, request, flash, session
# from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.user_model import User

# bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if "user_id" in session:
        return redirect('/dashboard')

    return render_template('index.html')


@app.route('/register', methods=['post'])
def register():
    if not User.register_valid(request.form):
        return redirect('/')

    hash_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        ** request.form,
        'password': hash_pass
    }

    user_id = User.create(data)
    session['user_id'] = user_id

    return redirect('/dashboard')

@app.route('/login', methods=['post'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash('Invalid Email')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Password')
        return redirect('/')
    session['user_id'] = user.id

    return redirect('/dashboard')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
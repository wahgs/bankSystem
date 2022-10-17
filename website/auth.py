#holds authentication webpages
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import random

auth = Blueprint('auth', __name__)

#generates a number between 1-10000
#used to generate a fake balance for new accounts.
def genbal():
    balance = random.randint(1,10000)
    return balance


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #queries email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
        else:
            flash('Incorrect password, try again.', category='error')
            
    return render_template('login.html', user=current_user)
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        genbal()
        print(f"Generated balance for {email} : ")
        #grabs username from db if it exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) <2:
            flash('first name needs to be longer than 2 chars.', category='error')
        elif password1 != password2:
            flash('passwords are not equal', cagetory='error')
        elif len(password1) <7:
            flash('password must be longer than 7 characters.', category='error')
        #all checks passed
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            flash('Please login.', category='success')
            return redirect(url_for('auth.login'))
        
    return render_template("sign_up.html", user=current_user)
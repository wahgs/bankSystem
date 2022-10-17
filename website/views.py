#stores url endpoints for home, removing notes,
from unicodedata import category
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
import json
import jsonify
import random



views = Blueprint('views', __name__)

@views.route("/")
def duh():
    #if the user's alr logged in, takes them to home, otherwise takes them to login
    #checks if the users balance has been set.
    #if the user has a balance set.
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    else:
        return redirect(url_for('auth.login'))



@views.route("/home", methods =['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        #for returns
        pass
    
    else:
        #if the user has a balance set.
        if current_user.balance:
            return render_template("home.html", firstName=current_user.first_name, user=current_user, balance=current_user.balance)
        #if the user does not have a balance
        elif not current_user.balance:
            #creates a balance and assigns it to the current user.
            balance = random.randint(1,10000)
            current_user.balance = balance
            db.session.commit()
            return render_template("home.html", firstName=current_user.first_name, user=current_user, balance=current_user.balance)
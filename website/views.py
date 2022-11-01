#stores url endpoints for home, removing notes,
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from .auth import genbal
from . import db
import json
import jsonify
import random
from time import sleep


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



@views.route("/home")
@login_required 
def home():
    if current_user.balance:
        return render_template("home.html", firstName=current_user.first_name, user=current_user, balance=current_user.balance)
    #if the user does not have a balance
    elif not current_user.balance:
        #references auth.py's function genbal
        balance = genbal
        current_user.balance = balance
        db.session.commit()
        return render_template("home.html", firstName=current_user.first_name, user=current_user, balance=current_user.balance)

@views.route("/withdrawal", methods=['GET', 'POST'])
@login_required
def withdrawal():
    if request.method == 'POST':
        amount = int(request.form.get("amount"))
        currentbal = int(current_user.balance)
        if amount >= 500 or currentbal - amount <= 1000:
            return redirect(url_for("auth.passwordRequired", amount=amount))
        else:
            newbal = currentbal - amount
            current_user.balance = newbal
            db.session.commit()
            flash("Balance successfully updated to " + str(newbal) + "! Redirecting to home...")
            return redirect(url_for("views.home"))
    #get method response
    else:
        return render_template("withdrawal.html", bal=current_user.balance, name=current_user.first_name, auth=current_user.is_authenticated, user=current_user)

@views.route("/deposit", methods=['GET', 'POST'])
@login_required
def deposit():
    if request.method == 'POST':
        amount = request.form.get('amount')
        bal = current_user.balance
        newbal = int(bal) + int(amount)
        current_user.balance = newbal
        db.session.commit()
        flash(f"You have successfully added ${str(amount)} to your balance", category="success")
        return redirect(url_for('views.home'))
    else:
        return render_template("deposit.html", bal=current_user.balance, name=current_user.first_name, user=current_user)

@views.route("/settings", methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        #determines which button was clicked lol
        if ''
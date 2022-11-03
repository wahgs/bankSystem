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

#blueprint function to render templates
#this function will return the template with any information any of the templates need.
def render(var):
    if current_user.is_authenticated:
        if not current_user.balance:
            return render_template(str(var), firstName=current_user.first_name, user=current_user, auth=current_user.is_authenticated, mode=current_user.mode)
        else:    
            return render_template(str(var), firstName=current_user.first_name, user=current_user, balance=current_user.balance, auth=current_user.is_authenticated, mode=current_user.mode)
    else:
        return render_template(str(var), auth=current_user.is_authenticated)


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
        return render("home.html")
    #if the user does not have a balance
    else:
        #references auth.py's function genbal
        balance1 = genbal
        current_user.balance = balance1
        db.session.commit()
        return render("home.html")


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
        return render("withdrawal.html")

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
        return render("deposit.html")

@views.route("/removeAccount", methods=['GET', 'POST'])
@login_required
def removeAccount():
    #working on later
    if request.method == 'POST':
        sentEmail = request.form.get('email')
        if current_user.email == sentEmail:
            name = current_user.name
            db.session.query(User).filter(User.email == sentEmail).delete()
            db.session.commit()
            flash(f"The account for {name.title()} has been deleted!", category="error")
            return redirect(url_for("auth.login"))
        if current_user.email != sentEmail:
            flash("Invalid Email Address, try again.")
            return render("removeAccount.html")
    else:
        return render("removeAccount.html")



@views.route("/settings", methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        #determines which button was clicked
        form = str(request.form.form).lower()
        if form == 'lightmode' or form == 'darkmode' or 'removeaccount':
            if form == 'lightmode':
                try:
                    current_user.mode = 'light'
                    db.session.commit()
                    flash('Switched to dark mode', category="success")
                except Exception as e:
                    flash(f'Error switching to dark mode: \'{e}\'', cagtegory="error")
                    print(f'Exception in line 92 views.py: "{str(e)}"')
                finally:
                    return render("settings.html")
            #attempts to create the current users mode to dark mode.
            elif form == 'darkmode':
                try:
                    current_user.mode = 'dark'
                    db.session.commit()
                    flash('Switched to light mode', category="success")
                except Exception as e:
                    flash(f'Error switching to light mode: \'{e}\'', category="error")
                    print(f'Exception in line 92 views.py: "{str(e)}"')
                finally:
                    return render("settings.html")
            elif form == 'removeaccount':
                return redirect(url_for("views.removeAccount"))
    else:
        return render("settings.html")
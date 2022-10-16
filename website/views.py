#stores url endpoints for home, removing notes,
from unicodedata import category
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json
import jsonify


views = Blueprint('views', __name__)

@views.route("/")
def duh():
    #if the user's alr logged in, takes them to home, otherwise takes them to login
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
        return render_template("home.html", firstName=current_user.first_name, user=current_user)

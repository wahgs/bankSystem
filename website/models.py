#holds database models
from .  import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #unique = True means that the email is going to be unique, no other object can have this.
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    balance = db.Column(db.Integer)
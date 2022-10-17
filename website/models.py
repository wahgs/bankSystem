#holds database models
#holds Users and Balance
from .  import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #note
    data = db.Column(db.String(10000))
    #keeps the id of the user that created this.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #unique = True means that the email is going to be unique, no other object can have this.
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    balance = db.Column(db.Integer())
    notes = db.relationship('Note')
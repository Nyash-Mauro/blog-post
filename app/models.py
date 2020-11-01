from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(255),nullable=False,unique=True)
    secondstname = db.Column(db.String(255),nullable=False,unique=True)
    username = db.Column(db.String(255),nullable=False,unique=True)
    email = db.Column(db.String(255),nullable=False,unique=True)  
    bio = db.Column(db.String(255))
    post = db.relationship('Post',backref='user',lazy ='dynamic')  
    password = db.Column(db.String(255),nullable=False)
    
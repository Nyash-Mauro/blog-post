from flask import Flask,render_template , url_for,request,redirect
from . import main
from flask_login import login_required,current_user
from app.models import User,Post,Comment
from .. import db,photos
from app.requests import get_Quotes
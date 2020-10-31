from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_required,current_user, login_user,logout_user
import re
from app.models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get("username")
        password = form.get("password")

        user= User.query.filter_by(username=username).first()
        if user == None :
            error ="User with username does not exist"
            return render_template('login.html', error = error)
        is_correct_password = user.check_password(password)
        if is_correct_password == False:
            error ="User with  password does not exist"
            return render_template('login.html', error=error)
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Login')

@auth.route('/registration',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form = request.form
        firstname = form.get("firstname")
        secondname = form.get("secondname")
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        confirm_password = form.get("confirm_password")       
        
from flask import Blueprint,render_template,redirect,request,flash, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import User,StatData

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username").lower()
        password = request.form.get("password")
        user = User.query.filter_by(uname=username).first()
        if user:
            hashed_pw = generate_password_hash(user.password)
            if check_password_hash(hashed_pw, password):
                flash("Login was successful", category='success')
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash("Wrong password!", category='error')
        else:
            flash("User not exists", category="error")
        
    return render_template('login.html', user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
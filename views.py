from flask import Blueprint, render_template, request,redirect,url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy.sql import expression
from models import StatData,User,Car, db
from datetime import datetime, date

views = Blueprint("views", __name__,)



@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route("/charts")
@login_required
def charts():
    return '<h1>Charts will go here</h1>'

@views.route("/view_data", methods = ["GET", "POST"])
@login_required
def view_data():
    filter_value = request.form.get('filter')
    datas = StatData.query.all()
    return render_template('datas.html', datas = datas, user = current_user)


@views.route("/add", methods = ['GET', 'POST'])
@login_required
def add():
    cars = Car.query.all()
    if request.method == 'POST':
        lplate = request.form.get("selected_car")
        amount = request.form.get("amount")
        add_date = request.form.get("date")
        if add_date == '':
            add_date = datetime.now().strftime('%Y-%m-%d')
        user_id = current_user.id
        user_name = current_user.name
        car_id = db.session.query(Car.id).filter(Car.license_plate == lplate)
        data = StatData(lplate,amount,add_date,user_id,car_id, user_name)
        db.session.add(data)
        db.session.commit()
        flash("Data added succesfully!", category="success")
    return render_template("add_data.html", user = current_user, cars = cars)


@views.route("/add_user", methods = ['POST','GET'])
@login_required
def add_user():
    if request.method == "POST":
        admin_rights = request.form.get("is_admin")
        full_name = request.form.get("full_name").title()
        username = request.form.get("username").lower()
        password = request.form.get("password")
        email = request.form.get("email")
        
        if admin_rights == 'True':
            new_user = User(uname = username, name = full_name, email = email, password = password, is_admin = expression.true())
        else:
            new_user = User(uname = username, name = full_name, email = email, password = password, is_admin = expression.false())
        db.session.add(new_user)
        db.session.commit()
        flash("New user created!", category="success")
        print(new_user)
    return render_template("add_user.html", user = current_user)




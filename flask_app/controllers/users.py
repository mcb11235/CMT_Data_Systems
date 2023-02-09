from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html")
@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }
    if not User.validate_register(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    current_user = User.save(data)
    print("S E S S I O N")
    session['user'] = current_user
    print(session['user'])
    return redirect('/dashboard')
@app.route("/login", methods=['POST'])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    user = User.get_by_email(data)
    if not bcrypt.check_password_hash(user.password, data['password']):
        flash("Invalid Password!")
        return redirect('/')
    if not user:
        flash("Email Does Not Exist!")
        return redirect('/')
    session['user'] = user.id        
    return redirect('/dashboard')
@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
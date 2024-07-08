from flask import Flask, redirect, render_template, request, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_principal import Permission, Principal, RoleNeed
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookings.db"
app.config["SECRET_KEY"] = "secret_key"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
principal = Principal(app)


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for("new"))
        else:
            return "Invalid Username or Password!"
    return render_template("login.html")
    # return redirect(url_for("success", name=user))


@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "UserName had already taken"
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)


@app.route("/")
def new():
    return render_template("new.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/book", methods=["POST", "GET"])
def book():
    name = request.form.get("name")
    service = request.form.get("service")
    booking = Booking(name=name, service=service)
    db.session.add(booking)
    db.session.commit()
    # return f"Thank you, {name}, for booking {service}!"
    return redirect(url_for("bookings"))


@app.route("/bookings")
def bookings():
    all_bookings = Booking.query.all()
    return render_template("bookings.html", bookings=all_bookings)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()

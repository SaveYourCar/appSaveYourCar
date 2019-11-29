from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.forms.userForm import LoginForm, RegistrationForm
from app import db, login_manager, bcrypt
from app.models.modelUsers import User, UserLogin
from app.models.modelCars import Car

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        user_login = UserLogin(email=form.email.data, password=hashed_password, id_user=user.id)
        db.session.add(user_login)
        db.session.commit()
        flash('Il tuo account è stato creato! Ora puoi effettuare il log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        userLogin = UserLogin.query.filter_by(email=form.email.data).first()
        if userLogin and bcrypt.check_password_hash(userLogin.password, form.password.data):
            user = User.query.filter_by(id=userLogin.id).first()
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Il login non è andato a buon fine. Controlla email e password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
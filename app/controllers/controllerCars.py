from flask import Blueprint
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from app import db, bcrypt
from app.forms.carForm import CarForm
from app.models.modelCars import Car, CarDataValue, CarData
from flask_login import current_user, login_required
from app.controllers.utilsCars import *

cars = Blueprint('cars', __name__)

@cars.route('/auto')
def auto():
    return "Lista Auto"

@cars.route("/car/new_car", methods=['GET', 'POST'])
@login_required
def new_car():
    form = CarForm()
    if form.validate_on_submit():
       car = Car(name=form.name.data, fuel= form.fuel.data,
                 matriculation=form.matriculation.data, author=current_user)
       db.session.add(car)
       AddCarValueToDb(car,form)
       db.session.commit()
       flash('I dati della tua auto sono stati salvati !', 'success')
       return redirect(url_for('main.home'))
    return render_template('new_car.html', title='New Car',
                            form=form, legend='Nuova Auto')
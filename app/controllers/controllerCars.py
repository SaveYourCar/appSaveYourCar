from flask import Blueprint

cars = Blueprint('cars', __name__)

@cars.route('/auto')
def auto():
    return "Lista Auto"